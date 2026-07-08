---
id: UNC@20.15.2@MMLCommand@MOD LCSAPLNK
type: MMLCommand
name: MOD LCSAPLNK（修改LCSAP链路配置）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: LCSAPLNK
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- LCS
- LCSAP链路配置
status: active
---

# MOD LCSAPLNK（修改LCSAP链路配置）

## 功能

**适用网元：MME**

此命令用于修改LCSAP链路配置。

## 注意事项

- 此命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LINKIDX | 链路索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定LCSAP链路索引。该参数用来在系统范围内部唯一标识一条LCSAP链路。<br>数据来源：整网规划<br>取值范围：0～23<br>默认值：无 |
| PRIORITY | 优先级 | 可选必选说明：可选参数<br>参数含义：该参数用于指定链路优先级。<br>数据来源：整网规划<br>取值范围：0～3<br>默认值：无<br>配置原则：<br>- 在链路选择中选择高优先级链路。<br>- 0优先级最高，3优先级最低。 |
| SCTPINDX | SCTP协议参数索引 | 可选必选说明：可选参数<br>参数含义：该参数用于指定LCSAP链路所引用的SCTP协议参数索引。<br>前提条件：在<br>UNC<br>MML窗口上执行命令<br>[**ADD SCTPPARA**](../../../信令传输管理/SCTP管理/增加SCTP协议参数(ADD SCTPPARA)_26306150.md)<br>设置此参数。<br>数据来源：整网规划<br>取值范围：0～65534<br>默认值：无 |
| CROSSIPFLAG | 是否交叉路径可用 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SCTP双归属的交叉路径是否可用。<br>数据来源：整网规划<br>取值范围：<br>“NO（否）”<br>、<br>“YES（是）”<br>默认值：无<br>配置原则：<br>- 交叉路径会增加组网的复杂度，建议配置为交叉路径不可用。<br>- SCTP双归属下配置交叉路径不可用时，“本端IPv4(IPv6)地址1”与“对端IPv4(IPv6)地址1”，“本端IPv4(IPv6)地址2”与“对端IPv4(IPv6)地址2”两条路径可用，“本端IPv4(IPv6)地址1”与“对端IPv4(IPv6)地址2”，“本端IPv4(IPv6)地址2”与“对端IPv4(IPv6)地址1”两条路径不可用。<br>- SCTP双归属下配置交叉路径可用时，“本端IPv4(IPv6)地址1”与“对端IPv4(IPv6)地址1”，“本端IPv4(IPv6)地址1”与“对端IPv4(IPv6)地址2”，“本端IPv4(IPv6)地址2”与“对端IPv4(IPv6)地址1”，“本端IPv4(IPv6)地址2”与“对端IPv4(IPv6)地址2”四条路径均可用。 |
| LINKNAM | 链路名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定链路名称，标识LCSAP链路。<br>数据来源：整网规划<br>取值范围：1～20位字符串<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@LCSAPLNK]] · LCSAP链路配置（LCSAPLNK）

## 使用实例

修改一条 “链路索引” 为 “1” 的LCSAP链路配置记录，其中 “优先级” 为 “3” ：

MOD LCSAPLNK: LINKIDX=1, PRIORITY=3;

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-LCSAPLNK.md`
