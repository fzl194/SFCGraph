---
id: UNC@20.15.2@MMLCommand@DSP SCCPDPC
type: MMLCommand
name: DSP SCCPDPC（显示SCCP目的信令点状态）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: SCCPDPC
command_category: 查询类
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

# DSP SCCPDPC（显示SCCP目的信令点状态）

## 功能

**适用网元：SGSN、MME、SMSF**

此命令用于查询SCCP目的信令点状态。

## 注意事项

- 系统会自行选取可用的信令进程（SPP/SGP），因此，执行该操作的时候要确保系统中有可用的信令进程。否则，操作将不能正常执行。
- 支持目的信令点索引、目的信令点状态、目的信令点名称的单独查询方式和任意组合查询方式。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SPU资源单元名称。该参数可以通过<br>[DSP RU](../../../../../../平台服务管理/单体服务公共功能管理/系统管理/资源管理/RU管理/显示资源单元信息（DSP RU）_59103857.md)<br>命令查询。<br>取值范围：1~63位字符串<br>默认值：无 |
| PT | 进程类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定进程的进程类型。<br>取值范围：<br>- “SPP(SPP)”<br>- “SGP(SGP)”<br>默认值：无 |
| PN | 进程号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定进程号。<br>取值范围：0~11<br>默认值：无 |
| DPX | 目的信令点索引 | 可选必选说明：可选参数<br>参数含义：该参数用于指定目的信令点索引。<br>前提条件：此目的信令点索引记录必须在SCCP目的信令点表中存在，通过命令<br>[**LST SCCPDPC**](查询SCCP目的信令点(LST SCCPDPC)_72225999.md)<br>查询。<br>取值范围：0~1279<br>默认值：无 |
| DPS | 目的信令点状态 | 可选必选说明：可选参数<br>参数含义：该参数用于指定查询目的信令点时需要匹配的状态，即只有符合该状态的目的信令点才显示。<br>取值范围：<br>- “ALLOW(允许)”<br>- “INHIBIT(禁止)”<br>- “OPRINHIBIT（人工禁止）”<br>- “OPRALLOW（人工允许）”<br>默认值：无 |
| DPN | 目的信令点名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定目的信令点名。<br>取值范围：长度不超过32的字符串<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SCCPDPC]] · SCCP目的信令点（SCCPDPC）

## 使用实例

查询SCCP目的信令点状态：

DSP SCCPDPC:;

```
%%DSP SCCPDPC:;%%
RETCODE = 0  操作成功。

查询SCCP目的信令点状态
----------------------
 目的信令点索引  网络指示语  目的信令点编码  本局信令点编码  目的信令点状态  负荷分担信令点状态  备用信令点状态  SCCP状态  拥塞状态

 0               国内网      0x200000        0x100000        禁止            NULL                NULL            禁止      非拥塞  
 1               国内网      0x200001        0x100000        禁止            NULL                NULL            禁止      非拥塞  
(结果个数 = 2)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-SCCPDPC.md`
