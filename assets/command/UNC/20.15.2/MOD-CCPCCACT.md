---
id: UNC@20.15.2@MMLCommand@MOD CCPCCACT
type: MMLCommand
name: MOD CCPCCACT（修改融合计费Proxy基于CC处理动作）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: CCPCCACT
command_category: 配置类
applicable_nf:
- NCG
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- NCG业务及策略管理
- 融合计费Proxy基于CC处理动作
status: active
---

# MOD CCPCCACT（修改融合计费Proxy基于CC处理动作）

## 功能

**适用NF：NCG**

该命令用于修改融合计费Proxy基于CC处理动作。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CCTYPE | CC类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定CC的类型。<br>数据来源：本端规划<br>取值范围：<br>- DEFAULT（针对未指定的CC设置处理动作）<br>- VALUE（针对CC设置处理动作）<br>默认值：无<br>配置原则：无 |
| CHGCHAR | 指定计费属性值 | 可选必选说明：该参数在"CCTYPE"配置为"VALUE"时为条件必选参数。<br>参数含义：该参数用于指定计费属性的值。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~6。十六进制数据类型，仅支持输入0x/X、a-f/A-F 、0-9，允许不输入0x前缀，字母不区分大小写，取值范围0x0000~0xFFFF。<br>默认值：无<br>配置原则：无 |
| CHGCHARMASK | 指定计费属性掩码 | 可选必选说明：该参数在"CCTYPE"配置为"VALUE"时为条件可选参数。<br>参数含义：该参数用于指定计费属性的掩码。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~6。十六进制数据类型，仅支持输入0x/X、a-f/A-F 、0-9，允许不输入0x前缀，字母不区分大小写，取值范围0x0000~0xFFFF。<br>默认值：无<br>配置原则：无 |
| FWDOCSENABLE | 是否转发OCS | 可选必选说明：可选参数<br>参数含义：该参数用于设置是否转发OCS。<br>数据来源：本端规划<br>取值范围：<br>- TRUE(TRUE)<br>- FALSE(FALSE)<br>默认值：无<br>配置原则：无 |
| FOTNM | Failover模板标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定融合计费Proxy Failover模板的名称，FOTNM参数来源是ADD CCPFOT:FOTNM。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~32。<br>默认值：无<br>配置原则：无 |
| GENCHGDATAREF | 是否生成计费数据标识 | 可选必选说明：可选参数<br>参数含义：该参数用于设置是否生成数据计费标识(ChargingDataRef)。<br>数据来源：本端规划<br>取值范围：<br>- TRUE(TRUE)<br>- FALSE(FALSE)<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [融合计费Proxy基于CC处理动作（CCPCCACT）](configobject/UNC/20.15.2/CCPCCACT.md)

## 使用实例

修改指定计费属性值为“0x1234”的融合计费Proxy基于CC处理动作，设置计费属性掩码为“0x4567”：

```
MOD CCPCCACT: CCTYPE=VALUE, CHGCHAR="0x1234", CHGCHARMASK="0x4567";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改融合计费Proxy基于CC处理动作（MOD-CCPCCACT）_45110924.md`
