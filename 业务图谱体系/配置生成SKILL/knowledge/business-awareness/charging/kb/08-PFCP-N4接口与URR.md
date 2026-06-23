## 第八章：PFCP/N4接口与URR

### K122: URR定义与关键参数 [原理]
> 来源: K47

URR（Usage Reporting Rule / 使用量上报规则）：SMF通过N4(PFCP)向UPF下发的规则，指示UPF测量和报告网络资源使用情况。

- 测量维度：流量(Volume)、时长(Duration)、事件(Event)
- 上报触发：阈值到达、周期性、应请求上报

URR关键参数：URR ID, Measurement Method, Reporting Triggers, Volume Quota, Time Quota, Volume Threshold, Time Threshold, Linked URR ID, Measurement Information。

---

### K123: URR生命周期——Create/Update/Remove [协议]
> 来源: K209, K210, K211

**Create URR**必选信元：URR ID、Measurement Method、Reporting Triggers。

条件必选信元（按需出现）：

| 信元 | 触发条件 |
|------|----------|
| Volume Threshold | 使用流量测量且需要流量阈值上报 |
| Volume Quota | 使用流量测量且需要提供流量配额 |
| Event Threshold | 使用事件测量且需要事件阈值上报 |
| Event Quota | 使用事件测量且需要事件配额 |
| Time Threshold | 使用时间测量且需要时间阈值上报 |
| Time Quota | 使用时间测量且需要时间配额 |
| Quota Holding Time | 时间/流量/事件测量中，不活动期间不传包时需要 |
| Inactivity Detection Time | 使用时间测量，不活动时需挂起时间测量 |
| Linked URR ID | 需要链接使用报告 |
| Measurement Information | Inactive/Reduced/ISTM标志位为1时 |
| Aggregated URRs | URR支持信用池 |
| FAR ID for Quota Action | 有配额且UPF支持配额动作特性 |

可选信元：Monitoring Time及其Subsequent系列（Subsequent Volume/Time/Event Threshold/Quota）。

**Update URR**与Create URR的差异：
- URR ID仍为必选（标识要修改的URR）
- 其余信元为条件必选（"如果需要修改xxx，该信元应出现"）
- 新增FAR ID for Quota Action：URR中新增配额且UPF支持配额动作时可能出现
- Aggregated URRs在Update时提供完整列表（替换而非增量）

**Remove URR**仅包含一个必选信元：URR ID。用于去激活或删除PFCP会话中的URR，触发PFCP Session Modification Response上报终止用量报告（TERMR触发）。

---

### K124: URR ID信元与编码规则 [协议]
> 来源: K212

- 功能：在PFCP会话配置的所有URR中唯一标识一个URR
- 第5字节bit8含义：
  - 0：Rule由控制面功能（SMF）动态分配
  - 1：Rule在用户面功能（UPF）中预定义

---

### K125: Usage Report Trigger完整编码（3字节位图） [协议]
> 来源: K213

**第5字节（bit1-8）：**

| bit | 名称 | 含义 |
|-----|------|------|
| 1 | PERIO | 定期上报 |
| 2 | VOLTH | 流量阈值到达 |
| 3 | TIMTH | 时间阈值到达 |
| 4 | QUHTI | 配额保持时间超时（无报文） |
| 5 | START | 流量开始 |
| 6 | STOPT | 流量结束 |
| 7 | DROTH | 下行丢弃流量达阈值 |
| 8 | IMMER | 立即上报 |

**第6字节（bit1-8）：**

| bit | 名称 | 含义 |
|-----|------|------|
| 1 | VOLQU | 流量配额耗尽 |
| 2 | TIMQU | 时间配额耗尽 |
| 3 | LIUSA | 关联使用报告（Linked URR触发） |
| 4 | TERMR | 终止报告（会话删除/URR删除） |
| 5 | MONIT | 监控时间到达 |
| 6 | ENVCL | 信封关闭 |
| 7 | MACAR | MAC地址上报 |
| 8 | EVETH | 事件阈值到达 |

**第7字节：** bit1: EVEQU（事件配额耗尽），bit2-8备用。

至少一个bit为1，可多个bit同时为1。

---

### K126: Measurement Method信元 [协议]
> 来源: K214

- 功能：指示测量网络资源使用情况的方法
- 第5字节编码：
  - bit1 DURAT：时长测量
  - bit2 VOLUM：流量测量
  - bit3 EVENT：事件测量
  - bit4-8：备用
- 至少一个bit为1，可多个bit同时为1（如DURATION_VOLUME对应DURAT+VOLUM）

---

### K127: Volume Measurement信元 [协议]
> 来源: K215

- 功能：指示测量的话务量
- 第5字节编码：
  - bit1 TOVOL：Total Volume字段存在
  - bit2 ULVOL：Uplink Volume字段存在
  - bit3 DLVOL：Downlink Volume字段存在
- Total/Uplink/Downlink Volume编码为Unsigned64，单位字节

---

### K128: Duration Measurement信元 [协议]
> 来源: K216

- 功能：指示已用时间
- 单位：秒

---

### K129: Volume Quota与Time Quota信元 [协议]
> 来源: K217, K218

**Volume Quota：**
- 功能：指示UPF需要监控的流量配额
- 编码同Volume Measurement（TOVOL/ULVOL/DLVOL标志位+对应值）
- Unsigned64类型，单位字节

**Time Quota：**
- 功能：指示UPF需要监控的时间配额
- 单位：秒

---

### K130: Reporting Triggers信元（N4接口） [协议]
> 来源: K219

N4接口的Reporting Triggers编码与Usage Report Trigger基本一致但略有差异：

- 第5字节：PERIO/VOLTH/TIMTH/QUHTI/START/STOPT/DROTH/LIUSA
- 第6字节：VOLQU/TIMQU/ENVCL/MACAR/EVETH/EVEQU

与Usage Report Trigger的差异：第5字节bit8是LIUSA（非IMMER），第6字节bit3是ENVCL（非TERMR），bit4是MACAR（非MONIT），无第7字节。

---

### K131: Quota Holding Time信元（N4接口） [协议]
> 来源: K49, K205, K220

- 功能：指示配额保持时间
- 单位：秒
- 含义：在给定不活动期间没有收到数据包时，不再允许数据包传输，触发QUHTI上报
- 特殊值：QHT=0禁用该机制
- 适用于流量和时长计费

**在线计费**：QHT到期=SMF不请求配额，配额仅在下一次业务活动时请求。
**离线计费**：QHT到期=触发关闭当前业务容器。
**N40接口**：CHF在Create Response中下发quotaHoldingTime，SMF映射到N4的Quota Holding Time下发给UPF。

---

### K132: Aggregated URRs信元（信用池机制） [协议]
> 来源: K221

- 功能：支持URR信用池（多个URR共享同一配额）
- 子信元：
  - Aggregated URR ID：共享信用池的聚合URR ID（必选）
  - Multiplier：乘法器，应用于测量抽象业务单元从信用池中消耗的流量（必选）
- 使用场景：多个业务共享一个总配额池，按不同权重消耗

---

### K133: Linked URR ID信元 [协议]
> 来源: K222

- 功能：指示Linked URR的ID
- 机制：上报某个URR时，也会上报其关联的URR。例如A link B，当B上报时也会上报A
- 可存在多个相同类型的信元表示与该URR相关的多个链接URR

---

### K134: Subsequent Volume Quota信元 [协议]
> 来源: K223

- 功能：指示UPF在监控时间（Monitoring Time）之后仍需要监控的流量配额
- 编码同Volume Quota（TOVOL/ULVOL/DLVOL标志位+对应值）
- 前提：存在Monitoring Time信元且使用基于流量的测量

---

### K135: Usage Report信元（PFCP Session Report） [协议]
> 来源: K198

UPF上报的Usage Report包含：

| 信元 | 说明 |
|------|------|
| URR ID | 标识上报的URR |
| UR-SEQN | 唯一标识该URR的Usage Report |
| Start Time / End Time | 起止时间 |
| Volume Measurement | 总流量/上行/下行 |
| Duration Measurement | 时长使用情况 |
| Time of First Packet / Last Packet | 首尾包时间 |

Duration Measurement的ISTM标志位说明：
- ISTM=0或不携带：从UPF首次收到业务数据包开始，到业务终止结束
- ISTM=1：从UPF首次收到授权配额成功开始，到用户去激活或配额管理实例终止

配额更新超时保护：定时器 = T3RESPONSE * N3REQUEST + 4秒（`SET UPPFCPPATH`配置），超时未收到配额更新则UPF阻塞业务。

---

