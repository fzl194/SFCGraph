---
id: UNC@20.15.2@MMLCommand@DSP DBGHAFD
type: MMLCommand
name: DSP DBGHAFD（显示HAFD调试命令结果）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: DBGHAFD
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 可靠性管理
- 微服务可靠性管理
status: active
---

# DSP DBGHAFD（显示HAFD调试命令结果）

## 功能

该命令用于CMF内部功能调试。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CELLID | 进程标识 | 可选必选说明：必选参数<br>参数含义：该参数是进程唯一的身份标识。通过执行<br>[**OPR DBGDATA**](../../系统调测/工程调测/5G工程命令/调试信息（OPR DBGDATA）_09587904.md)<br>：DBGTYPE=CELLTYPE，CELLTYPE=156，DEBUGNAME=“DSP MSACTIVE 102\|999”；获取dcfctrl的主进程ID。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~1024。<br>默认值：无<br>配置原则：无 |
| DEBUGNAME | 调试命令 | 可选必选说明：必选参数<br>参数含义：该参数是用户输入的调试命令，例如：cmf agent。<br>，用于获取输入命令者所期望获取的查询信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~1024。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@DBGHAFD]] · HAFD调试命令结果（DBGHAFD）

## 使用实例

查询调试命令结果

```
%%DSP DBGHAFD: CELLID="cmf-pod-2__167__0", DEBUGNAME="cmf agent";%%
RETCODE = 0  操作成功

结果如下
------------------------
Name           VersionNum              CanSync              LastUpdateTime
CELL_DCF       5534966406382843146     true            2020-09-04 02:36:09 PM                                               
MOMP           2954825132359450060     true            2020-09-04 02:35:06 PM
.... 
NULL    
(结果个数 = 32)
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-DBGHAFD.md`
