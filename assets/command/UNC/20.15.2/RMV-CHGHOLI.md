---
id: UNC@20.15.2@MMLCommand@RMV CHGHOLI
type: MMLCommand
name: RMV CHGHOLI（删除节假日配置）
nf: UNC
version: 20.15.2
verb: RMV
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

# RMV CHGHOLI（删除节假日配置）

## 功能

**适用网元：SGSN**

该命令用来表示在节假日配置表中删除一条节假日配置。

## 注意事项

- “年”、“月”、“日”和“计费属性”确定某一条节假日记录。
- 该命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| YEAR | 年 | 可选必选说明：必选参数<br>参数含义：该参数用于表示此参数是节假日所属的年份。<br>取值范围：1998～2099<br>默认值：无 |
| MONTH | 月 | 可选必选说明：必选参数<br>参数含义：该参数用于表示此参数是节假日所属的月份。<br>取值范围：1～12<br>默认值：无 |
| DAY | 日 | 可选必选说明：必选参数<br>参数含义：该参数用于表示此参数是节假日所属的日期。<br>取值范围：1～31<br>默认值：无 |
| CC | 计费属性 | 可选必选说明：必选参数<br>参数含义：该参数用于表示“计费属性”是该节假日是对普通计费属性用户、预付费计费属性用户、包月制计费属性用户还是对实时计费属性用户有效。<br>取值范围：<br>- “NORMAL(普通计费)”<br>- “PREPAID(预付费)”<br>- “FLATRATE(包月制)”<br>- “HOTBILLING(实时计费)”<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/CHGHOLI]] · 节假日配置（CHGHOLI）

## 使用实例

删除一条普通计费属性的节假日配置：2001年5月1日，配置格式为：

RMV CHGHOLI: YEAR=2001, MONTH=5, DAY=1, CC=NORMAL;

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除节假日配置(RMV-CHGHOLI)_72225063.md`
