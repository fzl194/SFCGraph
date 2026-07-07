# 命令证据包：SET CDRTRANSFER
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/GTPP信令/话单发送参数/设置话单发送控制参数（SET CDRTRANSFER）_09896850.md`
> 用该命令的特性数：1

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：SGW-C、PGW-C、SMF**

设置话单发送控制参数。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。
- 该命令最大记录数为1。
- SET CDRTRANSFER命令的五个字段都是可选参数，如果参数没有输入，不做任何修改；如果参数有输入，则修改输入的字段。
- CG故障或者负载过重的情况下，话单重传时间间隔会有所延长。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | GTPPMAXPAYLOAD | RETRANSTIMES | RETRAN

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| GTPPMAXPAYLOAD | GTP'消息最大可携带的话单字节数 | local_planned | optional | 无 | 整数类型，取值范围为1200～7180。 |
| RETRANSTIMES | Echo and Data Record Transfer Request重传次数 | local_planned | optional | 无 | 整数类型，取值范围为1～3。 |
| RETRANSINTERVAL | Data Record Transfer Request重传时间间隔（秒） | local_planned | optional | 无 | 整数类型，取值范围为1～10。 |
| NARESTRANSINTVL | Node Alive消息重传时间间隔（秒） | local_planned | optional | 无 | 整数类型，取值范围为5～600。 |
| CGSELECTIONMODE | CG选择模式 | local_planned | optional | 无 | 枚举类型。 |
| UDPCHECKSUM | GTP'报文CheckSum开关 | local_planned | optional | 无 | 枚举类型。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-011201

**md：`WSFD-011201/离线计费业务流程（GGSN_SGW-C_PGW-C）_89122042.md`**
- 操作步骤上下文（±2 行原文）：
  L64:
    > 
    > 1. SGW-C/PGW-C在配置完CG数据后（ **ADD CG** ），会主动向CG发送Node Alive Request消息，如果没有收到Node Alive Response响应消息，则重发，直到收到响应为止。
    > 2. SGW-C/PGW-C会根据Echo消息响应情况判断链路状态。SGW-C/PGW-C固定每隔一分钟发送Echo Request消息给CG，缺省3次（通过 **SET CDRTRANSFER** 设置）没有收到CG响应，则认为物理链路状态异常，触发告警 **ALM-81021 CG无响应** ，否则认为正常。
    > 3. SGW-C/PGW-C产生话单后，如果CG状态正常，会将话单发送到CG；如果UNC没有收到话单响应消息，则根据重发时间间隔和重发次数（通过 **SET CDRTRANSFER** 设置）发送话单，超时后会认为CG状态不正常。
    > 4. CG故障或负载过重的情况下，会给SGW-C/PGW-C发送Redirection Request消息，通知SGW-C/PGW-C将话单重定向到另外一个CG上。
  L65:
    > 1. SGW-C/PGW-C在配置完CG数据后（ **ADD CG** ），会主动向CG发送Node Alive Request消息，如果没有收到Node Alive Response响应消息，则重发，直到收到响应为止。
    > 2. SGW-C/PGW-C会根据Echo消息响应情况判断链路状态。SGW-C/PGW-C固定每隔一分钟发送Echo Request消息给CG，缺省3次（通过 **SET CDRTRANSFER** 设置）没有收到CG响应，则认为物理链路状态异常，触发告警 **ALM-81021 CG无响应** ，否则认为正常。
    > 3. SGW-C/PGW-C产生话单后，如果CG状态正常，会将话单发送到CG；如果UNC没有收到话单响应消息，则根据重发时间间隔和重发次数（通过 **SET CDRTRANSFER** 设置）发送话单，超时后会认为CG状态不正常。
    > 4. CG故障或负载过重的情况下，会给SGW-C/PGW-C发送Redirection Request消息，通知SGW-C/PGW-C将话单重定向到另外一个CG上。
    > 

**md：`WSFD-011201/配置到CG的数据（GGSN_SGW-C_PGW-C）_95923479.md`**
- 数据规划表（该命令的参数行）：
  | **SET CDRTRANSFER** | CG选择模式（CGSELECTIONMODE） | MSG_BASED_LB | 本端规划 | CG负荷分担算法 |
  | **SET CDRTRANSFER** | Echo and Data Record Transfer Request重传次数（RETRANSTIMES） | 3 | 本端规划 | GTP’消息控制 |
  | **SET CDRTRANSFER** | Data Record Transfer Request重传时间间隔（秒）（RETRANSINTERVAL） | 2 | 本端规划 | GTP’消息控制 |
  | **SET CDRTRANSFER** | Node Alive消息重传时间间隔（秒）（NARESTRANSINTVL） | 20 | 本端规划 | GTP’消息控制 |
  | **SET CDRTRANSFER** | GTP'消息最大可携带的话单字节数（GTPPMAXPAYLOAD） | 1400 | 本端规划 | 为了合理控制话单消息发送长度，避免频繁发送话单消息或话单消息分片，采用此命令设置话单发送消息的最大字节数。为了避免数据包分片，建议该值小于网络MTU。 |
- 任务示例脚本（该命令行）：
  `SET CDRTRANSFER:GTPPMAXPAYLOAD=1400,RETRANSTIMES=3,RETRANSINTERVAL=2,NARESTRANSINTVL=20,CGSELECTIONMODE=MSG_BASED_LB;`
- 操作步骤上下文（±2 行原文）：
  L90:
    >       **ADD CGGRPBINDING**
    >     f. 配置CG的负荷分担算法。
    >       **SET CDRTRANSFER**
    > 7. 配置GTP'消息控制命令。配置GTP’消息的重发次数和重发间隔、GGSN/SGW-C/PGW-C发给CG的node-alive消息超时重发时间、GTP'消息发送话单时每个数据包的最大字节数。
    >   **SET CDRTRANSFER**
  L92:
    >       **SET CDRTRANSFER**
    > 7. 配置GTP'消息控制命令。配置GTP’消息的重发次数和重发间隔、GGSN/SGW-C/PGW-C发给CG的node-alive消息超时重发时间、GTP'消息发送话单时每个数据包的最大字节数。
    >   **SET CDRTRANSFER**
    > 
    >   > **说明**
  L145:
    >   ```
    >   ```
    >   SET CDRTRANSFER:GTPPMAXPAYLOAD=1400,RETRANSTIMES=3,RETRANSINTERVAL=2,NARESTRANSINTVL=20,CGSELECTIONMODE=MSG_BASED_LB;
    >   ```

**md：`WSFD-011201/调测到CG的数据_95923534.md`**
- 操作步骤上下文（±2 行原文）：
  L68:
    > 
    >   ![](调测到CG的数据_95923534.assets/zh-cn_image_0295923519_2.png "点击放大")
    >     - 如有多个IP分片报文，可能会造成CG响应不及时。此时GGSN/SGW-C/PGW-C发送 Data Record Transfer Request 消息后会再重发（重发次数默认为3，请参考 **SET CDRTRANSFER** 命令），如果超过重发次数，则导致CG链路abnormal。在Echo消息正常交互后，CG链路normal，这样便出现CG闪断。
    >       此时请确认CG服务器性能是否满足，或者GGSN/SGW-C/PGW-C上设置的数据包字节数是否合适，请执行 [步骤 7](#ZH-CN_OPI_0295923534__stp60) 。
    >     - 如果没有IP分片报文，请执行 [步骤 8](#ZH-CN_OPI_0295923534__step1829245425110) 。
  L87:
    > 
    > 1. GGSN/SGW-C/PGW-C在配置完CG数据后，会主动向CG发送 Node Alive Request 消息，如果没有收到CG的 Node Alive Response 响应消息，则重发，直到收到响应为止。
    > 2. GGSN/SGW-C/PGW-C在配置完CG数据后，每隔一分钟会主动向CG发送Echo Request消息，如果收到CG的Echo Response消息，则CG状态正常，如果超过重发次数（参考**SET CDRTRANSFER**命令，其中RETRANSTIMES代表重发次数，默认为3）后没有收到Echo Response消息，则CG状态不正常。
    > 3. GGSN/SGW-C/PGW-C产生话单后，如果CG状态正常，会将话单发送到CG；如果GGSN/SGW-C/PGW-C没有收到话单响应消息，则根据重发时间的间隔和重发次数发送话单（参考**SET CDRTRANSFER**命令），超过重发次数后，会产生CG状态不正常。
    > 
  L88:
    > 1. GGSN/SGW-C/PGW-C在配置完CG数据后，会主动向CG发送 Node Alive Request 消息，如果没有收到CG的 Node Alive Response 响应消息，则重发，直到收到响应为止。
    > 2. GGSN/SGW-C/PGW-C在配置完CG数据后，每隔一分钟会主动向CG发送Echo Request消息，如果收到CG的Echo Response消息，则CG状态正常，如果超过重发次数（参考**SET CDRTRANSFER**命令，其中RETRANSTIMES代表重发次数，默认为3）后没有收到Echo Response消息，则CG状态不正常。
    > 3. GGSN/SGW-C/PGW-C产生话单后，如果CG状态正常，会将话单发送到CG；如果GGSN/SGW-C/PGW-C没有收到话单响应消息，则根据重发时间的间隔和重发次数发送话单（参考**SET CDRTRANSFER**命令），超过重发次数后，会产生CG状态不正常。
    > 
    > 相关概念

## ④ 自动比对
- 命令真相参数（6）：['CGSELECTIONMODE', 'GTPPMAXPAYLOAD', 'NARESTRANSINTVL', 'RETRANSINTERVAL', 'RETRANSTIMES', 'UDPCHECKSUM']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'本端规划': 5}（多值→atom 应考虑 decision_driven）
