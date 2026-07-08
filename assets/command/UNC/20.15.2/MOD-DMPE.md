---
id: UNC@20.15.2@MMLCommand@MOD DMPE
type: MMLCommand
name: MOD DMPE（修改Diameter对端实体）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: DMPE
command_category: 配置类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 信令传输管理
- Diameter管理
- Diameter对端实体
status: active
---

# MOD DMPE（修改Diameter对端实体）

## 功能

**适用网元：SGSN、MME**

该命令用于修改Diameter对端实体的配置。Diameter协议用于支持MME与HSS（Home Subscriber Server）传递签约及鉴权数据。

UNC 需增加的Diameter对端实体为HSS时，需要执行此命令。

## 注意事项

- 该命令执行后立即生效。
- 执行该命令可以修改对端实体名，不能修改对端实体索引。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PEERIDX | 对端实体索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定Diameter对端实体索引。<br>数据来源：本端规划<br>取值范围：0～639<br>默认值：无<br>配置原则：<br>- “对端实体索引”与“对端主机名”唯一确定一个Diameter对端实体。<br>- “对端实体索引”不能重复，建议从0开始顺序取值。 |
| PEERNAM | 对端实体名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定待修改的对端实体名称。<br>数据来源：与对端HSS协商。<br>取值范围：1～32位字符串<br>默认值：无 |
| APPCAP | 节点支持的应用 | 可选必选说明：可选参数<br>参数含义：表示指定的对端实体索引支持的应用信息。<br>数据来源：本网规划<br>取值范围：<br>- “S6a/S6d(S6a/S6d)”<br>- “S13(S13)”<br>- “SLg(SLg)”<br>- “T6a/T6ai/T6b/T6bi(T6a/T6ai/T6b/T6bi)”<br>配置原则：主要用于在Diameter连接建立时交换节点间支持的能力时使用。不要全部清空，在全部清空的场景下，链路节点能力交换流程可能会失败。 |
| CONGSW | 对端拥塞避免开关 | 可选必选说明：可选参数<br>参数含义：该参数用于设置是否针对此对端启动对端拥塞流控处理功能。<br>数据来源：对端协商<br>取值范围：<br>- “ON（开启）”<br>- “OFF（关闭）”<br>配置原则：只对对端DRA设备打开此开关，对直连的其他对端，不要打开此开关。<br>说明：- 拥塞流控功能是指当收到对端的消息且携带DIAMETER_TOO_BUSY(3004)错误码时，则针对此对端启动检测定时器，在定时器超时前不向此对端发送请求消息。定时器时长由[**SET DMFUNC**](../Diameter参数/设置Diameter配置(SET DMFUNC)_72225949.md)中“对端拥塞避免定时器(s)”参数设置。 |

## 操作的配置对象

- [Diameter对端实体（DMPE）](configobject/UNC/20.15.2/DMPE.md)

## 使用实例

修改Diameter对端实体配置，把 “对端实体索引” 为2的 “对端实体名” 改为“HSS1”， “节点支持的应用” 增加 “S6a/S6d-0” ， “对端拥塞避免开关” 改为 “OFF（关闭）” ：

MOD DMPE: PEERIDX=2, PEERNAM="HSS1", APPCAP=S6a/S6d-0, CONGSW=OFF;

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改Diameter对端实体(MOD-DMPE)_72345885.md`
