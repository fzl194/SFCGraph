# 命令证据包：SET HTTPCONF
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/HTTP管理/HTTP属性管理/设置HTTP属性（SET HTTPCONF）_83972196.md`
> 用该命令的特性数：4

## ② 命令真相（mml_commands.jsonl）
**功能**：![](设置HTTP属性（SET HTTPCONF）_83972196.assets/notice_3.0-zh-cn_2.png)

该命令中SIGNALROUTING参数用于设置信令路由开关，信令路由功能下HTTP性能降低，可能影响正常业务，不建议开启使用。 该命令中MAXCLIENTSTREAM参数用于设置最大并发流上限，值配置过大或过小均会造成HTTP性能降低，可能影响正常业务，建议直接使
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| SIGNALROUTING | HTTPLOGLEVEL | TCPLOGLEVEL | DETECTINTERVAL | LOADREPINTERVAL | LINKAGINGTIME | CLIENTRCVRSPTMT | SERVERRCVBDTMT | SERVERSNDRSPTMT | P

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| SIGNALROUTING | 信令路由开关 | local_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST HTTP | <br>- TRUE(TRUE) |
| HTTPLOGLEVEL | http-server日志级别 | local_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST HTTP | <br>- “DEBUG（DEBUG）”：打开调试级别及以上日志输出 |
| TCPLOGLEVEL | tcp-process日志级别 | local_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST HTTP | <br>- “DEBUG（DEBUG）”：打开调试级别及以上日志输出 |
| DETECTINTERVAL | 故障链路探测最长时间间隔(s) | local_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST HTTP | 整数类型，取值范围是1~720，单位是秒。 |
| LOADREPINTERVAL | 链路负载上报时间间隔(s) | local_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST HTTP | 整数类型，取值范围是1~100，单位是秒。 |
| LINKAGINGTIME | 链路老化时间(min) | local_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST HTTP | 整数类型，取值范围是10~14400，单位是分钟。 |
| CLIENTRCVRSPTMT | 客户端接收HTTP响应消息超时时间(s) | global_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST HTTP | 整数类型，取值范围是1~20，单位是秒。 |
| SERVERRCVBDTMT | 服务端接收HTTP请求消息体超时时间(s) | global_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST HTTP | 整数类型，取值范围是1~20，单位是秒。 |
| SERVERSNDRSPTMT | 服务端回复HTTP响应消息超时时间(s) | global_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST HTTP | 整数类型，取值范围是1~20，单位是秒。 |
| PINGSWITCH | 客户端HTTP PING探测开关 | local_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST HTTP | <br>- TRUE(TRUE) |
| PINGINTVAL | 客户端HTTP PING探测时间间隔(s) | local_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST HTTP | 整数类型，取值范围是10~600，单位是秒。协议规定的最小值是60秒。如要设置为低于60秒，必须首先 |
| PINGPROBES | 客户端HTTP PING探测次数 | local_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST HTTP | 整数类型，取值范围是2~10。 |
| KEEPALIVESW | Keepalive功能开关 | local_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST HTTP | <br>- “ON（打开）”：打开 |
| KEEPALIVETIME | Keepalive空闲时间(s) | local_planned | conditional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST HTTP | 整数类型，取值范围是60~65535，单位是秒。 |
| KEEPALIVEINTVL | Keepalive探测间隔(s) | local_planned | conditional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST HTTP | 整数类型，取值范围是1~150，单位是秒。 |
| KEEPALIVEPROBES | Keepalive探测次数 | local_planned | conditional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST HTTP | 整数类型，取值范围是1~20，单位是次。 |
| DESCRIPTION | 描述 | local_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST HTTP | 字符串类型，输入长度范围是0~255。 |
| MAXBODYSIZE | 最大消息体大小(MBytes) | local_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST HTTP | 整数类型，取值范围是2~16。 |
| MAXJSONLEAFNUM | JSON数据最多叶子节点个数 | local_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST HTTP | 整数类型，取值范围是16000~512000。 |
| TCPSEDELTIME | TCP会话删除延迟时间(s) | local_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST HTTP | 整数类型，取值范围是3~10，单位是秒。 |
| MAXCLIENTSTREAM | 客户端最大并发流 | local_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST HTTP | 整数类型，取值范围是0~32768，单位是条。0为无法处理的非法值，当配置为0时，实际以4096的最 |
| INITLINKINTVL | 初始重建链间隔(ms) | local_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST HTTP | 整数类型，取值范围是200~10000，单位是毫秒。 |
| IPDETECTSW | IP可达自动探测的功能开关 | local_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST HTTP | <br>- TRUE(TRUE) |
| PERFSTATSW | 性能统计功能开关 | local_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST HTTP | <br>- TRUE(TRUE) |
| LINKSETRECOVERTIME | 发送恢复链路集信息请求的时间间隔 | local_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST HTTP | 整数类型，取值范围是10~60，单位是秒。 |
| CONFCHECKSW | 配置核查开关 | local_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST HTTP | <br>- TRUE(TRUE) |
| LINKCHECKSW | 链路核查开关 | local_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST HTTP | <br>- TRUE(TRUE) |
| COMPRESSTH | 压缩报文阈值 (KBytes) | local_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST HTTP | 整数类型，取值范围是0~4096，单位是千字节。 |
| REQCBFCSW | Reqcb流控开关 | local_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST HTTP | <br>- TRUE(TRUE) |
| SYNREXINTERVAL | TCP SYN包重传时间间隔(ms) | local_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST HTTP | 整数类型，取值范围是100~120000，单位是毫秒。 |
| SYNREXTIMES | TCP SYN包重传最大次数 | local_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST HTTP | 整数类型，取值范围是0~13，单位是次。 |
| ESTABREXTIMES | TCP建链成功后包重传最大次数 | local_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST HTTP | 整数类型，取值范围是0~13，单位是次。 |
| BACKOFFINTERVAL | HTTP建链自动退避时间间隔(ms) | local_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST HTTP | 整数类型，取值范围是0~10000，单位是毫秒。 |
| HTTPVERSIONSW | 使能HTTP1.1开关 | local_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST HTTP | <br>- TRUE(TRUE) |
| HTTPGOAWAYSW | HTTP Goaway处理开关 | local_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST HTTP | <br>- TRUE(TRUE) |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-206101

**md：`WSFD-206101/WSFD-206101 UDM全故障业务保活特性概述_90966326.md`**
- 操作步骤上下文（±2 行原文）：
  L79:
    > - 本特性不适合ToB用户使用。因为ToB用户签约数据差异大，无法针对所有ToB用户配置本地签约数据。建议按照不配置最小签约方式部署，只保护已有会话惯性运行。
    > - 默认签约数据支持按照IMSI前缀配置（建议按PLMN粒度配置），不支持按照用户粒度配置个性化签约数据，例如：不支持按UE的地址（UDM签约静态地址）/DNN/APN/切片/QOS等参数进行差异化配置。
    > - 在AMF探测出AUSF/UDM/SCP故障期间（时长默认4分钟，可通过命令**[SET HTTPCONF](../../../../../OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/HTTP管理/HTTP属性管理/设置HTTP属性（SET HTTPCONF）_83972196.md)**命令的“PINGINTVAL”和“PINGGRPOBES”参数配置）内，UE发起注册流程可能会失败。
    > - 在SMF探测出UDM/SCP故障期间（默认4分钟，可通过命令**[SET HTTPCONF](../../../../../OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/HTTP管理/HTTP属性管理/设置HTTP属性（SET HTTPCONF）_83972196.md)**命令的“PINGINTVAL”和“PINGGRPOBES”参数配置）内，UE发起会话激活流程或者4G到5G会话切换失败，探测出UDM/SCP故障后会话可以进入UDM Bypass状态。
    > - 在UDM全故障时，无论是否开启UDM全故障业务保活功能，在用户发起inter AMF移动性管理流程后，由于UDM全部故障源侧AMF不会收到去注册消息，源侧AMF上用户上下文无法及时删除，可能导致系统资源（比如静态上下文信息等）使用率升高。
  L80:
    > - 默认签约数据支持按照IMSI前缀配置（建议按PLMN粒度配置），不支持按照用户粒度配置个性化签约数据，例如：不支持按UE的地址（UDM签约静态地址）/DNN/APN/切片/QOS等参数进行差异化配置。
    > - 在AMF探测出AUSF/UDM/SCP故障期间（时长默认4分钟，可通过命令**[SET HTTPCONF](../../../../../OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/HTTP管理/HTTP属性管理/设置HTTP属性（SET HTTPCONF）_83972196.md)**命令的“PINGINTVAL”和“PINGGRPOBES”参数配置）内，UE发起注册流程可能会失败。
    > - 在SMF探测出UDM/SCP故障期间（默认4分钟，可通过命令**[SET HTTPCONF](../../../../../OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/HTTP管理/HTTP属性管理/设置HTTP属性（SET HTTPCONF）_83972196.md)**命令的“PINGINTVAL”和“PINGGRPOBES”参数配置）内，UE发起会话激活流程或者4G到5G会话切换失败，探测出UDM/SCP故障后会话可以进入UDM Bypass状态。
    > - 在UDM全故障时，无论是否开启UDM全故障业务保活功能，在用户发起inter AMF移动性管理流程后，由于UDM全部故障源侧AMF不会收到去注册消息，源侧AMF上用户上下文无法及时删除，可能导致系统资源（比如静态上下文信息等）使用率升高。
    > - UDM故障后用户发生互操作流程，由于协议定义互操作流程中无法获取UE的MSISDN，如果UE后续发起会话重建，AMF默认使会话创建失败，对应的业务失败。AMF可以通过软参DWORD17 BIT32配置允许PDU会话创建成功，但由于无MSISDN，SMF和PCF交互可能失败导致会话创建失败；如果会话能创建成功，则会出现无MSISDN的异常话单。

### WSFD-130011

**md：`WSFD-130011/容灾原理_46546724.md`**
- 操作步骤上下文（±2 行原文）：
  L12:
    > 
    > - 业务超时应答，超时时间为3秒。
    > - HTTP PING检测，默认检测3次，周期60秒。您可以通过**SET HTTPCONF**命令调整检测参数。
    > - AMF向NRF订阅SMSF状态，当SMSF故障，NRF将SMSF状态置位Suspended，并将状态通知到AMF。
    > 

### WSFD-109101

**md：`WSFD-109101/配置QoS能力开放功能_48518810.md`**
- 数据规划表（该命令的参数行）：
  | **[SET HTTPCONF](../../../../../../../OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/HTTP管理/HTTP属性管理/设置HTTP属性（SET HTTPCONF）_83972196.md)** | 使能HTTP1.1开关（HTTPVERSIONSW ） | TRUE | 本端规划 | 使能HTTP1.1开关 |
- 任务示例脚本（该命令行）：
  `SET HTTPCONF: HTTPVERSIONSW=TRUE;`
- 操作步骤上下文（±2 行原文）：
  L78:
    >   **[ADD SBIAPLE](../../../../../../../OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/SBI管理/服务化接口本端实体管理/增加服务化接口本端实体（ADD SBIAPLE）_28971835.md)**
    > 8. 使能HTTP1.1开关。
    >   **[SET HTTPCONF](../../../../../../../OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/HTTP管理/HTTP属性管理/设置HTTP属性（SET HTTPCONF）_83972196.md)**
    > 9. 开启QoS能力开放功能开关。
    >   **[SET SMCOMMFUNC](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/会话协议参数管理/会话管理拓展功能/通用会话管理拓展功能/设置通用会话拓展功能（SET SMCOMMFUNC）_08433263.md)**
  L148:
    > 
    >   ```
    >   SET HTTPCONF: HTTPVERSIONSW=TRUE;
    >   ```
    > 7. 开启QoS能力开放功能。

### WSFD-010801

**md：`WSFD-010801/WSFD-010801 系统过载控制功能（服务化接口流控）参考信息_63630845.md`**
- 操作步骤上下文（±2 行原文）：
  L44:
    > **[LST HTTPGLBFIXEDBWFC](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/HTTP流控管理/HTTP全局固定带宽流控管理/查询HTTP全局固定带宽流控（LST HTTPGLBFIXEDBWFC）_03315070.md)**
    > 
    > **[SET HTTPCONF](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/HTTP管理/HTTP属性管理/设置HTTP属性（SET HTTPCONF）_83972196.md)**
    > 
    > **[LST HTTPCONF](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/HTTP管理/HTTP属性管理/查询HTTP属性（LST HTTPCONF）_28971839.md)**

**md：`WSFD-010801/WSFD-010801 系统过载控制功能（服务化接口流控）特性概述_63350977.md`**
- 操作步骤上下文（±2 行原文）：
  L102:
    > - **基于资源的流控**
    >   UNC 支持基于关键资源使用情况对HTTP链路上的消息进行流控，关键资源包括：HTTP进程的请求消息控制块资源、HTTP进程的PBUF资源和HTTP进程的内存资源。
    >     - HTTP进程的请求消息控制块资源：当**[SET HTTPCONF](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/HTTP管理/HTTP属性管理/设置HTTP属性（SET HTTPCONF）_83972196.md)**命令的“Reqcb流控开关（REQCBFCSW）”为“TRUE”，通过**[ADD HTTPRESCFG](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/HTTP流控管理/HTTP资源流控管理/增加HTTP资源流控门限（ADD HTTPRESCFG）_01384190.md)**命令配置开启流控的资源类型、链路和门限。当对应HTTP链路剩余的请求消息控制块资源小于配置的资源门限（“THRESHOLD”）时，对消息进行流控，并上报**[ALM-100117 HTTP资源过载](../../../../../../网络运维/故障处理/UNC告警处理/平台告警/ALM-100117 HTTP资源过载_25943791.md)**告警。
    >     - HTTP进程的内存资源：当**[SET HTTPMEMFC](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/HTTP流控管理/HTTP内存流控管理/设置HTTP内存流控（SET HTTPMEMFC）_01384198.md)**命令的“内存流控开关（MEMFCSWITCH）”为“TRUE”，并且HTTP进程上HTTP Body内存分区的剩余连续内存小于“内存流控起控阈值（MEMFCSTARTTHD）”时，对消息大小大于“内存流控大包阈值（MEMFCBIGPKTTHD）”的HTTP消息进行流控，并上报**[ALM-100117 HTTP资源过载](../../../../../../网络运维/故障处理/UNC告警处理/平台告警/ALM-100117 HTTP资源过载_25943791.md)**告警；当HTTP进程上HTTP Body内存分区的剩余连续内存大于等于“内存流控停控阈值（MEMFCSTOPTHD）”时，停止流控并恢复**[ALM-100117 HTTP资源过载](../../../../../../网络运维/故障处理/UNC告警处理/平台告警/ALM-100117 HTTP资源过载_25943791.md)**告警。
    >     - HTTP进程的PBUF资源：当HTTP进程上的PBUF使用率超过80%时，UNC对消息进行流控，并上报**[ALM-100117 HTTP资源过载](../../../../../../网络运维/故障处理/UNC告警处理/平台告警/ALM-100117 HTTP资源过载_25943791.md)**告警；当HTTP进程上的PBUF使用率低于75%时，UNC停止流控，并恢复**[ALM-100117 HTTP资源过载](../../../../../../网络运维/故障处理/UNC告警处理/平台告警/ALM-100117 HTTP资源过载_25943791.md)**告警。

**md：`WSFD-010801/激活服务化接口流控_14991114.md`**
- 数据规划表（该命令的参数行）：
  | **[SET HTTPCONF](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/HTTP管理/HTTP属性管理/设置HTTP属性（SET HTTPCONF）_83972196.md)** | Reqcb流控开关（REQCBFCSW） | TRUE | 全网规划 | 开启ReqCB流控开关。 |
- 任务示例脚本（该命令行）：
  `SET HTTPCONF: REQCBFCSW=TRUE;`
- 操作步骤上下文（±2 行原文）：
  L135:
    >   **[SET HTTPGLBFIXEDBWFC](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/HTTP流控管理/HTTP全局固定带宽流控管理/设置HTTP全局固定带宽流控（SET HTTPGLBFIXEDBWFC）_56474481.md)**
    > 7. 开启ReqCB流控开关。
    >   **[SET HTTPCONF](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/HTTP管理/HTTP属性管理/设置HTTP属性（SET HTTPCONF）_83972196.md)**
    > 8. 配置基于ReqCB资源的流控信息。
    >   **[ADD HTTPRESCFG](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/HTTP流控管理/HTTP资源流控管理/增加HTTP资源流控门限（ADD HTTPRESCFG）_01384190.md)**
  L226:
    > 
    > ```
    > SET HTTPCONF: REQCBFCSW=TRUE; 
    > ```
    > 

## ④ 自动比对
- 命令真相参数（35）：['BACKOFFINTERVAL', 'CLIENTRCVRSPTMT', 'COMPRESSTH', 'CONFCHECKSW', 'DESCRIPTION', 'DETECTINTERVAL', 'ESTABREXTIMES', 'HTTPGOAWAYSW', 'HTTPLOGLEVEL', 'HTTPVERSIONSW', 'INITLINKINTVL', 'IPDETECTSW', 'KEEPALIVEINTVL', 'KEEPALIVEPROBES', 'KEEPALIVESW', 'KEEPALIVETIME', 'LINKAGINGTIME', 'LINKCHECKSW', 'LINKSETRECOVERTIME', 'LOADREPINTERVAL', 'MAXBODYSIZE', 'MAXCLIENTSTREAM', 'MAXJSONLEAFNUM', 'PERFSTATSW', 'PINGINTVAL', 'PINGPROBES', 'PINGSWITCH', 'REQCBFCSW', 'SERVERRCVBDTMT', 'SERVERSNDRSPTMT', 'SIGNALROUTING', 'SYNREXINTERVAL', 'SYNREXTIMES', 'TCPLOGLEVEL', 'TCPSEDELTIME']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'本端规划': 1, '全网规划': 1}（多值→atom 应考虑 decision_driven）
