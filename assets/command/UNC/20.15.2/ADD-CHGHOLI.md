---
id: UNC@20.15.2@MMLCommand@ADD CHGHOLI
type: MMLCommand
name: ADD CHGHOLI（增加节假日配置）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: CHGHOLI
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 计费管理
- 计费节假日配置
status: active
---

# ADD CHGHOLI（增加节假日配置）

## 功能

**适用网元：SGSN**

该命令用于配置普通计费属性用户、预付费计费属性用户、包月制计费属性用户或实时计费属性用户的节假日。该命令的配置是为了实现对S-CDR话单进行不同费率时段的计费。该命令与费率时段配置（ [**ADD CHGTARI**](../计费费率时段配置/增加费率时段配置(ADD CHGTARI)_26305208.md) ）相结合，进行灵活的费率时段控制。

## 注意事项

- 该命令执行后立即生效。
- 同一计费属性的节假日总数不能超过50，本表记录总数不能超过200。
- 在节假日配置表中，“年”、“月”、“日”和“计费属性”唯一确定一条记录。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| YEAR | 年 | 可选必选说明：必选参数<br>参数含义：该参数用于指定节假日所属的年份。<br>数据来源：整网规划<br>取值范围：1998～2099<br>默认值：无 |
| MONTH | 月 | 可选必选说明：必选参数<br>参数含义：该参数用于指定节假日所属的月份。<br>数据来源：整网规划<br>取值范围： 1～12<br>默认值：无 |
| DAY | 日 | 可选必选说明：必选参数<br>参数含义：该参数用于指定节假日所属的日期。<br>数据来源：整网规划<br>取值范围：1～31<br>默认值：无 |
| CC | 计费属性 | 可选必选说明：必选参数<br>参数含义：该参数用于指定该节假日是对普通计费属性用户、预付费计费属性用户、包月制计费属性用户还是对实时计费属性用户有效。<br>数据来源：整网规划<br>取值范围：<br>- “NORMAL(普通计费)”<br>- “PREPAID(预付费)”<br>- “FLATRATE(包月制)”<br>- “HOTBILLING(实时计费)”<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/CHGHOLI]] · 节假日配置（CHGHOLI）

## 关联任务

- [[UNC@20.15.2@Task@0-00019]]

## 使用实例

增加一条预付费计费属性的节假日配置：2001年5月1日，配置格式为：

ADD CHGHOLI: YEAR=2001, MONTH=5, DAY=1, CC=PREPAID;

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加节假日配置(ADD-CHGHOLI)_26145382.md`
