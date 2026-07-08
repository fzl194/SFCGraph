---
id: UNC@20.15.2@MMLCommand@MOD DMLNK
type: MMLCommand
name: MOD DMLNK（修改Diameter链路配置）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: DMLNK
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
- Diameter链路
status: active
---

# MOD DMLNK（修改Diameter链路配置）

## 功能

**适用网元：SGSN、MME**

该命令用于修改一条Diameter链路配置。

## 注意事项

- 该命令执行后立即生效。
- 执行该命令可修改Diameter链路的“链路集索引”、“SCTP协议参数索引”、“链路名称”和“交叉路径是否可用”的全部或部分信息，不能修改Diameter的“链路索引”。
- 如果Diameter链路的C/S模式为客户端，修改“链路集索引”或“SCTP协议参数索引”后该链路会重建链；如果Diameter链路的C/S模式为服务器端，修改“链路集索引”或“SCTP协议参数索引”后该链路会断链，对端重新建链后恢复。
- 一个Diameter链路集下最多允许配置32条Diameter链路。
- Diameter链路不支持ADLER32校验和算法。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LINKIDX | 链路索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定Diameter链路的索引。<br>数据来源：整网规划<br>取值范围：0~1279<br>默认值：无<br>说明：可以通过<br>[**LST DMLNK**](查询Diameter链路配置(LST DMLNK)_26146276.md)<br>命令查看已有配置，确认所要修改的Diameter链路的索引。 |
| LINKSIDX | Diameter链路集索引 | 可选必选说明：可选参数<br>参数含义：该参数用于指定Diameter链路所属的链路集索引。<br>前提条件：<br>在“MML命令行-UNC”窗口上执行命令<br>[**ADD DMLKS**](../Diameter链路集/增加Diameter链路集配置(ADD DMLKS)_72225957.md)<br>设置此参数。<br>数据来源：整网规划<br>取值范围：0~639<br>默认值：无<br>说明：如修改后，原Diameter链路集上没有配置的Diameter链路，将导致原Diameter链路集上业务中断。 |
| SCTPINDX | SCTP协议参数索引 | 可选必选说明：可选参数<br>参数含义：该参数用于指定Diameter链路所引用的SCTP协议参数索引。<br>前提条件：<br>在“MML命令行-UNC”窗口上执行命令<br>[**ADD SCTPPARA**](../../SCTP管理/增加SCTP协议参数(ADD SCTPPARA)_26306150.md)<br>设置此参数。<br>数据来源：整网规划<br>取值范围：0~65534<br>默认值：无<br>说明：修改SCTP协议参数索引影响参见<br>[**ADD SCTPPARA**](../../SCTP管理/增加SCTP协议参数(ADD SCTPPARA)_26306150.md)<br>。 |
| LINKNAM | 链路名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定链路名称，标识Diameter链路。<br>数据来源：整网规划<br>取值范围：0~32位字符串<br>默认值：无<br>配置原则：建议取有实际意义的名称，以方便识别。例如<br>“To-HSS0”<br>。 |
| CROSSIPFLAG | 交叉路径是否可用 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SCTP双归属的交叉路径是否可用。<br>数据来源：整网规划<br>取值范围：<br>- “NO(否)”<br>- “YES(是)”<br>默认值：无<br>配置原则：<br>- 交叉路径会增加组网的复杂度，建议配置为交叉路径不可用。<br>- SCTP双归属下配置交叉路径不可用时，“本端IPv4(IPv6)地址1”与“对端IPv4(IPv6)地址1”，“本端IPv4(IPv6)地址2”与“对端IPv4(IPv6)地址2”两条路径可用，“本端IPv4(IPv6)地址1”与“对端IPv4(IPv6)地址2”，“本端IPv4(IPv6)地址2”与“对端IPv4(IPv6)地址1”两条路径不可用。<br>- SCTP双归属下配置交叉路径可用时，“本端IPv4(IPv6)地址1”与“对端IPv4(IPv6)地址1”，“本端IPv4(IPv6)地址1”与“对端IPv4(IPv6)地址2”，“本端IPv4(IPv6)地址2”与“对端IPv4(IPv6)地址1”，“本端IPv4(IPv6)地址2”与“对端IPv4(IPv6)地址2”四条路径均可用。<br>说明：修改交叉路径是否可用将使链路的可靠性受到影响。若之前交叉路径可用，且<br>“本端IPv4(IPv6)地址1”<br>与<br>“对端IPv4(IPv6)地址1”<br>，<br>“本端IPv4(IPv6)地址2”<br>与<br>“对端IPv4(IPv6)地址2”<br>两条路径故障，正在使用交叉路径进行通信，修改为交叉路径不可用时，将导致链路中断。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@DMLNK]] · Diameter链路配置（DMLNK）

## 使用实例

将链路索引为0的Diameter链路所在链路集索引改为1，SCTP协议参数索引改为1，交叉路径是否可用改为YES：

MOD DMLNK: LINKIDX=0, LINKSIDX=1, SCTPINDX=1, CROSSIPFLAG=YES;

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-DMLNK.md`
