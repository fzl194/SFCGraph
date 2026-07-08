---
id: UNC@20.15.2@MMLCommand@RMV WEEKDAY
type: MMLCommand
name: RMV WEEKDAY（删除计费星期表）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: WEEKDAY
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
- 费率切换
- 工作日
status: active
---

# RMV WEEKDAY（删除计费星期表）

## 功能

**适用NF：SGW-C、PGW-C、SMF**

该命令用来删除指定计费属性星期配置信息。

## 注意事项

- 该命令执行后立即生效。
- 全局配置的星期配置信息不能删除，只能恢复默认配置。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GLOBALFLG | 全局配置 | 可选必选说明：必选参数<br>参数含义：该参数用于指定计费类型。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- GLOBAL：指定计费属性为缺省全局计费属性。<br>- CHARGE_CHARACT：指定计费属性为配置的特殊计费属性值。<br>默认值：无<br>配置原则：<br>- GLOBAL：当GLOBALFLG值为GLOBAL时，表示要恢复全局计费星期配置信息。<br>- CHARGE_CHARACT：当GLOBALFLG值为CHARGE_CHARACT时，表示要删除指定计费属性配置信息。 |
| CCVALUE | 计费属性值 | 可选必选说明：条件必选参数<br>前提条件：该参数在“GLOBALFLG”配置为“CHARGE_CHARACT”时为必选参数。<br>参数含义：该参数用于指定特殊的CC值。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～6。该参数为十六进制数据类型，仅支持输入0x/X、a-f/A-F 、0-9，允许不输入0x前缀，字母不区分大小写，取值范围0x0000~0xFFFF。<br>默认值：无<br>配置原则：无 |
| CCMASK | 计费属性掩码 | 可选必选说明：条件可选参数<br>前提条件：该参数在“GLOBALFLG”配置为“CHARGE_CHARACT”时为可选参数。<br>参数含义：该参数用于指定计费属性的掩码。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～6。该参数为十六进制数据类型，仅支持输入0x/X、a-f/A-F 、0-9，允许不输入0x前缀，字母不区分大小写，取值范围0x0001~0xFFFF。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/WEEKDAY]] · 计费星期表（WEEKDAY）

## 使用实例

删除计费属性值为0x0400的用户的计费属性星期配置信息：

```
RMV WEEKDAY: GLOBALFLG=CHARGE_CHARACT,CCVALUE="0x400";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除计费星期表（RMV-WEEKDAY）_09896833.md`
