using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CommonData : MonoBehaviour
{
    public enum ColorText
    {
        ������ = 1,
        ��Ȳ��,
        �����,
        �ʷϻ�,
        �Ķ���,
        ����,
        �����
    }

    public enum Figure
    {
        �ﰢ�� = 0,
        �簢��,
        ��
    }

    public enum State
    {
        GAME1 = 0,
        PAUSE,
        GAME2,
        GAME3
    }

    public static int FigureNum = 4;

    public static int Score = 0;

    public static int gameCount = 15;

    public static int UserHighAttention = 0; // 0�� ����(����) 1�� ������(����)

    public static Queue<string> SendMsgQueue = new Queue<string>();
    public static Queue<string> RecvMsgQueue = new Queue<string>();
}
