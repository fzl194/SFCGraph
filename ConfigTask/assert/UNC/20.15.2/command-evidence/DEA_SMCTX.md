# 命令证据包：DEA SMCTX
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/去活SM上下文/去激活或者停止去活SM上下文（DEA SMCTX）_25120879.md`
> 用该命令的特性数：3

## ② 命令真相（mml_commands.jsonl）
**功能**：![](去激活或者停止去活SM上下文（DEA SMCTX）_25120879.assets/notice_3.0-zh-cn_2.png)

该命令会去激活指定的签约用户。因为去活用户需要通知周边网元清除相关资源，所以当去活速率过高时，网络上会产生大量消息需要CPU进行处理，导致CPU使用率升高。

**适用NF：PGW-C、SGW-C、SMF、GGSN**

该命令用于去活会话管理上下文。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。

- 该命令只去激活当前系统已有用户，即不会去激活该命令下发之后激活的用户。
- 当批量去激活用户时，系统负荷增大，CPU使用率会有一定程度的升高。待去激活完成后，系统会恢复正常。
- 基于APN去活时，若该APN对应的Radius服务器支持可选计费，且要求单用户去活过程中不需要向Radius服务器发送Accounting Stop Request消息，在去活用户完成时

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| ACTIONTYPE | 操作类型 | local_planned | required | 无 | <br>- START_DEA（开始去活） |
| DEATYPE | 去活方式 | local_planned | conditional | 无 | <br>- “APN（APN）”：按APN名称去激活用户 |
| IMSI | IMSI | local_planned | conditional | 无 | 字符串类型，输入长度范围是5~15。每个字符必须为0~9的数字。 |
| MSISDN | MSISDN | local_planned | conditional | 无 | 字符串类型，输入长度范围是1~15。每个字符必须为0~9的数字。 |
| IMEI | 国际移动用户识别码 | local_planned | conditional | 无 | 字符串类型，输入长度范围是15~16。 |
| SEGSTART | 号段起始字符串 | local_planned | conditional | 无 | 字符串类型，输入长度范围是5~15。每个字符必须为0~9的数字。 |
| SEGEND | 号段结束字符串 | local_planned | conditional | 无 | 字符串类型，输入长度范围是5~15。每个字符必须为0~9的数字。 |
| NODETYPE | 网元类型 | local_planned | conditional | 无 | <br>- UPF（UPF） |
| NFINSTANCEID | NF实例标识 | local_planned | conditional | 无 | 字符串类型，输入长度范围是1~50。 |
| APNTYPE | APN类型 | local_planned | conditional | SERVICE | <br>- REQUESTED（请求的） |
| APN | APN名称 | local_planned | conditional | 无 | 字符串类型，输入长度范围是1~63。不区分大小写，只能由“-”、数字、大小写字母和“.”组成，不能以 |
| UPFROLE | UPF角色 | local_planned | conditional | BOTH | <br>- BOTH（PSA-UPF和I-UPF） |
| WLNETWKTYPE | 无线网络类型 | local_planned | conditional | 无 | <br>- NW2G3G4G（2/3/4G网络） |
| BEARERID | 承载索引 | local_planned | conditional | 无 | 整数类型，取值范围是1~63。 |
| PDUSESSIONID | PDU会话标识 | local_planned | conditional | 无 | 整数类型，取值范围是1~255。 |
| QFI | QOS流标识 | local_planned | conditional | 无 | 整数类型，取值范围是1~15。 |
| HOLDPDPTYPE | 保留承载类型 | local_planned | conditional | 无 | <br>- “VOLTE（语音业务承载）”：指定该参数时，在HOLDTIME超时前不删除正在进行语音 |
| HOLDTIME | 承载保持时长(分钟) | local_planned | conditional | 0 | 整数类型，取值范围是0~1440，单位是分钟。 |
| PCSCFGROUPNAME | P-CSCF组名称 | local_planned | conditional | 无 | 字符串类型，输入长度范围是1~63。由英文字母、数字、“.”、“-”、“_”构成，不区分大小写。 |
| PCSCFIPVERSION | P-CSCF IP地址版本 | local_planned | conditional | 无 | <br>- “IPv4（IPv4）”：IPv4地址类型 |
| PCSCFIPV4 | P-CSCF IPv4地址 | local_planned | conditional | 无 | IPv4地址类型。 |
| PCSCFIPV6 | P-CSCF IPv6地址 | local_planned | conditional | 无 | IPv6地址类型。 |
| ACCESSTYPE234G | 接入类型 | local_planned | conditional | AT_3GPP_ACCESS-1&AT_UNTRUSTED_NON_3GPP_A | <br>- AT_3GPP_ACCESS（3GPP_ACCESS） |
| FAILHANDLETYPE | 旁路处理失败类型 | local_planned | conditional | 无 | <br>- “AUTHFAIL_BYPASS（Radius鉴权失败旁路用户）”：去活Radius鉴权 |
| LOCKDEACTIVE | 锁定APN的去激活 | local_planned | conditional | 无 | <br>- DISABLE（不使能） |
| RATTYPE | RAT类型 | 对端协商 | conditional | 无 | <br>- UTRAN（通用陆地无线接入网） |
| PCFINSTANCEID | PCF实例标识 | local_planned | conditional | 无 | 字符串类型，输入长度范围是0~50。 |
| PCRFHOSTNAME | PCRF主机名 | local_planned | conditional | 无 | 字符串类型，输入长度范围是1~127。 |
| NODEIPVERSION | 对端网元IP地址版本 | local_planned | conditional | 无 | <br>- “IPv4（IPv4）”：IPv4地址类型 |
| NODEIPV4 | 对端网元IPv4地址 | local_planned | conditional | 无 | IPv4地址类型。 |
| NODEIPV6 | 对端网元IPv6地址 | local_planned | conditional | 无 | IPv6地址类型。 |
| STARTDATE | 开始日期 | local_planned | conditional | 无 | DATE。输入格式是YYYY/MM/DD。YYYY表示年份，MM表示月份，DD表示日，均为整数形式。 |
| STARTTIME | 开始时间 | local_planned | conditional | 无 | TIME。输入格式是HH:MM:SS。HH表示小时，整数形式，取值范围是0～23；MM表示分，整数形 |
| ENDDATE | 截止日期 | local_planned | conditional | 无 | DATE。输入格式是YYYY/MM/DD。YYYY表示年份，MM表示月份，DD表示日，均为整数形式。 |
| ENDTIME | 截止时间 | local_planned | conditional | 无 | TIME。输入格式是HH:MM:SS。HH表示小时，整数形式，取值范围是0～23；MM表示分，整数形 |
| USERPROFILE | 用户模板 | local_planned | conditional | 无 | 字符串类型，输入长度范围是1~63。不支持空格，不区分大小写。 |
| REMAINSGWCTX | 保留SGW上下文 | local_planned | conditional | 无 | <br>- DISABLE（不使能） |
| CHARGINGTYPE | 计费类型 | local_planned | conditional | 无 | <br>- OFFLINE（离线） |
| BEARERSTATE | 承载状态 | local_planned | conditional | 无 | <br>- “MAINTAIN（保持态）”：保留承载。 |
| LACGROUP | LAC组 | local_planned | conditional | 无 | 字符串类型，输入长度范围是1~32。不支持空格，不区分大小写。 |
| TACGROUP | TAC组 | local_planned | conditional | 无 | 字符串类型，输入长度范围是1~32。不支持空格，不区分大小写。 |
| NGLANGROUPID | 5G LAN组ID | local_planned | conditional | 无 | 字符串类型，输入长度范围是18~37。字母大小写不敏感且全局唯一。 |
| RATIOTYPE | 去活比例类型 | local_planned | conditional | 无 | <br>- “SGWRATIO（按比例去激活SGW-C上的会话）”：当选择SGWRATIO时，指定待 |
| RATIOVALUE | 用户数的比例(%) | local_planned | conditional | 100 | 整数类型，取值范围是1~100，单位是百分比。 |
| DNAI | 数据网络访问标识符 | global_planned | conditional | 无 | 字符串类型，输入长度范围是1~63。不支持空格，不区分大小写。 |
| MULTIDNNTYPE | 智能分流DNN类型 | local_planned | conditional | 无 | <br>- “ALL_DNN（所有专用DNN）”：去活所有专用DNN关联的通用DNN用户。 |
| DEDDNN | 专用DNN | global_planned | conditional | 无 | 字符串类型，输入长度范围是1~64。不支持空格，不区分大小写。 |
| LBISW | 去激活未分配LBI的用户 | local_planned | conditional | 无 | <br>- DISABLE（不使能） |
| NASCAUSE | NAS原因值 | local_planned | conditional | 无 | 整数类型，取值范围是0~4294967295。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-106203

**md：`WSFD-106203/WSFD-106203 别名APN参考信息（适用于GGSN_PGW-C_SMF）_34797882.md`**
- 操作步骤上下文（±2 行原文）：
  L15:
    > - [**ADD APNALIAS**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/别名APN/增加APN别名配置（ADD APNALIAS）_28567622.md)
    > - [**LCK APNALIAS**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/别名APN/锁定APN别名配置（LCK APNALIAS）_28567625.md)
    > - [**DEA SMCTX**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/去活SM上下文/去激活或者停止去活SM上下文（DEA SMCTX）_25120879.md)
    > - [**SET DEACTIVERATE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/去活PDP速率/设置去激活用户承载的速率（SET DEACTIVERATE）_09652156.md)
    > 

**md：`WSFD-106203/激活别名APN_34797880.md`**
- 数据规划表（该命令的参数行）：
  | [**DEA SMCTX**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/去活SM上下文/去激活或者停止去活SM上下文（DEA SMCTX）_25120879.md) | 操作类型（ACTIONTYPE） | START_DEA | 本端规划 | 基于别名APN批量去激活用户，去激活之前必须通过<br>[**LCK APNALIAS**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/别名APN/锁定APN别名配置（LCK APNALIAS）_28567625.md)<br>命令锁定别名APN。 |
  | [**DEA SMCTX**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/去活SM上下文/去激活或者停止去活SM上下文（DEA SMCTX）_25120879.md) | 去活方式（DEATYPE） | APN | 本端规划 | 基于别名APN批量去激活用户，去激活之前必须通过<br>[**LCK APNALIAS**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/别名APN/锁定APN别名配置（LCK APNALIAS）_28567625.md)<br>命令锁定别名APN。 |
  | [**DEA SMCTX**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/去活SM上下文/去激活或者停止去活SM上下文（DEA SMCTX）_25120879.md) | APN类型（APNTYPE） | REQUESTED | 本端规划 | 基于别名APN批量去激活用户，去激活之前必须通过<br>[**LCK APNALIAS**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/别名APN/锁定APN别名配置（LCK APNALIAS）_28567625.md)<br>命令锁定别名APN。 |
  | [**DEA SMCTX**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/去活SM上下文/去激活或者停止去活SM上下文（DEA SMCTX）_25120879.md) | APN（APN） | apn1 | 本端规划 | 基于别名APN批量去激活用户，去激活之前必须通过<br>[**LCK APNALIAS**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/别名APN/锁定APN别名配置（LCK APNALIAS）_28567625.md)<br>命令锁定别名APN。 |

### WSFD-205105

**md：`WSFD-205105/WSFD-205105 上下文回收管理参考信息_28341923.md`**
- 操作步骤上下文（±2 行原文）：
  L16:
    > - **[SET DFTSESSIONTIME](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/SMF公共配置/空闲上下文定时器/设置默认会话上下文定时器（SET DFTSESSIONTIME）_96243108.md)**
    > - **[SET APNSESSIONTIME](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN定时器属性/设置APN会话上下文定时器配置（SET APNSESSIONTIME）_96243086.md)**
    > - **[DEA SMCTX](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/去活SM上下文/去激活或者停止去活SM上下文（DEA SMCTX）_25120879.md)**
    > 
    > #### [告警](#ZH-CN_TOPIC_0228341923)

**md：`WSFD-205105/激活上下文回收管理_27434204.md`**
- 数据规划表（该命令的参数行）：
  | **[DEA SMCTX](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/去活SM上下文/去激活或者停止去活SM上下文（DEA SMCTX）_25120879.md)** | 操作类型（ACTIONTYPE） | START_DEA | 本端规划 | 配置去激活指定用户会话上下文。 |
  | **[DEA SMCTX](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/去活SM上下文/去激活或者停止去活SM上下文（DEA SMCTX）_25120879.md)** | 去活方式（DEATYPE） | IMSI | 本端规划 | 配置去激活指定用户会话上下文。 |
  | **[DEA SMCTX](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/去活SM上下文/去激活或者停止去活SM上下文（DEA SMCTX）_25120879.md)** | IMSI（IMSI） | 123456789 | 本端规划 | 配置去激活指定用户会话上下文。 |
- 任务示例脚本（该命令行）：
  `DEA SMCTX: ACTIONTYPE=START_DEA, DEATYPE=IMSI, IMSI="123456789";`
- 操作步骤上下文（±2 行原文）：
  L59:
    >   **[SET APNSESSIONTIME](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN定时器属性/设置APN会话上下文定时器配置（SET APNSESSIONTIME）_96243086.md)**
    > 6. 去激活指定用户的会话上下文。
    >   **[DEA SMCTX](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/去活SM上下文/去激活或者停止去活SM上下文（DEA SMCTX）_25120879.md)**
    > 7. 打开上下文回收管理特性的License配置开关。
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
  L94:
    >   //去激活指定IMSI（123456789）用户会话上下文。
    >   ```
    >   DEA SMCTX: ACTIONTYPE=START_DEA, DEATYPE=IMSI, IMSI="123456789";
    >   ```
    >   //打开本特性的License配置开关。

### WSFD-109101

**md：`WSFD-109101/调测PCC基本功能_45059543.md`**
- 任务示例脚本（该命令行）：
  `DEA SMCTX: ACTIONTYPE=START_DEA, DEATYPE=IMSI, IMSI="460000123456789";`
- 操作步骤上下文（±2 行原文）：
  L50:
    >   ```
    > 3. 创建用户跟踪任务，消息类型选择N4和N7。
    > 4. 执行 [**DEA SMCTX**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/去活SM上下文/去激活或者停止去活SM上下文（DEA SMCTX）_25120879.md) 命令，去激活指定IMSI的签约用户。确保拨测用户未激活。
    >   ```
    >   DEA SMCTX: ACTIONTYPE=START_DEA, DEATYPE=IMSI, IMSI="460000123456789";
  L52:
    > 4. 执行 [**DEA SMCTX**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/去活SM上下文/去激活或者停止去活SM上下文（DEA SMCTX）_25120879.md) 命令，去激活指定IMSI的签约用户。确保拨测用户未激活。
    >   ```
    >   DEA SMCTX: ACTIONTYPE=START_DEA, DEATYPE=IMSI, IMSI="460000123456789";
    >   ```
    > 5. 测试终端使用APN“apn-test”接入网络。
  L80:
    >   ```
    >   > **说明**
    >   > 如拨测用户不需要使用拨测时的PCF，则需要执行 [**DEA SMCTX**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/去活SM上下文/去激活或者停止去活SM上下文（DEA SMCTX）_25120879.md) 命令，去激活拨测用户，确保拨测用户处于未激活状态。
    > 10. 执行 [**LST TSTPCFBINDING**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCF发现和选择管理/PCF拨测管理/查询拨测用户和PCF的绑定关系（LST TSTPCFBINDING）_77037096.md) 命令，查看是否存在拨测用户和PCF的绑定关系。
    >     - 不存在，拨测结束。

**md：`WSFD-109101/异常处理流程_53323998.md`**
- 操作步骤上下文（±2 行原文）：
  L18:
    > > 等待PCF响应超时或者PCF返回异常可能会导致回滚为本地PCC。SMF执行如下命令可将回滚为本地PCC的会话去活。SET DEACTIVERATE可用于配置去活速率。
    > >
    > > DEA SMCTX: ACTIONTYPE=START_DEA, DEATYPE=FAIL_HANDLE_TYPE, FAILHANDLETYPE=PCC_ROLLBACK;

## ④ 自动比对
- 命令真相参数（49）：['ACCESSTYPE234G', 'ACTIONTYPE', 'APN', 'APNTYPE', 'BEARERID', 'BEARERSTATE', 'CHARGINGTYPE', 'DEATYPE', 'DEDDNN', 'DNAI', 'ENDDATE', 'ENDTIME', 'FAILHANDLETYPE', 'HOLDPDPTYPE', 'HOLDTIME', 'IMEI', 'IMSI', 'LACGROUP', 'LBISW', 'LOCKDEACTIVE', 'MSISDN', 'MULTIDNNTYPE', 'NASCAUSE', 'NFINSTANCEID', 'NGLANGROUPID', 'NODEIPV4', 'NODEIPV6', 'NODEIPVERSION', 'NODETYPE', 'PCFINSTANCEID', 'PCRFHOSTNAME', 'PCSCFGROUPNAME', 'PCSCFIPV4', 'PCSCFIPV6', 'PCSCFIPVERSION', 'PDUSESSIONID', 'QFI', 'RATIOTYPE', 'RATIOVALUE', 'RATTYPE', 'REMAINSGWCTX', 'SEGEND', 'SEGSTART', 'STARTDATE', 'STARTTIME', 'TACGROUP', 'UPFROLE', 'USERPROFILE', 'WLNETWKTYPE']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'本端规划': 7}（多值→atom 应考虑 decision_driven）
