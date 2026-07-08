---
id: UNC@20.15.2@MMLCommand@RMV SGWCHGMETH
type: MMLCommand
name: RMV SGWCHGMETH（删除SGW Charge Method）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: SGWCHGMETH
command_category: 配置类
applicable_nf:
- SGW-C
effect_mode: 对新用户生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 离线计费
- SGW计费控制
- 计费属性控制
status: active
---

# RMV SGWCHGMETH（删除SGW Charge Method）

## 功能

**适用NF：SGW-C**

该命令用于删除SGW计费方式。

## 注意事项

该命令执行后只对新激活用户生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CHARGECHAR | 计费属性 | 可选必选说明：必选参数<br>参数含义：该参数用于指定SGW计费属性。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- PREPAID：表示要配置计费属性为预付费，对应的特殊CC值为0x0400。<br>- NORMAL：表示要配置计费属性为普通计费，对应的特殊CC值为0x0800。<br>- HOT_BILLING：表示要配置计费属性为热计费，对应的特殊CC值为0x0100。<br>- FLAT_BILLING：表示要配置计费属性为统一费率，对应的特殊CC值为0x0200。<br>- SPECIFIC_VALUE：表示要配置计费属性为特殊CC值。<br>- DEFAULT：表示要配置计费属性为缺省，对应的特殊CC值为0x0000。<br>默认值：无<br>配置原则：无 |
| CHARGECHARVALUE | 计费属性值 | 可选必选说明：条件必选参数<br>前提条件：该参数在“CHARGECHAR”配置为“SPECIFIC_VALUE”时为必选参数。<br>参数含义：该参数用于指定SGW计费属性值。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～6。该参数为十六进制数据类型，仅支持输入0x/X、a-f/A-F 、0-9，允许不输入0x前缀，字母不区分大小写，取值范围0x0000~0xFFFF。<br>默认值：无<br>配置原则：无 |
| CCMASK | 计费属性掩码 | 可选必选说明：条件可选参数<br>前提条件：该参数在“CHARGECHAR”配置为“SPECIFIC_VALUE”时为可选参数。<br>参数含义：该参数用于指定SGW计费属性掩码。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～6。该参数为十六进制数据类型，仅支持输入0x/X、a-f/A-F 、0-9，允许不输入0x前缀，字母不区分大小写，取值范围0x0001~0xFFFF。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SGWCHGMETH]] · SGW Charge Method（SGWCHGMETH）

## 使用实例

根据需求，删除SGW计费方式，则可以如下配置：

```
RMV SGWCHGMETH:CHARGECHAR=PREPAID;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除SGW-Charge-Method（RMV-SGWCHGMETH）_09896986.md`
