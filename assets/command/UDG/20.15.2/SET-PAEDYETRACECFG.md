---
id: UDG@20.15.2@MMLCommand@SET PAEDYETRACECFG
type: MMLCommand
name: SET PAEDYETRACECFG（设置PAE染色流控开关及阈值参数）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: PAEDYETRACECFG
command_category: 配置类
effect_mode: ''
is_dangerous: true
category_path:
- 平台服务管理
- 系统调测
- PAE 调测命令
- 染色流控
status: active
---

# SET PAEDYETRACECFG（设置PAE染色流控开关及阈值参数）

## 功能

![](设置PAE染色流控开关及阈值参数（SET PAEDYETRACECFG）_20679422.assets/notice_3.0-zh-cn.png)

该命令是高危命令。染色流控开关关闭后，染色跟踪流控功能失效，可能会对现有业务造成影响，请谨慎操作。

该命令用于修改PAE染色跟踪流控开关及阈值参数。

> **说明**
> - 该命令执行后立即生效。
>
> - 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：
>
> | FLOWSWITCH | STARTFLOW_X86 | STOPFLOW_X86 | STARTFLOW_ARM | STOPFLOW_ARM | DYECPUPERFLMT |
> | --- | --- | --- | --- | --- | --- |
> | ON | 880 | 800 | 1000 | 900 | 40 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| FLOWSWITCH | 全流控开关 | 可选必选说明：可选参数<br>参数含义：染色跟踪全流控开关。<br>数据来源：本端规划<br>取值范围：<br>- “ON（开）”：染色全流控开关打开<br>- “OFF（关）”：染色全流控开关关闭<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST PAEDYETRACECFG查询当前参数配置值。<br>配置原则：无 |
| STARTFLOW_X86 | 起控阈值X86 (‰) | 可选必选说明：可选参数<br>参数含义：X86染色跟踪开启流控的阈值，千分比形式。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~1000。大于等于X86停控阈值 (‰)。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST PAEDYETRACECFG查询当前参数配置值。<br>配置原则：无 |
| STOPFLOW_X86 | 停控阈值X86 (‰) | 可选必选说明：可选参数<br>参数含义：X86染色跟踪停止流控的阈值，千分比形式。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~1000。小于等于X86起控阈值 (‰)。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST PAEDYETRACECFG查询当前参数配置值。<br>配置原则：无 |
| STARTFLOW_ARM | 起控阈值ARM (‰) | 可选必选说明：可选参数<br>参数含义：ARM染色跟踪开启流控的阈值，千分比形式。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~1000。大于等于ARM停控阈值 (‰)。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST PAEDYETRACECFG查询当前参数配置值。<br>配置原则：无 |
| STOPFLOW_ARM | 停控阈值ARM (‰) | 可选必选说明：可选参数<br>参数含义：ARM染色跟踪停止流控的阈值，千分比形式。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~1000。小于等于ARM起控阈值 (‰)。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST PAEDYETRACECFG查询当前参数配置值。<br>配置原则：无 |
| DYECPUPERFLMT | 染色消耗CPU比例阈值 (‰) | 可选必选说明：可选参数<br>参数含义：染色跟踪部分流控中染色模块消耗CPU比例阈值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~1000。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST PAEDYETRACECFG查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/PAEDYETRACECFG]] · PAE染色流控开关及阈值参数（PAEDYETRACECFG）

## 使用实例

设置染色跟踪流控开关及阈值参数，设置全流控开关为开，X86起控阈值为800，X86停控阈值为700，ARM起控阈值为1000，ARM停控阈值为900，染色消耗CPU比例阈值为50

```
+++    UNC/*MEID:0 MENAME:env103*/        2024-12-13 00:58:26
O&M    #5589
%%SET PAEDYETRACECFG: FLOWSWITCH=ON, STARTFLOW_X86=800, STOPFLOW_X86=700, STARTFLOW_ARM=1000, STOPFLOW_ARM=900, DYECPUPERFLMT=50;%%
RETCODE = 0  操作成功

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-PAEDYETRACECFG.md`
