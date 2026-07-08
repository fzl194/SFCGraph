---
id: UNC@20.15.2@MMLCommand@ADD GBIPRMTENDPT
type: MMLCommand
name: ADD GBIPRMTENDPT（增加对端端点配置）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: GBIPRMTENDPT
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
max_records: 8192
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- Gb接口管理
- Gb over IP管理
- 对端IP端点配置
status: active
---

# ADD GBIPRMTENDPT（增加对端端点配置）

## 功能

**适用网元：SGSN**

该命令用于增加一个Gb接口对端端点。对端端点权重表用来配置对端IP端点的数据权重和信令权重，在IP网络NSVC链路负荷分担时根据数据权重或者信令权重来选择对端IP端点。

## 注意事项

- 本命令执行立即生效。
- 本表可以动态设定。
- 本表最大记录数为8192。
- 配置对端端点时，NSE必须已经配置。
- SGSN仅支持一个NSE下配置512个IPv4类型的对端端点。
- SGSN仅支持一个NSE下配置512个IPv6类型的对端端点。
- 配置对端端点的时候需要考虑当前IPNsvc链路的数目。SGSN支持每个进程上1024条IPNsvc链路，整系统16384条IPNsvc链路。
- 目前暂不支持IPv6。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPT | IP地址类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定IP地址类型。<br>数据来源：整网规划<br>取值范围：<br>- “IPV4(IPv4)”<br>- “IPV6(IPv6)”<br>默认值：无 |
| RIPV4 | 对端IPv4地址 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定对端PCU使用的IPv4地址。<br>前提条件：该参数在<br>“IP地址类型”<br>设置为<br>“IPV4(IPv4)”<br>时才生效。<br>数据来源：整网规划<br>取值范围：0.0.0.0~255.255.255.255<br>默认值：无<br>配置原则：IPv4地址不能为0.0.0.0，255.255.255.255 |
| RIPV6 | 对端IPv6地址 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定对端PCU使用的IPv6地址。<br>前提条件：该参数在<br>“IP地址类型”<br>设置为<br>“IPV6(IPv6)”<br>时才生效。<br>数据来源：整网规划<br>取值范围： ::~FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无 |
| RUP | 对端UDP端口号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定对端PCU使用的UDP端口号。<br>数据来源：整网规划<br>取值范围：0~65535<br>默认值：无 |
| NSEI | NSE标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定端点所在的网络服务实体标识。<br>数据来源：整网规划<br>取值范围：0~65535<br>默认值：无 |
| DW | 数据权重 | 可选必选说明：可选参数<br>参数含义：该参数用于指定该对端端点的数据权重。数据权重越大，NS发送数据消息时根据IP网络NSVC链路负荷分担功能选择该对端IP端点的概率就越大。<br>数据来源：整网规划<br>取值范围：0~255<br>默认值：255 |
| SW | 信令权重 | 可选必选说明：可选参数<br>参数含义：该参数用于指定该对端端点的信令权重。信令权重越大，NS发送信令消息时根据IP网络NSVC链路负荷分担功能选择该对端IP端点的概率就越大。<br>数据来源：整网规划<br>取值范围：0~255<br>默认值：255 |
| DESC | 描述 | 可选必选说明：可选参数<br>参数含义：该参数用于指定对端端点名称。<br>数据来源：整网规划<br>取值范围：长度不超过32的字符串<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@GBIPRMTENDPT]] · 对端端点配置（GBIPRMTENDPT）

## 使用实例

增加一个对端端点记录，对端IPv4地址为"172.22.44.66"，UDP端口为4000，对应BSC1：

ADD GBIPRMTENDPT: IPT=IPV4, RIPV4="172.22.44.66", RUP=4000, NSEI=200, DW=50, SW=100, DESC="FOR BSC1";

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-GBIPRMTENDPT.md`
