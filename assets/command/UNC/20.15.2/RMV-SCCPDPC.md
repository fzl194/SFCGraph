---
id: UNC@20.15.2@MMLCommand@RMV SCCPDPC
type: MMLCommand
name: RMV SCCPDPC（删除SCCP目的信令点）
nf: UNC
version: 20.15.2
verb: RMV
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

# RMV SCCPDPC（删除SCCP目的信令点）

## 功能

**适用网元：SGSN、MME、SMSF**

此命令用于删除SCCP目的信令点。

## 注意事项

- 此命令执行后立即生效。
- 执行此命令将中断到目的信令点的所有服务。
- 当SCCP子系统表、SCCP GT表或SCCP DPC多点负荷分担表中存在此目的信令点相关的记录时，不允许删除该记录。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DPX | 目的信令点索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定SCCP目的信令点索引。<br>前提条件：此目的信令点索引记录必须在SCCP目的信令点表中存在，通过命令<br>[**LST SCCPDPC**](查询SCCP目的信令点(LST SCCPDPC)_72225999.md)<br>查询。<br>取值范围：0~1279<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SCCPDPC]] · SCCP目的信令点（SCCPDPC）

## 使用实例

删除索引为1的SCCP目的信令点：

RMV SCCPDPC: DPX=1;

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除SCCP目的信令点(RMV-SCCPDPC)_72345919.md`
