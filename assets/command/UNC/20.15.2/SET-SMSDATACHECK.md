---
id: UNC@20.15.2@MMLCommand@SET SMSDATACHECK
type: MMLCommand
name: SET SMSDATACHECK（设置数据核查扫描参数）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: SMSDATACHECK
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

# SET SMSDATACHECK（设置数据核查扫描参数）

## 功能

**适用NF：SMSF**

该命令用于设置SMSF数据核查时的扫描速率和周期，以及SMSF数据有效时长。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| DATACHECKRATE | DATACHECKPERIOD | VALIDTIMESW | VALIDTIME | UDMDATACHECKSW |
| --- | --- | --- | --- | --- |
| 5 | 30 | FUNC_OFF | 24 | FUNC_ON |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DATACHECKRATE | sms数据核查速率(个每秒) | 可选必选说明：可选参数<br>参数含义：该参数用于表示sms数据核查时的扫描速率。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~1000，单位是个每秒。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SMSDATACHECK查询当前参数配置值。<br>配置原则：无 |
| DATACHECKPERIOD | sms数据核查周期(分钟) | 可选必选说明：可选参数<br>参数含义：该参数用于表示sms数据核查扫描周期。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~1440，单位是分钟。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SMSDATACHECK查询当前参数配置值。<br>配置原则：无 |
| VALIDTIMESW | SMSF数据有效时长开关 | 可选必选说明：可选参数<br>参数含义：该参数用于表示SMSF数据有效时长生效开关。<br>数据来源：本端规划<br>取值范围：<br>- “FUNC_ON（打开）”：功能开关打开<br>- “FUNC_OFF（关闭）”：功能开关关闭<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SMSDATACHECK查询当前参数配置值。<br>配置原则：<br>如果需要将长期不进行业务的用户从SMSF注销， 或数据核查时需要将超过SMSF向注册中心注册更新的时间间隔的用户在注册中心的信息进行更新，需要打开该开关。 |
| VALIDTIME | SMSF上用户数据的有效时长(小时) | 可选必选说明：可选参数<br>参数含义：该参数用于表示SMSF上用户数据的有效时长。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~720，单位是小时。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SMSDATACHECK查询当前参数配置值。<br>配置原则：无 |
| UDMDATACHECKSW | UDM数据核查开关 | 可选必选说明：可选参数<br>参数含义：该参数用于表示是否开启SMSF向UDM进行数据核查功能。<br>数据来源：本端规划<br>取值范围：<br>- “FUNC_ON（打开）”：功能开关打开<br>- “FUNC_OFF（关闭）”：功能开关关闭<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SMSDATACHECK查询当前参数配置值。<br>配置原则：<br>当需要开启SMSF向UDM进行数据核查功能时，需要先执行SET COMMONSOFTPARAOFBIT命令设置软参DWORD16中BIT3的取值为“1”。 |

## 操作的配置对象

- [数据核查扫描参数（SMSDATACHECK）](configobject/UNC/20.15.2/SMSDATACHECK.md)

## 使用实例

运营商希望设置SMSF数据核查扫描速率、核查周期，以及设置用户数据有效性时长及开关，执行如下命令：

```
SET SMSDATACHECK: DATACHECKRATE=5, DATACHECKPERIOD=30, VALIDTIMESW=FUNC_ON, VALIDTIME=48, UDMDATACHECKSW=FUNC_ON;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置数据核查扫描参数（SET-SMSDATACHECK）_64343919.md`
