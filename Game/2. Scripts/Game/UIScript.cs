using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class UIScript : MonoBehaviour
{
    public Text IngameScoreText;

    private void Start()
    {
        InvokeRepeating("TextUpdate", 0f, 2f);
    }

    void TextUpdate()
    {
        IngameScoreText.text = string.Format("현재 점수: {0}",CommonData.Score.ToString());
    }
}
