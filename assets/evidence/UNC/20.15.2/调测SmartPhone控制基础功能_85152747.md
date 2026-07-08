# 调测SmartPhone控制基础功能

- [操作场景](#ZH-CN_OPI_0185152747__1.3.1)
- [必备事项](#ZH-CN_OPI_0185152747__1.3.2)
- [操作步骤](#ZH-CN_OPI_0185152747__1.3.3)

## [操作场景](#ZH-CN_OPI_0185152747)

Smartphone的应用使网络信令日益增加， UNC 通过SmartPhone控制基础功能避免网络拥塞和设备过载现象的发生。本操作介绍了通过调测手段检查 UNC 是否正确配置该功能的过程。

> **说明**
> 适用于 SGSN 。

## [必备事项](#ZH-CN_OPI_0185152747)

前提条件

- 请仔细阅读[WSFD-206005 Smartphone控制基础功能特性概述](特性概述_85628479.md)。
- 完成[激活SmartPhone控制基础功能](激活SmartPhone控制基础功能_85152746.md)。

数据

该操作无需准备数据。

工具

- 测试终端。
- OM Portal跟踪。

## [操作步骤](#ZH-CN_OPI_0185152747)

- 禁止去激活非活动PDP场景。
    1. 进入 “MML命令行-UNC” 窗口。
    2. 检查是否禁止 UNC 去激活非活动PDP。
      [**LST SMARTCFG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/Smartphone管理/Smartphone控制基础功能/查询智能用户功能（LST SMARTCFG）_72225429.md) :;
          - 预期结果：各项参数显示结果与配置结果一致，其中 “是否启用SMART用户识别功能” 显示结果为 “是” ， “SMART用户是否禁止启用去活非活动PDP功能” 显示结果为 “是” 。
            ```
            %%LST SMARTCFG:;%%
            RETCODE = 0  操作成功。

            输出结果如下
            ------------
                                是否启用SMART用户识别功能  =  是
            识别SMART用户的SERVICE REQUEST门限（times/h）  =  10
                              SMART用户是否禁止启用DT功能  =  是
                   SMART用户是否禁止启用去活非活动PDP功能  =  是
            (结果个数 = 1)
            ---    END
            ```
          - 异常结果： “是否启用SMART用户识别功能” 和 “SMART用户是否禁止启用去活非活动PDP功能” 参数显示结果与配置结果不一致。
            参考 [激活SmartPhone控制基础功能](激活SmartPhone控制基础功能_85152746.md) ，查看配置是否正确。
    3. 进行业务测试。
          a. [创建用户跟踪](../../../../../网络运维/日常维护/UNC基础运维操作/创建消息跟踪/创建用户跟踪_71693950.md)。
            参数选择如下：
                  - IMSI：被跟踪用户的IMSI。
                  - 其它参数：选择默认值。
          b. 用户附着成功，一小时内发起N次Service Request流程。
            > **说明**
            > N次指命令 [**SET SMARTCFG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/Smartphone管理/Smartphone控制基础功能/设置智能用户功能（SET SMARTCFG）_26145750.md) 中的参数 “SERVREQTHRESHOLD” （识别SMART用户的SERVICE REQUEST门限）设置为 “N” 次，N的取值范围为2~1000。
          c. 查询用户MM上下文，确定用户是否处于智能手机状态。
            [**DSP COMMMCTX**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/融合接入业务管理/融合用户数据库管理/显示移动性管理上下文的相关信息（DSP COMMMCTX）_58365337.md) :;
                  - 预期结果： “智能手机状态” 显示结果为 “是” 。
                    ```
                    %%DSP COMMMCTX: QUERYOPT=BYIMSI, IMSI="460123456789";%%
                    RETCODE = 0  操作成功

                    MM上下文信息：
                    ----------------
                               
                                            智能手机状态  =  是

                    ---    END
                    ```
                  - 异常结果： “智能手机状态” 显示结果为 “否” ，说明此用户没有被识别为智能手机，不能禁止 UNC 去激活非活动PDP。
          d. 用户激活PDP上下文成功，并保持T时间内不进行数据传输。
            > **说明**
            > T指命令 [**ADD CHGBEHA**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/计费管理/计费行为参数配置/增加计费行为参数(ADD CHGBEHA)_26145366.md) 中的参数 “PURGELEN” （关闭空闲PDP定时器时长）设置为 “T” 时间，T的取值范围为30min~1440min。此时间为 UNC 判断是否自动去激活非活动PDP的定时器时间，如果在定时器时间内用户激活的PDP没有进行数据传输，即PDP一直保持非活动状态，则在定时器超时后 UNC 将自动去激活此PDP。
          e. 查看跟踪结果。观察 UNC 是否发起去激活该PDP的流程。
                  - 预期结果：不存在 UNC 去激活该PDP流程的任何消息。
                  - 异常结果：存在 UNC 去激活该PDP流程的消息，即存在 UNC 向MS发送的Deactivate PDP Context Request消息。
                    参考 [激活SmartPhone控制基础功能](激活SmartPhone控制基础功能_85152746.md) ，查看配置是否正确。
- 禁止基于用户识别的Direct Tunnel功能场景
    1. 进入 “MML命令行-UNC” 窗口。
    2. 检查是否禁止Smartphone用户使用Direct Tunnel功能。
      [**LST SMARTCFG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/Smartphone管理/Smartphone控制基础功能/查询智能用户功能（LST SMARTCFG）_72225429.md) :;
          - 预期结果：各项参数显示结果与配置结果一致，其中 “是否启用SMART用户识别功能” 显示结果为 “是” ， “SMART用户是否禁止启用DT功能” 显示结果为 “是” 。
            ```
            %%LST SMARTCFG:;%%
            RETCODE = 0  操作成功。

            输出结果如下
            ------------
                                是否启用SMART用户识别功能  =  是
            识别SMART用户的SERVICE REQUEST门限（times/h）  =  10
                              SMART用户是否禁止启用DT功能  =  是
                   SMART用户是否禁止启用去活非活动PDP功能  =  否
            (结果个数 = 1)
            ---    END
            ```
          - 异常结果： “是否启用SMART用户识别功能” 和 “SMART用户是否禁止启用DT功能” 参数显示结果与配置结果不一致。
            参考 [激活SmartPhone控制基础功能](激活SmartPhone控制基础功能_85152746.md) ，查看配置是否正确。
    3. 进行业务测试。
          a. [创建用户跟踪](../../../../../网络运维/日常维护/UNC基础运维操作/创建消息跟踪/创建用户跟踪_71693950.md) 。
            参数选择如下：
                  - IMSI：被跟踪用户的IMSI。
                  - 其它参数：选择默认值。
          b. 配置用户满足使用Direct Tunnel功能的条件（具体内容请参考 [WSFD-104506 支持Direct Tunnel功能](../../组网功能/WSFD-104506 支持Direct Tunnel功能_91285441.md) ）。用户附着成功，一小时内发起N次Service Request流程。
            > **说明**
            > N次指命令 [**SET SMARTCFG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/Smartphone管理/Smartphone控制基础功能/设置智能用户功能（SET SMARTCFG）_26145750.md) 中的参数 “SERVREQTHRESHOLD” （识别SMART用户的SERVICE REQUEST门限）设置为 “N” 次，N的取值范围为2~1000。
          c. 查看跟踪结果。
                  - 预期结果：前N-1次Service Request流程中都存在Update PDP Context Request消息，且消息中的dti信元都为1，如 [图1](#ZH-CN_OPI_0185152747__zh-cn_opi_0130429025_fig1) 所示。
                    **图1** 前N-1次Service Request流程消息（样例）

                    <br>

                    ![](调测SmartPhone控制基础功能_85152747.assets/zh-cn_image_0185156571_2.png "点击放大")

                    <br>
                    第N次Service Request流程中，不存在Update PDP Context Request消息，如 [图2](#ZH-CN_OPI_0185152747__zh-cn_opi_0130429025_fig2) 所示。
                    **图2** 第N次Service Request流程消息（样例）

                    <br>

                    ![](调测SmartPhone控制基础功能_85152747.assets/zh-cn_image_0185156572_2.png "点击放大")

                    <br>
                  - 异常结果：用户的PDP上下文信息与 [图1](#ZH-CN_OPI_0185152747__zh-cn_opi_0130429025_fig1) 、 [图2](#ZH-CN_OPI_0185152747__zh-cn_opi_0130429025_fig2) 不一致。
                    参考 [激活SmartPhone控制基础功能](激活SmartPhone控制基础功能_85152746.md) ，查看配置是否正确。
- 禁止基于终端类型的Direct Tunnel功能场景
    1. 检查IMEI或APN NI数据库配置信息。
      > **说明**
      > 根据具体场景选择性查询一种数据库的配置信息。
          - 可选：检查IMEI数据库配置信息。
            进入 “MML命令行-UNC” 窗口。
            [**LST IMEILIB**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/Smartphone管理/终端类型识别/IMEI库管理/查询IMEI库记录（LST IMEILIB）_26305544.md) : SELMODE=选择方式;
                  - 预期结果： “设备型号核准号码” 与 “终端类型” 存在对应关系。
                    ```
                    %%LST IMEILIB:SELMODE=ALL;%%
                    RETCODE = 0  操作成功。

                    输出结果如下
                    --------------
                     设备型号核准号码  终端类型  终端详细信息

                     12345677          Windows          NULL        
                     12345678          Black Berry      NULL        
                     87654321          Black Berry      NULL        
                     12345670          iOS              ok          
                    (结果个数 = 4)
                    ---    END
                    ```
                  - 异常结果： “设备型号核准号码” 与 “终端类型” 无任何对应关系。
                    参考 [激活SmartPhone控制基础功能](激活SmartPhone控制基础功能_85152746.md) ，查看配置是否正确。
          - 可选：检查APN NI数据库配置信息。
            [**LST APNNILIB**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/Smartphone管理/终端类型识别/APNNI库管理/查询APNNI库记录（LST APNNILIB）_26305546.md) :SELMODE=选择方式;
                  - 预期结果： “APNNI” 与 “终端类型” 存在对应关系。
                    ```
                    %%LST APNNILIB:;%%
                    RETCODE = 0  操作成功。

                    输出结果如下
                    ------------
                    APNNI         APN类型    终端类型       终端详细信息

                    HUAWEI.CN     签约APN    Windows        CN          
                    HUAWEI.COM    请求APN    Android        huawei      
                    (结果个数 = 2)
                    ---    END
                    ```
                  - 异常结果： “APNNI” 与 “终端类型” 无任何对应关系。
                    参考 [激活SmartPhone控制基础功能](激活SmartPhone控制基础功能_85152746.md) ，查看配置是否正确。
    2. 检查 UNC 是否可识别出用户的终端类型。
      [**DSP COMMMCTX**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/融合接入业务管理/融合用户数据库管理/显示移动性管理上下文的相关信息（DSP COMMMCTX）_58365337.md) :;
          - 预期结果： “终端类型” 有具体的类型结果，例如 “ANDROID” 、 “BLACKBERRY” 等，说明 UNC 可识别出用户的终端类型。
            ```
            %%DSP COMMMCTX: QUERYOPT=BYIMSI, IMSI="460123456789";%%
            RETCODE = 0  操作成功

            MM上下文信息：
            ----------------
                               
                                        终端类型  =  Black Berry
                                抑制中APN网络标识 =  HUAWEI123
                             智能终端激活抑制类型 =  NULL
                                    智能手机状态  =  否
            ---    END
            ```
          - 异常结果： “终端类型” 没有具体的类型结果，说明 UNC 不可识别出用户的终端类型。
    3. 检查是否对已识别出的Smartphone终端类型用户禁止使用Direct Tunnel功能。
      [**LST SMARTDT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/Smartphone管理/基于终端类型的DT限制/查询基于终端类型的DT限制（LST SMARTDT）_72345339.md) :;
          - 预期结果： “DT限制开关” 显示结果为 “开启” 。
            ```
            %%LST SMARTDT: UETYPE=WINDOWS;%%
            RETCODE = 0  操作成功。

            输出结果如下
            ------------
              终端类型  =  Windows
            DT限制开关  =  开启
                  描述  =  NULL
            (结果个数 = 1)
            ---    END
            ```
          - 异常结果： “DT限制开关” 显示结果为 “关闭” 或查看不到相关配置信息。
            参考 [激活SmartPhone控制基础功能](激活SmartPhone控制基础功能_85152746.md) ，查看配置是否正确。
    4. 进行业务测试。
          a. [创建用户跟踪任务。](../../../../../网络运维/日常维护/UNC基础运维操作/创建消息跟踪/创建用户跟踪_71693950.md)
            参数选择如下：
                  - IMSI：被跟踪用户的IMSI。
                  - 其它参数：选择默认值。
          b. 用户附着，令用户满足Direct Tunnel条件（具体内容请参考 [WSFD-104506 支持Direct Tunnel功能](../../组网功能/WSFD-104506 支持Direct Tunnel功能_91285441.md) ），激活PDP上下文，并进行Service Request流程。
          c. 查看跟踪结果。
                  - 预期结果：用户的Service Request流程中不存在Update PDP Context Request消息，如 [图3](#ZH-CN_OPI_0185152747__zh-cn_opi_0130429025_fig3) 所示。
                    **图3** Service Request流程消息（样例）

                    <br>

                    ![](调测SmartPhone控制基础功能_85152747.assets/zh-cn_image_0185156572_2.png "点击放大")

                    <br>
                  - 异常结果：用户的Service Request流程消息与 [图3](#ZH-CN_OPI_0185152747__zh-cn_opi_0130429025_fig3) 不一致。
                    参考 [激活SmartPhone控制基础功能](激活SmartPhone控制基础功能_85152746.md) ，查看配置是否正确。
- 调测SmartPaging功能。
  > **说明**
  > 在调测操作前做如下准备：
  >
  > - 执行[**ADD LOWPRIDSCP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/移动性管理/低优先级DSCP/增加低优先级业务DSCP(ADD LOWPRIDSCP)_26145510.md)命令配置0-63为低优先级寻呼消息。
  > - 执行[**ADD GGSNCHARACT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/GTP-C接口管理/GnGp-GGSN_S5_S8接口管理/GGSN属性/增加GGSN属性配置信息(ADD GGSNCHARACT)_72225613.md)命令配置支持SmartPaging功能。
  > - SPP进程已处于四级过载。
    1. 进入 “MML命令行-UNC” 窗口。
    2. 查询GGSN是否支持SmartPaging功能。
      [**LST GGSNCHARACT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/GTP-C接口管理/GnGp-GGSN_S5_S8接口管理/GGSN属性/查询GGSN属性配置信息(LST GGSNCHARACT)_26145936.md) :;
      ```
      %%LST GGSNCHARACT: RANGE=SPECIAL_GGSN, IPT=IPV4, GGSNIPV4="10.12.168.219", MASKV4="255.255.255.255";%%
      RETCODE = 0  操作成功。

      GGSN属性配置表
      --------------
                     对端设备范围  =  指定GGSN
                       IP地址类型  =  IPV4
               GGSN的信令面IP地址  =  10.12.168.219
                             掩码  =  255.255.255.255
         GGSN是否支持DirectTunnel  =  不支持
                GGSN支持的QoS版本  =  R99QOS
              GCDR/e-GCDR信息上报  =  NULL
                     发送私有信息  =  OFF
      GnGp接口的GTP-C路径版本规则  =  V1
         GGSN是否支持Smart Paging  =  是
                  GGSN是否支持VIP  =  支持
                             描述  =  NULL
      (结果个数 = 1)
      ---    END
      ```
          - 预期结果：参数“GGSN是否支持Smart Paging”为“YES”。
          - 异常结果：参数 “GGSN是否支持Smart Paging” 为 “NO” 。
      参考 [激活SmartPhone控制基础功能](激活SmartPhone控制基础功能_85152746.md) ，查看配置是否正确。
    3. 查询低优先级业务识别功能。
      [**LST LOWPRIDSCP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/移动性管理/低优先级DSCP/查询低优先级业务DSCP(LST LOWPRIDSCP)_26305322.md) :;
      ```
      %%LST LOWPRIDSCP:;%%
      RETCODE = 0  操作成功。

      输出结果如下
      ------------
      DSCP起始值  =  0
      DSCP结束值  =  10
      (结果个数 = 1)
      ---    END
      ```
          - 预期结果：“DSCP起始值”和“DSCP结束值”有具体的结果。
          - 异常结果： “DSCP起始值” 和 “DSCP结束值” 没有具体的结果
      参考 [激活SmartPhone控制基础功能](激活SmartPhone控制基础功能_85152746.md) ，查看配置是否正确。
    4. 进行业务测试。
          a. [创建用户跟踪](../../../../../网络运维/日常维护/UNC基础运维操作/创建消息跟踪/创建用户跟踪_71693950.md) 。
            参数选择如下：

            - IMSI：被跟踪用户的IMSI。
                  - 其它参数：选择默认值。
          b. [创建Iu接口跟踪](../../../../../网络运维/日常维护/UNC基础运维操作/创建消息跟踪/创建接口跟踪_71693952.md) 。
            参数选择如下：

            - 进程类型：固定为SGP。
                  - RNC索引：对接RNC的索引。
                    命令： [**LST RNC**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/Iu接口管理/Iu接口RNC信息/查询Iu接口RNC信息(LST RNC)_72345641.md) :;查询。
                  - 其它参数：选择默认值。
          c. 用户附着，进行PDP激活，并且发起下行数据。
          d. 查看跟踪结果。
                  - 预期结果：SGSN收到用户的下行数据传输后未触发寻呼。
                  - 异常结果：SGSN收到用户的下行数据传输后触发寻呼。
