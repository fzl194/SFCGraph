---
id: UNC@20.15.2@MMLCommand@RMV RESELAREAMEM
type: MMLCommand
name: RMV RESELAREAMEM（删除AMF重选功能区域成员）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: RESELAREAMEM
command_category: 配置类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- AMF区域重选功能管理
- AMF重选功能区域成员
status: active
---

# RMV RESELAREAMEM（删除AMF重选功能区域成员）

## 功能

![](删除AMF重选功能区域成员（RMV RESELAREAMEM）_23623006.assets/notice_3.0-zh-cn_2.png)

执行该命令，如果仅输入RESELAREACODE，将删除该区域内的所有跟踪区成员。

**适用NF：AMF**

该命令用于从AMF重选功能指定的区域删除跟踪区成员。

## 注意事项

- 该命令执行后立即生效。

- 如果仅输入RESELAREACODE，那么执行本命令将删除该区域内的所有跟踪区成员。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RESELAREACODE | AMF重选功能区域编码 | 可选必选说明：必选参数<br>参数含义：该参数用于标识AMF服务的某区域范围。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~128。<br>默认值：无<br>配置原则：<br>RESELAREACODE参数依赖于RESELAREACODE命令的RESELAREACODE参数。 |
| MCC | MCC | 可选必选说明：可选参数<br>参数含义：该参数用于表示组成通用区域的位置区成员的移动国家码，与无线接入网的MCC一致。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是3。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |
| MNC | MNC | 可选必选说明：可选参数<br>参数含义：该参数用于表示组成通用区域的位置区成员的移动网号，与无线接入网的MNC一致。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是2~3。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：<br>两条记录间的MCC相同时，2位MNC与3位MNC的前两个数字不能相同。 |
| BGNTAC | 跟踪区编码起始值 | 可选必选说明：可选参数<br>参数含义：该参数用于表示跟踪区编码的起始值。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是6。TAC编码为16进制数，按照字符串格式输入，字符串长度为6，只能由数字（0-9），字母（A-F、a-f）组成。字母大小写不敏感。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [AMF重选功能区域成员（RESELAREAMEM）](configobject/UNC/20.15.2/RESELAREAMEM.md)

## 使用实例

针对同一个区域（ReSelZone），执行如下命令，将AMF上多定义的跟踪区（MCC="123", MNC="45",TAC="120101"）从该区域中删除：

```
RMV RESELAREAMEM: RESELAREACODE="ReSelZone", MCC="123", MNC="45", BGNTAC="120101";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除AMF重选功能区域成员（RMV-RESELAREAMEM）_23623006.md`
