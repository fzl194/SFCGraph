---
id: UNC@20.15.2@MMLCommand@ADD GLBDCCTEMPLATE
type: MMLCommand
name: ADD GLBDCCTEMPLATE（增加计费属性与在线计费模板绑定关系）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: GLBDCCTEMPLATE
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
max_records: 17
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 在线计费
- 信用控制
- 全局信用控制模板
status: active
---

# ADD GLBDCCTEMPLATE（增加计费属性与在线计费模板绑定关系）

## 功能

**适用NF：PGW-C、SMF**

该命令用于增加计费属性与在线计费模板的配置绑定关系。在线计费用户激活时会根据计费属性与在线计费模板绑定关系选择在线计费模板。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为17。
- 每个计费属性只能绑定一个在线计费模板。
- 计费属性的掩码和优先级参数必须同时配置。
- 用户激活时，如果用户携带的计费属性值与某记录中的计费属性掩码做与运算后，等于该记录中的计费属性值，则认为用户匹配到了该记录，会选择该记录绑定的在线计费模板。如果用户匹配记录失败，则使用缺省全局计费属性绑定的在线计费模板。
- 全局在线模板（DccTemplate名称为global）不允许绑定在计费属性下。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CHARGECHARACT | 计费属性 | 可选必选说明：必选参数<br>参数含义：该参数用于指定计费属性类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- GLOBAL：指定计费属性为缺省全局计费属性。<br>- CHARGE_CHARACT：指定计费属性为配置的特殊计费属性值。<br>默认值：无<br>配置原则：无 |
| SPECIFICCCVALUE | 计费属性值 | 可选必选说明：条件必选参数<br>前提条件：该参数在“CHARGECHARACT”配置为“CHARGE_CHARACT”时为必选参数。<br>参数含义：该参数用于指定特殊计费属性值。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～6。该参数为十六进制数据类型，仅支持输入0x/X、a-f/A-F 、0-9，允许不输入0x前缀，字母不区分大小写，取值范围0x0000~0xFFFF。<br>默认值：无<br>配置原则：无 |
| MASK | 计费属性掩码 | 可选必选说明：条件可选参数<br>前提条件：该参数在“CHARGECHARACT”配置为“CHARGE_CHARACT”时为可选参数。<br>参数含义：该参数用于指定计费属性的掩码。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～6。该参数为十六进制数据类型，仅支持输入0x/X、a-f/A-F 、0-9，允许不输入0x前缀，字母不区分大小写，取值范围0x0001~0xFFFF。<br>默认值：无<br>配置原则：配置的计费属性掩码计费属性值参数做与运算后，需要等于计费属性值，否则配置失败。 |
| PRIORITY | 优先级 | 可选必选说明：条件可选参数<br>前提条件：该参数在“CHARGECHARACT”配置为“CHARGE_CHARACT”时为可选参数。<br>参数含义：该参数用于指定计费属性的优先级。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～65535。<br>默认值：无<br>配置原则：不配置此参数时值默认为0。 |
| DCCTEMPLATENAME | 在线计费模板名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定在线计费模板名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：<br>- 该参数使用ADD DCCTEMPLATE命令配置生成。<br>- 配置该参数前，需要先使用ADD DCCTEMPLATE命令配置在线计费模板。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/GLBDCCTEMPLATE]] · 计费属性与在线计费模板绑定关系（GLBDCCTEMPLATE）

## 使用实例

如果希望计费属性为1314的用户使用在线计费模板dcc_normal，可以使用该命令为计费属性1314绑定在线计费模板dcc_normal：

```
ADD GLBDCCTEMPLATE:CHARGECHARACT=CHARGE_CHARACT,SPECIFICCCVALUE="0x1314",DCCTEMPLATENAME ="dcc_normal";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-GLBDCCTEMPLATE.md`
