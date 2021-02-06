using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ClientDontDestroy : MonoBehaviour
{
    public static ClientDontDestroy instance;

    private void Awake()
    {
        if (instance != null)
        {
            Destroy(gameObject);
        }
        instance = this;

        DontDestroyOnLoad(gameObject);
    }
}
