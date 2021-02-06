using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;
using UnityEngine.UI;

public class EndManager : MonoBehaviour
{
    public Text ScoreText;

    public Text HighAttentionText;

    // Start is called before the first frame update
    void Start()
    {
        for(int i=0; i<10;i++)
            Client.instance.SendMsg("2");

        ScoreText.text = string.Format("최종 점수: {0}", CommonData.Score.ToString());
        InvokeRepeating("RecvRate", 0f, 0.1f);
    }

    
    void RecvRate()
    {
        if(CommonData.RecvMsgQueue.Count > 0)
        {
            CommonData.UserHighAttention = int.Parse(CommonData.RecvMsgQueue.Dequeue());
            // 텍스트에 적용
            if (CommonData.UserHighAttention == 0)
            {
                HighAttentionText.text = "대단해요!";
            }
            else if (CommonData.UserHighAttention == 1)
            {
                HighAttentionText.text = "조금 더 집중해 봐요~";
            }
        }
    }

    public void MainScene()
    {
        CancelInvoke("RecvRate");
        SceneManager.LoadScene("Main");
    }
}
