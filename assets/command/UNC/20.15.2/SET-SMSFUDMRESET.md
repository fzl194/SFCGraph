---
id: UNC@20.15.2@MMLCommand@SET SMSFUDMRESET
type: MMLCommand
name: SET SMSFUDMRESET（设置UDM重选参数）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: SMSFUDMRESET
command_category: 配置类
applicable_nf:
- SMSF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- SMSF业务管理
- UDM重选管理
status: active
---

# SET SMSFUDMRESET（设置UDM重选参数）

## 功能

**适用NF：SMSF**

该命令用于设置SMSF的UDM重选参数信息。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| UDMRESETSWITCH | BYPRORATE | GETSUBSWITCH |
| --- | --- | --- |
| NO | 5 | NO |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| UDMRESETSWITCH | 是否触发扫描任务重选UDM | 可选必选说明：可选参数<br>参数含义：该参数表示是否触发SMSF扫描任务进行重选UDM。<br>数据来源：本端规划<br>取值范围：<br>- YES（是）<br>- NO（否）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SMSFUDMRESET查询当前参数配置值。<br>配置原则：无 |
| BYPRORATE | UDM重选扫描速率(个/秒) | 可选必选说明：可选参数<br>参数含义：该参数表示SMSF重选UDM时的扫描速率。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~1000，单位是个每秒。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SMSFUDMRESET查询当前参数配置值。<br>配置原则：无 |
| GETSUBSWITCH | UDM重选时是否重新获取签约数据 | 可选必选说明：可选参数<br>参数含义：该参数表示SMSF重选UDM时是否向其重新获取签约数据。<br>数据来源：本端规划<br>取值范围：<br>- YES（是）<br>- NO（否）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SMSFUDMRESET查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [SMSF的UDM重选（SMSFUDMRESET）](configobject/UNC/20.15.2/SMSFUDMRESET.md)

## 使用实例

如果运营商希望SMSF网元在UDM故障时支持其重选来保障SMSF业务正常，可以执行如下命令：

```
SET SMSFUDMRESET: UDMRESETSWITCH=YES;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置UDM重选参数（SET-SMSFUDMRESET）_46573525.md`
