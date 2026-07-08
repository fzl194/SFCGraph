---
id: UNC@20.15.2@MMLCommand@MOD SCCPOPC
type: MMLCommand
name: MOD SCCPOPC（修改SCCP本局信令点）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: SCCPOPC
command_category: 配置类
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
- SCCP本局信令点
status: active
---

# MOD SCCPOPC（修改SCCP本局信令点）

## 功能

**适用网元：SGSN、MME、SMSF**

此命令用来修改SCCP本局信令点表中指定的记录。

## 注意事项

该局信令点记录已经存在。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| OPX | 本局信令点索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定本局信令点索引。<br>数据来源：本端规划<br>取值范围：1～64<br>默认值：无 |
| OPN | 本局信令点名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定本局信令点名。<br>数据来源：本端规划<br>取值范围：长度不超过32的字符串<br>默认值：无 |

## 操作的配置对象

- [SCCP本局信令点（SCCPOPC）](configobject/UNC/20.15.2/SCCPOPC.md)

## 使用实例

以下命令将SCCP本局信令点表中索引为1的记录的信令点名修改为beijing：

MOD SCCPOPC: OPX=1, OPN="beijing";

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改SCCP本局信令点(MOD-SCCPOPC)_72345931.md`
