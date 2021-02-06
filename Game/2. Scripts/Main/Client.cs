using System.Collections;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Net;
using System.Net.Sockets;
using UnityEngine;
using System.Threading;

public class Client : MonoBehaviour
{
    public static Client instance;

    private Socket client;

    private Thread RecvThread;

    private void Awake()
    {
        instance = this;

        // ����
        RecvThread = new Thread(RecvMsg);
        RecvThread.Start();
    }

    private void Start()
    {

    }

    public void SendMsg(string msg)
    {
        // ���� �޽����� UTF8Ÿ���� byte �迭�� ��ȯ�Ѵ�.	
        var data = Encoding.UTF8.GetBytes(msg);

        Debug.Log("client: " + client);
        // big��������� ������ ���̸� ��ȯ�ϰ� ������ ���� �������� ���̸� ������. (4byte)	
        client.Send(BitConverter.GetBytes(data.Length));
        // �����͸� �����Ѵ�.	
        client.Send(data);
    }

    public void RecvMsg()
    {

        // ������ �����Ѵ�.	
        using (client = new Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.Tcp))
        {
            // Connect �Լ��� ����(127.0.0.1)�� ��Ʈ ��ȣ 9999�� ��� ���� socket�� �����Ѵ�.
            client.Connect(new IPEndPoint(IPAddress.Parse("172.30.1.49"), 9999));
            Debug.Log("client: " + client);

            // �������� ���̸� �����ϱ� ���� �迭�� �����Ѵ�. (4byte)
            var data = new byte[4];
            // �������� ���̸� �����Ѵ�.	
            client.Receive(data, data.Length, SocketFlags.None);
            // server���� big��������� ������ �ߴµ��� little ��������� �´�. big������ little������� �迭�� ������ �ݴ��̹Ƿ� reverse�Ѵ�.	

            Array.Reverse(data);
            // �������� ���̸�ŭ byte �迭�� �����Ѵ�.	
            data = new byte[BitConverter.ToInt32(data, 0)];
            // �����͸� �����Ѵ�.	
            client.Receive(data, data.Length, SocketFlags.None);
            // ���ŵ� �����͸� UTF8���ڵ����� string Ÿ������ ��ȯ �Ŀ� �ֿܼ� ����Ѵ�.	
            Debug.Log(Encoding.UTF8.GetString(data));
            // ���� ������ ����
            CommonData.RecvMsgQueue.Enqueue(Encoding.UTF8.GetString(data));
        }
    }
}
