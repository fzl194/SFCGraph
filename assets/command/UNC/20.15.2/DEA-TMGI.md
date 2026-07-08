---
id: UNC@20.15.2@MMLCommand@DEA TMGI
type: MMLCommand
name: DEA TMGI（去激活TMGI）
nf: UNC
version: 20.15.2
verb: DEA
object_keyword: TMGI
command_category: 动作类
applicable_nf:
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 5G组播广播管理
- MB-SMF组播广播管理
- 去激活MB-SMF TMGI
status: active
---

# DEA TMGI（去激活TMGI）

## 功能

**适用NF：SMF**

该命令用于去激活TMGI。

## 注意事项

- 该命令执行后立即生效。

- 该命令执行成功后，会话可能不会立即被删除。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DEATYPE | 去激活方式 | 可选必选说明：必选参数<br>参数含义：该参数用于指定去激活方式。<br>数据来源：本端规划<br>取值范围：<br>- TMGI（TMGI）<br>默认值：无<br>配置原则：无 |
| MCC | 移动国家代码 | 可选必选说明：该参数在"DEATYPE"配置为"TMGI"时为条件必选参数。<br>参数含义：该参数用于指定移动国家代码。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度是3。仅支持0-9的数字。<br>默认值：无<br>配置原则：无 |
| MNC | 移动网号 | 可选必选说明：该参数在"DEATYPE"配置为"TMGI"时为条件必选参数。<br>参数含义：该参数用于指定移动网号。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是2~3。仅支持0-9的数字。<br>默认值：无<br>配置原则：无 |
| MBSSERVICEID | 组播广播服务标识 | 可选必选说明：该参数在"DEATYPE"配置为"TMGI"时为条件必选参数。<br>参数含义：该参数用于指定组播广播服务标识。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度是6。组播广播服务标识编码为16进制数，按照字符串格式输入，字符串长度为6，只能由数字（0-9），字母（A-F、a-f）组成。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [TMGI（TMGI）](configobject/UNC/20.15.2/TMGI.md)

## 使用实例

当需要去激活MCC为460，MNC为03，MBSSERVICEID为000001的TMGI时，执行如下命令：

```
DEA TMGI: DEATYPE=TMGI, MCC="460", MNC="03", MBSSERVICEID="000001";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/去激活TMGI（DEA-TMGI）_96822090.md`
