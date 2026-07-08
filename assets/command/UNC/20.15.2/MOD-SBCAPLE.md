---
id: UNC@20.15.2@MMLCommand@MOD SBCAPLE
type: MMLCommand
name: MOD SBCAPLE（修改SBCAP本地实体）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: SBCAPLE
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- SBc接口管理
- SBCAP本地实体
status: active
---

# MOD SBCAPLE（修改SBCAP本地实体）

## 功能

**适用网元：MME**

该命令用于修改SBc链路本地实体配置。

## 注意事项

- 该命令执行后立即生效。
- 执行该命令可修改SBc链路的“SCTP协议参数索引”、“交叉路径是否可用”和“链路本地实体”的全部或部分信息，不能修改SBc的“链路本地实体号”。

## 权限

manage-ug;system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LLEINDEX | 本端实体号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定需要修改的SBc链路本地实体号。<br>数据来源：本端规划<br>取值范围：0~127<br>默认值：无<br>说明：可以通过<br>[**LST SBCAPLE**](查询SBCAP本地实体(LST SBCAPLE)_26146378.md)<br>命令查看已有配置，确认所要修改的SBc链路的索引。 |
| SCTPINDX | SCTP协议参数索引 | 可选必选说明：可选参数<br>参数含义：该参数为SCTPPARA表的索引号，用于指定SBc链路使用的SCTP协议栈参数索引。<br>前提条件：SCTP协议参数索引在ADD SCTPPATA里面已经设置过。<br>数据来源：整网规划<br>取值范围：0~65534<br>默认值：无<br>说明：修改SCTP协议参数索引影响参见<br>[**ADD SCTPPARA**](../../信令传输管理/SCTP管理/增加SCTP协议参数(ADD SCTPPARA)_26306150.md)<br>。 |
| CROSSIPFLAG | 交叉路径是否可用 | 可选必选说明：可选参数<br>参数含义：该参数用于表明交叉路径是否可用。交叉路径是指本端第一个IP地址到对端第二个IP地址和本端第二个IP地址到对端第一个IP地址所组成的路径。<br>数据来源：整网规划<br>取值范围：<br>- “NO(否)”<br>- “YES(是)”<br>默认值：无<br>配置原则：<br>- 交叉路径会增加组网的复杂度，建议配置为交叉路径不可用。<br>- SCTP双归属下配置交叉路径不可用时，“本端IPv4(IPv6)地址1”与“对端IPv4(IPv6)地址1”，“本端IPv4(IPv6)地址2”与“对端IPv4(IPv6)地址2”两条路径可用，“本端IPv4(IPv6)地址1”与“对端IPv4(IPv6)地址2”，“本端IPv4(IPv6)地址2”与“对端IPv4(IPv6)地址1”两条路径不可用。<br>- SCTP双归属下配置交叉路径可用时，“本端IPv4(IPv6)地址1”与“对端IPv4(IPv6)地址1”，“本端IPv4(IPv6)地址1”与“对端IPv4(IPv6)地址2”，“本端IPv4(IPv6)地址2”与“对端IPv4(IPv6)地址1”，“本端IPv4(IPv6)地址2”与“对端IPv4(IPv6)地址2”四条路径均可用。<br>说明：修改交叉路径是否可用将使链路的可靠性受到影响。若之前交叉路径可用，且<br>“本端IPv4(IPv6)地址1”<br>与<br>“对端IPv4(IPv6)地址1”<br>，<br>“本端IPv4(IPv6)地址2”<br>与<br>“对端IPv4(IPv6)地址2”<br>两条路径故障，正在使用交叉路径进行通信，修改为交叉路径不可用时，将导致链路中断。 |
| LLENAM | 本端实体名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SBc链路本地实体名称。<br>数据来源：整网规划<br>取值范围：0~32位字符串<br>默认值：无<br>配置原则：建议取有实际意义的名称，以方便识别。例如<br>“To-CBC”<br>。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SBCAPLE]] · SBCAP本地实体（SBCAPLE）

## 使用实例

将本地实体索引为0的SBc链路的SCTP协议参数索引改为1，交叉路径是否可用改为YES：

MOD SBCAPLE: LLEINDEX=0,SCTPINDX=1, CROSSIPFLAG=YES;

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-SBCAPLE.md`
