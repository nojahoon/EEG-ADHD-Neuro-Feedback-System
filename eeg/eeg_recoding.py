from socket import *  # 소켓 라이브러리 임포트
from cortex2 import EmotivCortex2Client
import make_eeg_db
import plaidml.keras
from sklearn.model_selection import train_test_split

plaidml.keras.install_backend()
from tensorflow.keras.models import load_model
import pandas as pd

start = 0
col = ['O1/theta', 'O1/alpha', 'O1/betaL', 'O1/betaH', 'O1/gamma']
al = pd.DataFrame(columns=col)


def soket():
    global al
    while True:
        con = connectionSock.recv(100)
        d = con.decode()

        if '1' in d:
            a.export_csv(a.data_request_mk_data_frame(client.receive_data()))
            print(a.data_request_mk_data_frame(client.receive_data())['pow'].loc[:, 'O1/theta':'O1/gamma'])
            al = pd.concat(
                [al, a.data_request_mk_data_frame(client.receive_data())['pow'].loc[:, 'O1/theta':'O1/gamma']])

        if '2' in d:
            al=al[:490]
            al['theta/betaH'] = al['O1/theta'] / al['O1/betaH']
            al['theta/betaL'] = al['O1/theta'] / al['O1/betaL']
            b = load_model('./lstm_model_adults_keyboard_extend.h5')
            model = b.predict(
                [al['O1/theta'], al['O1/alpha'], al['O1/betaL'], al['O1/betaH'], al['O1/gamma'], al['theta/betaH'],
                 al['theta/betaL']])
            print(model.squeeze(axis=1).mean())
            connectionSock.send('1'.encode('utf-8'))  # 클라이언트쪽으로 보내는 문구
            break


if __name__ == '__main__':
    serverSock = socket(AF_INET, SOCK_STREAM)  # 소켓 생성
    serverSock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    serverSock.bind(('172.30.1.49', 9999))  # 서버 바인드
    serverSock.listen(1)
    connectionSock, addr = serverSock.accept()  # 접속 허가

    url = "wss://localhost:6868"

    client = EmotivCortex2Client(url,
                                 client_id='qWPGYgzUyamd0NWBg3pCqjD9bEH5T3A2FjBjV75T',
                                 client_secret="jwS2y1YO6zGYAogpJlQwfJ0ht8HGWZXFz5zIbfWZhleDyjiM7JwfnFjG3rRvWeoePhP7Q9cl66GwcLBmIvqIueG1YAQzmiTc9kddr6zebXnQphtvfpjWHS1YM1av5nr7",
                                 check_response=True,
                                 authenticate=True,
                                 debug=True, data_deque_size=1, license='9f39d233-5b0d-4bb1-88f8-2a4b8c44c247',
                                 debit=10)

    Apparatus = client.query_headsets()
    print(Apparatus)
    chk_connect = client.connect_headset(0)
    print(chk_connect)
    user_data = client.create_activated_session(0)
    print(user_data)

    sub = ['pow']
    client.subscribe(streams=[sub[0]])
    client.request_access()
    a = make_eeg_db.frame_calculator(client, sub)
    soket()
