---
id: UNC@20.15.2@MMLCommand@MOD SCCPDPC
type: MMLCommand
name: MOD SCCPDPC（修改SCCP目的信令点）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: SCCPDPC
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
- SCCP目的信令点
status: active
---

# MOD SCCPDPC（修改SCCP目的信令点）

## 功能

**适用网元：SGSN、MME、SMSF**

此命令用来修改SCCP目的信令点表中指定的记录。

## 注意事项

- 此命令执行后立即生效。
- 要修改的目的信令点记录已经存在。
- 备用/负荷分担信令点索引和目的信令点索引不能相同，且应该对应相同的本局信令点。
- 目的信令点编码在同一网络中是唯一的。
- 在DSP表中，目的信令点编码、本局信令点索引在表中唯一确定一条记录。
- OPC与DPC不能等于0。
- 当该SCCP目的信令点在多点负荷分担表中作为主SCCP DPC存在时，不允许将负荷分担类型从MULTIDPCLOADSHARE修改为其他的类型。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DPX | 目的信令点索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定SCCP目的信令点索引。<br>前提条件：此目的信令点索引记录必须在SCCP目的信令点表中存在，通过命令<br>[**LST SCCPDPC**](查询SCCP目的信令点(LST SCCPDPC)_72225999.md)<br>查询。<br>数据来源：本端规划<br>取值范围：0~1279<br>默认值：无 |
| LDP | 负荷分担类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定负荷分担类型，指示此目的信令点是否使用负荷分担或者主备用功能。<br>数据来源：整网规划<br>取值范围：<br>- “NOUSE(不使用)”<br>- “BACKUP(主备方式)”<br>- “LOADSHARE(动态负荷分担方式)”<br>- “MULTIDPCLOADSHARE(多点负荷分担方式)”<br>默认值：无 |
| SDPX | 负荷分担目的信令点索引 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定负荷分担信令点对应的索引值。<br>前提条件：该参数在<br>“负荷分担类型”<br>参数设置为<br>“LOADSHARE(动态负荷分担方式)”<br>时，才需要配置。数据来源：整网规划<br>取值范围：0~1279<br>默认值：无 |
| BDPX | 备用目的信令点索引 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定备用目的信令点索引。<br>前提条件：该参数在<br>“负荷分担类型”<br>参数设置为<br>“BACKUP(主备方式)”<br>时，才需要配置。<br>数据来源：整网规划<br>取值范围：0~1279<br>默认值：无 |
| DPN | 目的信令点名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定目的信令点名。<br>数据来源：与对端网元协商<br>取值范围：长度不超过32的字符串<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SCCPDPC]] · SCCP目的信令点（SCCPDPC）

## 使用实例

以下命令将SCCP目的信令点表中索引为1的记录的目的信令点名修改为beijing，备用目的信令点索引修改为3：

MOD SCCPDPC: DPX=1, LDP=BACKUP, BDPX=3, DPN="beijing";

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改SCCP目的信令点(MOD-SCCPDPC)_26146320.md`
