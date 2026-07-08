---
id: UNC@20.15.2@MMLCommand@RMV CHARGEMETHOD
type: MMLCommand
name: RMV CHARGEMETHOD（删除计费方式）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: CHARGEMETHOD
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
effect_mode: 对新用户生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 计费控制
- 计费属性计费控制
status: active
---

# RMV CHARGEMETHOD（删除计费方式）

## 功能

**适用NF：PGW-C、SMF**

RMV CHARGEMETHOD命令用来删除基于用户计费属性配置在线计费和离线计费方式。

## 注意事项

- 该命令执行后只对新激活用户生效。
- 已经激活的用户，仍保留原有的在线离线、融合计费方式。
- 不能删除参数CHARGECHARACT的值为DEFAULT类型的记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CHARGECHARACT | 计费属性 | 可选必选说明：必选参数<br>参数含义：该参数用于指定计费属性。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- PREPAID：表示要配置计费属性为预付费，对应的特殊CC值为0x0400。<br>- NORMAL：表示要配置计费属性为普通计费，对应的特殊CC值为0x0800。<br>- HOT_BILLING：表示要配置计费属性为热计费，对应的特殊CC值为0x0100。<br>- FLAT_BILLING：表示要配置计费属性为统一费率，对应的特殊CC值为0x0200。<br>- SPECIFIC_VALUE：表示要配置计费属性为特殊CC值。<br>- DEFAULT：表示要配置计费属性为缺省，对应的特殊CC值为0x0000。<br>默认值：无<br>配置原则：无 |
| CCVALUE | 计费属性值 | 可选必选说明：条件必选参数<br>前提条件：该参数在“CHARGECHARACT”配置为“SPECIFIC_VALUE”时为必选参数。<br>参数含义：该参数用于指定特殊的CC值。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～6。该参数为十六进制数据类型，仅支持输入0x/X、a-f/A-F 、0-9，允许不输入0x前缀，字母不区分大小写，取值范围0x0000~0xFFFF。<br>默认值：无<br>配置原则：无 |
| MASK | 计费属性掩码 | 可选必选说明：条件可选参数<br>前提条件：该参数在“CHARGECHARACT”配置为“SPECIFIC_VALUE”时为可选参数。<br>参数含义：该参数用于指定计费属性的掩码。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～6。该参数为十六进制数据类型，仅支持输入0x/X、a-f/A-F 、0-9，允许不输入0x前缀，字母不区分大小写，取值范围0x0001~0xFFFF。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/CHARGEMETHOD]] · 计费方式（CHARGEMETHOD）

## 使用实例

删除计费属性值为1024的用户的计费属性配置信息：

```
RMV CHARGEMETHOD:CHARGECHARACT=SPECIFIC_VALUE,CCVALUE="0x400";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-CHARGEMETHOD.md`
