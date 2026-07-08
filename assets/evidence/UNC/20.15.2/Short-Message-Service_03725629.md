# Short Message Service

- [SMS消息流程](#ZH-CN_TOPIC_0000001603725629__1.3.1.1)

#### [SMS消息流程](#ZH-CN_TOPIC_0000001603725629)

Short Message Service（SMS），全称为短消息业务。在网络中，短消息提供两种方案，SMS over IMS和SMS over NAS。

- SMS over IMS：短消息业务和其他数据业务一样，需要建立至IMS网络的用户面通路，故也称为IP短消息。该方案主要应用于手机终端，并且终端用户签约了IMS业务，5G网络和4G网络中IP短消息实现方案无差异，经由用户面网关UPF完成短消息通过数据通道的传输，MT跟普通数据一样，需要从UPF触发DDN的流程。具体流程请参考 [5G 短消息](../../../短消息功能/5G短消息_51020664.md) 。
- SMS over NAS：5G网络引入了SMSF（Short Message Service Function，短信服务功能）支持NAS短信，该方案主要应用于数据卡和物联网终端（如IoT、CPE等）。在NAS短信流程中，存在UE不可达的情况。
    - eDRX用户主要应用SMS over NAS。
          - 当用户在寻呼窗口时，流程与MT短消息类似，请参照[MT短消息](../../../短消息功能/5G短消息/短消息业务流程/MT短消息_41955496.md)。
          - 当用户不在寻呼窗口时，流程关键变化参照[图1](#ZH-CN_TOPIC_0000001603725629__fig20317151184114)。
            **图1** eDRX模式下SM发送流程

            ![](Short Message Service_03725629.assets/zh-cn_image_0000001552967454_2.png)
                  1. **Step1&2**：NF服务消费者（例如SMSF）向AMF发送Namf_MT_EnableUEReachability Request消息。若此时UE不在寻呼窗口内，AMF给SMSF返回Namf_MT_EnableUEReachability Response消息，携带状态码为504 Gateway Timeout “UE_NOT_REACHABLE“。AMF此时会将该用户加入延迟寻呼列表。
                  2. **Step 3**：SMSF返回失败响应消息Failure Report给SMSC。
                  3. **Step 4**：SMSC通知UDM，UE接收短消息失败。UDM将该用户设置为MNRF（Mobile Station Not Reachable Flag）。
                  4. **Step 5：**UDM向AMF发送消息Namf_EventExposure_CreateSubscription Request订阅UE可达性事件。
                  5. **Step 7**：当用户到达寻呼窗口时，AMF寻呼用户，寻呼成功后，复用普通用户可达后的处理。
                  6. **Step 8**：AMF向UDM发送Namf_EventExposure_Notify Request消息，通知UDM对应UE进入可达状态。如果发生了Inter AMF注册流程，新侧AMF会向UDM发送的Nudm_UECM_Registration Request消息，进行注册。
                  7. **Step 9&10**：UDM收到Namf_EventExposure_Notify Request/Nudm_UECM_Registration Request后，UDM删除MNRF标识，并通知SMSC重新下发短消息，SMSC重新在UDM中查询SMSF的信息。
                  8. **Step 11**：UE发起服务请求，后续流程同普通的MT流程。
            **性能指标**
            下表中性能指标的打点请见流程 [表1](#ZH-CN_TOPIC_0000001603725629__table15301633287) 。
            *表1 AMF性能指标*

            | 测量网元 | 测量集 | 测量单元 | 测量对象 | 测量指标 | 测量点触发消息 | 流程图打点 |
            | --- | --- | --- | --- | --- | --- | --- |
            | AMF | AMF移动性管理 | N2模式寻呼 | 整机 | [1929450141 N2模式SMS发起的eDRX寻呼请求次数](../../../../../../OM参考/性能指标/UNC业务性能指标/业务性能指标/AMF_SMF_GW-C_NRF_NSSF_SMSF_NCG业务性能指标/AMF 移动性管理/N2模式寻呼/1929450141 N2模式SMS发起的eDRX寻呼请求次数_25632167.md) | Paging | P1b |
            | AMF | AMF移动性管理 | N2模式寻呼 | 整机 | [1929450142 N2模式SMS发起的eDRX寻呼成功次数](../../../../../../OM参考/性能指标/UNC业务性能指标/业务性能指标/AMF_SMF_GW-C_NRF_NSSF_SMSF_NCG业务性能指标/KPI_18600245.md) | Service Request | P9b |
