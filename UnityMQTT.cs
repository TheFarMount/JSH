using System.Collections;

using System.Collections.Generic;

using UnityEngine;

using UnityEngine.UI;

using HslCommunication.MQTT;

using System.Text;

using System.Diagnostics;

using System;

using System.IO;

using Newtonsoft.Json.Linq;

public class MQTT : MonoBehaviour

{
    private MqttClient mqttClient;

    void Start()

    {

        mqttClient = new MqttClient(new MqttConnectionOptions()

        {

            ClientId = "ABC",                     

            IpAddress = "54.87.92.106",             

        });


        HslCommunication.OperateResult connect = mqttClient.ConnectServer();

        if (connect.IsSuccess)

        {


            UnityEngine.Debug.Log("connect success");

        }

        else

        {

            UnityEngine.Debug.Log("connect failed");

        }

        HslCommunication.OperateResult sub = mqttClient.SubscribeMessage("/python/mqtt1");

        if (sub.IsSuccess)

        {

            UnityEngine.Debug.Log("subscribe success");

        }

        else

        {

            UnityEngine.Debug.Log("subscribr failed");

        }


        mqttClient.OnMqttMessageReceived += (MqttClient client, string topic, byte[] payload) =>

        {

            UnityEngine.Debug.Log("Topic:" + topic);

            UnityEngine.Debug.Log("Payload:" + Encoding.UTF8.GetString(payload));


        };

    }

    private void Update()

    {

    }

}
