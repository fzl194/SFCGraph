---
id: UNC@20.15.2@MMLCommand@ADD DMPE
type: MMLCommand
name: ADD DMPE（增加Diameter对端实体）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: DMPE
command_category: 配置类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
max_records: 640
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 信令传输管理
- Diameter管理
- Diameter对端实体
status: active
---

# ADD DMPE（增加Diameter对端实体）

## 功能

**适用网元：SGSN、MME**

该命令用于增加Diameter对端实体的配置。Diameter协议用于支持MME与HSS（Home Subscriber Server）传递签约及鉴权数据；或用于检查MME与EIR（Equipment Identity Register）用户设备标识是否合法，以授权用户接入EPS（Evolved Packet System）网络；或用于支持MME与DRA（Diameter Routing Agent）转接其他对端实体。

UNC 需增加的Diameter对端实体为HSS、EIR或DRA时，需要执行此命令。

## 注意事项

- 该命令执行后立即生效。
- 该表最大记录数为640。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PEERIDX | 对端实体索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定Diameter对端实体索引。<br>数据来源：本端规划<br>取值范围：0～639<br>默认值：无<br>配置原则：<br>- “对端实体索引”与“对端主机名”唯一确定一个Diameter对端实体。<br>- “对端实体索引”不能重复，建议从0开始顺序取值。 |
| PEERHTNAM | 对端主机名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定Diameter对端主机名称。<br>数据来源：全网规划<br>取值范围：1～127位字符串<br>默认值：无<br>配置原则：<br>- 不能为非法字符，只允许输入字母，数字，“.”和“-”。例如:hss.epc.mnc123.mcc123.3gppnetwork.org。<br>- 同一主机名不能在Diameter对端实体和Diameter主机路由中同时存在。如果DMHOSTRT中“对端实体选择模式”是“对端主机名”，且“对端实体主机名”在DMPE中已经配置，建议直接引用该DMPE索引。 |
| PEERNAM | 对端实体名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定对端实体名称。<br>数据来源：本端规划<br>取值范围：1～32位字符串<br>默认值：无 |
| APPCAP | 节点支持的应用 | 可选必选说明：可选参数<br>参数含义：表示指定的对端实体索引支持的应用信息。<br>数据来源：全网规划<br>取值范围：<br>- “S6a/S6d(S6a/S6d)”<br>- “S13(S13)”<br>- “SLg(SLg)”<br>- “T6a/T6ai/T6b/T6bi(T6a/T6ai/T6b/T6bi)”<br>默认值：S6a/S6d(S6a/S6d)-S13(S13)-SLg(SLg)-T6a/T6ai/T6b/T6bi(T6a/T6ai/T6b/T6bi)<br>配置原则：主要用于在Diameter连接建立时交换节点间支持的能力时使用。不要全部清空，在全部清空的场景下，链路节点能力交换流程可能会失败。<br>说明：- 对于“T6a/T6ai/T6b/T6bi(T6a/T6ai/T6b/T6bi)”，当前UNC只支持T6a，其他三个都不支持。 |
| CONGSW | 对端拥塞避免开关 | 可选必选说明：可选参数<br>参数含义：该参数用于设置是否针对此对端启动对端拥塞流控处理功能。<br>数据来源：对端协商<br>取值范围：<br>- “ON（开启）”<br>- “OFF（关闭）”<br>默认值：<br>“OFF（关闭）”<br>配置原则：只对对端DRA设备打开此开关，对直连的其他对端，不要打开此开关。<br>说明：- 拥塞流控功能是指当收到对端的消息且携带DIAMETER_TOO_BUSY(3004)错误码时，则针对此对端启动检测定时器，在定时器超时前不向此对端发送请求消息。定时器时长由[**SET DMFUNC**](../Diameter参数/设置Diameter配置(SET DMFUNC)_72225949.md)中“对端拥塞避免定时器（s）”参数设置。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/DMPE]] · Diameter对端实体（DMPE）

## 使用实例

增加Diameter对端实体配置，对端实体索引为1，对端主机名为hss.epc.mnc123.mcc123.3gppnetwork.org，对端实体名为HSS1，对端拥塞避免开关为OFF：

ADD DMPE: PEERIDX=1, PEERHTNAM="hss.epc.mnc123.mcc123.3gppnetwork.org", PEERNAM="HSS1", CONGSW=OFF;

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加Diameter对端实体(ADD-DMPE)_72225963.md`
