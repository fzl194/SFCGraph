---
id: UNC@20.15.2@MMLCommand@MOD SGSLNK
type: MMLCommand
name: MOD SGSLNK（修改SGs链路）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: SGSLNK
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 电路域联合业务
- SGSAP
- SGsAP链路管理
status: active
---

# MOD SGSLNK（修改SGs链路）

## 功能

**适用网元：MME**

此命令用于修改SGs链路配置对应的相关参数。

当需要修改SGs链路的 “SGs链路名称” 、 “SCTP协议参数索引” 和 “交叉路径是否可用” 的全部或者部分信息时，用此命令进行修改。

## 注意事项

此命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LNK | 链路索引 | 可选必选说明：必选参数<br>参数含义：待修改链路的索引。<br>数据来源：整网规划<br>取值范围：0~511<br>默认值：无 |
| SGSLNKNM | SGs链路名称 | 可选必选说明：可选参数<br>参数含义：待修改的SGs链路的名称。<br>数据来源：本端规划<br>取值范围：0~32位字符串<br>默认值：无<br>配置原则：建议取有实际意义的名称，以方便识别。例如<br>“VLRconf”<br>。 |
| SCTPINDX | SCTP协议参数索引 | 可选必选说明：可选参数<br>参数含义：待修改所引用的SCTP协议参数索引。<br>前提条件：该参数已经增加，参见<br>[**ADD SCTPPARA**](../../../信令传输管理/SCTP管理/增加SCTP协议参数(ADD SCTPPARA)_26306150.md)<br>。<br>数据来源：整网规划<br>取值范围：0~65534<br>默认值：无<br>说明：修改<br>“SCTP协议参数索引”<br>影响请参见<br>[**ADD SCTPPARA**](../../../信令传输管理/SCTP管理/增加SCTP协议参数(ADD SCTPPARA)_26306150.md)<br>。 |
| CROSSIPFLAG | 交叉路径是否可用 | 可选必选说明：可选参数<br>参数含义：待修改SCTP双归属的交叉路径是否可用。<br>数据来源：整网规划<br>取值范围：<br>- “NO(否)”<br>- “YES(是)”<br>默认值：无<br>配置原则：<br>- 交叉路径会增加组网的复杂度，建议配置为交叉路径不可用。<br>- SCTP双归属下配置交叉路径不可用时，“本地IPv4地址1”与“VLRIPv4地址1”，“本地IPv4地址2”与“VLRIPv4地址2”两条路径可用，“本地IPv4地址1”与“VLRIPv4地址2”，“本地IPv4地址2”与“VLRIPv4地址1”两条路径不可用。<br>- SCTP双归属下配置交叉路径可用时，“本地IPv4地址1”与“VLRIPv4地址1”，“本地IPv4地址1”与“VLRIPv4地址2”，“本地IPv4地址2”与“VLRIPv4地址1”，“本地IPv4地址2”与“VLRIPv4地址2”四条路径均可用。<br>说明：修改交叉路径是否可用将使链路的可靠性受到影响。若之前交叉路径可用，且<br>“本地IPv4地址1”<br>与<br>“VLRIPv4地址1”<br>，<br>“本地IPv4地址2”<br>与<br>“VLRIPv4地址2”<br>两条路径故障，正在使用交叉路径进行通信，修改为交叉路径不可用时，将导致链路中断。 |

## 操作的配置对象

- [SGs链路（SGSLNK）](configobject/UNC/20.15.2/SGSLNK.md)

## 使用实例

将链路索引为1的SGs链路名修改为test，交叉路径是否可用改为是：

MOD SGSLNK: LNK=1, SGSLNKNM="test", CROSSIPFLAG=YES;

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改SGs链路(MOD-SGSLNK)_72225115.md`
