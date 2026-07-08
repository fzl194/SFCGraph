---
id: UNC@20.15.2@MMLCommand@MOD RCAPLNK
type: MMLCommand
name: MOD RCAPLNK（修改注册中心链路）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: RCAPLNK
command_category: 配置类
applicable_nf:
- SMSF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 信令传输管理
- 注册中心管理
status: active
---

# MOD RCAPLNK（修改注册中心链路）

## 功能

**适用NF：SMSF**

此命令用于修改注册中心的链路配置。

## 注意事项

- 该命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LNK | 链路索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定链路的索引。在系统范围内部唯一标识一条Rcenter链路。<br>数据来源：整网规划<br>取值范围：0~1023<br>默认值：无 |
| RCAPLNKNM | RCAP链路名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定Rcenter链路的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1~63<br>默认值：NONAME<br>配置原则：无 |
| SCTPINDX | SCTP协议参数索引 | 可选必选说明：可选参数<br>参数含义：该参数用于指定所引用的SCTP协议参数索引。<br>前提条件：该SCTP协议参数已在<br>[**ADD SCTPPARA**](../SCTP管理/增加SCTP协议参数(ADD SCTPPARA)_26306150.md)<br>命令中配置。<br>数据来源：整网规划<br>取值范围：0~65534<br>默认值：无<br>说明：修改<br>“SCTP协议参数索引”<br>影响请参见<br>[**ADD SCTPPARA**](../SCTP管理/增加SCTP协议参数(ADD SCTPPARA)_26306150.md)<br>。 |
| CROSSIPFLAG | 交叉路径是否可用 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SCTP双归属的交叉路径是否可用。<br>数据来源：整网规划<br>取值范围：<br>- “NO(否)”<br>- “YES(是)”<br>默认值：无<br>配置原则：<br>- 交叉路径会增加组网的复杂度，建议配置为交叉路径不可用。<br>- SCTP双归属下配置交叉路径不可用时，“本地IPv4地址1”与“RCAP IPv4地址1”，“本地IPv4地址2”与“RCAP IPv4地址2”两条路径可用，“本地IPv4地址1”与“RCAP IPv4地址2”，“本地IPv4地址2”与“RCAP IPv4地址1”两条路径不可用。<br>- SCTP双归属下配置交叉路径可用时，“本地IPv4地址1”与“RCAP IPv4地址1”，“本地IPv4地址1”与“RCAP IPv4地址2”，“本地IPv4地址2”与“RCAP IPv4地址1”，“本地IPv4地址2”与“RCAP IPv4地址2”四条路径均可用。<br>说明：修改交叉路径是否可用将使链路的可靠性受到影响。若之前交叉路径可用，且<br>“本地IPv4地址1”<br>与<br>“RCAP IPv4地址1”<br>，<br>“本地IPv4地址2”<br>与<br>“RCAP IPv4地址2”<br>两条路径故障，正在使用交叉路径进行通信，修改为交叉路径不可用时，将导致链路中断。 |

## 操作的配置对象

- [注册中心链路（RCAPLNK）](configobject/UNC/20.15.2/RCAPLNK.md)

## 使用实例

1.将链路索引为1的交叉路径是否可用改为是：

MOD RCAPLNK: LNK=1, CROSSIPFLAG=Yes;

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改注册中心链路-(MOD-RCAPLNK)_46028502.md`
