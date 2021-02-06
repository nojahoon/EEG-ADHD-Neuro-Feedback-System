using System;
using System.Collections;
using System.Collections.Generic;
using System.Threading;
using UnityEngine;
using UnityEngine.SceneManagement;
using UnityEngine.UI;

public class GameManager : MonoBehaviour
{
    private Coroutine coroutine;

    private bool isCheck = false;

    private float totalGameTime = 3;
    private float gameTime = 3;
    private int count = 0;

    private int answer = 0;

    private Vector2 targetPos = new Vector2(-4.5f, -1f);

    private CommonData.State gameState = CommonData.State.GAME1;

    private List<GameObject> allGameObject;

    public List<int> ExampleFigures;
    public List<int> QuestionFigures;

    public GameObject Triangle;
    public GameObject Square;
    public GameObject Circle;

    public GameObject TriangleBtn;
    public GameObject SquareBtn;
    public GameObject CircleBtn;

    public Slider TimerSlider;

    public GameObject Game1Panel;
    public GameObject PausePanel;
    public GameObject Game2Panel;
    public GameObject Game3Panel;
    public GameObject MainPanel;

    public Text Game3PanelText;

    private void Awake()
    {
        ExampleFigures = new List<int>();
        QuestionFigures = new List<int>();

        allGameObject = new List<GameObject>();
    }

    private void Start()
    {
        
        Game1();
    }

    void Update()
    {
        
        gameTime -= Time.deltaTime;
        TimerSlider.value = gameTime / totalGameTime;
        if(TimerSlider.value <= 0.3)
            Client.instance.SendMsg("1");
        if (TimerSlider.value <= 0)
        {
            
            switch (gameState)
            {
                case CommonData.State.GAME1:
                    gameTime = 3f;
                    Game1Panel.SetActive(false);
                    PausePanel.SetActive(true);
                    Game2Panel.SetActive(false);
                    Game3Panel.SetActive(false);
                    gameState = CommonData.State.PAUSE;
                    break;
                case CommonData.State.PAUSE:
                    gameTime = 3f;
                    gameState = CommonData.State.GAME2;
                    Game2();
                    break;
                case CommonData.State.GAME2:
                    gameTime = 3f;
                    Game1Panel.SetActive(false);
                    PausePanel.SetActive(false);
                    Game2Panel.SetActive(false);
                    Game3Panel.SetActive(true);

                    for (int i = 0; i < allGameObject.Count; i++)
                    {
                        Destroy(allGameObject[i]);
                    }

                    allGameObject.Clear();

                    if (isCheck == false)
                    {
                        CommonData.Score -= 2;
                        Game3PanelText.text = "시간초과ㅠㅠ";
                    }

                    gameState = CommonData.State.GAME3;

                    break;
                case CommonData.State.GAME3:

                    gameTime = 3f;
                    if (count >= 15)
                    {
                        SceneManager.LoadScene("End");
                    }
                    else
                    {
                        ExampleFigures = new List<int>();
                        QuestionFigures = new List<int>();
                        gameState = CommonData.State.GAME1;
                        
                        Debug.Log(CommonData.Score);
                        
                        Game1();
                    }
                    break;
            }
        }
    }

    void Game1()
    {
        #region 색 맞추기 하던거
        //// 이미지 색
        //int randomColor = Random.Range(1, 8);
        //// 텍스트 종류
        //int randomColorText = Random.Range(1, 8);

        //// 텍스트 종류 적용
        //CommonData.ColorText colorTextEnum;
        //colorTextEnum = (CommonData.ColorText)randomColorText;
        //colorText.text = colorTextEnum.ToString();

        //switch (randomColor)
        //{
        //    case 1:
        //        image.color = Color.red;
        //        break;
        //    case 2:
        //        image.color = new Color(255f, 127f, 0f);
        //        break;
        //    case 3:
        //        image.color = Color.yellow;
        //        break;
        //    case 4:
        //        image.color = Color.green;
        //        break;
        //    case 5:
        //        image.color = Color.blue;
        //        break;
        //    case 6:
        //        image.color = new Color(17f, 38f, 79f);
        //        break;
        //    case 7:
        //        image.color = new Color(139f, 0f, 255f);
        //        break;
        //}
        #endregion

        Game1Panel.SetActive(true);
        PausePanel.SetActive(false);
        Game2Panel.SetActive(false);
        Game3Panel.SetActive(false);
        isCheck = false;

        count++;

        for (int i = 0; i < CommonData.FigureNum; i++)
        {
            int random = UnityEngine.Random.Range(0, 3);
            ExampleFigures.Add(random);
        }

        for(int i = 0; i < ExampleFigures.Count; i++)
        {
            GameObject go;
            int num = 3;
            switch (ExampleFigures[i])
            {
                case 0:
                    go = Instantiate(Triangle, targetPos + Vector2.right * (num * i), Quaternion.identity);
                    go.transform.SetParent(Game1Panel.transform);
                    allGameObject.Add(go);
                    break;
                case 1:
                    go = Instantiate(Square, targetPos + Vector2.right * (num * i), Quaternion.identity);
                    go.transform.SetParent(Game1Panel.transform);
                    allGameObject.Add(go);
                    break;
                case 2:
                    go = Instantiate(Circle, targetPos + Vector2.right * (num * i), Quaternion.identity);
                    go.transform.SetParent(Game1Panel.transform);
                    allGameObject.Add(go);
                    break;
            }
            
        }

    }
    void Game2()
    {
        Game1Panel.SetActive(false);
        PausePanel.SetActive(false);
        Game2Panel.SetActive(true);
        Game3Panel.SetActive(false);

        int randomIdx = UnityEngine.Random.Range(0, 3);
        answer = randomIdx;

        int random;

        QuestionFigures = new List<int>();

        foreach (int list in ExampleFigures)
        {
            QuestionFigures.Add(list);
        }

        do
        {
            random = UnityEngine.Random.Range(0, 3);
            QuestionFigures[randomIdx] = random;
        } while (ExampleFigures[randomIdx] == random);


        for (int i = 0; i < QuestionFigures.Count; i++)
        {
            GameObject go;
            int num = 3;
            switch (QuestionFigures[i])
            {
                case 0:
                    go = Instantiate(TriangleBtn, targetPos + Vector2.right * (num * i), Quaternion.identity);
                    go.transform.SetParent(MainPanel.transform);
                    go.transform.localScale = Vector3.one;
                    allGameObject.Add(go);
                    break;
                case 1:
                    go = Instantiate(SquareBtn, targetPos + Vector2.right * (num * i), Quaternion.identity);
                    go.transform.SetParent(MainPanel.transform);
                    go.transform.localScale = Vector3.one;
                    allGameObject.Add(go);
                    break;
                case 2:
                    go = Instantiate(CircleBtn, targetPos + Vector2.right * (num * i), Quaternion.identity);
                    go.transform.SetParent(MainPanel.transform);
                    go.transform.localScale = Vector3.one;
                    allGameObject.Add(go);
                    break;
            }
        }
        try
        {
            Button bt1 = allGameObject[4].GetComponent<Button>();
            bt1.onClick.AddListener(() => Check(0));

            Button bt2 = allGameObject[5].GetComponent<Button>();
            bt2.onClick.AddListener(() => Check(1));

            Button bt3 = allGameObject[6].GetComponent<Button>();
            bt3.onClick.AddListener(() => Check(2));

            Button bt4 = allGameObject[7].GetComponent<Button>();
            bt4.onClick.AddListener(() => Check(3));
        }
        catch(Exception ex)
        {
            Debug.Log(ex);
        }
    }

    void EndScene()
    {
        SceneManager.LoadScene("End");
    }

    void Check(int n)
    {
        isCheck = true;
        Debug.Log("n: " + n);
        if (answer == n)
        {
            CommonData.Score += 1;
            Game3PanelText.text = "맞았어요!";
        }
        else
        {
            CommonData.Score -= 1;
            Game3PanelText.text = "틀렸어요!";
        }
        gameState = CommonData.State.GAME2;
        gameTime = 0;
    }

    public void EndGame()
    {
        count = 15;
        gameState = CommonData.State.GAME3;
    }
}
