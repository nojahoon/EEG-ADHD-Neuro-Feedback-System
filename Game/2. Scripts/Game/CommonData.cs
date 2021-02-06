using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CommonData : MonoBehaviour
{
    public enum ColorText
    {
        빨간색 = 1,
        주황색,
        노란색,
        초록색,
        파란색,
        남색,
        보라색
    }

    public enum Figure
    {
        삼각형 = 0,
        사각형,
        원
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

    public static int UserHighAttention = 0; // 0이 정상(높음) 1이 비정상(낮음)

    public static Queue<string> SendMsgQueue = new Queue<string>();
    public static Queue<string> RecvMsgQueue = new Queue<string>();
}
