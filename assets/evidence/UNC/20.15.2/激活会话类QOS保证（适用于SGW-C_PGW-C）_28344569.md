# 激活 会话类QOS保证 （适用于SGW-C/PGW-C）

- [操作场景](#ZH-CN_OPI_0228344569__1.3.1)
- [必备事项](#ZH-CN_OPI_0228344569__1.3.2)
- [操作步骤](#ZH-CN_OPI_0228344569__1.3.3)
- [任务示例](#ZH-CN_OPI_0228344569__1.3.4)

## [操作场景](#ZH-CN_OPI_0228344569)

当移动IP网络中部署了具有实时性特点的会话类业务时，要求移动IP网络转发时延低、抖动小，因此需要提供端到端的QoS保证。

> **说明**
> 适用于SGW-C、PGW-C。

## [必备事项](#ZH-CN_OPI_0228344569)

前提条件

- 请仔细阅读 [WSFD-109202 会话类QoS保证特性概述](WSFD-109202 会话类QOS保证特性概述_28258186.md) 。
- 完成配置普通APN [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md) 。
- 完成加载License。

数据

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| [**SET QOSGLOBAL**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/全局QoS功能配置/全局QoS参数/设置全局QoS配置（SET QOSGLOBAL）_09652976.md) | QOSPROFILENAME (QoS Profile名) | qos1 | 本端规划 | 配置全局的QoS信息。 |
| [**SET QOSGLOBAL**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/全局QoS功能配置/全局QoS参数/设置全局QoS配置（SET QOSGLOBAL）_09652976.md) | BINDEPSSUBQOS（EPS用户QOS） | ENABLE | 本端规划 | 配置全局的QoS信息。 |
| [**SET QOSGLOBAL**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/全局QoS功能配置/全局QoS参数/设置全局QoS配置（SET QOSGLOBAL）_09652976.md) | EPSSUBQOS（EPS用户QOS索引） | 1 | 本端规划 | 配置全局的QoS信息。 |
| [**SET DEFEPSQOS**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/EPS QoS配置/全局EPS QoS纠错/设置EPS缺省QoS参数（SET DEFEPSQOS）_09653732.md) | QOSCLASSID（QCI值） | 1 | 本端规划 | 配置EPS QoS缺省QoS参数。 |
| [**SET DEFEPSQOS**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/EPS QoS配置/全局EPS QoS纠错/设置EPS缺省QoS参数（SET DEFEPSQOS）_09653732.md) | ARPVALUE（ARP值） | 1 | 本端规划 | 配置EPS QoS缺省QoS参数。 |
| [**SET DEFEPSQOS**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/EPS QoS配置/全局EPS QoS纠错/设置EPS缺省QoS参数（SET DEFEPSQOS）_09653732.md) | GBRDL (下行GBR(千比特/秒)) | 200bit/s | 本端规划 | 配置EPS QoS缺省QoS参数。 |
| [**SET DEFEPSQOS**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/EPS QoS配置/全局EPS QoS纠错/设置EPS缺省QoS参数（SET DEFEPSQOS）_09653732.md) | GBRUL（上行保证带宽） | 230bit/s | 本端规划 | 配置EPS QoS缺省QoS参数。 |
| [**SET DEFEPSQOS**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/EPS QoS配置/全局EPS QoS纠错/设置EPS缺省QoS参数（SET DEFEPSQOS）_09653732.md) | MBRDL（下行最大带宽） | 300bit/s | 本端规划 | 配置EPS QoS缺省QoS参数。 |
| [**SET DEFEPSQOS**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/EPS QoS配置/全局EPS QoS纠错/设置EPS缺省QoS参数（SET DEFEPSQOS）_09653732.md) | MBRUL（上行最大带宽） | 300bit/s | 本端规划 | 配置EPS QoS缺省QoS参数。 |
| [**SET DEFEPSQOS**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/EPS QoS配置/全局EPS QoS纠错/设置EPS缺省QoS参数（SET DEFEPSQOS）_09653732.md) | APNAMBRDL（下行APN AMBR） | 1000bit/s | 本端规划 | 配置EPS QoS缺省QoS参数。 |
| [**SET DEFEPSQOS**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/EPS QoS配置/全局EPS QoS纠错/设置EPS缺省QoS参数（SET DEFEPSQOS）_09653732.md) | APNAMBRUL（上行APN AMBR） | 1000bit/s | 本端规划 | 配置EPS QoS缺省QoS参数。 |
| [**ADD QOSPROFILE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/QoS模板/增加QoS描述配置（ADD QOSPROFILE）_09654430.md) | QOSPROFILENAME (QoS Profile名) | qos2 | 本端规划 | 配置QosProfile的配置信息。 |
| [**ADD EPSQOSACTION**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/EPS QoS配置/EPS QoS控制动作/增加EPS QoS控制动作配置（ADD EPSQOSACTION）_09654382.md) | QOSPROFILENAME (QoS Profile名) | qos2 | 本端规划 | 配置QoS上下行保证带宽门限、最高带宽门限以及带宽超过门限值时对QoS用户的处理动作。 |
| [**ADD EPSQOSACTION**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/EPS QoS配置/EPS QoS控制动作/增加EPS QoS控制动作配置（ADD EPSQOSACTION）_09654382.md) | QCI（QCI值） | 1 | 本端规划 | 配置QoS上下行保证带宽门限、最高带宽门限以及带宽超过门限值时对QoS用户的处理动作。 |
| [**ADD EPSQOSACTION**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/EPS QoS配置/EPS QoS控制动作/增加EPS QoS控制动作配置（ADD EPSQOSACTION）_09654382.md) | GBRDL（下行保证带宽） | 256bit/s | 本端规划 | 配置QoS上下行保证带宽门限、最高带宽门限以及带宽超过门限值时对QoS用户的处理动作。 |
| [**ADD EPSQOSACTION**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/EPS QoS配置/EPS QoS控制动作/增加EPS QoS控制动作配置（ADD EPSQOSACTION）_09654382.md) | GBRDLACTION（超过下行GBR的处理） | DEGRADE(降级) | 本端规划 | 配置QoS上下行保证带宽门限、最高带宽门限以及带宽超过门限值时对QoS用户的处理动作。 |
| [**ADD EPSQOSACTION**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/EPS QoS配置/EPS QoS控制动作/增加EPS QoS控制动作配置（ADD EPSQOSACTION）_09654382.md) | GBRUL（上行保证带宽） | 128bit/s | 本端规划 | 配置QoS上下行保证带宽门限、最高带宽门限以及带宽超过门限值时对QoS用户的处理动作。 |
| [**ADD EPSQOSACTION**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/EPS QoS配置/EPS QoS控制动作/增加EPS QoS控制动作配置（ADD EPSQOSACTION）_09654382.md) | GBRULACTION（超过上行GBR的处理） | DEGRADE(降级) | 本端规划 | 配置QoS上下行保证带宽门限、最高带宽门限以及带宽超过门限值时对QoS用户的处理动作。 |
| [**ADD EPSQOSACTION**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/EPS QoS配置/EPS QoS控制动作/增加EPS QoS控制动作配置（ADD EPSQOSACTION）_09654382.md) | MBRDL（下行最大带宽） | 384bit/s | 本端规划 | 配置QoS上下行保证带宽门限、最高带宽门限以及带宽超过门限值时对QoS用户的处理动作。 |
| [**ADD EPSQOSACTION**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/EPS QoS配置/EPS QoS控制动作/增加EPS QoS控制动作配置（ADD EPSQOSACTION）_09654382.md) | MBRDLACTION<br>（超过下行MBR的处理） | DEGRADE(降级) | 本端规划 | 配置QoS上下行保证带宽门限、最高带宽门限以及带宽超过门限值时对QoS用户的处理动作。 |
| [**ADD EPSQOSACTION**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/EPS QoS配置/EPS QoS控制动作/增加EPS QoS控制动作配置（ADD EPSQOSACTION）_09654382.md) | MBRUL（上行最大带宽） | 192bit/s | 本端规划 | 配置QoS上下行保证带宽门限、最高带宽门限以及带宽超过门限值时对QoS用户的处理动作。 |
| [**ADD EPSQOSACTION**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/EPS QoS配置/EPS QoS控制动作/增加EPS QoS控制动作配置（ADD EPSQOSACTION）_09654382.md) | MBRULACTION<br>（超过上行MBR的处理） | DEGRADE(降级) | 本端规划 | 配置QoS上下行保证带宽门限、最高带宽门限以及带宽超过门限值时对QoS用户的处理动作。 |
| [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md) | APN (APN名称) | apn1 | 本端规划 | 指定APN实例。 |
| [**SET APNQOSATTR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/APN的QoS属性/设置指定APN的QoS属性配置信息（SET APNQOSATTR）_09651825.md) | APN (APN名称) | apn1 | 本端规划 | 为APN实例绑定QosProfile。 |
| [**SET APNQOSATTR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/APN的QoS属性/设置指定APN的QoS属性配置信息（SET APNQOSATTR）_09651825.md) | HASQOSPROFILE（是否配置QosProfile） | ENABLE | 本端规划 | 为APN实例绑定QosProfile。 |
| [**SET APNQOSATTR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/APN的QoS属性/设置指定APN的QoS属性配置信息（SET APNQOSATTR）_09651825.md) | QOSPROFILENAME (QoS Profile名) | qos1 | 本端规划 | 为APN实例绑定QosProfile。 |
| [**SET QOSREMARK**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/全局QoS功能配置/全局DSCP_ToS映射功能/设置全局QoS到TOS_DSCP的映射规则（SET QOSREMARK）_09653840.md) | DOWNLINK (下行标记) | ENABLE | 本端规划 | 整机上下行QosRemark功能开关。 |
| [**SET QOSREMARK**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/全局QoS功能配置/全局DSCP_ToS映射功能/设置全局QoS到TOS_DSCP的映射规则（SET QOSREMARK）_09653840.md) | UPLINK（上行标记） | ENABLE | 本端规划 | 整机上下行QosRemark功能开关。 |
| **[ADD EPSREMARK](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/EPS QoS配置/EPS Qos映射ToS_DSCP/增加EPS QoS到TOS_DSCP的映射规则（ADD EPSREMARK）_09652275.md)** | QOSPROFILENAME（QoS Profile名） | qos1 | 全网规划 | 配置EPS QoS到DSCP或者TOS的映射规则。 |
| **[ADD EPSREMARK](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/EPS QoS配置/EPS Qos映射ToS_DSCP/增加EPS QoS到TOS_DSCP的映射规则（ADD EPSREMARK）_09652275.md)** | QCI（QCI值） | 1 | 全网规划 | 配置EPS QoS到DSCP或者TOS的映射规则。 |
| **[ADD EPSREMARK](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/EPS QoS配置/EPS Qos映射ToS_DSCP/增加EPS QoS到TOS_DSCP的映射规则（ADD EPSREMARK）_09652275.md)** | ARPPL（ARP的优先级别） | 1 | 全网规划 | 配置EPS QoS到DSCP或者TOS的映射规则。 |
| **[ADD EPSREMARK](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/EPS QoS配置/EPS Qos映射ToS_DSCP/增加EPS QoS到TOS_DSCP的映射规则（ADD EPSREMARK）_09652275.md)** | REMARKTYPE（标记类型） | DSCP | 全网规划 | 配置EPS QoS到DSCP或者TOS的映射规则。 |
| **[ADD EPSREMARK](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/EPS QoS配置/EPS Qos映射ToS_DSCP/增加EPS QoS到TOS_DSCP的映射规则（ADD EPSREMARK）_09652275.md)** | DSCP | EF(对应的DSCP的值为101110) | 全网规划 | 配置EPS QoS到DSCP或者TOS的映射规则。 |
| **[ADD EPSREMARK](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/EPS QoS配置/EPS Qos映射ToS_DSCP/增加EPS QoS到TOS_DSCP的映射规则（ADD EPSREMARK）_09652275.md)** | S1UDSCPSWITCH（S1-U DSCP配置开关） | ENABLE | 全网规划 | 配置EPS QoS到DSCP或者TOS的映射规则。 |
| **[ADD EPSREMARK](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/EPS QoS配置/EPS Qos映射ToS_DSCP/增加EPS QoS到TOS_DSCP的映射规则（ADD EPSREMARK）_09652275.md)** | S1UDSCP（S1-U DSCP） | DSCP_VALUE(映射的DSCP值) | 全网规划 | 配置EPS QoS到DSCP或者TOS的映射规则。 |
| **[ADD EPSREMARK](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/EPS QoS配置/EPS Qos映射ToS_DSCP/增加EPS QoS到TOS_DSCP的映射规则（ADD EPSREMARK）_09652275.md)** | S1UDSCPVALUE（S1-U DSCP值） | 22 | 全网规划 | 配置EPS QoS到DSCP或者TOS的映射规则。 |
| **[ADD EPSREMARK](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/EPS QoS配置/EPS Qos映射ToS_DSCP/增加EPS QoS到TOS_DSCP的映射规则（ADD EPSREMARK）_09652275.md)** | S5SDSCPSWITCH（SGW S5 DSCP配置开关） | ENABLE | 全网规划 | 配置EPS QoS到DSCP或者TOS的映射规则。 |
| **[ADD EPSREMARK](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/EPS QoS配置/EPS Qos映射ToS_DSCP/增加EPS QoS到TOS_DSCP的映射规则（ADD EPSREMARK）_09652275.md)** | S5SDSCP（SGW S5 DSCP） | DSCP_VALUE(映射的DSCP值) | 全网规划 | 配置EPS QoS到DSCP或者TOS的映射规则。 |
| **[ADD EPSREMARK](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/EPS QoS配置/EPS Qos映射ToS_DSCP/增加EPS QoS到TOS_DSCP的映射规则（ADD EPSREMARK）_09652275.md)** | S5SDSCPVALUE（SGW S5 DSCP值） | 23 | 全网规划 | 配置EPS QoS到DSCP或者TOS的映射规则。 |
| **[ADD EPSREMARK](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/EPS QoS配置/EPS Qos映射ToS_DSCP/增加EPS QoS到TOS_DSCP的映射规则（ADD EPSREMARK）_09652275.md)** | S5PDSCPSWITCH（PGW S5 DSCP配置开关） | ENABLE | 全网规划 | 配置EPS QoS到DSCP或者TOS的映射规则。 |
| **[ADD EPSREMARK](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/EPS QoS配置/EPS Qos映射ToS_DSCP/增加EPS QoS到TOS_DSCP的映射规则（ADD EPSREMARK）_09652275.md)** | S5PDSCP（PGW S5 DSCP） | DSCP_VALUE(映射的DSCP值) | 全网规划 | 配置EPS QoS到DSCP或者TOS的映射规则。 |
| **[ADD EPSREMARK](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/EPS QoS配置/EPS Qos映射ToS_DSCP/增加EPS QoS到TOS_DSCP的映射规则（ADD EPSREMARK）_09652275.md)** | S5PDSCPVALUE（PGW S5 DSCP值） | 24 | 全网规划 | 配置EPS QoS到DSCP或者TOS的映射规则。 |
| **[ADD EPSREMARK](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/EPS QoS配置/EPS Qos映射ToS_DSCP/增加EPS QoS到TOS_DSCP的映射规则（ADD EPSREMARK）_09652275.md)** | S8SDSCPSWITCH（SGW S8 DSCP配置开关） | ENABLE | 全网规划 | 配置EPS QoS到DSCP或者TOS的映射规则。 |
| **[ADD EPSREMARK](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/EPS QoS配置/EPS Qos映射ToS_DSCP/增加EPS QoS到TOS_DSCP的映射规则（ADD EPSREMARK）_09652275.md)** | S8SDSCP（SGW S8 DSCP） | DSCP_VALUE(映射的DSCP值) | 全网规划 | 配置EPS QoS到DSCP或者TOS的映射规则。 |
| **[ADD EPSREMARK](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/EPS QoS配置/EPS Qos映射ToS_DSCP/增加EPS QoS到TOS_DSCP的映射规则（ADD EPSREMARK）_09652275.md)** | S8SDSCPVALUE（SGW S8 DSCP值） | 25 | 全网规划 | 配置EPS QoS到DSCP或者TOS的映射规则。 |
| **[ADD EPSREMARK](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/EPS QoS配置/EPS Qos映射ToS_DSCP/增加EPS QoS到TOS_DSCP的映射规则（ADD EPSREMARK）_09652275.md)** | S8PDSCPSWITCH（PGW S8 DSCP配置开关） | ENABLE | 全网规划 | 配置EPS QoS到DSCP或者TOS的映射规则。 |
| **[ADD EPSREMARK](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/EPS QoS配置/EPS Qos映射ToS_DSCP/增加EPS QoS到TOS_DSCP的映射规则（ADD EPSREMARK）_09652275.md)** | S8PDSCP（PGW S8 DSCP） | DSCP_VALUE(映射的DSCP值) | 全网规划 | 配置EPS QoS到DSCP或者TOS的映射规则。 |
| **[ADD EPSREMARK](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/EPS QoS配置/EPS Qos映射ToS_DSCP/增加EPS QoS到TOS_DSCP的映射规则（ADD EPSREMARK）_09652275.md)** | S8PDSCPVALUE（PGW S8 DSCP值） | 26 | 全网规划 | 配置EPS QoS到DSCP或者TOS的映射规则。 |
| **[ADD EPSREMARK](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/EPS QoS配置/EPS Qos映射ToS_DSCP/增加EPS QoS到TOS_DSCP的映射规则（ADD EPSREMARK）_09652275.md)** | SGIDSCPSWITCH（PGW SGi DSCP配置开关） | ENABLE | 全网规划 | 配置EPS QoS到DSCP或者TOS的映射规则。 |
| **[ADD EPSREMARK](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/EPS QoS配置/EPS Qos映射ToS_DSCP/增加EPS QoS到TOS_DSCP的映射规则（ADD EPSREMARK）_09652275.md)** | SGIDSCP（PGW SGi DSCP） | DSCP_VALUE(映射的DSCP值) | 全网规划 | 配置EPS QoS到DSCP或者TOS的映射规则。 |
| **[ADD EPSREMARK](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/EPS QoS配置/EPS Qos映射ToS_DSCP/增加EPS QoS到TOS_DSCP的映射规则（ADD EPSREMARK）_09652275.md)** | SGIDSCPVALUE（PGW SGi DSCP值） | 27 | 全网规划 | 配置EPS QoS到DSCP或者TOS的映射规则。 |
| [**ADD USRPROFGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板组/增加用户模板组（ADD USRPROFGROUP）_09897220.md) | USERPROFGNAME (用户模板组名称) | usrg | 本端规划 | 配置用户模板组User Profile Group |
| [**ADD UPBINDUPG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md) | USERPROFGNAME (用户模板组名称) | usrg | 全网规划 | 将UserProfile绑定到用户模板组 |
| [**ADD UPBINDUPG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md) | UPBINDTYPE | DEFAULT | 全网规划 | 将UserProfile绑定到用户模板组 |
| [**ADD UPBINDUPG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md) | USERPROFILENAME（用户模板名称） | profile1 | 本端规划 | 将UserProfile绑定到用户模板组 |
| [**ADD APNUSRPROFG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md) | APN (APN名称) | apn1 | 全网规划 | 将UserProfile Group绑定到APN |
| [**ADD APNUSRPROFG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md) | USERPROFGNAME（用户模板组名称） | usrg | 全网规划 | 将UserProfile Group绑定到APN |
| [**SET QOSCTRL**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/全局QoS功能配置/全局QoS控制功能/设置QoS控制配置（SET QOSCTRL）_09653269.md) | USERTYPE (用户漫游类型) | VISITING | 全网规划 | 配置用户带宽控制的全局开关 |

## [操作步骤](#ZH-CN_OPI_0228344569)

1. 进入 “MML命令行-UNC” 窗口。
2. 打开License配置开关。
  [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md) [设置License项的开关（SET LICENSESWITCH）](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
3. 设置全局的QoS信息。
  [**SET QOSGLOBAL**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/全局QoS功能配置/全局QoS参数/设置全局QoS配置（SET QOSGLOBAL）_09652976.md)
4. 配置EPS QoS缺省QoS参数。
  [**SET DEFEPSQOS**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/EPS QoS配置/全局EPS QoS纠错/设置EPS缺省QoS参数（SET DEFEPSQOS）_09653732.md)
5. 配置EPS QoS协商控制。
    - 进入 “MML命令行-UNC” 窗口。
    - 配置指定APN实例下的QosProfile名称（非全局），并进入QoS实例。
      [**ADD QOSPROFILE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/QoS模板/增加QoS描述配置（ADD QOSPROFILE）_09654430.md)
    - 配置会话类QoS上下行最高带宽门限、会话类QoS上下行保证带宽门限以及带宽超过门限值时对此类QoS用户的处理动作。
      [**ADD EPSQOSACTION**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/EPS QoS配置/EPS QoS控制动作/增加EPS QoS控制动作配置（ADD EPSQOSACTION）_09654382.md)
    - 配置APN实例。
      [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)
    - 为APN实例绑定QoS profile。
      [**SET APNQOSATTR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/APN的QoS属性/设置指定APN的QoS属性配置信息（SET APNQOSATTR）_09651825.md)
6. 配置EPS QoS到DSCP的映射关系。
    - 配置用户的上下行remark功能开关
      [**SET QOSREMARK**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/全局QoS功能配置/全局DSCP_ToS映射功能/设置全局QoS到TOS_DSCP的映射规则（SET QOSREMARK）_09653840.md)
    - 配置指定APN实例下的QosProfile名称（非全局），并进入QoS实例。
      [**ADD QOSPROFILE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/QoS模板/增加QoS描述配置（ADD QOSPROFILE）_09654430.md)
    - 配置EPS QoS到DSCP的映射规则。
      **[ADD EPSREMARK](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/EPS QoS配置/EPS Qos映射ToS_DSCP/增加EPS QoS到TOS_DSCP的映射规则（ADD EPSREMARK）_09652275.md)**
    - 配置用户模板组User Profile Group。
      [**ADD USRPROFGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板组/增加用户模板组（ADD USRPROFGROUP）_09897220.md)
    - 将UserProfile绑定到用户模板组UserProfileGroup。
      [**ADD UPBINDUPG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)
    - 配置APN实例。
      [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)
    - 将UserProfile Group绑定到APN。
      [**ADD APNUSRPROFG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md)
    - 为APN实例绑定QoS profile。
      [**SET APNQOSATTR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/APN的QoS属性/设置指定APN的QoS属性配置信息（SET APNQOSATTR）_09651825.md)
7. 配置QoS带宽控制。
  [**SET QOSCTRL**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/全局QoS功能配置/全局QoS控制功能/设置QoS控制配置（SET QOSCTRL）_09653269.md)

## [任务示例](#ZH-CN_OPI_0228344569)

任务描述

- 配置基于全局的EPS QoS信息。
- 配置基于全局的EPS缺省QoS参数。
- 配置基于APN的EPS QoS协商控制。
- 配置基于APN的EPS QoS到DSCP的映射关系。
- 配置基于全局的EPS QoS带宽控制。

脚本

- 配置基于全局的EPS QoS信息。
  //打开本特性的License配置开关。

  ```
  SET LICENSESWITCH:LICITEM="LKV3W9TCQS11",SWITCH=ENABLE;
  ```
  ```
  SET QOSGLOBAL:QOSPROFILENAME="qos1",BINDEPSSUBQOS=ENABLE,EPSSUBQOS=1;
  ```
- 配置基于全局的EPS缺省QoS参数。
  //打开本特性的License配置开关。

  ```
  SET LICENSESWITCH:LICITEM="LKV3W9TCQS11",SWITCH=ENABLE;
  ```
  ```
  SET DEFEPSQOS: QOSCLASSID=1, ARPVALUE=1, GBRDL=200, GBRUL=230, MBRDL=300, MBRUL=300, APNAMBRDL=1000, APNAMBRUL=1000;
  ```
- 配置基于APN的EPS QoS协商控制。
  //打开本特性的License配置开关。

  ```
  SET LICENSESWITCH:LICITEM="LKV3W9TCQS11",SWITCH=ENABLE;
  ```
  //配置指定APN实例下的QosProfile名称（非全局），并进入QoS实例。
  ```
  ADD QOSPROFILE:QOSPROFILENAME="qos2";
  ```
  //配置会话类QoS上下行最高带宽门限、QoS上下行保证带宽门限以及带宽超过门限值时对此类QoS用户的处理动作。
  ```
  ADD EPSQOSACTION:QOSPROFILENAME="qos2",QCI=1,GBRDL=256,GBRDLACTION=DEGRADE,GBRUL=128,GBRULACTION=DEGRADE,MBRDL=384,
  MBRDLACTION=DEGRADE,MBRUL=192,MBRULACTION=DEGRADE;
  ```
  //进入指定APN实例。
  ```
  ADD APN:APN="apn1";
  ```
  //为该APN实例绑定QosProfile。
  ```
  SET APNQOSATTR:APN="apn1",HASQOSPROFILE=ENABLE,QOSPROFILENAME="qos2";
  ```
- 配置基于APN的EPS QoS到DSCP的映射关系
  //打开本特性的License配置开关。

  ```
  SET LICENSESWITCH:LICITEM="LKV3W9TCQS11",SWITCH=ENABLE;
  ```
  //配置用户的上下行remark功能。
  ```
  SET QOSREMARK:DOWNLINK=ENABLE,UPLINK=ENABLE;
  ```
  //配置指定APN实例下的QosProfile名称（非全局），并进入QoS实例。
  ```
  ADD QOSPROFILE:QOSPROFILENAME="gp1";
  ```
  //配置EPS QoS到DSCP的映射规则。
  ```
  ADD EPSREMARK: QOSPROFILENAME="qosprofile1", QCI=1, ARPPL=1, REMARKTYPE=DSCP, DSCP=EF, S1UDSCPSWITCH=ENABLE, S1UDSCP=DSCP_VALUE, S1UDSCPVALUE=22, S5SDSCPSWITCH=ENABLE, S5SDSCP=DSCP_VALUE, S5SDSCPVALUE=23, S5PDSCPSWITCH=ENABLE, S5PDSCP=DSCP_VALUE, S5PDSCPVALUE=24, S8SDSCPSWITCH=ENABLE, S8SDSCP=DSCP_VALUE, S8SDSCPVALUE=25, S8PDSCPSWITCH=ENABLE, S8PDSCP=DSCP_VALUE, S8PDSCPVALUE=26, SGIDSCPSWITCH=ENABLE, SGIDSCP=DSCP_VALUE, SGIDSCPVALUE=27;
  ```
  //配置控制信令的DSCP值。
  ```
  SET IFDSCP: MSGCLS=SIGNALLING, INTFTP_SHOW=GTP_PROTOCOL_SIGNALING, DSCPV=63, CCDSCP=EF;
  ```
  //配置UserProfile Group。
  ```
  ADD USRPROFGROUP:USERPROFGNAME="usrg";
  ```
  //将UserProfile绑定到UserProfileGroup。
  ```
  ADD UPBINDUPG:USERPROFGNAME="usrg",UPBINDTYPE=DEFAULT,USERPROFILENAME="profile1";
  ```
  //进入指定APN实例。
  ```
  ADD APN:APN="apn1";
  ```
  //将UserProfile Group绑定到APN。
  ```
  ADD APNUSRPROFG:APN="apn1",USERPROFGNAME="usrg";
  ```
  //为该APN实例绑定QosProfile。
  ```
  SET APNQOSATTR:APN="apn1",HASQOSPROFILE=ENABLE,QOSPROFILENAME="gp1";
  ```
- 配置基于全局的EPS QoS带宽控制。
  //打开本特性的License配置开关。

  ```
  SET LICENSESWITCH:LICITEM="LKV3W9TCQS11",SWITCH=ENABLE;
  ```
  ```
  SET QOSCTRL USERTYPE=VISITING;
  ```
