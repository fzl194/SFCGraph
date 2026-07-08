---
id: UNC@20.15.2@MMLCommand@RMV TARIFFGROUP
type: MMLCommand
name: RMV TARIFFGROUP（删除费率切换组）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: TARIFFGROUP
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
- 费率切换组
status: active
---

# RMV TARIFFGROUP（删除费率切换组）

## 功能

**适用NF：SGW-C、PGW-C、SMF**

该命令用来删除指定的费率切换组记录。

## 注意事项

- 该命令执行后立即生效。
- 删除前，需要先通过命令LST APNCHARGECTRL、LST USRPROFCHARGE和LST GLBTARIFFGROUP查看本命令是否被这些命令绑定了。如果被绑定，则不允许删除。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TARIFFGRPNAME | 费率切换组名 | 可选必选说明：必选参数<br>参数含义：指定费率切换组名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：无 |
| GLOBALFLG | 全局配置 | 可选必选说明：可选参数<br>参数含义：指定全局配置。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- GLOBAL：指定计费属性为缺省全局计费属性。<br>- CHARGE_CHARACT：指定计费属性为配置的特殊计费属性值。<br>默认值：无<br>配置原则：<br>- GLOBAL：全局。<br>- CHARGE_CHARACT：计费属性。 |
| CCVALUE | Charge Characteristic值 | 可选必选说明：条件必选参数<br>前提条件：该参数在“GLOBALFLG”配置为“CHARGE_CHARACT”时为必选参数。<br>参数含义：指定Charge Characteristic（计费属性）值。当“GLOBALFLG”设置为“CHARGE_CHARACT”时，该参数必须设置。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～6。该参数为十六进制数据类型，仅支持输入0x/X、a-f/A-F 、0-9，允许不输入0x前缀，字母不区分大小写，取值范围0x0000~0xFFFF。<br>默认值：无<br>配置原则：无 |
| CCMASK | Charge Characteristic掩码 | 可选必选说明：条件可选参数<br>前提条件：该参数在“GLOBALFLG”配置为“CHARGE_CHARACT”时为可选参数。<br>参数含义：指定Charge Characteristic(计费属性)掩码值。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～6。该参数为十六进制数据类型，仅支持输入0x/X、a-f/A-F 、0-9，允许不输入0x前缀，字母不区分大小写，取值范围0x0001~0xFFFF。<br>默认值：无<br>配置原则：无 |
| TARIFFTYPE | 费率类型 | 可选必选说明：条件必选参数<br>前提条件：该参数在“GLOBALFLG”配置为“CHARGE_CHARACT” 或 “GLOBAL”时为必选参数。<br>参数含义：指定配置费率类型为工作日、节假日或者周末。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- WORKDAY<br>- WEEKEND<br>- FESTIVAL<br>默认值：无<br>配置原则：无 |
| STARTTIME | 费率切换起始时间 | 可选必选说明：条件必选参数<br>前提条件：该参数在“TARIFFTYPE”配置为“FESTIVAL”、“WEEKEND” 或 “WORKDAY”时为必选参数。<br>可选必选说明：条件必选参数<br>前提条件：该参数在“GLOBALFLG”配置为“CHARGE_CHARACT” 或 “GLOBAL”时为必选参数。<br>参数含义：指定费率切换起始时间。<br>数据来源：本端规划<br>取值范围：时间类型，输入格式是HH:MM。<br>默认值：无<br>配置原则：无 |
| ENDTIME | 费率切换终止时间 | 可选必选说明：条件必选参数<br>前提条件：该参数在“TARIFFTYPE”配置为“FESTIVAL”、“WEEKEND” 或 “WORKDAY”时为必选参数。<br>可选必选说明：条件必选参数<br>前提条件：该参数在“GLOBALFLG”配置为“CHARGE_CHARACT” 或 “GLOBAL”时为必选参数。<br>参数含义：费率切换结束时间。<br>数据来源：本端规划<br>取值范围：时间类型，输入格式是HH:MM。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [费率切换组（TARIFFGROUP）](configobject/UNC/20.15.2/TARIFFGROUP.md)

## 使用实例

删除费率切换组，TARIFFGRPNAME为“huawei”，GLOBALFLG为“CHARGE_CHARACT”，CCVALUE为“0x0100”，CCMASK为“0x0100”，TARIFFTYPE为“WORKDAY”，STARTTIME为“09:00”，ENDTIME为“17:00”，命令为：

```
RMV TARIFFGROUP:TARIFFGRPNAME="huawei",GLOBALFLG=CHARGE_CHARACT,CCVALUE="0x100",CCMASK="0x100",TARIFFTYPE=WORKDAY,STARTTIME=09&00,ENDTIME=17&00;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除费率切换组（RMV-TARIFFGROUP）_09896837.md`
