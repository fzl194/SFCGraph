---
id: UNC@20.15.2@MMLCommand@OPR DBGDATA
type: MMLCommand
name: OPR DBGDATA（调试信息）
nf: UNC
version: 20.15.2
verb: OPR
object_keyword: DBGDATA
command_category: 动作类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 系统调测
- 工程调测
- 5G工程命令
status: active
---

# OPR DBGDATA（调试信息）

## 功能

此命令用于查询服务的调试信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DBGTYPE | 操作对象 | 可选必选说明：可选参数<br>参数含义：该参数用于表示调试消息发送对象类型。<br>数据来源：本端规划<br>取值范围：<br>- CELLTYPE（进程类型）<br>- CELLID（进程标识）<br>默认值：无<br>配置原则：无 |
| CELLTYPE | 进程类型 | 可选必选说明：该参数在"DBGTYPE"配置为"CELLTYPE"时为条件必选参数。<br>参数含义：该参数用于表示发给同一类型的进程。通过DSP MSPROCTYPE来查询。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~4294967295。<br>默认值：无<br>配置原则：无 |
| CELLID | 进程标识 | 可选必选说明：该参数在"DBGTYPE"配置为"CELLID"时为条件必选参数。<br>参数含义：该参数用于表示发给某一个进程。通过DSP MSPROCESS查询。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~100。不支持空格，区分大小写。<br>默认值：无<br>配置原则：无 |
| DEBUGNAME | 调试信息 | 可选必选说明：可选参数<br>参数含义：该参数用于表示调试信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~250。<br>默认值：无<br>配置原则：<br>调试信息举例如下：<br>DSP MSACTIVE：该命令用于查询选举域内的主信息。<br>DSP PREFIX：该命令用于查询环境内所有的选举域。<br>DSP SCF INSTANTSTATUS：查询实例化流程总体进度。<br>DSP DCF TOKENPLY：该命令用于查询Token的策略信息。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/DBGDATA]] · 调试信息（DBGDATA）

## 使用实例

查询操作对象为进程类型，进程类型为100，DEBUGNAME为DSP CELLID时的调试信息：

```
%%OPR DBGDATA: DBGTYPE=CELLTYPE, CELLTYPE=100, DEBUGNAME="DSP CELLID";%%
RETCODE = 0  操作成功

结果如下
--------
调测输出  =  
all topo cell count is 198

(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/OPR-DBGDATA.md`
