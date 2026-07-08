---
id: UNC@20.15.2@MMLCommand@ADD GLBOFCTEMPLATE
type: MMLCommand
name: ADD GLBOFCTEMPLATE（增加全局离线计费模板）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: GLBOFCTEMPLATE
command_category: 配置类
applicable_nf:
- SGW-C
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
max_records: 17
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 离线计费
- 离线计费基础参数
- 全局离线计费模板
status: active
---

# ADD GLBOFCTEMPLATE（增加全局离线计费模板）

## 功能

**适用NF：SGW-C、PGW-C、SMF**

此命令用来配置全局离线计费配置，分GLOBAL类型和Charge Characteristic类型的全局离线模板。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为17。
- 整机最多可以配置16条Charge Characteristic类型的离线模板，外加1条全局类型的离线计费模板。
- 配置全局离线计费模板时，必须配置离线模板。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GLOBALFLAG | 全局记录 | 可选必选说明：必选参数<br>参数含义：可以为计费属性绑定离线计费模板，也可以为全局绑定离线计费模板。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- GLOBAL：指定计费属性为缺省全局计费属性。<br>- CHARGE_CHARACT：指定计费属性为配置的特殊计费属性值。<br>默认值：无<br>配置原则：无 |
| CCVALUE | Charge Characteristic值 | 可选必选说明：条件必选参数<br>前提条件：该参数在“GLOBALFLAG”配置为“CHARGE_CHARACT”时为必选参数。<br>参数含义：指定Charge Characteristic值。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～6。该参数为十六进制数据类型，仅支持输入0x/X、a-f/A-F 、0-9，允许不输入0x前缀，字母不区分大小写，取值范围0x0000~0xFFFF。<br>默认值：无<br>配置原则：无 |
| CCMASK | Charge Characteristic特定值掩码 | 可选必选说明：条件可选参数<br>前提条件：该参数在“GLOBALFLAG”配置为“CHARGE_CHARACT”时为可选参数。<br>参数含义：指定Charge Characteristic的掩码，通过配置掩码可以实现全匹配CC值，还是只匹配部分bit位。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～6。该参数为十六进制数据类型，仅支持输入0x/X、a-f/A-F 、0-9，允许不输入0x前缀，字母不区分大小写，取值范围0x0000~0xFFFF。<br>默认值：无<br>配置原则：无 |
| CCPRIORITY | Charge Characteristic优先级 | 可选必选说明：条件可选参数<br>前提条件：该参数在“GLOBALFLAG”配置为“CHARGE_CHARACT”时为可选参数。<br>参数含义：设置优先级，配置mask时必须指定优先级。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65535。<br>默认值：无<br>配置原则：不配置此参数时值默认为0。 |
| PGWTEMPLATE | PGW离线计费模板名 | 可选必选说明：条件可选参数<br>前提条件：该参数在“GLOBALFLAG”配置为“GLOBAL” 或 “CHARGE_CHARACT”时为可选参数。<br>参数含义：指定template名称，为指定的charge characteristic或全局离线计费配置绑定PGW形态取用的离线计费模板。离线计费模板可以通过ADD OFCTEMPLATE命令配置。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格。<br>默认值：无<br>配置原则：<br>- 该参数使用ADD OFCTEMPLATE命令配置生成。<br>- UNC获取离线配置的优先级顺序由高到低为：User Profile、APN、Charge Characteristic、Global。<br>- 当高级别没有绑定离线计费模板时，则会采用下一个级别的离线计费模板配置，如果所有的级别都没有绑定离线计费模板，则取系统缺省值。<br>- 如果获取到了绑定的离线计费模板，则采用此模板的配置，对应此模板下没有配置的参数，取用参数的缺省值。当对应离线计费模板中THRESHINHERIT参数为INHERIT时，表示继承下一个级别的模板中SET OFCTHRESHOLD命令中的配置。 |
| SGWTEMPLATE | SGW离线计费模板名 | 可选必选说明：条件可选参数<br>前提条件：该参数在“GLOBALFLAG”配置为“GLOBAL” 或 “CHARGE_CHARACT”时为可选参数。<br>参数含义：指定template名称，为指定的charge characteristic或全局离线计费配置绑定SGW形态取用的离线计费模板。离线计费模板可以通过ADD OFCTEMPLATE命令配置。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格。<br>默认值：无<br>配置原则：<br>- 该参数使用ADD OFCTEMPLATE命令配置生成。<br>- UNC获取离线配置的优先级顺序由高到低为：User Profile、APN、Charge Characteristic、Global。<br>- 当高级别没有绑定离线计费模板时，则会采用下一个级别的离线计费模板配置，如果所有的级别都没有绑定离线计费模板，则取系统缺省值。<br>- 如果获取到了绑定的离线计费模板，则采用此模板的配置，对应此模板下没有配置的参数，取用参数的缺省值。当对应离线计费模板中THRESHINHERIT参数为INHERIT时，表示继承下一个级别的模板中SET OFCTHRESHOLD命令中的配置。 |
| GGSNTEMPLATE | GGSN离线计费模板名 | 可选必选说明：条件可选参数<br>前提条件：该参数在“GLOBALFLAG”配置为“GLOBAL” 或 “CHARGE_CHARACT”时为可选参数。<br>参数含义：指定模板名称，为指定的charge characteristic或全局离线计费配置绑定GGSN形态取用的离线计费模板。离线计费模板可以通过ADD OFCTEMPLATE命令配置。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格。<br>默认值：无<br>配置原则：<br>- 该参数使用ADD OFCTEMPLATE命令配置生成。<br>- UNC获取离线配置的优先级顺序由高到低为：User Profile、APN、Charge Characteristic、Global。<br>- 当高级别没有绑定离线计费模板时，则会采用下一个级别的离线计费模板配置，如果所有的级别都没有绑定离线计费模板，则取系统缺省值。<br>- 如果获取到了绑定的离线计费模板，则采用此模板的配置，对应此模板下没有配置的参数，取用参数的缺省值。当对应离线计费模板中THRESHINHERIT参数为INHERIT时，表示继承下一个级别的模板中SET OFCTHRESHOLD命令中的配置。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@GLBOFCTEMPLATE]] · 全局离线计费模板（GLBOFCTEMPLATE）

## 使用实例

- 增加GLOBAL类型的全局离线计费模板，PGWTEMPLATE为“ofc1”，SGWTEMPLATE为“ofc2”，GGSNTEMPLATE为“ofc3”：
  ```
  ADD GLBOFCTEMPLATE:GLOBALFLAG=GLOBAL,PGWTEMPLATE="ofc1",SGWTEMPLATE="ofc2",GGSNTEMPLATE="ofc3";
  ```
- 增加CHARGE_CHARACT类型的全局离线模板，CCVALUE为0x0003，CCMASK为0x0003，CCPRIORITY为1，PGWTEMPLATE为“ofc1”，SGWTEMPLATE为“ofc2”，GGSNTEMPLATE为“ofc3”：
  ```
  ADD GLBOFCTEMPLATE:GLOBALFLAG=CHARGE_CHARACT,CCVALUE="0x3",CCMASK="0x3",CCPRIORITY=1,PGWTEMPLATE="ofc1",SGWTEMPLATE="ofc2",GGSNTEMPLATE="ofc3";
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-GLBOFCTEMPLATE.md`
