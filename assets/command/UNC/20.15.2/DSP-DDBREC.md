---
id: UNC@20.15.2@MMLCommand@DSP DDBREC
type: MMLCommand
name: DSP DDBREC（查询DDB记录）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: DDBREC
command_category: 查询类
applicable_nf:
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- MME链式备份管理
- 扩展调测
- 平台调测
- 通信调测
status: active
---

# DSP DDBREC（查询DDB记录）

## 功能

**适用网元：MME**

该命令用于查询DDB记录。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定要查询的资源单元名称。该参数可以通过<br>[DSP RU](../../../../../../平台服务管理/单体服务公共功能管理/系统管理/资源管理/RU管理/显示资源单元信息（DSP RU）_59103857.md)<br>命令查询。<br>可选必选说明：可选参数<br>取值范围：1 ~ 63位字符串<br>默认值：无 |
| PROCTYPE | 进程类型 | 可选必选说明：必选参数<br>参数含义：该参数用于要查询的进程类型。<br>取值范围：<br>- “SAP(SAP)”<br>- “SRP(SRP)”<br>- “OMP(OMP)”<br>默认值：无 |
| PROCNO | 进程序列号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定要查询的进程序号。<br>取值范围：0~20<br>默认值：无 |
| SQL | SQL语句 | 可选必选说明：必选参数<br>参数含义：该参数用于指定查询的sql语句。<br>取值范围：无<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/DDBREC]] · DDB记录（DDBREC）

## 使用实例

查询资源单元为MCR_SP_RU_0065的0号SAP进程的315号表的所有DDB记录：

DSP DDBREC: RUNAME="MCR_SP_RU_0065", PROCTYPE=SAP, PROCNO=0, SQL="select * from 315";

```
%%DSP DDBREC: RUNAME="MCR_SP_RU_0065", PROCTYPE=SAP, PROCNO=0, SQL="select * from 315";%%
RETCODE = 0  操作成功。

操作结果如下
--------------
Output  =  ----------CPUID: 2241200376----------
exesql "select * from 315"

	DDBQueryMultiRecordsUnintentionally: Success.
		Get record number: 1. 

		Field 0: 
0
		Field 1: 
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff
		Field 2: 
01 00 00 00
		Field 3: 
00 00 00 00

(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询DDB记录(DSP-DDBREC)_72346911.md`
