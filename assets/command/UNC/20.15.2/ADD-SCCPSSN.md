---
id: UNC@20.15.2@MMLCommand@ADD SCCPSSN
type: MMLCommand
name: ADD SCCPSSN（增加SCCP子系统）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: SCCPSSN
command_category: 配置类
applicable_nf:
- SGSN
- MME
- SMSF
effect_mode: 立即生效
is_dangerous: false
max_records: 2048
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 信令传输管理
- SCCP管理
- SCCP子系统
status: active
---

# ADD SCCPSSN（增加SCCP子系统）

## 功能

**适用网元：SGSN、MME、SMSF**

此命令用于增加SCCP子系统表中指定的记录，子系统SSN是SCCP使用的本地寻址信息，用于识别一个节点中的各个SCCP用户。

## 注意事项

- 此命令执行后立即生效。
- 此命令的最大记录数为2048。
- 子系统号在同一信令点下唯一。
- 本地SCCP必须配置SCMG和SGSN子系统。
- 当子系统使用主备用功能时负荷分担类型需要配置为BACKUP(主备方式)，并且配置备用子系统索引，备用子系统索引和子系统索引不能相同。当本子系统不可达时，到本子系统的业务将发往备用子系统。
- 执行此命令之前需要完成如下配置：
    - 目的信令点的配置：[**ADD SCCPDPC**](../SCCP目的信令点/增加SCCP目的信令点(ADD SCCPDPC)_26306130.md)。
    - 本局信令点的配置：[**ADD SCCPOPC**](../SCCP本局信令点/增加SCCP本局信令点(ADD SCCPOPC)_72226009.md)。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SSNX | 子系统索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定子系统对应的索引值。<br>数据来源：本端规划<br>取值范围：0~2047<br>默认值：无 |
| SSN | 子系统号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定子系统号。<br>数据来源：整网规划<br>取值范围：<br>- “NODEFINE(未定义)”<br>- “SCMG(1)”<br>- “STANDBY0(2)”<br>- “RANAP(142)”<br>- “OMAP(4)”<br>- “MAP(5)”<br>- “HLR(6)”<br>- “VLR(7)”<br>- “MSC(8)”<br>- “STANDBY1(11)”<br>- “INAP(12)”<br>- “CAP(146)”<br>- “SGSN(149)”<br>- “GGSN(150)”<br>- “BSSAP(254)”<br>- “BSSAP+(BSSAP+)”<br>- “GMLC(145)”<br>- “EIR(9)”<br>默认值：无<br>配置原则：<br>- 每个信令点上应该配置一个管理子系统(SCMG)。<br>- 在配置Gr接口时，还需要在SGSN上配置SGSN子系统、HLR目的信令点上配置HLR子系统。<br>- 配置Gs接口时，还需要在SGSN上配置BSSAP+子系统，VLR目的信令点上配置BSSAP+子系统。<br>- 配置Ge接口时，还需要在SGSN上配置CAP子系统，SCP目的信令点上配置CAP子系统。<br>- 配置Gd接口时，还需要在SGSN上配置SGSN子系统，SMC目的信令点上配置MSC子系统。<br>- 配置Iu接口的时候，还需要在SGSN和RNC目的信令点上都配置RANAP子系统。 |
| NI | 网络指示语 | 可选必选说明：必选参数<br>参数含义：该参数用于指定网络指示语。<br>数据来源：整网规划<br>取值范围：<br>- “INT(国际网)”<br>- “INTB(国际备用网)”<br>- “NAT(国内网)”<br>- “NATB(国内备用网)”<br>默认值：无<br>配置原则：配置的信令网络指示语在信令属性表中应该配置为有效。 |
| DPC | 目的信令点编码 | 可选必选说明：必选参数<br>参数含义：该参数用于指定目的信令点编码，可以采用14位信令点编码或24位信令点编码。<br>数据来源：整网规划<br>取值范围：长度不超过8的字符串<br>默认值：无<br>配置原则：<br>- 配置的信令点编码结构需要和信令属性表中对应的信令网络的网络结构保持一致。<br>- 取值为0x1~0x3FFF（对应14位编码）或0x1~0xFFFFFF（对应24位编码），不输入0x也取输入为十六进制值，即输入123等价于0x123。 |
| OPC | 本局信令点编码 | 可选必选说明：必选参数<br>参数含义：该参数用于指定本局信令点编码，可以采用14位信令点编码或24位信令点编码。<br>数据来源：整网规划<br>取值范围：长度不超过8的字符串<br>默认值：无<br>配置原则：<br>- 配置的信令点编码结构需要和信令属性表中对应的信令网络的网络结构保持一致。<br>- 取值为0x1~0x3FFF（对应14位编码）或0x1~0xFFFFFF（对应24位编码），不输入0x也取输入为十六进制值，即输入123等价于0x123。 |
| SSNNAME | 子系统名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定子系统名。<br>数据来源：本端规划<br>取值范围：长度不超过32的字符串<br>默认值：noname |
| LOADSHARETYPE | 负荷分担类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定负荷分担类型。<br>数据来源：整网规划<br>取值范围：<br>- “NOUSE(不使用)”<br>- “BACKUP(主备方式)”<br>默认值：无<br>说明：指示此子系统是否使用主备用功能。 |
| BACKUPINDEX | 备用子系统索引 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定备用子系统索引。<br>前提条件：该参数在<br>“负荷分担类型”<br>参数设置为<br>“BACKUP(主备方式)”<br>时，才需要配置。<br>数据来源：整网规划<br>取值范围：0~2047<br>默认值：无 |

## 操作的配置对象

- [SCCP子系统（SCCPSSN）](configobject/UNC/20.15.2/SCCPSSN.md)

## 使用实例

增加SCCP子系统表中指定的记录：

ADD SCCPSSN: SSNX=1, SSN=SCMG, NI=INT, DPC="0x12", OPC="0x3", SSNNAME="rnc", LOADSHARETYPE=NOUSE;

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加SCCP子系统(ADD-SCCPSSN)_26306144.md`
