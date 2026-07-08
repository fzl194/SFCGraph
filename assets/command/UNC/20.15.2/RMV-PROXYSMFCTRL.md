---
id: UNC@20.15.2@MMLCommand@RMV PROXYSMFCTRL
type: MMLCommand
name: RMV PROXYSMFCTRL（删除proxy SMF控制）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: PROXYSMFCTRL
command_category: 配置类
applicable_nf:
- SMF
effect_mode: 对新用户生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- Proxy SGW_SMF管理
- Proxy SMFS8管理
status: active
---

# RMV PROXYSMFCTRL（删除proxy SMF控制）

## 功能

**适用NF：SMF**

该命令用于删除PROXYSMFCTRL配置。

## 注意事项

该命令执行后只对新激活用户生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MCC | 移动国家码 | 可选必选说明：必选参数<br>参数含义：该参数用于配置移动国家码信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度是3。<br>默认值：无<br>配置原则：无 |
| MNC | 移动网号 | 可选必选说明：必选参数<br>参数含义：该参数用于配置移动网号信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是2~3。<br>默认值：无<br>配置原则：无 |
| CTRLTYPE | 控制类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定控制类型。<br>数据来源：全网规划<br>取值范围：<br>- DNN_LEVEL（DNN级别）<br>- GLOBAL_LEVEL（整系统级别）<br>默认值：无<br>配置原则：无 |
| DNN | DNN | 可选必选说明：该参数在"CTRLTYPE"配置为"DNN_LEVEL"时为条件必选参数。<br>参数含义：该参数用于指定组成QoS控制的DNN，即用户请求的DNN。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：<br>输入的DNN名称需要符合DNN命名规则，仅支持配置APN NI（Network Identifier），例如“huawei.com”。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@PROXYSMFCTRL]] · proxy SMF控制（PROXYSMFCTRL）

## 使用实例

假设运营商需要删除MCC为“460”、MNN为“00”、控制类型为整系统级别的PROXYSMFCTRL配置。

```
RMV PROXYSMFCTRL:MCC="460",MNC="00",CTRLTYPE=GLOBAL_LEVEL;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-PROXYSMFCTRL.md`
