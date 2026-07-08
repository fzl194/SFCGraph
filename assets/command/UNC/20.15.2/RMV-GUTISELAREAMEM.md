---
id: UNC@20.15.2@MMLCommand@RMV GUTISELAREAMEM
type: MMLCommand
name: RMV GUTISELAREAMEM（删除GUTI选网功能区域成员）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: GUTISELAREAMEM
command_category: 配置类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- AMF区域GUTI选网功能管理
- GUTI选网功能区域成员
status: active
---

# RMV GUTISELAREAMEM（删除GUTI选网功能区域成员）

## 功能

**适用NF：AMF**

该命令用于从GUTI选网功能指定的区域删除跟踪区成员。

## 注意事项

- 该命令执行后立即生效。

- 该命令用于从GUTI选网功能指定的区域删除跟踪区成员。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GUTISELAREACODE | GUTI选网功能区域编码 | 可选必选说明：必选参数<br>参数含义：该参数用于标识AMF服务的某区域范围。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~128。<br>默认值：无<br>配置原则：<br>GUTISELAREACODE参数依赖于GUTISELAREACODE命令的GUTISELAREACODE参数。 |
| MCC | MCC | 可选必选说明：必选参数<br>参数含义：该参数用于表示组成通用区域的位置区成员的移动国家码，与无线接入网的MCC一致。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是3。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |
| MNC | MNC | 可选必选说明：必选参数<br>参数含义：该参数用于表示组成通用区域的位置区成员的移动网号，与无线接入网的MNC一致。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是2~3。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：<br>两条记录间的MCC相同时，2位MNC与3位MNC的前两个数字不能相同。 |
| BGNTAC | 跟踪区编码起始值 | 可选必选说明：必选参数<br>参数含义：该参数用于表示跟踪区编码的起始值。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是6。TAC编码为16进制数，按照字符串格式输入，字符串长度为6，只能由数字（0-9），字母（A-F、a-f）组成。字母大小写不敏感。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@GUTISELAREAMEM]] · GUTI选网功能区域成员（GUTISELAREAMEM）

## 使用实例

针对同一个区域（GUTISelZone），执行如下命令，将AMF上多定义的跟踪区（MCC="123", MNC="45",TAC="120101"）从该区域中删除：

```
RMV GUTISELAREAMEM: GUTISELAREACODE="GUTISelZone", MCC="123", MNC="45", BGNTAC="120101";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-GUTISELAREAMEM.md`
