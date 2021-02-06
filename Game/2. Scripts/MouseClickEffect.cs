using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class MouseClickEffect : MonoBehaviour
{
    public static MouseClickEffect instance;
    private Vector2 mousePos;
    private Camera camera;

    public GameObject ButtonClickEffect;

    private void Awake()
    {
        if (instance != null)
        {
            Destroy(gameObject);
        }
        instance = this;

        DontDestroyOnLoad(gameObject);
    }
    void Start()
    {
        InvokeRepeating("CameraSet", 0f, 1f);
    }

    void CameraSet()
    {
        camera = GameObject.Find("Main Camera").GetComponent<Camera>();
    }

    void Update()
    {
        if (Input.GetMouseButtonDown(0))
        {
            mousePos = Input.mousePosition;
            mousePos = camera.ScreenToWorldPoint(mousePos);

            ButtonEffect(mousePos);
        }
    }

    void ButtonEffect(Vector2 pos)
    {
        ButtonClickEffect.transform.position = pos;

        ButtonClickEffect.GetComponent<ParticleSystem>().Play();
    }
}
