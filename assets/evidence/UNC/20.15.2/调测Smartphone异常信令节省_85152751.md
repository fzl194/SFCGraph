# 调测Smartphone异常信令节省

- [操作场景](#ZH-CN_OPI_0185152751__1.3.1)
- [必备事项](#ZH-CN_OPI_0185152751__1.3.2)
- [操作步骤](#ZH-CN_OPI_0185152751__1.3.3)

## [操作场景](#ZH-CN_OPI_0185152751)

在Smartphone终端反复激活，产生大量异常信令的场景下， UNC 和 UDG 通过配置Smartphone异常信令节省功能减少网络的信令负荷。本操作介绍了通过调测手段检查 UNC 和 UDG 是否正确配置该功能的过程。

> **说明**
> 适用于 SGSN 。

## [必备事项](#ZH-CN_OPI_0185152751)

前提条件

- 请仔细阅读[WSFD-206006 Smartphone异常信令节省特性概述](特性概述_86930572.md)。
- 完成[激活Smartphone异常信令节省](激活Smartphone异常信令节省_85152750.md)。

数据

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| 用户跟踪任务 | IMSI | 460123456789 | 测试终端自带 | - |

工具

- 测试终端。
- OM Portal跟踪。

## [操作步骤](#ZH-CN_OPI_0185152751)

1. 检查IMEI或APN NI数据库配置信息。
  > **说明**
  > 根据具体场景选择性查询一种数据库的配置信息。
    - 可选：检查IMEI数据库配置信息。
      进入 “MML命令行-UNC” 窗口。
      [**LST IMEILIB**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/Smartphone管理/终端类型识别/IMEI库管理/查询IMEI库记录（LST IMEILIB）_26305544.md) : SELMODE=选择方式;
          - 预期结果： “设备型号核准号码” 与 “终端类型” 存在对应关系。
            ```
            %%LST IMEILIB: SELMODE=ALL;%%
            RETCODE = 0  操作成功。

            输出结果如下
            ------------
            设备型号核准号码    终端类型       终端详细信息

            12345670            iOS            NULL        
            12345678            Windows        NULL        
            46001111            Black Berry    NULL        
            87654321            Black Berry    NULL        
            (结果个数 = 4)
            ---    END
            ```
          - 异常结果： “设备型号核准号码” 与 “终端类型” 无任何对应关系。
            参考 [激活Smartphone异常信令节省](激活Smartphone异常信令节省_85152750.md) ，查看配置是否正确。
    - 可选：检查APN NI数据库配置信息。
      [**LST APNNILIB**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/Smartphone管理/终端类型识别/APNNI库管理/查询APNNI库记录（LST APNNILIB）_26305546.md) :SELMODE=选择方式;
          - 预期结果： “APNNI” 与 “终端类型” 存在对应关系。
            ```
            %%LST APNNILIB:;%%
            RETCODE = 0  操作成功。

            输出结果如下
            ------------
            APNNI         APN类型    终端类型    终端详细信息

            HUAWEI.CN     签约APN    Windows     cn          
            HUAWEI.COM    请求APN    Android     huawei      
            (结果个数 = 2)
            ---    END
            ```
          - 异常结果： “APNNI” 与 “终端类型” 无任何对应关系。
            参考 [激活Smartphone异常信令节省](激活Smartphone异常信令节省_85152750.md) ，查看配置是否正确。
2. 检查 UNC 是否可识别出用户的终端类型。
  [**DSP COMMMCTX**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/融合接入业务管理/融合用户数据库管理/显示移动性管理上下文的相关信息（DSP COMMMCTX）_58365337.md) :;
    - 预期结果： “终端类型” 有具体的类型结果，例如 “ANDROID” 、 “BLACKBERRY” 等，说明 UNC 可识别出用户的终端类型。
      ```
      %%DSP COMMMCTX: QUERYOPT=BYIMSI, IMSI="460123456789";%%
      RETCODE = 0  操作成功

      MM上下文信息：
      ----------------
                      ..................................   
                               终端类型  =  Black Berry
                      智能终端激活抑制类型 =  NULL
                            智能手机状态  =  否

      ---    END
      ```
    - 异常结果： “终端类型” 没有具体的类型结果，说明 UNC 不可识别出用户的终端类型。
3. 检查抑制规则配置信息。
  [**LST SMARTACT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/Smartphone管理/异常信令节省/激活抑制规则管理/查询激活抑制规则（LST SMARTACT）_26145744.md) :;
    - 预期结果：各项参数显示结果与配置结果相一致。
      ```
      %%LST SMARTACT:;%%
      RETCODE = 0  操作成功。

      查询结果如下
      ------------
                        终端类型  =  Black Berry
      特定原因值拒绝激活功能开关  =  开启
           Backoff Timer分配开关  =  关闭
       Parking APN假激活功能开关  =  关闭
            主动分离用户功能开关  =  关闭
                  激活拒绝原因值  =  Requested service option not subscribed 33
                      分离原因值  =  GPRS services not allowed 7
      (结果个数 = 1)
      ---    END
      ```
    - 异常结果：各项参数显示结果与配置结果不一致或查看不到相关配置信息。
      参考 [激活Smartphone异常信令节省](激活Smartphone异常信令节省_85152750.md) ，查看配置是否正确。
4. 检查抑制规则参数配置信息。
  [**LST SMARTACTPARA**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/Smartphone管理/异常信令节省/激活抑制参数管理/查询激活抑制参数（LST SMARTACTPARA）_72345341.md) :;
    - 预期结果：各项参数显示结果与配置的结果一致。
      ```
      %%LST SMARTACTPARA:;%%
      RETCODE = 0  操作成功。

      输出结果如下
      ------------
                 识别异常激活行为的门限（times/h）  =  30
                             抑制唤醒定时器（min）  =  30
                                       Parking APN  =  huawei2.com
      分离异常用户的SERVICE REQUEST门限（times/h）  =  120
             分离异常用户的激活行为门限（times/h）  =  30
                        特定原因值拒绝激活唤醒开关  =  关
                         Parking APN假激活唤醒开关  =  开
      (结果个数 = 1)
      ---    END
      ```
    - 异常结果：各项参数显示结果与配置的结果不一致。
      参考 [激活Smartphone异常信令节省](激活Smartphone异常信令节省_85152750.md) ，查看配置是否正确。
5. 进行业务测试。
    a. [创建用户跟踪。](../../../../../网络运维/日常维护/UNC基础运维操作/创建消息跟踪/创建用户跟踪_71693950.md)
      参数选择如下：
          - IMSI：被跟踪用户的IMSI。
          - 其它参数：选择默认值。
    b. 用户附着成功，在1小时内重复发起多次激活、去激活PDP上下文流程。
      查看跟踪结果，用户成功发起的N-1次激活PDP上下文流程，消息显示如 [图1](#ZH-CN_OPI_0185152751__zh-cn_opi_0130429038_fig1) 所示。
      > **说明**
      > N次指的是命令 [**SET SMARTACTPARA**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/Smartphone管理/异常信令节省/激活抑制参数管理/设置激活抑制参数（SET SMARTACTPARA）_26305550.md) 中的参数 “ABNORACTTHRESH” （识别异常激活行为的门限）设置为 “N” 次，N的取值范围为2~1000。
      **图1** 用户第1次到第N-1次激活PDP上下文成功消息（样例）

      <br>

      ![](调测Smartphone异常信令节省_85152751.assets/zh-cn_image_0185156592_2.png "点击放大")

      <br>
    c. 用户发起第N次激活PDP上下文流程，查看跟踪结果。
          - 场景1：只配置了特定原因值拒绝激活抑制规则
                  - 预期结果：用户发起的第N次激活PDP上下文流程失败， UNC 发送给用户的Activate PDP context reject消息中携带的拒绝原因值与配置的参数一致，例如当配置的 “SPECCAUSESW” （激活拒绝原因值）参数为 “requested-service-option-not-subscribed (33)” 时，消息跟踪结果如 [图2](#ZH-CN_OPI_0185152751__zh-cn_opi_0130429038_fig2) 所示。
                    **图2** UNC 拒绝用户激活消息的原因值（样例）

                    <br>

                    ![](调测Smartphone异常信令节省_85152751.assets/zh-cn_image_0185156593_2.png "点击放大")

                    <br>
                  - 异常结果：用户发起的第N次激活PDP上下文流程成功，显示消息如 [图1](#ZH-CN_OPI_0185152751__zh-cn_opi_0130429038_fig1) 所示。
                    参考 [激活Smartphone异常信令节省](激活Smartphone异常信令节省_85152750.md) ，查看配置是否正确。
          - 场景2：只配置了Parking APN假激活抑制规则
                  - 预期结果：在用户发起的第N次激活PDP上下文流程中，查看到用户发送给GGSN的Create PDP Context Request消息中携带的APN NI与配置的参数一致，例如当配置的 “PARKING APNNI” 参数为 “huawei2.com” 时，消息跟踪结果如 [图3](#ZH-CN_OPI_0185152751__zh-cn_opi_0130429038_fig4) 所示。
                    **图3** 创建PDP上下文消息中携带的APNNI（样例）

                    <br>

                    ![](调测Smartphone异常信令节省_85152751.assets/zh-cn_image_0185156594_2.png "点击放大")

                    <br>
                  - 异常结果：用户发送给GGSN的Create PDP Context Request消息中携带的APN NI与配置的参数不一致。
                    参考 [激活Smartphone异常信令节省](激活Smartphone异常信令节省_85152750.md) ，查看配置是否正确。
          - 场景3：只配置了主动分离用户抑制规则
                  - 预期结果：在用户发起的第N次激活PDP上下文流程中，查看到 UNC 发送给用户的PMM Detach Request消息中携带的分离原因值与配置的参数一致，例如当配置的 “SMARTDETACHCAUSE” （分离原因值）参数为 “gprs-services-not-allowed (7)” 时，消息跟踪结果如 [图4](#ZH-CN_OPI_0185152751__zh-cn_opi_0130429038_fig6) 所示。
                    **图4** UNC 发起分离消息中的原因值（样例）

                    <br>

                    ![](调测Smartphone异常信令节省_85152751.assets/zh-cn_image_0185156595_2.png "点击放大")

                    <br>
                  - 异常结果： UNC 发送给用户的PMM Detach Request消息中携带的分离原因值与配置的参数不一致。
                    参考 [激活Smartphone异常信令节省](激活Smartphone异常信令节省_85152750.md) ，查看配置是否正确。
          - 场景4：配置了特定原因值拒绝激活、Parking APN假激活和主动分离用户抑制规则中的任意两种或三种
                  - 预期结果：查看跟踪结果，如果查看到的过程结果与 [场景1](#ZH-CN_OPI_0185152751__zh-cn_opi_0130429038_c1) 、 [场景2](#ZH-CN_OPI_0185152751__zh-cn_opi_0130429038_c2) 和 [场景3](#ZH-CN_OPI_0185152751__zh-cn_opi_0130429038_c3) 中的任意一个或多个场景的预期结果一致，则说明该对应场景的抑制规则被触发，配置成功。
                  - 异常结果：查看跟踪结果，如果查看到的过程结果与 [场景1](#ZH-CN_OPI_0185152751__zh-cn_opi_0130429038_c1) 、 [场景2](#ZH-CN_OPI_0185152751__zh-cn_opi_0130429038_c2) 和 [场景3](#ZH-CN_OPI_0185152751__zh-cn_opi_0130429038_c3) 中的任意一个场景的预期结果不一致，则说明抑制规则配置有误或数据规划错误。
                    参考 [激活Smartphone异常信令节省](激活Smartphone异常信令节省_85152750.md) ，查看配置是否正确。
