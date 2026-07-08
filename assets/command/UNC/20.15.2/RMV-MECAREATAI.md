---
id: UNC@20.15.2@MMLCommand@RMV MECAREATAI
type: MMLCommand
name: RMV MECAREATAI（删除5G MEC TAI信息）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: MECAREATAI
command_category: 配置类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- AM策略和UE策略管理
- 本地特色业务区域管理
- 本地特色业务区域TAI成员管理
status: active
---

# RMV MECAREATAI（删除5G MEC TAI信息）

## 功能

**适用NF：AMF**

该命令用于删除5G MEC跟踪区成员。

## 注意事项

下一次移动性流程生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MCC | MCC | 可选必选说明：必选参数<br>参数含义：该参数用于表示移动国家码，与无线接入网的MCC一致。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是3。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |
| MNC | MNC | 可选必选说明：必选参数<br>参数含义：该参数用于表示移动网号，与无线接入网的MNC一致。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是2~3。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |
| TACBEGIN | 跟踪区起始编码 | 可选必选说明：必选参数<br>参数含义：该参数用于表示跟踪区编码起始值。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是6。TAC编码为16进制数，按照字符串格式输入，字符串长度为6，只能由数字（0-9），字母（A-F、a-f）组成，且字母大小写不敏感。<br>默认值：无<br>配置原则：无 |
| TACEND | 跟踪区结束编码 | 可选必选说明：必选参数<br>参数含义：该参数用于表示跟踪区编码结束值。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是6。TAC编码为16进制数，按照字符串格式输入，字符串长度为6，只能由数字（0-9），字母（A-F、a-f）组成，且字母大小写不敏感。本参数表示的跟踪区编码不能小于“跟踪区起始编码”。<br>默认值：无<br>配置原则：无 |
| AREAID | 区域标识 | 可选必选说明：可选参数<br>参数含义：该参数用于表示区域（例如：商场或景区）的标识。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~1024。<br>默认值：无<br>配置原则：<br>AREAID需要通过ADD MECAREA命令配置添加。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/MECAREATAI]] · 5G MEC TAI信息（MECAREATAI）

## 使用实例

删除标识为“1”的区域的一个跟踪区成员（MCC="123", MNC="45", TACBEGIN="123456", TACEND="123456"），执行如下命令：

```
RMV MECAREATAI:AREAID=1,MCC="123",MNC="45",TACBEGIN="123456",TACEND="123456";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除5G-MEC-TAI信息（RMV-MECAREATAI）_85091977.md`
