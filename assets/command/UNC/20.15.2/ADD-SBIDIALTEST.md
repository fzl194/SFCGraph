---
id: UNC@20.15.2@MMLCommand@ADD SBIDIALTEST
type: MMLCommand
name: ADD SBIDIALTEST（增加间接路由拨测用户配置）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: SBIDIALTEST
command_category: 配置类
applicable_nf:
- SMF
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 服务化接口管理
- 拨测管理
status: active
---

# ADD SBIDIALTEST（增加间接路由拨测用户配置）

## 功能

**适用NF：SMF、AMF**

该命令暂未生效。

## 注意事项

- 该命令执行后立即生效。

- 相同拨测用户范围的两条记录的拨测用户范围不可以重叠。
- 该命令的匹配拨测用户的方式为全匹配。
- 该命令每条记录配置的拨测用户数不大于100。

- 最多可输入80条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| USERRANGE | 用户标识类型 | 可选必选说明：必选参数<br>参数含义：该参数用于配置拨测用户范围。<br>数据来源：本端规划<br>取值范围：<br>- SUPI（SUPI）<br>- GPSI（GPSI）<br>默认值：无<br>配置原则：无 |
| BEGINSUPI | 起始SUPI | 可选必选说明：该参数在"USERRANGE"配置为"SUPI"时为条件必选参数。<br>参数含义：该参数用于配置拨测用户的起始SUPI。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是5~15。<br>默认值：无<br>配置原则：无 |
| ENDSUPI | 终止SUPI | 可选必选说明：该参数在"USERRANGE"配置为"SUPI"时为条件必选参数。<br>参数含义：该参数用于配置拨测用户的终止SUPI。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是5~15。<br>默认值：无<br>配置原则：无 |
| BEGINGPSI | 起始GPSI | 可选必选说明：该参数在"USERRANGE"配置为"GPSI"时为条件必选参数。<br>参数含义：该参数用于配置拨测用户的起始GPSI的。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是5~15。<br>默认值：无<br>配置原则：无 |
| ENDGPSI | 终止GPSI | 可选必选说明：该参数在"USERRANGE"配置为"GPSI"时为条件必选参数。<br>参数含义：该参数用于配置拨测用户的终止GPSI的。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是5~15。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [间接路由拨测用户配置（SBIDIALTEST）](configobject/UNC/20.15.2/SBIDIALTEST.md)

## 使用实例

增加一条拨测用户配置，UserRange类型为SUPI，待拨测用着SUPI长度为15位，用户范围为123450000000000~123460000000000。

```
ADD SBIDIALTEST: USERRANGE=SUPI, BEGINSUPI="123450000000000", ENDSUPI="123460000000000";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加间接路由拨测用户配置（ADD-SBIDIALTEST）_06510925.md`
