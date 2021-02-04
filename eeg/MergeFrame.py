import pandas as pd
import os

def Merge(feature):
    for i, f in enumerate(feature):
        try:
            if i == 0:
                a = pd.read_csv(f)
                all_data = a

            else:
                a = pd.read_csv(f)
                all_data = pd.merge(all_data, a, on='Unnamed: 0', how='outer')
                print(all_data)

        except:
            pass

    return all_data


channel = ['O1', 'O2', 'P7', 'T7', 'T8']
who='Control'

file = f'dataset/select_{who}_frame_model/'
try:
    os.mkdir(file)
except:
    pass

df = pd.DataFrame()
for c in channel:
    path = f'./dataset/ratio2/Theta_Beta_ratio_{who}_band_power/{who}_{c}.csv'
    data = pd.read_csv(path)
    df[c] = data['Theta/Beta']
print(df)
df.to_csv(file+who+'.csv',index=False)

