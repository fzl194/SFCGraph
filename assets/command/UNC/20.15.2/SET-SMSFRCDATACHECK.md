---
id: UNC@20.15.2@MMLCommand@SET SMSFRCDATACHECK
type: MMLCommand
name: SET SMSFRCDATACHECK（设置SMSF核查注册中心状态功能）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: SMSFRCDATACHECK
command_category: 配置类
applicable_nf:
- SMSF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- SMSF业务管理
- 数据核查
status: active
---

# SET SMSFRCDATACHECK（设置SMSF核查注册中心状态功能）

## 功能

**适用NF：SMSF**

该命令用于设置SMSF核查注册中心状态功能，运营商可以根据需要设置核查功能的开关，每秒核查条目，核查周期等信息。

## 注意事项

- 该命令执行后立即生效。

- 双活组网的场景下，如果需要配置此命令，则两个SMSF上均需执行此命令，且配置参数一致。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| DATACHECKSW | DATACHECKRATE | DATACHECKPERIOD |
| --- | --- | --- |
| FUNC_OFF | 5 | 30 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DATACHECKSW | SMSF核查注册中心状态功能开关 | 可选必选说明：可选参数<br>参数含义：该参数用于表示是否开启SMSF对注册中心状态的核查功能。<br>数据来源：本端规划<br>取值范围：<br>- “FUNC_ON（打开）”：功能开关打开<br>- “FUNC_OFF（关闭）”：功能开关关闭<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SMSFRCDATACHECK查询当前参数配置值。<br>配置原则：<br>当需要开启SMSF对注册中心状态的核查功能时，需要先执行SET COMMONSOFTPARAOFBIT命令设置软参DWORD16中BIT3的取值为“1”。 |
| DATACHECKRATE | 每秒钟SMSF核查注册中心状态的条数(个每秒) | 可选必选说明：可选参数<br>参数含义：该参数用于表示每秒钟SMSF核查注册中心状态的条数。该参数暂不生效。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~1000，单位是个每秒。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SMSFRCDATACHECK查询当前参数配置值。<br>配置原则：无 |
| DATACHECKPERIOD | SMSF核查注册中心状态周期(分钟) | 可选必选说明：可选参数<br>参数含义：该参数用于表示SMSF核查注册中心状态周期。该参数暂不生效。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~1440，单位是分钟。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SMSFRCDATACHECK查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SMSFRCDATACHECK]] · SMSF核查注册中心状态功能配置（SMSFRCDATACHECK）

## 使用实例

运营商希望设置“SMSF核查注册中心状态功能开关”为“打开”，“每秒钟SMSF核查注册中心状态的条数(个每秒)”为“5”，“SMSF核查注册中心状态周期(分钟)”为“5”，执行如下命令：

```
SET SMSFRCDATACHECK: DATACHECKSW=FUNC_ON, DATACHECKRATE=5, DATACHECKPERIOD=5;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置SMSF核查注册中心状态功能（SET-SMSFRCDATACHECK）_04041281.md`
