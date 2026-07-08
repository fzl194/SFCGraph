---
id: UNC@20.15.2@MMLCommand@ADD EPLMNGRPMEM
type: MMLCommand
name: ADD EPLMNGRPMEM（增加等价PLMN组成员）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: EPLMNGRPMEM
command_category: 配置类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 运营商管理
- 等价PLMN组成员管理
status: active
---

# ADD EPLMNGRPMEM（增加等价PLMN组成员）

## 功能

**适用NF：AMF**

该命令用于为等价PLMN组添加PLMN成员。在一个等价PLMN组内的PLMN互为等价PLMN。

## 注意事项

- 该命令执行后立即生效。

- 一个等价PLMN组内PLMN成员数量的最大值是15。
- 同一等价PLMN组内PLMN成员互不相同。

- 最多可输入128条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GRPIDX | 等价PLMN组号 | 可选必选说明：必选参数<br>参数含义：该参数用于标识等价PLMN组，通过命令ADD EPLMNGRP进行配置。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~127。<br>默认值：无<br>配置原则：无 |
| MCC | 移动国家码 | 可选必选说明：必选参数<br>参数含义：该参数用于表示组成等价PLMN的移动国家码信息。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是3。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |
| MNC | 移动网号 | 可选必选说明：必选参数<br>参数含义：该参数用于表示组成等价PLMN的移动网号信息。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是2~3。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |
| DESC | 描述信息 | 可选必选说明：可选参数<br>参数含义：该参数用于对等价PLMN组成员的描述，在运维中起助记作用。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~32。<br>默认值：无<br>配置原则：<br>输入单空格将删除该参数已有配置项。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/EPLMNGRPMEM]] · 等价PLMN组成员（EPLMNGRPMEM）

## 使用实例

为PLMN为12345的Serving PLMN增加等价PLMN 12389，其中Serving PLMN 12345使用的等价PLMN组号为0，执行如下命令：

```
ADD EPLMNGRPMEM: GRPIDX=0, MCC="123", MNC="89", DESC="add eplmn 12389 for 12345";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-EPLMNGRPMEM.md`
