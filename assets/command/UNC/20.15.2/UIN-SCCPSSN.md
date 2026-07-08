---
id: UNC@20.15.2@MMLCommand@UIN SCCPSSN
type: MMLCommand
name: UIN SCCPSSN（解禁SCCP子系统）
nf: UNC
version: 20.15.2
verb: UIN
object_keyword: SCCPSSN
command_category: 调测类
applicable_nf:
- SGSN
- MME
- SMSF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 信令传输管理
- SCCP管理
- SCCP子系统
status: active
---

# UIN SCCPSSN（解禁SCCP子系统）

## 功能

**适用网元：SGSN、MME、SMSF**

此命令用于解禁SCCP子系统。

## 注意事项

- 系统会自行选取可用的信令进程，因此，执行该操作的时候要确保系统中有可用的信令进程。否则，操作将不能正常执行。
- 只有处于禁止状态的SCCP子系统才能执行解禁操作。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NI | 网络指示语 | 可选必选说明：必选参数<br>参数含义：该参数用于指定网络指示语。<br>取值范围：<br>- “INT(国际网)”<br>- “INTB(国际备用网)”<br>- “NAT(国内网)”<br>- “NATB(国内备用网)”<br>默认值：无<br>说明：配置的信令网络指示语在信令属性表中应该配置为有效。 |
| DPC | 目的信令点编码 | 可选必选说明：必选参数<br>参数含义：该参数用于指定目的信令点编码，可以采用14位信令点编码或24位信令点编码。<br>取值范围：长度不超过8的字符串<br>默认值：无<br>配置原则：取值为0x1~0x3FFF（对应14位编码），或0x1~0xFFFFFF（对应24位编码），不输入0x也取输入为十六进制值，即输入123等价于0x123。<br>说明：配置的信令点编码结构需要和信令属性表中对应的信令网络的网络结构保持一致。 |
| SSN | 子系统号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定子系统号。<br>取值范围：<br>- “NODEFINE(未定义)”<br>- “SCMG(1)”<br>- “STANDBY0(2)”<br>- “RANAP(142)”<br>- “OMAP(4)”<br>- “MAP(5)”<br>- “HLR(6)”<br>- “VLR(7)”<br>- “MSC(8)”<br>- “STANDBY1(11)”<br>- “INAP(12)”<br>- “CAP(146)”<br>- “SGSN(149)”<br>- “GGSN(150)”<br>- “BSSAP(254)”<br>- “BSSAP(BSSAP+)”<br>- “GMLC(145)”<br>- “EIR(9)”<br>默认值：无<br>说明：每个信令点上应该配置一个管理子系统(SCMG)，一般SGSN上还需要配置SGSN(Gr)、CAP(Ge)、BSSAP+(Gs)子系统；HLR的目的信令点上还需要配置HLR子系统，SMC的目的信令点上还需要配置MSC子系统。 |
| OPC | 本局信令点编码 | 可选必选说明：必选参数<br>参数含义：该参数用于指定本局信令点编码，可以采用14位信令点编码或24位信令点编码。<br>取值范围：长度不超过8的字符串<br>默认值：无<br>配置原则：取值为0x1~0x3FFF（对应14位编码），或0x1~0xFFFFFF（对应24位编码），不输入0x也取输入为十六进制值，即输入123等价于0x123。<br>说明：配置的信令点编码结构需要和信令属性表中对应的信令网络的网络结构保持一致。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SCCPSSN]] · SCCP子系统（SCCPSSN）

## 使用实例

解禁SCCP子系统：

UIN SCCPSSN: NI=NAT, DPC="0x290270", SSN=RANAP, OPC="0x290333";

## 证据

- 原始手册：`evidence/UNC/20.15.2/UIN-SCCPSSN.md`
