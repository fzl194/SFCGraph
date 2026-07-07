# 命令证据包：ADD CDRFIELDTEMP
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/话单字段控制/话单字段模板/增加话单字段模板（ADD CDRFIELDTEMP）_09896890.md`
> 用该命令的特性数：9

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：SGW-C、PGW-C、SMF**

该命令用来新增话单字段模板的配置，用于控制话单中是否携带对应字段。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。
- 该命令最大记录数为100。
- 当前版本不支持此命令的EXTCHARGEID、THREEGPP2USRLOC、ULIWLAN参数。
- RecordExtType参数配置为GLB、DT时，PGW话单扩展字段中是否携带IP层的报文包数不受参数PacketNum控制。
- PacketNum参数为ENABLE选项时，只有配置了费率时，PGW话单扩展字段中才能携带IP层的

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| TEMPLATENAME | 话单字段模板名 | local_planned | required | 无 | 字符串类型，输入长度范围为1～63。 |
| APNNETWORKID | apn-network-identifier | local_planned | optional | ENABLE | 枚举类型。 |
| APNSELECTMODE | apn-selection-mode | local_planned | optional | ENABLE | 枚举类型。 |
| CCSELETIONMODE | charge-characteristic-selection-mode | local_planned | optional | ENABLE | 枚举类型。 |
| DIAGNOSTICS | diagnostics | local_planned | optional | ENABLE | 枚举类型。 |
| DYNADDRFLAG | dynamic-address-flag | local_planned | optional | ENABLE | 枚举类型。 |
| EXTCHARGEID | external-charging-identifier | local_planned | optional | ENABLE | 枚举类型。 |
| IMSSIGCONTEXT | ims-signalling-context | local_planned | optional | ENABLE | 枚举类型。 |
| LOSD | list-of-service-data | local_planned | optional | ENABLE | 枚举类型。 |
| LOTV | list-of-traffic-volume | local_planned | optional | ENABLE | 枚举类型。 |
| LOCALRECSEQNUM | local-record-sequence-number | local_planned | optional | ENABLE | 枚举类型。 |
| MSISDN | MSISDN | local_planned | optional | ENABLE | 枚举类型。 |
| MSTIMEZONE | ms-time-zone | local_planned | optional | ENABLE | 枚举类型。 |
| NETINITPDPCONT | network-initiated-pdp-context | local_planned | optional | ENABLE | 枚举类型。 |
| NODEID | node-id | local_planned | optional | ENABLE | 枚举类型。 |
| PDPTYPE | pdp-type | local_planned | optional | ENABLE | 枚举类型。 |
| PGWADDRESSIPV6 | pgw-address-ipv6 | local_planned | optional | ENABLE | 枚举类型。 |
| PSFCI | ps-furnish-charging-information | local_planned | optional | ENABLE | 枚举类型。 |
| RATTYPE | rat-type | local_planned | optional | ENABLE | 枚举类型。 |
| RECSEQNUMBER | record-sequence-number | local_planned | optional | ENABLE | 枚举类型。 |
| SERVEDIMEISV | served-imeisv | local_planned | optional | ENABLE | 枚举类型。 |
| SERVEDPDPADDR | served-pdp-address | local_planned | optional | ENABLE | 枚举类型。 |
| SGSNSGWPLMNID | sgsn-sgw-plmn-identifier | local_planned | optional | ENABLE | 枚举类型。 |
| THREEGPP2USRLOC | threegpp2-user-location | local_planned | optional | ENABLE | 枚举类型。 |
| ULI | user-location-information | local_planned | optional | ENABLE | 枚举类型。 |
| IMSIUNAUTHFLAG | imsi-unauthenticated-flag | local_planned | optional | DISABLE | 枚举类型。 |
| PDNCONNECTIONID | pdn-connection-id | local_planned | optional | DISABLE | 枚举类型。 |
| PGWADDRESSUSED | pgw-address-used | local_planned | optional | DISABLE | 枚举类型。 |
| PGWPLMNID | pgw-plmn-identifier | local_planned | optional | DISABLE | 枚举类型。 |
| RECORDEXTENTION | record-extensions开关 | local_planned | optional | DISABLE | 枚举类型。 |
| RECORDEXTTYPE | 运营商record-extensions | local_planned | conditional | CCB | 枚举类型。 |
| CCBURL | 业务URL存在标识 | local_planned | conditional | DISABLE | 枚举类型。 |
| CCBUSGDURATION | 业务使用时长存在标识 | local_planned | conditional | DISABLE | 枚举类型。 |
| HPTIME | 高精度时间标识 | local_planned | conditional | ENABLE | 枚举类型。 |
| DTRECORD | Direct Tunnel记录 | local_planned | conditional | ENABLE | 枚举类型。 |
| STARTTIME | start-time | local_planned | optional | DISABLE | 枚举类型。 |
| STOPTIME | stop-time | local_planned | optional | DISABLE | 枚举类型。 |
| ULIWLAN | ULI携带WLAN地址信息 | global_planned | conditional | DISABLE | 枚举类型。 |
| OID | object identifier | global_planned | conditional | 1.3.6.1.4.1.2011.2.63 | 字符串类型，输入长度范围为1～63。点分十进制。 |
| SECRATUSAGE | RAN-SecondaryRAT-Usage-Report | local_planned | optional | DISABLE | 枚举类型。 |
| CPEPSOINDICATOR | cp-eps-optimisation-indicator | local_planned | optional | DISABLE | 枚举类型。 |
| EPDGUEIPPORT | ePDG UE Local IP 和 Port | local_planned | conditional | DISABLE | 枚举类型。 |
| PDPTYPEEXT | pdp-type-extention | local_planned | optional | DISABLE | 枚举类型。 |
| UNIPDUCPONLY | uni-pdu-cp-only-flag | local_planned | optional | DISABLE | 枚举类型。 |
| SGIPTPTUNMETH | sgi-ptp-tunnelling-method | local_planned | optional | DISABLE | 枚举类型。 |
| SRVPLMNRATECTRL | serving-plmn-rate-control | local_planned | optional | DISABLE | 枚举类型。 |
| APNRATECTRL | apn-rate-control | local_planned | optional | DISABLE | 枚举类型。 |
| LOWPRIIND | low-priority-indicator | local_planned | optional | DISABLE | 枚举类型。 |
| MOEXCPTDATA | mo-exception-data | local_planned | optional | DISABLE | 枚举类型。 |
| SGWADDRESSIPV6 | sgw-address-ipv6 | local_planned | optional | ENABLE | 枚举类型。 |
| SCSASADDR | scs-as-address | local_planned | optional | DISABLE | 枚举类型。 |
| PACKETNUM | packet-number | local_planned | conditional | DISABLE | 枚举类型。 |
| SNSSAI | Snssai | global_planned | conditional | DISABLE | 枚举类型。 |
| SSCMODE | SscMode | global_planned | conditional | DISABLE | 枚举类型。 |
| UWANULI | UWAN-user-location-information | global_planned | optional | DISABLE | 枚举类型。 |
| UWANUDPSRCPORT | UWAN-UDP-source-port | global_planned | conditional | DISABLE | 枚举类型。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-216104

**md：`WSFD-216104/WSFD-216104 基于APN的eMTC终端接入速率控制参考信息_75993426.md`**
- 操作步骤上下文（±2 行原文）：
  L20:
    > - [**RMV DCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/信用控制/信用控制模板/删除DCC模板（RMV DCCTEMPLATE）_09896925.md)
    > - [**LST DCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/信用控制/信用控制模板/查询DCC模板（LST DCCTEMPLATE）_09896933.md)
    > - [**ADD CDRFIELDTEMP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/话单字段控制/话单字段模板/增加话单字段模板（ADD CDRFIELDTEMP）_09896890.md)
    > - [**MOD CDRFIELDTEMP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/话单字段控制/话单字段模板/修改话单字段模板（MOD CDRFIELDTEMP）_09896891.md)
    > - [**RMV CDRFIELDTEMP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/话单字段控制/话单字段模板/删除话单字段模板（RMV CDRFIELDTEMP）_09896892.md)

**md：`WSFD-216104/激活基于APN的eMTC终端接入速率控制_77396887.md`**
- 操作步骤上下文（±2 行原文）：
  L43:
    >   [**ADD DCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/信用控制/信用控制模板/增加DCC模板（ADD DCCTEMPLATE）_09896923.md)
    > 5. **可选：**配置CDR话单中携带APN Rate Control字段。
    >   [**ADD CDRFIELDTEMP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/话单字段控制/话单字段模板/增加话单字段模板（ADD CDRFIELDTEMP）_09896890.md)
    > 6. **可选：**配置PGW-CDR中携带APN Rate Control字段。
    >   [**SET OFCCDRPARA**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/离线计费基础参数/离线公共参数/配置离线计费话单参数（SET OFCCDRPARA）_09896905.md)

### WSFD-216105

**md：`WSFD-216105/WSFD-216105 基于服务PLMN的eMTC终端接入速率控制参考信息_75993431.md`**
- 操作步骤上下文（±2 行原文）：
  L20:
    > - [**RMV DCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/信用控制/信用控制模板/删除DCC模板（RMV DCCTEMPLATE）_09896925.md)
    > - [**LST DCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/信用控制/信用控制模板/查询DCC模板（LST DCCTEMPLATE）_09896933.md)
    > - [**ADD CDRFIELDTEMP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/话单字段控制/话单字段模板/增加话单字段模板（ADD CDRFIELDTEMP）_09896890.md)
    > - [**MOD CDRFIELDTEMP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/话单字段控制/话单字段模板/修改话单字段模板（MOD CDRFIELDTEMP）_09896891.md)
    > - [**RMV CDRFIELDTEMP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/话单字段控制/话单字段模板/删除话单字段模板（RMV CDRFIELDTEMP）_09896892.md)

**md：`WSFD-216105/激活基于服务PLMN的eMTC终端接入速率控制_77396889.md`**
- 操作步骤上下文（±2 行原文）：
  L44:
    >   [**ADD DCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/信用控制/信用控制模板/增加DCC模板（ADD DCCTEMPLATE）_09896923.md)
    > 5. **可选：**配置CDR话单中携带Serving PLMN Rate Control字段。
    >   [**ADD CDRFIELDTEMP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/话单字段控制/话单字段模板/增加话单字段模板（ADD CDRFIELDTEMP）_09896890.md)
    > 6. **可选：**配置PGW-CDR或SGW-CDR中携带Serving PLMN Rate Control字段。
    >   [**SET OFCCDRPARA**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/离线计费基础参数/离线公共参数/配置离线计费话单参数（SET OFCCDRPARA）_09896905.md)

### WSFD-215101

**md：`WSFD-215101/WSFD-215101 基于信令面的数据传输参考信息（SGW-C）_77260998.md`**
- 操作步骤上下文（±2 行原文）：
  L12:
    > 本特性相关MML命令如下：
    > 
    > [**ADD CDRFIELDTEMP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/话单字段控制/话单字段模板/增加话单字段模板（ADD CDRFIELDTEMP）_09896890.md)
    > 
    > #### [告警](#ZH-CN_TOPIC_0277260998)

**md：`WSFD-215101/激活基于信令面的数据传输（SGW-C）_77260996.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD CDRFIELDTEMP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/话单字段控制/话单字段模板/增加话单字段模板（ADD CDRFIELDTEMP）_09896890.md) | TEMPLATENAME | cdrfieldtemp | 本端规划 | 指定话单字段模板的名称。 |
  | [**ADD CDRFIELDTEMP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/话单字段控制/话单字段模板/增加话单字段模板（ADD CDRFIELDTEMP）_09896890.md) | CPEPSOINDICATOR | ENABLE | 本端规划 | 置话单中是否携带cp-eps-optimisation-indicator字段。 |
  | [**ADD CDRFIELDTEMP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/话单字段控制/话单字段模板/增加话单字段模板（ADD CDRFIELDTEMP）_09896890.md) | UNIPDUCPONLY | ENABLE | 本端规划 | 配置话单中是否携带uni-pdu-cp-only-flag字段。 |
- 任务示例脚本（该命令行）：
  `ADD CDRFIELDTEMP:TEMPLATENAME="cdrfieldtemp",CPEPSOINDICATOR=ENABLE,UNIPDUCPONLY=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L36:
    >   [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 3. **可选：**配置话单中是否携带CP CIoT EPS Optimisation Indicator、UNI PDU CP Only Flag字段。
    >   [**ADD CDRFIELDTEMP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/话单字段控制/话单字段模板/增加话单字段模板（ADD CDRFIELDTEMP）_09896890.md)
    > 
    > ## [任务示例](#ZH-CN_OPI_0277260996)
  L55:
    > 
    > ```
    > ADD CDRFIELDTEMP:TEMPLATENAME="cdrfieldtemp",CPEPSOINDICATOR=ENABLE,UNIPDUCPONLY=ENABLE;
    > ```

**md：`WSFD-215101/特性概述_77260995.md`**
- 操作步骤上下文（±2 行原文）：
  L95:
    > #### [计费与话单](#ZH-CN_TOPIC_0277260995)
    > 
    > 可通过命令 [**ADD CDRFIELDTEMP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/话单字段控制/话单字段模板/增加话单字段模板（ADD CDRFIELDTEMP）_09896890.md) 配置话单中是否携带CP CIoT EPS Optimisation Indicator、UNI PDU CP Only Flag字段。
    > 
    > #### [特性规格](#ZH-CN_TOPIC_0277260995)

### WSFD-215103

**md：`WSFD-215103/激活Non-IP数据传输（S_PGW-C）_77449667.md`**
- 任务示例脚本（该命令行）：
  `ADD CDRFIELDTEMP:TEMPLATENAME="cdrfieldtemp",PDPTYPEEXT=ENABLE,SGIPTPTUNMETH=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L59:
    >   [**ADD M2MSVRGRPBIND**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/M2M/M2M服务器组绑定关系/增加M2M服务器组绑定关系（ADD M2MSVRGRPBIND）_73321227.md)
    > 8. **可选：**配置话单中是否携带pdp-type-extension、sgi-ptp-tunnelling-method字段。
    >   [**ADD CDRFIELDTEMP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/话单字段控制/话单字段模板/增加话单字段模板（ADD CDRFIELDTEMP）_09896890.md)
    > 
    > ## [任务示例](#ZH-CN_OPI_0277449667)
  L108:
    > 
    > ```
    > ADD CDRFIELDTEMP:TEMPLATENAME="cdrfieldtemp",PDPTYPEEXT=ENABLE,SGIPTPTUNMETH=ENABLE;
    > ```

**md：`WSFD-215103/特性概述_77449666.md`**
- 操作步骤上下文（±2 行原文）：
  L108:
    > #### [计费与话单](#ZH-CN_TOPIC_0277449666)
    > 
    > 可通过命令 [**ADD CDRFIELDTEMP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/话单字段控制/话单字段模板/增加话单字段模板（ADD CDRFIELDTEMP）_09896890.md) 配置话单中是否携带pdp-type-extension、sgi-pgp-tunnelling-method字段。
    > 
    > #### [特性规格](#ZH-CN_TOPIC_0277449666)

### WSFD-215204

**md：`WSFD-215204/WSFD-215204 基于APN的NB-IoT终端接入速率控制参考信息（PGW-C）_77673131.md`**
- 操作步骤上下文（±2 行原文）：
  L20:
    > - [**RMV DCCTEMPLATE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/信用控制/信用控制模板/删除DCC模板（RMV DCCTEMPLATE）_09896925.md)
    > - [**LST DCCTEMPLATE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/信用控制/信用控制模板/查询DCC模板（LST DCCTEMPLATE）_09896933.md)
    > - [**ADD CDRFIELDTEMP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/话单字段控制/话单字段模板/增加话单字段模板（ADD CDRFIELDTEMP）_09896890.md)
    > - [**MOD CDRFIELDTEMP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/话单字段控制/话单字段模板/修改话单字段模板（MOD CDRFIELDTEMP）_09896891.md)
    > - [**RMV CDRFIELDTEMP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/话单字段控制/话单字段模板/删除话单字段模板（RMV CDRFIELDTEMP）_09896892.md)

**md：`WSFD-215204/激活基于APN的NB-IoT终端接入速率控制（PGW-C）_77673129.md`**
- 操作步骤上下文（±2 行原文）：
  L43:
    >   [**ADD DCCTEMPLATE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/信用控制/信用控制模板/增加DCC模板（ADD DCCTEMPLATE）_09896923.md)
    > 5. **可选：**配置CDR话单中携带APN Rate Control字段。
    >   [**ADD CDRFIELDTEMP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/话单字段控制/话单字段模板/增加话单字段模板（ADD CDRFIELDTEMP）_09896890.md)
    > 6. **可选：**配置PGW-CDR中携带APN Rate Control字段。
    >   [**SET OFCCDRPARA**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/离线计费基础参数/离线公共参数/配置离线计费话单参数（SET OFCCDRPARA）_09896905.md)

### WSFD-215205

**md：`WSFD-215205/WSFD-215205 基于服务PLMN的NB-IoT终端接入速率控制参考信息（S_PGW-C）_77673138.md`**
- 操作步骤上下文（±2 行原文）：
  L20:
    > - [**RMV DCCTEMPLATE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/信用控制/信用控制模板/删除DCC模板（RMV DCCTEMPLATE）_09896925.md)
    > - [**LST DCCTEMPLATE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/信用控制/信用控制模板/查询DCC模板（LST DCCTEMPLATE）_09896933.md)
    > - [**ADD CDRFIELDTEMP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/话单字段控制/话单字段模板/增加话单字段模板（ADD CDRFIELDTEMP）_09896890.md)
    > - [**MOD CDRFIELDTEMP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/话单字段控制/话单字段模板/修改话单字段模板（MOD CDRFIELDTEMP）_09896891.md)
    > - [**RMV CDRFIELDTEMP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/话单字段控制/话单字段模板/删除话单字段模板（RMV CDRFIELDTEMP）_09896892.md)

**md：`WSFD-215205/激活基于服务PLMN的NB-IoT终端接入速率控制（S_PGW-C）_77673136.md`**
- 操作步骤上下文（±2 行原文）：
  L45:
    >   [**ADD DCCTEMPLATE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/信用控制/信用控制模板/增加DCC模板（ADD DCCTEMPLATE）_09896923.md)
    > 5. **可选：**配置CDR话单中携带Serving PLMN Rate Control字段。
    >   [**ADD CDRFIELDTEMP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/话单字段控制/话单字段模板/增加话单字段模板（ADD CDRFIELDTEMP）_09896890.md)
    > 6. **可选：**配置PGW-CDR或SGW-CDR中携带Serving PLMN Rate Control字段。
    >   [**SET OFCCDRPARA**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/离线计费基础参数/离线公共参数/配置离线计费话单参数（SET OFCCDRPARA）_09896905.md)

### WSFD-011511

**md：`WSFD-011511/WSFD-011511 NSA用户数据话单生成和上报参考信息_28784144.md`**
- 操作步骤上下文（±2 行原文）：
  L12:
    > 本特性相关的MML命令如下：
    > 
    > - **[**ADD CDRFIELDTEMP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/话单字段控制/话单字段模板/增加话单字段模板（ADD CDRFIELDTEMP）_09896890.md)**
    > - **[**MOD CDRFIELDTEMP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/话单字段控制/话单字段模板/修改话单字段模板（MOD CDRFIELDTEMP）_09896891.md)**
    > - **[**RMV CDRFIELDTEMP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/话单字段控制/话单字段模板/删除话单字段模板（RMV CDRFIELDTEMP）_09896892.md)**

**md：`WSFD-011511/特性概述_28784141.md`**
- 操作步骤上下文（±2 行原文）：
  L103:
    > - Change Notification Request
    > 
    > 5.SGW-C/PGW-C生成话单并上报到CG。SGW-C/PGW-C需配置 [**ADD CDRFIELDTEMP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/话单字段控制/话单字段模板/增加话单字段模板（ADD CDRFIELDTEMP）_09896890.md) 命令中的 “RAN-SecondaryRAT-Usage-Report” 参数，使话单支持携带RAN-SecondaryRAT-Usage-Report字段。
    > 
    > > **说明**

### WSFD-011201

**md：`WSFD-011201/WSFD-011201 支持离线计费参考信息（适用于GGSN_SGW-C_PGW-C）_29423866.md`**
- 操作步骤上下文（±2 行原文）：
  L35:
    > - [**ADD TARIFFGROUP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/费率切换/费率切换组/配置费率切换组（ADD TARIFFGROUP）_09896836.md)
    > - [**SET GLBTARIFFGROUP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/费率切换/全局费率切换组/配置全局费率切换组（SET GLBTARIFFGROUP）_09896840.md)
    > - [**ADD CDRFIELDTEMP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/话单字段控制/话单字段模板/增加话单字段模板（ADD CDRFIELDTEMP）_09896890.md)
    > - [**SET GLBCDRFLDTEMP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/话单字段控制/全局话单字段模板/设置全局话单模板（SET GLBCDRFLDTEMP）_09896895.md)
    > - [**FOC GENERATECDR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费维护/强制生成话单/强制生成话单（FOC GENERATECDR）_09897016.md)

**md：`WSFD-011201/配置话单字段（GGSN_SGW-C_PGW-C）_95923364.md`**
- 数据规划表（该命令的参数行）：
  | **ADD CDRFIELDTEMP** | 话单字段模板名（TEMPLATENAME） | cdrfield-test | 本端规划 | 配置单字段模板，控制话单中是否携带对应字段。 |
  | **ADD CDRFIELDTEMP** | apn-network-identifier（APNNETWORKID） | DISABLE | 本端规划 | 配置话单中是否包含APN网络节点标识信息，默认值是<br>**ENABLE**<br>。 |
  | **ADD CDRFIELDTEMP** | ms-time-zone（MSTIMEZONE） | DISABLE | 与对端协商 | 配置话单中是否携带ms-time-zone字段，默认值是<br>**ENABLE**<br>。 |
  | **ADD CDRFIELDTEMP** | MSISDN字段 | 该字段记录用户的MSISDN号。 |
  | **ADD CDRFIELDTEMP** | served-imeisv字段 | 该字段记录用户的IMEISV号。 |
  | **ADD CDRFIELDTEMP** | CCSeletionMode字段 | 该字段记录计费属性Charging Characteristics的选择模式，是使用用户激活消息中所携带的<br>SGSN/S-GW<br>/MME计费属性，还是使用GGSN/SGW-C/PGW-C所配置的计费属性。 |
  | **ADD CDRFIELDTEMP** | ApnNetworkId字段 | 该字段记录APN中的网络节点标识信息。 |
  | **ADD CDRFIELDTEMP** | ApnSelectMode字段 | 该字段记录<br>SGSN/MME<br>的APN选择模式。 |
  | **ADD CDRFIELDTEMP** | PDPType字段 | 该字段记录PDP类型，IP或者PPP。 |
  | **ADD CDRFIELDTEMP** | SGSNSGWPLMNId字段 | 该字段记录<br>SGSN/S-GW<br>/MME的PLMN。 |
  | **ADD CDRFIELDTEMP** | ServedPDPAddr字段 | 该字段记录用户地址。 |
  | **ADD CDRFIELDTEMP** | DynAddrFlag字段 | 该字段标识用户地址是动态分配地址。<br>说明：对于单栈用户，该字段用于标识IPv4或IPv6类型的动态地址。 |
  | **ADD CDRFIELDTEMP** | ULI字段 | 该字段记录3GPP用户位置信息。<br>说明：3GPP用户接入时，只有<br>SGSN/S-GW<br>和SGW-C/PGW-C都支持user-location-information字段，在话单格式里配置此字段该字段才会生效，否则配置无效。 |
  | **ADD CDRFIELDTEMP** | RATType字段 | 该字段记录用户的无线接入技术类型，取值有<br>**UTRAN**<br>、<br>**GERAN**<br>、<br>**GAN**<br>、<br>**UTRAN**<br>和<br>**HSPA Evolution**<br>。<br>说明：只有<br>SGSN/S-GW<br>/SGW-C/MME和PGW-C都支持携带RATType字段，在话单格式里配置此字段该字段才会生效，否则配置无效。 |
  | **ADD CDRFIELDTEMP** | MSTimeZone字段 | 该字段记录用户所在时区。<br>说明：只有<br>SGSN/S-GW<br>/SGW-C和PGW-C都支持携带ms-time-zone字段，在话单格式里配置此字段该字段才会生效，否则配置无效。 |
  | **ADD CDRFIELDTEMP** | PGWAddressUsed字段 | 该字段记录P-GW的控制面地址，该字段记录IPv4地址。 |
  | **ADD CDRFIELDTEMP** | PGWAddressIPv6字段 | 该字段记录P-GW或S5/S8接口的IPv6地址。<br>说明：该字段协议定义仅R9、R10版本的PGW-CDR支持。 |
  | **ADD CDRFIELDTEMP** | PGWPLMNId字段 | 该字段记录P-GW的PLMN。 |
  | **ADD CDRFIELDTEMP** | NodeId字段 | 该字段记录GGSN/SGW-C/PGW-C的节点标识，节点标识名称通过命令<br>**SET OFCCDRPARA**<br>进行设置。 |
  | **ADD CDRFIELDTEMP** | NetInitPDPCont | 该字段记录用户<br>PDP上下文/EPS承载<br>是由网络侧激活的。 |
  | **ADD CDRFIELDTEMP** | PDNConnectionId字段 | 该字段记录缺省承载的计费标识，以此可以识别出同一个PDN连接内的话单。<br>说明：**ADD CDRFIELDTEMP**<br>命令设置的字段对应于话单中的pdn-connection-charging-id字段。 |
  | **ADD CDRFIELDTEMP** | msiUnauthFlag字段 | 该字段记录用户的IMSI是否未鉴权。<br>说明：通过GTPv2接入的紧急呼叫用户如果IMSI未鉴权，GGSN/SGW-C/PGW-C向CG上报R9及之后版本话单时携带该字段。 |
  | **ADD CDRFIELDTEMP** | LoTV字段 | 该字段记录用户上下行流量信息。 |
  | **ADD CDRFIELDTEMP** | LoSD字段 | 该字段记录业务上下行流量信息。<br>说明：R6版本以后的eG-CDR话单中支持该字段。<br>R8版本以后的PGW-CDR和SGW-CDR话单中支持该字段。 |
  | **ADD CDRFIELDTEMP** | RecordExtention字段 | 该字段记录运营商或设备制造商定义的扩展信息。<br>说明：内容计费G-CDR话单需要扩展RecordExtention字段，普通计费G-CDR话单不需要扩展该字段。R4及之后版本的G-CDR话单以及R6及之后版本的eG-CDR才支持该字段。<br>说明：当参数<br>“record-extensions-operator”<br>设置为<br>“glb”<br>时：<br>- 若同时开启AAA RADIUS计费功能，则可在PGW-CDR话单扩展字段（record-extensions）中携带RADIUS Acct-Session-ID、Termination-Cause字段。<br>- 若同时开启内容计费功能，则可在PGW-CDR话单扩展字段（record-extensions）中携带各业务（RG+SID）上下行报文数。 |
  | **ADD CDRFIELDTEMP** | ImsSigContext字段 | 该字段用户标识是IMS信令专用上下文。 |
  | **ADD CDRFIELDTEMP** | StartTime字段 | 该字段记录<br>PDP上下文/EPS承载<br>激活的时间。 |
  | **ADD CDRFIELDTEMP** | StopTime字段 | 该字段记录<br>PDP上下文/EPS承载<br>去激活的时间。 |
  | **ADD CDRFIELDTEMP** | Diagnostics字段 | 该字段记录用户去激活的原因。 |
  | **ADD CDRFIELDTEMP** | RecSeqNumber字段 | 该字段记录同一<br>PDP上下文/EPS承载<br>中产生的话单的帧序列号。 |
  | **ADD CDRFIELDTEMP** | LocalRecSeqNum字段 | 该字段记录GGSN/SGW-C/PGW-C重启后分配的话单顺序号。 |
  | **ADD CDRFIELDTEMP** | PSFCI字段 | 该字段记录运营商或设备制造商定义的信息。 |
- 任务示例脚本（该命令行）：
  `ADD CDRFIELDTEMP: TEMPLATENAME="cdrfield-test",APNNETWORKID=DISABLE,MSTIMEZONE=DISABLE,ULI=ENABLE,RECORDEXTENTION=DISABLE;`
  `ADD CDRFIELDTEMP: TEMPLATENAME="cdrfield-test",APNNETWORKID=DISABLE,MSTIMEZONE=DISABLE,ULI=ENABLE,RECORDEXTENTION=DISABLE;`
- 操作步骤上下文（±2 行原文）：
  L118:
    > 
    > ```
    > ADD CDRFIELDTEMP: TEMPLATENAME="cdrfield-test",APNNETWORKID=DISABLE,MSTIMEZONE=DISABLE,ULI=ENABLE,RECORDEXTENTION=DISABLE;
    > ```
    > 
  L128:
    > 
    > ```
    > ADD CDRFIELDTEMP: TEMPLATENAME="cdrfield-test",APNNETWORKID=DISABLE,MSTIMEZONE=DISABLE,ULI=ENABLE,RECORDEXTENTION=DISABLE;
    > ```
    > 

### WSFD-011309

**md：`WSFD-011309/WSFD-011309 支持用户属性反射参考信息_28361028.md`**
- 操作步骤上下文（±2 行原文）：
  L20:
    > - [**SET DFTSRVNODERAT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入控制/获取RAT管理/全局RAT配置/设置默认RAT类型（SET DFTSRVNODERAT）_09653166.md)
    > - [**LST DFTSRVNODERAT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入控制/获取RAT管理/全局RAT配置/查询默认RAT类型（LST DFTSRVNODERAT）_09652266.md)
    > - [**ADD CDRFIELDTEMP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/话单字段控制/话单字段模板/增加话单字段模板（ADD CDRFIELDTEMP）_09896890.md)
    > - [**MOD CDRFIELDTEMP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/话单字段控制/话单字段模板/修改话单字段模板（MOD CDRFIELDTEMP）_09896891.md)
    > - [**RMV CDRFIELDTEMP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/话单字段控制/话单字段模板/删除话单字段模板（RMV CDRFIELDTEMP）_09896892.md)

**md：`WSFD-011309/激活支持用户属性反射_28361026.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD CDRFIELDTEMP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/话单字段控制/话单字段模板/增加话单字段模板（ADD CDRFIELDTEMP）_09896890.md) | rat-type（RATTYPE） | ENABLE | 与对端协商 | 配置话单中携带的字段，只有SGSN/S-GW和GGSN/PGW-C/SMF都支持携带rat-type字段，在话单格式里配置此字段才会生效，否则配置无效。 |
  | [**ADD CDRFIELDTEMP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/话单字段控制/话单字段模板/增加话单字段模板（ADD CDRFIELDTEMP）_09896890.md) | user-location-information（ULI） | ENABLE | 与对端协商 | 配置话单中携带的字段，只有SGSN/S-GW和GGSN/PGW-C/SMF都支持携带rat-type字段，在话单格式里配置此字段才会生效，否则配置无效。 |
  | [**ADD CDRFIELDTEMP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/话单字段控制/话单字段模板/增加话单字段模板（ADD CDRFIELDTEMP）_09896890.md) | ms-time-zone（MSTIMEZONE） | ENALBE | 与对端协商 | 配置话单中携带的字段，只有SGSN/S-GW和GGSN/PGW-C/SMF都支持携带rat-type字段，在话单格式里配置此字段才会生效，否则配置无效。 |
- 任务示例脚本（该命令行）：
  `ADD CDRFIELDTEMP:TEMPLATENAME="cdr-field-test",RATTYPE=ENABLE,ULI=ENABLE,MSTIMEZONE=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L48:
    >   > SGSN/S-GW IP地址段与RAT类型的映射表配有默认项，当SGSN/S-GW IP在表中没有匹配项时，会用默认的RAT类型作为它对应的RAT类型。当要配置默认表项时，使用 [**ADD DFTSRVNODERAT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入控制/获取RAT管理/全局RAT配置/设置默认RAT类型（SET DFTSRVNODERAT）_09653166.md) 命令。
    > 5. 配置话单中携带的字段。
    >   [**ADD CDRFIELDTEMP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/话单字段控制/话单字段模板/增加话单字段模板（ADD CDRFIELDTEMP）_09896890.md)
    > 6. 配置APN实例，设置是否允许此APN下的用户通过SGSN/S-GW-IP映射方式来获取RAT Type。
    >   [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)
  L83:
    > 
    > ```
    > ADD CDRFIELDTEMP:TEMPLATENAME="cdr-field-test",RATTYPE=ENABLE,ULI=ENABLE,MSTIMEZONE=ENABLE;
    > ```
    > 

## ④ 自动比对
- 命令真相参数（56）：['APNNETWORKID', 'APNRATECTRL', 'APNSELECTMODE', 'CCBURL', 'CCBUSGDURATION', 'CCSELETIONMODE', 'CPEPSOINDICATOR', 'DIAGNOSTICS', 'DTRECORD', 'DYNADDRFLAG', 'EPDGUEIPPORT', 'EXTCHARGEID', 'HPTIME', 'IMSIUNAUTHFLAG', 'IMSSIGCONTEXT', 'LOCALRECSEQNUM', 'LOSD', 'LOTV', 'LOWPRIIND', 'MOEXCPTDATA', 'MSISDN', 'MSTIMEZONE', 'NETINITPDPCONT', 'NODEID', 'OID', 'PACKETNUM', 'PDNCONNECTIONID', 'PDPTYPE', 'PDPTYPEEXT', 'PGWADDRESSIPV6', 'PGWADDRESSUSED', 'PGWPLMNID', 'PSFCI', 'RATTYPE', 'RECORDEXTENTION', 'RECORDEXTTYPE', 'RECSEQNUMBER', 'SCSASADDR', 'SECRATUSAGE', 'SERVEDIMEISV', 'SERVEDPDPADDR', 'SGIPTPTUNMETH', 'SGSNSGWPLMNID', 'SGWADDRESSIPV6', 'SNSSAI', 'SRVPLMNRATECTRL', 'SSCMODE', 'STARTTIME', 'STOPTIME', 'TEMPLATENAME', 'THREEGPP2USRLOC', 'ULI', 'ULIWLAN', 'UNIPDUCPONLY', 'UWANUDPSRCPORT', 'UWANULI']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'本端规划': 5, '与对端协商': 4}（多值→atom 应考虑 decision_driven）
