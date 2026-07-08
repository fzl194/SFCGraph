---
id: UNC@20.15.2@MMLCommand@MOD SCCPSSN
type: MMLCommand
name: MOD SCCPSSN（修改SCCP子系统）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: SCCPSSN
command_category: 配置类
applicable_nf:
- SGSN
- MME
- SMSF
effect_mode: 立即生效
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

# MOD SCCPSSN（修改SCCP子系统）

## 功能

**适用网元：SGSN、MME、SMSF**

此命令用来修改SCCP子系统表中指定的记录。

## 注意事项

- 此命令执行后立即生效。
- 子系统号在同一信令点下必须唯一。
- 输入本局信令点编码应该在本局信令点表中存在。
- 目的信令点编码应该在目的信令点表中存在。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SSNX | 子系统索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定子系统对应的索引值。<br>数据来源：本端规划<br>取值范围：0~2047<br>默认值：无 |
| SSN | 子系统号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定子系统号。<br>数据来源：整网规划<br>取值范围：<br>- “NODEFINE(未定义)”<br>- “SCMG(1)”<br>- “STANDBY0(2)”<br>- “RANAP(142)”<br>- “OMAP(4)”<br>- “MAP(5)”<br>- “HLR(6)”<br>- “VLR(7)”<br>- “MSC(8)”<br>- “STANDBY1(11)”<br>- “INAP(12)”<br>- “CAP(146)”<br>- “SGSN(149)”<br>- “GGSN(150)”<br>- “BSSAP(254)”<br>- “BSSAP+(BSSAP+)”<br>- “GMLC(145)”<br>- “EIR(9)”<br>默认值：无<br>配置原则：每个信令点上应该配置一个管理子系统(SCMG)，一般SGSN上还需要配置SGSN(Gr)、CAP(Ge)、BSSAP+(Gs)子系统；HLR的目的信令点上还需要配置HLR子系统，SMC的目的信令点上还需要配置MSC子系统。 |
| NI | 网络指示语 | 可选必选说明：可选参数<br>参数含义：该参数用于指定网络指示语。<br>数据来源：整网规划<br>取值范围：<br>- “INT(国际网)”<br>- “INTB(国际备用网)”<br>- “NAT(国内网)”<br>- “NATB(国内备用网)”<br>默认值：无<br>配置原则：配置的信令网络指示语在信令属性表中应该配置为有效。 |
| DPC | 目的信令点编码 | 可选必选说明：可选参数<br>参数含义：该参数用于指定目的信令点编码，可以采用14位信令点编码或24位信令点编码。<br>数据来源：整网规划<br>取值范围：长度不超过8的字符串<br>默认值：无<br>配置原则：配置的信令点编码结构需要和信令属性表中对应的信令网络的网络结构保持一致。 |
| OPC | 本局信令点编码 | 可选必选说明：可选参数<br>参数含义：该参数用于指定本局信令点编码，可以采用14位信令点编码或24位信令点编码。<br>数据来源：整网规划<br>取值范围：长度不超过8的字符串<br>默认值：无<br>配置原则：配置的信令点编码结构需要和信令属性表中对应的信令网络的网络结构保持一致。 |
| SSNNAME | 子系统名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定子系统名。<br>数据来源：本端规划<br>取值范围：长度不超过32的字符串<br>默认值：无 |
| LOADSHARETYPE | 负荷分担类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定负荷分担类型。<br>数据来源：整网规划<br>取值范围：<br>- “NOUSE(不使用)”<br>- “BACKUP(主备方式)”<br>默认值：无<br>说明：指示此子系统是否使用主备用功能。 |
| BACKUPINDEX | 备用子系统索引 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定备用子系统索引。<br>前提条件：该参数在<br>“负荷分担类型”<br>参数设置为<br>“BACKUP(主备方式)”<br>时，才需要配置。<br>数据来源：整网规划<br>取值范围：0~2047<br>默认值：无 |

## 操作的配置对象

- [SCCP子系统（SCCPSSN）](configobject/UNC/20.15.2/SCCPSSN.md)

## 使用实例

以下命令修改SCCP子系统表中指定的记录，其中网络标识为国内网，子系统名为ssn9：

MOD SCCPSSN: SSNX=1, SSN=SGSN, NI=NAT, SSNNAME="ssn9";

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改SCCP子系统(MOD-SCCPSSN)_26146334.md`
