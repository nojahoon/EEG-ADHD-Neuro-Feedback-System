using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;
using UnityEngine.UI;

public class MainMenuBtn : MonoBehaviour
{
    public GameObject GameStartPanel;    

    //public Image PanelImage;

    //public FadeIO FadeIo;

    // Start is called before the first frame update
    void Start()
    {
        GameStartPanel.SetActive(false);

        //StartCoroutine(Activate());
    }

    //IEnumerator Activate()
    //{
    //    while (true)
    //    {
    //        if (PanelImage.color.a <= 0)
    //        {
    //            FadeIo.FadeIn(1f);
    //        }
    //        else if (PanelImage.color.a >= 0.49)
    //        {
    //            FadeIo.FadeOut(1f);
    //        }
    //        yield return new WaitForSeconds(0.1f);
    //    }
    //}


    public void GameStartBtn()
    {
        GameStartPanel.SetActive(true);
    }

    public void ShowGameScene()
    {
        SceneManager.LoadScene("Game");
    }

    public void GameQuit()
    {
        Application.Quit();
    }
}
