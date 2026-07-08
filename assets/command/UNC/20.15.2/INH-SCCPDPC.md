---
id: UNC@20.15.2@MMLCommand@INH SCCPDPC
type: MMLCommand
name: INH SCCPDPC（禁止SCCP目的信令点）
nf: UNC
version: 20.15.2
verb: INH
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

# INH SCCPDPC（禁止SCCP目的信令点）

## 功能

![](禁止SCCP目的信令点(INH SCCPDPC)_72345921.assets/notice_3.0-zh-cn_2.png)

- 系统会自行选取可用的信令进程（SPP/SGP），因此，执行该操作的时候要确保系统中有可用的信令进程。否则，操作将不能正常执行。
- 禁止SCCP目的信令点将会导致到达该目的信令点的业务无法进行。
- 禁止SCCP目的信令点是要和对端交互的，如果交互失败，禁止操作不一定成功。

**适用网元：SGSN、MME、SMSF**

此命令用于禁止SCCP目的信令点。

## 注意事项

- 系统会自行选取可用的信令进程（SPP/SGP），因此，执行该操作的时候要确保系统中有可用的信令进程。否则，操作将不能正常执行。
- 禁止SCCP目的信令点将会导致到达该目的信令点的业务无法进行。禁止SCCP目的信令点是要和对端交互的，如果交互失败，禁止操作不一定成功。
- 该命令会在进程复位后失效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DPX | 目的信令点索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定目的信令点索引。<br>前提条件：此目的信令点索引记录必须在SCCP目的信令点表中存在，通过命令<br>[**LST SCCPDPC**](查询SCCP目的信令点(LST SCCPDPC)_72225999.md)<br>查询。<br>取值范围：0～1279<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SCCPDPC]] · SCCP目的信令点（SCCPDPC）

## 使用实例

禁止信令点索引为1的SCCP目的信令点：

INH SCCPDPC: DPX=1;

## 证据

- 原始手册：`evidence/UNC/20.15.2/禁止SCCP目的信令点(INH-SCCPDPC)_72345921.md`
