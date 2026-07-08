---
id: UNC@20.15.2@MMLCommand@RMV NRA
type: MMLCommand
name: RMV NRA（删除空路由区对照表）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: NRA
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 电路域联合业务
- 空路由区信息
status: active
---

# RMV NRA（删除空路由区对照表）

## 功能

![](删除空路由区对照表(RMV NRA)_26145418.assets/notice_3.0-zh-cn_2.png)

删除空路由区配置表记录后有可能会降低电路域寻呼的成功率。

**适用网元：SGSN**

该命令用于删除空路由区配置表。对每个存在不支持GPRS业务的小区的位置区，SGSN将属于该位置区的所有不支持GPRS业务的小区组成称之为NULL RA。配置此命令后，在2.5G/3G手机的电路域寻呼流程中，系统除了寻呼支持GPRS业务的路由区，还会寻呼空路由区表内的路由区，从而提高电路域寻呼的成功率。同一位置区下，只能有一个NULL RA，NULL RA与普通RA的编码格式相同。

## 注意事项

- 该命令执行后立即生效。
- 删除空路由区配置表记录后有可能会降低电路域寻呼的成功率。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LAI | LAI | 可选必选说明：必选参数<br>参数含义：该参数用于指定待删除空路由区所在的位置区。“LAI”由“MCC”、“MNC”和“LAC”共同构成。<br>数据来源：整网规划<br>取值范围：9～10位字符串<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NRA]] · 空路由区对照表（NRA）

## 使用实例

删除位置区123002233的空路由区记录：

RMV NRA: LAI="123002233";

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-NRA.md`
