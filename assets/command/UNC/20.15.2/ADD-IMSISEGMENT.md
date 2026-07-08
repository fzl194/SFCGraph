---
id: UNC@20.15.2@MMLCommand@ADD IMSISEGMENT
type: MMLCommand
name: ADD IMSISEGMENT（增加IMSI号码段）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: IMSISEGMENT
command_category: 配置类
applicable_nf:
- SGW-C
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- UPF选择管理
- UPF绑定用户漫游属性
status: active
---

# ADD IMSISEGMENT（增加IMSI号码段）

## 功能

**适用NF：SGW-C**

该命令用于增加IMSI号段，用于判断漫游状态进行UPF选择。

## 注意事项

- 该命令执行后立即生效。

- 最多可输入4096条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SEGMENTNAME | IMSI号段名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定IMSI号段名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~31。只允许输入字母、数字、“.”、“_”和“-”。字母会被转换为小写字母进行存储和处理。<br>默认值：无<br>配置原则：无 |
| SEGMENTTYPE | IMSI号段类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定使用运营商定制方式判断漫游状态进行UPF选择的IMSI号段类型。<br>数据来源：全网规划<br>取值范围： IMSI_PREFIX<br>- IMSI_PREFIX（IMSI前缀）<br>默认值：无<br>配置原则：无 |
| IMSIPRE | IMSI前缀 | 可选必选说明：该参数在"SEGMENTTYPE"配置为"IMSI_PREFIX"时为条件必选参数。<br>参数含义：该参数在"SEGMENTTYPE"配置为"IMSI_PREFIX"时为条件必选参数。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~15。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@IMSISEGMENT]] · IMSI号码段（IMSISEGMENT）

## 使用实例

当运营商需要判断漫游状态进行UPF选择时，执行命令如下：

```
ADD IMSISEGMENT: SEGMENTNAME="imsipre1",SEGMENTTYPE=IMSI_PREFIX, IMSIPRE="28602851";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-IMSISEGMENT.md`
