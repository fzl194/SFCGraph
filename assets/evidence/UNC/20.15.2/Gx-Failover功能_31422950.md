# Gx Failover功能

- [操作场景](#ZH-CN_OPI_0231422950__1.3.1)
- [必备事项](#ZH-CN_OPI_0231422950__1.3.2)
- [操作步骤](#ZH-CN_OPI_0231422950__1.3.3)
- [任务示例](#ZH-CN_OPI_0231422950__1.3.4)

## [操作场景](#ZH-CN_OPI_0231422950)

当用户初始激活或进行业务时，GGSN/PGW-C发送CCR请求消息给PCRF，在指定消息重传时间间隔时间内未收到PCRF的响应消息，即可判断PCRF服务器状态异常。如果 [**ADD PCRFGROUP**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF组/增加PCRF组（ADD PCRFGROUP）_09897090.md) 命令中 “FAILOVERSW” 参数值为 “ENABLE” ，则进行failover处理；否则按照 [**SET PCCFAILACTION**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC故障处理（SET PCCFAILACTION）_09897058.md) 和 [**ADD PCCTEMPLATE**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md) 命令设置的动作进行处理。

GGSN/PGW-C向备PCRF重发消息，如果备PCRF也没有响应或者备PCRF因状态异常、消息发送速率超过wal值等导致不可用，可以根据 [**SET PCCFAILACTION**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC故障处理（SET PCCFAILACTION）_09897058.md) 和 [**ADD PCCTEMPLATE**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md) 命令配置情况去活用户或者转为非PCC用户/本地PCC用户继续进行业务。

实现failover功能需要具备以下几个条件：

- PCRF采用负荷分担或者主备组网模式。
- GGSN/PGW-C本地配置支持failover功能。
- 主备PCRF存在LOCALHOSTNAME相同的Diameter链路组。
- PCRF支持failover功能，在PCRF使用failover时，PCRF发送给GGSN/PGW-C的CCA消息中携带的CC-Session-Failover AVP支持failover。
- PCRF支持热备份功能，即PCRF支持CC session的同步。
  如果PCRF不支持热备份功能，为了保证PCRF切换后用户不掉线，GGSN/PGW-C需支持failover增强功能。备PCRF可根据GGSN/PGW-C重发的CCR-U中携带的信息重建IP-CAN会话，并发送CCA-U消息给GGSN/PGW-C，通过CCA-U消息中携带的会话重建AVP中的值为DELETE_DEFAULT_AND_DEDICATED_BEARER_RULES (2)，指示UNC和UDG删除该用户的所有已安装规则及专有承载/二次PDP上下文，并为缺省承载/一次PDP上下文下发新的规则，相当于完成了一次初始激活。

> **说明**
> 适用于 GGSN、 PGW-C。

## [必备事项](#ZH-CN_OPI_0231422950)

前提条件

- 请仔细阅读[PCC基本功能（2G/3G/4G，基于Gx接口）](../../PCC基本功能（2G_3G_4G，基于Gx接口）_29056156.md)。
- 完成[配置与PCRF对接数据](配置与PCRF对接数据_30805096.md)。
- 部署主备PCRF组，且PCRF组支持failover，即在CCA消息中CC-Session-Failover AVP支持failover。

数据

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| [**ADD PCRF**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF/增加PCRF（ADD PCRF）_09897101.md) | PCRF主机名（HOSTNAME） | pcrf1<br>pcrf2 | 本端规划 | 配置PCRF的基本信息。 |
| [**ADD PCRF**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF/增加PCRF（ADD PCRF）_09897101.md) | PCRF域名（REALMNAME） | host1.example.com<br>host2.example.com | 本端规划 | 配置PCRF的基本信息。 |
| [**ADD DIAMPEERADDR**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md) | 主机名称（HOSTNAME） | pcrf1<br>pcrf2 | 已配置数据中获取 | 配置PCRF的IP地址。 |
| [**ADD DIAMPEERADDR**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md) | 地址类型（ADDRTYPE） | IPv4 | 与对端协商 | 配置PCRF的IP地址。 |
| [**ADD DIAMPEERADDR**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md) | IPv4地址（IPV4ADDRESS） | 10.10.10.1<br>10.10.10.2 | 与对端协商 | 配置PCRF的IP地址。 |
| [**ADD PCRFGROUP**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF组/增加PCRF组（ADD PCRFGROUP）_09897090.md) | PCRF组名称（PCRFGRPNAME） | pcrf.group.1 | 本端规划 | PCRF group信息。 |
| [**ADD PCRFGROUP**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF组/增加PCRF组（ADD PCRFGROUP）_09897090.md) | 负荷分担模式（LOADBALANCEMODE） | MASTER_SLAV | 全网规划 | PCRF group信息。 |
| [**ADD PCRFGROUP**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF组/增加PCRF组（ADD PCRFGROUP）_09897090.md) | 宕机备份开关（FAILOVERSW） | ENABLE | 本端规划 | PCRF group信息。 |
| [**ADD PCRFBINDGRP**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF绑定/增加PCRF与PCRF Group的关联关系（ADD PCRFBINDGRP）_09897096.md) | PCRF组名称（PCRFGRPNAME） | pcrf.group.1 | 已配置数据中获取 | 添加PCRF到PCRF分组中。 |
| [**ADD PCRFBINDGRP**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF绑定/增加PCRF与PCRF Group的关联关系（ADD PCRFBINDGRP）_09897096.md) | PCRF主机名称（PCRFHOSTNAME） | pcrf1<br>pcrf2 | 已配置数据中获取 | 添加PCRF到PCRF分组中。 |
| [**SET PCCTIMER**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/定时器/设置PCC定时器（SET PCCTIMER）_09897082.md) | 应用层重传时间间隔（秒）（APPRETRYTIMEOUT） | 10 | 本端规划 | Tx定时器。 |

## [操作步骤](#ZH-CN_OPI_0231422950)

1. 进入 “MML命令行-UNC” 窗口。
2. 配置PCRF信息。
    a. 配置PCRF信息。重复执行本步骤可增加多个PCRF信息。
      [**ADD PCRF**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF/增加PCRF（ADD PCRF）_09897101.md)
    b. 配置PCRF组。
      [**ADD PCRFGROUP**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF组/增加PCRF组（ADD PCRFGROUP）_09897090.md)
    c. **可选：**如果PCRF组的工作模式为主备模式，可使用如下命令修改PCRF分组内的缺省主用PCRF。
      [**SET MASTERPCRF**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF组/设置主用PCRF（SET MASTERPCRF）_09897094.md)
3. **可选：**配置PCC定时器的消息重传时间间隔。缺省使用默认值。
  [**SET PCCTIMER**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/定时器/设置PCC定时器（SET PCCTIMER）_09897082.md)
4. 将指定的PCRF分组绑定到指定APN。
  [**ADD PCRFGRPBNDAPN**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF组绑定APN/增加APN和Pcrf组关联关系（ADD PCRFGRPBNDAPN）_09897106.md)
5. **可选：**如果PCRF不支持热备份功能，GGSN/PGW-C上需要开启failover增强功能。
    a. GGSN/PGW-C上开启failover增强功能。
      [**SET SMFSOFTPARA**](../../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/软件参数管理/设置SMF软参（SET SMFSOFTPARA）_09653002.md)
      详细描述请参见 [BIT1202 控制Gx Failover增强功能是否生效](../../../../../../../OM参考/软件参数/UNC软件参数/业务软件参数/软件参数（SMF_GGSN_SGW-C_PGW-C）/PCC策略控制管理/BIT1202 控制Gx Failover增强功能是否生效_98644179.md) 。
    b. 配置GGSN/PGW-C发送的CCR-U消息中携带信元Called-Station-ID、User-Equipment-Info、Framed-IP-Address、Framed-IPv6-Prefix，Subscription-Id-Type和Subscription-Id携带MSISDN开关。
      [**SET PCCMSGATTR**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/客户端信元控制/设置PCC消息属性（SET PCCMSGATTR）_09897079.md)
    c. 配置GGSN/PGW-C发送的CCR-T消息中携带信元Called-Station-ID，Subscription-Id-Type和Subscription-Id携带MSISDN开关。
      [**SET PCCMSGATTR**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/客户端信元控制/设置PCC消息属性（SET PCCMSGATTR）_09897079.md)

## [任务示例](#ZH-CN_OPI_0231422950)

任务描述

网络中部署主备PCRF服务器，以进行有效的系统容灾。当主PCRF服务器故障后，GGSN/PGW-C执行Failover动作，将用户消息交互切换到备PCRF服务器上进行处理。

脚本

1. 配置主备PCRF设备标识。
  ```
  ADD PCRF:HOSTNAME="pcrf1",REALMNAME="host1.example.com";
  ```
  ```
  ADD PCRF:HOSTNAME="pcrf2",REALMNAME="host2.example.com";
  ```
  ```
  ADD DIAMPEERADDR:HOSTNAME="pcrf1",ADDRTYPE=IPv4,IPV4ADDRESS="10.10.10.1";
  ```
  ```
  ADD DIAMPEERADDR:HOSTNAME="pcrf2",ADDRTYPE=IPv4,IPV4ADDRESS="10.10.10.2";
  ```
2. 配置PCRF组。
  ```
  ADD PCRFGROUP:PCRFGRPNAME="pcrf.group.1",LOADBALANCEMODE=MASTER_SLAVE,FAILOVERSW=ENABLE;
  ```
  ```
  ADD PCRFBINDGRP:PCRFGRPNAME="pcrf.group.1",PCRFHOSTNAME="pcrf1";
  ```
  ```
  ADD PCRFBINDGRP:PCRFGRPNAME="pcrf.group.1",PCRFHOSTNAME="pcrf2";
  ```
3. 配置Tx定时器的时长。
  ```
  SET PCCTIMER:APPRETRYTIMEOUT=10;
  ```
4. 将PCRF分组绑定到指定APN。
  ```
  ADD PCRFGRPBNDAPN:APN="apn1",DEFAULTFLAG=DEFAULT,PCRFGRPNAME="pcrf.group.1";
  ```
5. PCRF不支持热备时，开启failover增强功能并配置上报[步骤 5.b](#ZH-CN_OPI_0231422950__substep826311974175816)和[步骤 5.c](#ZH-CN_OPI_0231422950__substep1922626752175816)描述的需携带的参数。
  ```
  SET SMFSOFTPARA: DT=BIT, BITNUM=1202, BITVALUE=1;
  SET PCCMSGATTR: MSGTYPE=CCRU, MSISDN=ENABLE, CALLEDSTATIONID=ENABLE, USREQUIPINFO=ENABLE, FRAMEDIPADDRESS=ENABLE, FRAMEDIPV6PREF=ENABLE;
  SET PCCMSGATTR: MSGTYPE=CCRT, MSISDN=ENABLE, CALLEDSTATIONID=ENABLE;
  ```
