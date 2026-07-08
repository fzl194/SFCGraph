---
id: UDG@20.15.2@MMLCommand@SET HIGHRISKPERIOD
type: MMLCommand
name: SET HIGHRISKPERIOD（设置高危时间段提示状态）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: HIGHRISKPERIOD
command_category: 配置类
effect_mode: ''
is_dangerous: true
category_path:
- 平台服务管理
- 操作维护
- 安全管理
- 高危时间段状态管理
status: active
---

# SET HIGHRISKPERIOD（设置高危时间段提示状态）

## 功能

本命令用于设置高危时间段提示状态、高危时间段和高危命令提示信息。

> **说明**
> - 该命令中参数“高危时间段提示状态”的初始设定值为“OFF(关闭)”。
> - 高危时间段提示状态默认关闭，通过**SET HIGHRISKPERIOD**命令开启高危时间段提示状态开关后，用户在此时间段执行系统中所有高危命令时，弹框中会新增用户在“提示信息”参数中所设置的提示信息。
> - 该命令执行后仅在网元OM Portal的MML界面生效，不支持在网管界面生效。

## 参数

| **参数标识** | **参数名称** | **参数说明** |
| --- | --- | --- |
| STATUS | 高危时间段提示状态 | 可选必选说明：必选参数。<br>参数含义： 高危时间段提示的状态。<br>取值范围：<br>- OFF(关闭)：关闭高危时间段提示。<br>- ON(开启)：开启高危时间段提示。<br>默认值：无。<br>配置原则：无。 |
| STARTTIME | 起始时间 | 可选必选说明：该参数在<br>“高危时间段提示状态”<br>参数为<br>“ON(开启)”<br>时为必选参数。<br>参数含义：用于指定高危时间段的具体起始时间，输入格式为“HH:MM”，“HH”代表时，“MM”代表分。<br>取值范围：00:00-23:59。<br>默认值：无。<br>配置原则：不能与参数<br>“结束时间”<br>的值相同。如果在MML界面编辑框、MML批处理界面等编辑输入时间，格式为HH&MM，“HH”代表时，“MM”代表分。 |
| ENDTIME | 结束时间 | 可选必选说明：该参数在<br>“高危时间段提示状态”<br>参数为<br>“ON(开启)”<br>时为必选参数。<br>参数含义：用于指定高危时间段的具体结束时间，输入格式为“HH:MM”，“HH”代表时，“MM”代表分。<br>取值范围：00:00-23:59。<br>默认值：无。<br>配置原则：不能与参数<br>“起始时间”<br>的值相同。如果在MML界面编辑框、MML批处理界面等编辑输入时间，格式为HH&MM，“HH”代表时，“MM”代表分。 |
| TIPS | 提示信息 | 可选必选说明：该参数在<br>“高危时间段提示状态”<br>参数为<br>“ON(开启)”<br>时为必选参数。<br>参数含义：高危时间段执行高危命令的提示信息。<br>取值范围：长度不超过512的字符串（注：一个中文字符占两个字节）。<br>默认值：无。<br>配置原则：无。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/HIGHRISKPERIOD]] · 高危时间段提示状态（HIGHRISKPERIOD）

## 使用实例

设置高危时间段提示状态：

```
%%SET HIGHRISKPERIOD: STATUS=ON, STARTTIME=09&36, ENDTIME=23&36, TIPS="SFWEFGSDF";%% 
RETCODE = 0  操作成功 

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置高危时间段提示状态（SET-HIGHRISKPERIOD）_15084970.md`
