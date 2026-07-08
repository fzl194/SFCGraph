---
id: UNC@20.15.2@MMLCommand@MOD HOMEGROUP
type: MMLCommand
name: MOD HOMEGROUP（修改Home Group）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: HOMEGROUP
command_category: 配置类
applicable_nf:
- PGW-C
- GGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- GGSN和P-GW Proxy
- Home Group
status: active
---

# MOD HOMEGROUP（修改Home Group）

## 功能

**适用NF：PGW-C、GGSN**

该命令用于修改Home Group的优先级、绑定的IMSI/MSISDN号码段组和计费特征组。

## 注意事项

- 该命令执行后立即生效。

- IMSIMSISDNGRPNAME和CCGROUPNAME两个参数必须至少有一个有效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| HOMEGROUPINDX | Home Group编号 | 可选必选说明：必选参数<br>参数含义：该参数用于设置Home Group的编号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~128。<br>默认值：无<br>配置原则：无 |
| HOMEGROUPPRI | Home Group优先级 | 可选必选说明：可选参数<br>参数含义：该参数用于设置Home Group的优先级。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~65535。值越小优先级越高。<br>默认值：无<br>配置原则：无 |
| IMSIMSISDNSW | 选择IMSI/MSISDN组开关 | 可选必选说明：可选参数<br>参数含义：该参数用于控制选择IMSI/MSISDN组。<br>数据来源：本端规划<br>取值范围：<br>- ENABLE（选择IMSI/MSISDN组）<br>- DISABLE（不选择IMSI/MSISDN号段组）<br>默认值：无<br>配置原则：无 |
| IMSIMSISDNGRPNM | Home Group绑定的用户号码段组名 | 可选必选说明：该参数在"IMSIMSISDNSW"配置为"ENABLE"时为条件必选参数。<br>参数含义：该参数用于设置Home Group绑定的IMSI/MSISDN号码段组名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~31。<br>默认值：无<br>配置原则：<br>该参数使用ADD PRIMSIMSISDNG命令配置生成。 |
| CCGROUPSW | 选择计费属性组 | 可选必选说明：可选参数<br>参数含义：该参数用于控制选择计费策略组。<br>数据来源：本端规划<br>取值范围：<br>- ENABLE（选择计费属性组）<br>- DISABLE（不选择计费属性组）<br>默认值：无<br>配置原则：无 |
| CCGROUPNAME | 计费特征组名称 | 可选必选说明：该参数在"CCGROUPSW"配置为"ENABLE"时为条件必选参数。<br>参数含义：该参数用于设置Home Group绑定的计费特征组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~31。<br>默认值：无<br>配置原则：<br>该参数使用ADD CCGROUP命令配置生成。 |
| MULTIDNNSW | 2B2C漫游双DNN特性功能开关 | 可选必选说明：可选参数<br>参数含义：该参数用于HOMEGROUP支持2B2C漫游双DNN特性功能。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE（不使能）<br>- ENABLE（使能）<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [Home Group（HOMEGROUP）](configobject/UNC/20.15.2/HOMEGROUP.md)

## 使用实例

修改“Home Group编号”为“1”的Home Group配置的“选择计费属性组”为“不选择计费属性组”：

```
MOD HOMEGROUP: HOMEGROUPINDX=1, HOMEGROUPPRI=65535, IMSIMSISDNSW=ENABLE, IMSIMSISDNGRPNM="group1", CCGROUPSW=DISABLE;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改Home-Group（MOD-HOMEGROUP）_42693474.md`
