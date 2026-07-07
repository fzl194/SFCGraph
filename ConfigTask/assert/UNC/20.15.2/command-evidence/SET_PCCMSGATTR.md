# 命令证据包：SET PCCMSGATTR
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/客户端信元控制/设置PCC消息属性（SET PCCMSGATTR）_09897079.md`
> 用该命令的特性数：1

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：PGW-C、SMF**

该命令用于配置Gx接口上CCR-I、CCR-U、CCR-T和RAA消息中可选AVP的携带方式。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。
- 该命令最大记录数为4。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | MSGTYPE | CHARGINGRULE | MSTIMEZONE | G3PPRATTYPE | IMSI | MSISDN | CALLEDSTATIONID | USREQUIPINFO | FRAMEDIPADDRESS | FRAMEDIPV6PREF |

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| MSGTYPE | 消息类型 | 对端协商 | required | 无 | 枚举类型。 |
| CHARGINGRULE | Charging-Rule-Base-Name和Charging-Rule-Name子AVP开关 | 对端协商 | conditional | 无 | 枚举类型。 |
| MSTIMEZONE | 3GPP-MS-TimeZone AVP开关 | 对端协商 | conditional | 无 | 枚举类型。 |
| G3PPRATTYPE | 3GPP-RAT-Type AVP开关 | 对端协商 | conditional | 无 | 枚举类型。 |
| IMSI | Subscription-Id-Type和Subscription-Id携带IMSI开关 | 对端协商 | conditional | 无 | 枚举类型。 |
| MSISDN | Subscription-Id-Type和Subscription-Id携带MSISDN开关 | 对端协商 | conditional | 无 | 枚举类型。 |
| CALLEDSTATIONID | Called-Station-ID AVP开关 | 对端协商 | conditional | 无 | 枚举类型。 |
| USREQUIPINFO | User-Equipment-Info AVP开关 | 对端协商 | conditional | 无 | 枚举类型。 |
| FRAMEDIPADDRESS | Framed-IP-Address AVP开关 | 对端协商 | conditional | 无 | 枚举类型。 |
| FRAMEDIPV6PREF | Framed-IPv6-Prefix AVP开关 | 对端协商 | conditional | 无 | 枚举类型。 |
| RATTYPE | RAT-Type AVP开关 | 对端协商 | conditional | 无 | 枚举类型。 |
| EXPERRESULTCODE | Experiment-Result-Code AVP开关 | 对端协商 | conditional | 无 | 枚举类型。 |
| ULITIME | User-Location-Info-Time AVP开关 | 对端协商 | conditional | 无 | 枚举类型。 |
| NETLOCACCESS | NetLoc-Access-Support AVP开关 | 对端协商 | conditional | 无 | 枚举类型。 |
| CLHONEGOBCM | CL切换更新时携带Network-Request-Support AVP开关 | 对端协商 | conditional | 无 | 枚举类型。 |
| ANCHARGINGADDR | Access-Network-Charging-Address AVP开关 | 对端协商 | conditional | 无 | 枚举类型。 |
| G3CC | 3GPP-Charging-Characteristics AVP开关 | 对端协商 | conditional | 无 | 枚举类型。 |
| G3GGSNADDR | 3GPP-GGSN-Address AVP开关 | 对端协商 | conditional | 无 | 枚举类型。 |
| G3SELECTMODE | 3GPP-Selection-Mode AVP开关 | 对端协商 | conditional | 无 | 枚举类型。 |
| DYNADDRFLG | Dynamic-Address-Flag AVP开关 | 对端协商 | conditional | 无 | 枚举类型。 |
| DYNADDRFLGEXT | Dynamic-Address-Flag-Extension AVP开关 | 对端协商 | conditional | 无 | 枚举类型。 |
| PDNCCHARGINGID | PDN-Connection-Charging-ID AVP开关 | 对端协商 | conditional | 无 | 枚举类型。 |
| QOSINFORMATION | QoS-Information AVP开关 | 对端协商 | conditional | 无 | 枚举类型。 |
| DFTEPSBEARERQOS | Default-EPS-Bearer-QoS AVP开关 | 对端协商 | conditional | 无 | 枚举类型。 |
| G3SGSNMCCMNC | 3GPP-SGSN-MCC-MNC AVP开关 | 对端协商 | conditional | 无 | 枚举类型。 |
| G3SGSNADDR | 3GPP-SGSN-Address AVP开关 | 对端协商 | conditional | 无 | 枚举类型。 |
| G3ULI | 3GPP-User-Location-Info AVP开关 | 对端协商 | conditional | 无 | 枚举类型。 |
| ANCHARGINGID | Access-Network-Charging-Identifier-Value AVP开关 | 对端协商 | conditional | 无 | 枚举类型。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-109101

**md：`WSFD-109101/Gx Failover功能_31422950.md`**
- 任务示例脚本（该命令行）：
  `SET PCCMSGATTR: MSGTYPE=CCRU, MSISDN=ENABLE, CALLEDSTATIONID=ENABLE, USREQUIPINFO=ENABLE, FRAMEDIPADDRESS=ENABLE, FRAMEDIPV6PREF=ENABLE;`
  `SET PCCMSGATTR: MSGTYPE=CCRT, MSISDN=ENABLE, CALLEDSTATIONID=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L69:
    >       详细描述请参见 [BIT1202 控制Gx Failover增强功能是否生效](../../../../../../../OM参考/软件参数/UNC软件参数/业务软件参数/软件参数（SMF_GGSN_SGW-C_PGW-C）/PCC策略控制管理/BIT1202 控制Gx Failover增强功能是否生效_98644179.md) 。
    >     b. 配置GGSN/PGW-C发送的CCR-U消息中携带信元Called-Station-ID、User-Equipment-Info、Framed-IP-Address、Framed-IPv6-Prefix，Subscription-Id-Type和Subscription-Id携带MSISDN开关。
    >       [**SET PCCMSGATTR**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/客户端信元控制/设置PCC消息属性（SET PCCMSGATTR）_09897079.md)
    >     c. 配置GGSN/PGW-C发送的CCR-T消息中携带信元Called-Station-ID，Subscription-Id-Type和Subscription-Id携带MSISDN开关。
    >       [**SET PCCMSGATTR**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/客户端信元控制/设置PCC消息属性（SET PCCMSGATTR）_09897079.md)
  L71:
    >       [**SET PCCMSGATTR**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/客户端信元控制/设置PCC消息属性（SET PCCMSGATTR）_09897079.md)
    >     c. 配置GGSN/PGW-C发送的CCR-T消息中携带信元Called-Station-ID，Subscription-Id-Type和Subscription-Id携带MSISDN开关。
    >       [**SET PCCMSGATTR**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/客户端信元控制/设置PCC消息属性（SET PCCMSGATTR）_09897079.md)
    > 
    > ## [任务示例](#ZH-CN_OPI_0231422950)
  L115:
    >   ```
    >   SET SMFSOFTPARA: DT=BIT, BITNUM=1202, BITVALUE=1;
    >   SET PCCMSGATTR: MSGTYPE=CCRU, MSISDN=ENABLE, CALLEDSTATIONID=ENABLE, USREQUIPINFO=ENABLE, FRAMEDIPADDRESS=ENABLE, FRAMEDIPV6PREF=ENABLE;
    >   SET PCCMSGATTR: MSGTYPE=CCRT, MSISDN=ENABLE, CALLEDSTATIONID=ENABLE;
    >   ```

## ④ 自动比对
- 命令真相参数（28）：['ANCHARGINGADDR', 'ANCHARGINGID', 'CALLEDSTATIONID', 'CHARGINGRULE', 'CLHONEGOBCM', 'DFTEPSBEARERQOS', 'DYNADDRFLG', 'DYNADDRFLGEXT', 'EXPERRESULTCODE', 'FRAMEDIPADDRESS', 'FRAMEDIPV6PREF', 'G3CC', 'G3GGSNADDR', 'G3PPRATTYPE', 'G3SELECTMODE', 'G3SGSNADDR', 'G3SGSNMCCMNC', 'G3ULI', 'IMSI', 'MSGTYPE', 'MSISDN', 'MSTIMEZONE', 'NETLOCACCESS', 'PDNCCHARGINGID', 'QOSINFORMATION', 'RATTYPE', 'ULITIME', 'USREQUIPINFO']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
