# 调测Flash CSFB with RIM

- [操作场景](#ZH-CN_OPI_0164009932__1.3.1)
- [必备事项](#ZH-CN_OPI_0164009932__1.3.2)
- [操作步骤](#ZH-CN_OPI_0164009932__1.3.3)

## [操作场景](#ZH-CN_OPI_0164009932)

本操作介绍了通过调测手段检查 UNC 是否正确配置该功能的过程。

> **说明**
> 适用于MME

## [必备事项](#ZH-CN_OPI_0164009932)

前提条件

已经加载支持该特性的License。

数据

该操作无需准备数据。

## [操作步骤](#ZH-CN_OPI_0164009932)

- 调测Flash CSFB业务。
    1. 创建用户跟踪，Gb接口跟踪，Iu接口跟踪，GTPC跟踪。
    2. 用户附着成功，移动到BSS/RNC覆盖区域，发起语音呼叫业务，触发跨小区重选，eNodeB识别目标网络为GERAN/UTRAN，且不支持PS切换，但支持CCO，发起RIM流程。
    3. 查看跟踪结果。
          - 预期结果：MME将eNodeB发送的RAN Information Request消息透传给SGSN，且Target CELL为BSS/RNC覆盖区域。并且MME将SGSN回传的Relay RAN Information透传给eNodeB。如 [图1](#ZH-CN_OPI_0164009932__fig1) ， [图2](#ZH-CN_OPI_0164009932__fig2) 所示，其中 [图1](#ZH-CN_OPI_0164009932__fig1) 为S1-MME接口跟踪， [图2](#ZH-CN_OPI_0164009932__fig2) 为GTP-C接口跟踪。
            **图1** MME将eNodeB发送的RAN Information Request消息透传给SGSN（样例）

            <br>

            ![](调测Flash CSFB with RIM_64009932.assets/cn_10_18_1452103_fig01_2.png "点击放大")

            <br>
            **图2** MME将SGSN回传的Relay RAN Information透传给eNodeB（样例）

            <br>

            ![](调测Flash CSFB with RIM_64009932.assets/cn_10_18_1452103_fig02_2.png "点击放大")

            <br>
          - 异常结果：MME未将RAN Information Request消息透传给SGSN或未将SGSN回传的Reply RAN Information透传给eNodeB。
