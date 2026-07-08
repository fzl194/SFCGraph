---
id: UNC@20.15.2@MMLCommand@RMV AREAMEM
type: MMLCommand
name: RMV AREAMEM（删除跟踪区成员）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: AREAMEM
command_category: 配置类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 通用配置管理
- 通用区域成员管理
status: active
---

# RMV AREAMEM（删除跟踪区成员）

## 功能

![](删除跟踪区成员（RMV AREAMEM）_44007540.assets/notice_3.0-zh-cn_2.png)

执行该命令，如果仅输入AREACODE，将删除该区域内的所有跟踪区成员。

**适用NF：AMF**

该命令用于从指定的区域删除跟踪区成员。

## 注意事项

- 该命令执行后立即生效。

- 如果仅输入AREACODE，那么执行本命令将删除该区域内的所有跟踪区成员。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| AREACODE | 区域编码 | 可选必选说明：必选参数<br>参数含义：该参数用于标识AMF服务的某区域范围。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~128。<br>默认值：无<br>配置原则：无 |
| BGNTAC | 跟踪区编码起始值 | 可选必选说明：可选参数<br>参数含义：该参数用于表示跟踪区编码的起始值。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是6。TAC编码为16进制数，按照字符串格式输入，字符串长度为6，只能由数字（0-9），字母（A-F、a-f）组成。字母大小写不敏感。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/AREAMEM]] · 跟踪区成员（AREAMEM）

## 使用实例

针对同一个区域（jq001.pd006.sh.mcc123.mnc45），AMF上的定义与UDM不一致。执行如下命令，将AMF上多定义的跟踪区（TAC="120101"）从该区域中删除：

```
RMV AREAMEM: AREACODE="jq001.pd006.sh.mcc123.mnc45", BGNTAC="120101";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除跟踪区成员（RMV-AREAMEM）_44007540.md`
