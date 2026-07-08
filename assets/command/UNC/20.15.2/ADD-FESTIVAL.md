---
id: UNC@20.15.2@MMLCommand@ADD FESTIVAL
type: MMLCommand
name: ADD FESTIVAL（增加计费节假日表）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: FESTIVAL
command_category: 配置类
applicable_nf:
- SGW-C
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
max_records: 1600
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 费率切换
- 节假日
status: active
---

# ADD FESTIVAL（增加计费节假日表）

## 功能

**适用NF：SGW-C、PGW-C、SMF**

该命令用于根据计费属性配置节假日信息，即配置指定日期的费率类型为节假日。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1600。
- 系统支持对16个计费属性配置节假日。
- 每个计费属性支持100条节假日记录，总共支持配置1600条节假日信息。
- 对于特定计费属性，如果新增加的节假日和系统中已配置的节假日有重叠的现象，则会配置失败。
- 不允许配置的CCVALUE和掩码CCMASK取与后的值不等于CCVALUE。
- 当CCMASK变化时，不允许配置的CCVALUE和掩码CCMASK取与后的值，与当前已有配置的CCVALUE和对应的CCMASK取与后的值相等。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GLOBALFLG | 全局配置 | 可选必选说明：必选参数<br>参数含义：本参数用于指定全局配置属性。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- GLOBAL：指定计费属性为缺省全局计费属性。<br>- CHARGE_CHARACT：指定计费属性为配置的特殊计费属性值。<br>默认值：无<br>配置原则：无 |
| CCVALUE | 计费属性值 | 可选必选说明：条件必选参数<br>前提条件：该参数在“GLOBALFLG”配置为“CHARGE_CHARACT”时为必选参数。<br>参数含义：指定Charge Characteristic（计费属性）值。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～6。该参数为十六进制数据类型，仅支持输入0x/X、a-f/A-F 、0-9，允许不输入0x前缀，字母不区分大小写，取值范围0x0000~0xFFFF。<br>默认值：无<br>配置原则：不配置此参数时值默认为0。 |
| CCMASK | 计费属性掩码 | 可选必选说明：条件可选参数<br>前提条件：该参数在“GLOBALFLG”配置为“CHARGE_CHARACT”时为可选参数。<br>参数含义：指定Charge Characteristic掩码值。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～6。该参数为十六进制数据类型，仅支持输入0x/X、a-f/A-F 、0-9，允许不输入0x前缀，字母不区分大小写，取值范围0x0001~0xFFFF。<br>默认值：无<br>配置原则：无 |
| CCPRIORITY | 计费属性优先级 | 可选必选说明：条件可选参数<br>前提条件：该参数在“GLOBALFLG”配置为“CHARGE_CHARACT”时为可选参数。<br>参数含义：设置计费属性的优先级，不允许指定相同的优先级。配置CCMASK时必须指定优先级。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～65535。<br>默认值：无<br>配置原则：<br>- 当GLOBALFLG值为CHARGE_CHARACT时，优先级的初始值为0。<br>- 不配置此参数时值默认为0。 |
| YEAR | 节假日年份 | 可选必选说明：条件可选参数<br>前提条件：该参数在“GLOBALFLG”配置为“CHARGE_CHARACT” 或 “GLOBAL”时为可选参数。<br>参数含义：配置节假日年份。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为2000～2099。<br>默认值：无<br>配置原则：当GLOBALFLG值为CHARGE_CHARACT或GLOBAL时，初始值为0。 |
| MONTH | 节假日月份 | 可选必选说明：必选参数<br>参数含义：配置节假日月份。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～12。<br>默认值：无<br>配置原则：无 |
| DAY | 节假日日期 | 可选必选说明：必选参数<br>参数含义：配置节假日期。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～31。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/FESTIVAL]] · 计费节假日表（FESTIVAL）

## 使用实例

配置节假日信息，GLOBALFLG为CHARGE_CHARACT，CCVALUE为0x0100 ，CCMASK为0x0100，CCPRIORITY为2 ，YEAR为2015 ，MONTH为10，DAY为1，命令为：

```
ADD FESTIVAL:GLOBALFLG=CHARGE_CHARACT,CCVALUE="0x100",CCMASK="0x100",CCPRIORITY=2,YEAR=2015,MONTH=10,DAY=1;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加计费节假日表（ADD-FESTIVAL）_09896827.md`
