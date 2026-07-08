---
id: UNC@20.15.2@MMLCommand@RMV GLBOFCTEMPLATE
type: MMLCommand
name: RMV GLBOFCTEMPLATE（删除全局离线计费模板）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: GLBOFCTEMPLATE
command_category: 配置类
applicable_nf:
- SGW-C
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 离线计费
- 离线计费基础参数
- 全局离线计费模板
status: active
---

# RMV GLBOFCTEMPLATE（删除全局离线计费模板）

## 功能

**适用NF：SGW-C、PGW-C、SMF**

此命令用来删除基于CC配置的离线模板，或者恢复全局缺省离线模板。

## 注意事项

- 该命令执行后立即生效。
- 离线计费模板绑定到全局离线计费模板不可删除，只能恢复成默认值。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GLOBALFLAG | 全局记录 | 可选必选说明：必选参数<br>参数含义：可以为计费属性绑定离线计费模板，也可以为全局绑定离线计费模板。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- GLOBAL：指定计费属性为缺省全局计费属性。<br>- CHARGE_CHARACT：指定计费属性为配置的特殊计费属性值。<br>默认值：无<br>配置原则：无 |
| CCVALUE | Charge Characteristic值 | 可选必选说明：条件必选参数<br>前提条件：该参数在“GLOBALFLAG”配置为“CHARGE_CHARACT”时为必选参数。<br>参数含义：指定Charge Characteristic值。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～6。该参数为十六进制数据类型，仅支持输入0x/X、a-f/A-F 、0-9，允许不输入0x前缀，字母不区分大小写，取值范围0x0000~0xFFFF。<br>默认值：无<br>配置原则：无 |
| TEMPLATETYPE | 模板类型 | 可选必选说明：条件可选参数<br>前提条件：该参数在“GLOBALFLAG”配置为“GLOBAL” 或 “CHARGE_CHARACT”时为可选参数。<br>参数含义：指定要删除的模板类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- PGW_TEMPLATE：指定PGW离线计费模板。<br>- SGW_TEMPLATE：指定SGW离线计费模板。<br>- GGSN_TEMPLATE：指定GGSN离线计费模板。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [全局离线计费模板（GLBOFCTEMPLATE）](configobject/UNC/20.15.2/GLBOFCTEMPLATE.md)

## 使用实例

删除指定的基于CC配置的离线计费模板，GLOBALFLAG为CHARGE_CHARACT，CCVALUE为0x0003，TEMPLATETYPE为SGW_TEMPLATE的配置：

```
RMV GLBOFCTEMPLATE:GLOBALFLAG=CHARGE_CHARACT,CCVALUE="0x3",TEMPLATETYPE=SGW_TEMPLATE;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除全局离线计费模板（RMV-GLBOFCTEMPLATE）_09896918.md`
