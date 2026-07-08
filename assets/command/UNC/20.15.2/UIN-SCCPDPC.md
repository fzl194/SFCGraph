---
id: UNC@20.15.2@MMLCommand@UIN SCCPDPC
type: MMLCommand
name: UIN SCCPDPC（解禁SCCP目的信令点）
nf: UNC
version: 20.15.2
verb: UIN
object_keyword: SCCPDPC
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
- SCCP目的信令点
status: active
---

# UIN SCCPDPC（解禁SCCP目的信令点）

## 功能

**适用网元：SGSN、MME、SMSF**

此命令用于解禁SCCP目的信令点。

## 注意事项

- 系统会自行选取可用的信令进程，因此，执行该操作的时候要确保系统中有可用的信令进程。否则，操作将不能正常执行。
- 只有处于禁止状态的SCCP目的信令点才能执行解禁操作。解禁SCCP目的信令点是要和对端交互的，如果交互失败，解禁操作不一定成功。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DPX | 目的信令点索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定目的信令点索引。<br>前提条件：此目的信令点索引记录必须在SCCP目的信令点表中存在，通过命令<br>[**LST SCCPDPC**](查询SCCP目的信令点(LST SCCPDPC)_72225999.md)<br>查询。<br>取值范围：0~1279<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SCCPDPC]] · SCCP目的信令点（SCCPDPC）

## 使用实例

解禁信令点索引为1的SCCP目的信令点：

UIN SCCPDPC: DPX=1;

## 证据

- 原始手册：`evidence/UNC/20.15.2/UIN-SCCPDPC.md`
