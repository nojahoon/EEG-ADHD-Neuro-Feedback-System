using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Net;
using System.Net.Sockets;
using System.Threading;
using UnityEngine;


public class Server : MonoBehaviour
{
    static void Main(string[] args)
    {
        // server ������ �����Ѵ�.	
        using (var server = new Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.Tcp))
        {
            // ip�� �����̰� ��Ʈ�� 9999�� listen ����Ѵ�.	
            server.Bind(new IPEndPoint(IPAddress.Any, 9999));
            server.Listen(20);

            Debug.Log("Server Start... Listen port 9999...");

            try
            {
                while (true)
                {
                    // ���� ������ ����ϱ� ���� Threadpool�� �̿��� ��Ƽ ������ ȯ���� �������.	
                    ThreadPool.QueueUserWorkItem(c =>
                    {
                        Socket client = (Socket)c;
                        try
                        {
                            // ���� ������ �޽����� ����Ѵ�.	
                            while (true)
                            {
                                // ó���� ������ ���̸� �ޱ� ���� 4byte�� �����Ѵ�.	
                                var data = new byte[4];
                                // python���� little ��������� ���� �´�. big������ little������� �迭�� ������ �ݴ��̹Ƿ� reverse�Ѵ�.	
                                client.Receive(data, 4, SocketFlags.None);
                                Array.Reverse(data);
                                // �������� ���̸�ŭ byte �迭�� �����Ѵ�.	
                                data = new byte[BitConverter.ToInt32(data, 0)];
                                // �����͸� �����Ѵ�.	
                                client.Receive(data, data.Length, SocketFlags.None);

                                // byte�� UTF8���ڵ����� string �������� ��ȯ�Ѵ�.	
                                var msg = Encoding.UTF8.GetString(data);
                                // �����͸� �ֿܼ� ����Ѵ�.
                                Debug.Log(msg);
                                // �޽����� echo�� ���ڸ� ������.	
                                msg = "C# server echo : " + msg;
                                // �����͸� UTF8���ڵ����� byte�������� ��ȯ�Ѵ�.	
                                data = Encoding.UTF8.GetBytes(msg);
                                // ������ ���̸� Ŭ���̾�Ʈ�� �����Ѵ�.	
                                client.Send(BitConverter.GetBytes(data.Length));
                                // �����͸� �����Ѵ�.	
                                client.Send(data, data.Length, SocketFlags.None);
                            }

                        }
                        catch (Exception)
                        {
                            // Exception�� �߻��ϸ� (����ġ ���� ���� ����) client socket�� �ݴ´�.	
                            client.Close();
                        }
                        // server�� client�� ������ �Ǹ� ThreadPool�� Thread�� �����˴ϴ�.	
                    }, server.Accept());
                }
            }
            catch (Exception e)
            {
                Debug.Log(e);
            }
        }
        Console.WriteLine("Press any key...");
        Console.ReadLine();
    }
}