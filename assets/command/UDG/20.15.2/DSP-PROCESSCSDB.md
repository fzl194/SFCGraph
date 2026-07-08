---
id: UDG@20.15.2@MMLCommand@DSP PROCESSCSDB
type: MMLCommand
name: DSP PROCESSCSDB（查询CSDB进程信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: PROCESSCSDB
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- CSDB功能管理
- 进程管理
status: active
---

# DSP PROCESSCSDB（查询CSDB进程信息）

## 功能

该命令用于请求系统显示进程的状态信息和静态配置信息。

## 注意事项

- 该命令只适用于业务进程范围，不能查询VNFP和VNRS_VNFC的进程信息。
- 系统在执行该命令时需要消耗主机一定的CPU资源，这种CPU资源的消耗与操作员需要查询的进程数成正比，为尽量减少查询大量进程状态时对主机CPU资源的消耗，建议操作员输入具体的“进程类型”

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：必选参数。<br>参数含义：进程所在资源单元的名称。<br>默认值：无。<br>数据来源：通过<br>**[DSP RU](../../单体服务公共功能管理/系统管理/资源管理/RU管理/显示资源单元信息（DSP RU）_59103857.md)**<br>命令可以查询资源单元名称。<br>取值范围：字符串形式，不支持空格和符号'?'，区分大小写，字符串长度为1～63。 |
| PROCESSTYPE | 进程类型 | 可选必选说明：可选参数。<br>参数含义：进程类型。<br>默认值：无<br>数据来源：整网规划<br>取值范围：<br>- “UNIPLT_MPU_SMU(UNIPLT_MPU_SMU) ”<br>- “UNIPLT_LPU_SMU(UNIPLT_LPU_SMU) ”<br>- “DNP(DNP) ”<br>- “PRP(PRP) ”<br>- “OMP(OMP) ” |
| SAMEPROCTYPEINS | 同类进程实例号 | 可选必选说明：可选参数。<br>参数含义：同类进程在资源单元上的实例ID。<br>默认值：无<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～63。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/PROCESSCSDB]] · CSDB进程信息（PROCESSCSDB）

## 使用实例

查询 “RU名称” 为 “CSDB_SD_RU_0064” 、 “进程类型” 为 “PRP(PRP)” 的信息：

```
DSP PROCESSCSDB: RUNAME=" CSDB_SD_RU_0064", PROCESSTYPE=PRP;
%%DSP PROCESSCSDB: RUNAME=" CSDB_SD_RU_0064", PROCESSTYPE=PRP;%%
RETCODE = 0  操作成功。
结果如下
--------
          进程类型  =  PRP
            进程ID  =  1020
            RU名称  =  CSDB_SD_RU_0064
  进程在RU的实例ID  =  4
          进程状态  =  正常
    同类进程实例号  =  0
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-PROCESSCSDB.md`
