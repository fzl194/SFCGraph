---
id: UNC@20.15.2@MMLCommand@ADD HNOINFO
type: MMLCommand
name: ADD HNOINFO（增加归属网络信息）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: HNOINFO
command_category: 配置类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
max_records: 192
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 网络管理
- 归属网络运营商管理
- 归属网络信息管理
status: active
---

# ADD HNOINFO（增加归属网络信息）

## 功能

**适用网元：SGSN、MME**

该命令用于增加归属网络信息。

## 注意事项

- 此命令最大记录数为192。
- 此命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NOID | 运营商标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定运营商标识。<br>数据来源：整网规划<br>取值范围：0～64，128～254<br>默认值：无<br>配置原则：<br>- 若该参数需要配置为0或128～254之间的值时，请先在[**ADD MNO**](../MNO管理/MNO配置表/增加MNO配置信息(ADD MNO)_72345671.md)中配置取值相同的“MNOID”参数。<br>- 若该参数需要配置为1～64之间的值时，须先在[**ADD MVNO**](../MVNO管理/MVNO配置表/增加MVNO配置信息(ADD MVNO)_72225747.md)中配置取值相同的“MVNOID”参数。 |
| SGSNN | 本局SGSN号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定服务GPRS支持节点（SGSN）号码，是SGSN的E.164地址。<br>前提条件：该参数已增加，参见<br>[**ADD SCCPOPC**](../../../信令传输管理/SCCP管理/SCCP本局信令点/增加SCCP本局信令点(ADD SCCPOPC)_72226009.md)<br>。<br>数据来源：整网规划<br>取值范围：1～16位十进制数<br>默认值：无<br>说明：系统获取本端SGSN号的策略：<br>- 如果IMSICHAR表配置了，从IMSICHAR表中获取。<br>- 如果IMSICHAR中没有配置，则从HNOINFO表中获取。<br>- 如果IMSICHAR和HNOINFO都没有配置，则从SCCPOPC表中获取。 |
| LOINDEX | 本地实体索引 | 可选必选说明：可选参数<br>参数含义：该参数用于指定Diameter链路集对应的本地实体的索引。<br>前提条件：<br>在“MML命令行-UNC”窗口上执行命令<br>[**ADD DMLE**](../../../信令传输管理/Diameter管理/Diameter本地实体/增加Diameter本端实体(ADD DMLE)_72345881.md)<br>设置此参数。<br>数据来源：本端规划<br>取值范围：0～31<br>默认值：无<br>说明：系统获取Diameter链路集对应的本地实体索引的策略：<br>- 如果IMSICHAR表配置了，从IMSICHAR表中获取。<br>- 如果IMSICHAR中没有配置，则从HNOINFO表中获取。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@HNOINFO]] · 归属网络信息（HNOINFO）

## 使用实例

增加一个HNOINFO， “运营商标识” 为 “128” ， “本局SGSN号” 为 “123” ：

ADD HNOINFO: NOID=128, SGSNN="123";

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-HNOINFO.md`
