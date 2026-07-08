---
id: UNC@20.15.2@MMLCommand@SET SMSFKEYCHECK
type: MMLCommand
name: SET SMSFKEYCHECK（设置SMSF用户关键信息数据核查扫描参数）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: SMSFKEYCHECK
command_category: 配置类
applicable_nf:
- SMSF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- SMSF业务管理
- 热备容灾
status: active
---

# SET SMSFKEYCHECK（设置SMSF用户关键信息数据核查扫描参数）

## 功能

**适用NF：SMSF**

该命令用于设置SMSF用户关键信息数据核查扫描速率和周期，以及数据有效时长。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| KEYCHECKSW | KEYCHECKRATE | KEYCHECKPERIOD | VALIDTIMESW | VALIDTIME |
| --- | --- | --- | --- | --- |
| FUNC_ON | 70 | 60 | FUNC_ON | 1440 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| KEYCHECKSW | SMSF用户关键信息表核查功能开关 | 可选必选说明：可选参数<br>参数含义：该参数用于表示SMSF用户关键信息核查功能开关。<br>数据来源：本端规划<br>取值范围：<br>- “FUNC_ON（打开）”：功能开关打开<br>- “FUNC_OFF（关闭）”：功能开关关闭<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SMSFKEYCHECK查询当前参数配置值。<br>配置原则：无 |
| KEYCHECKRATE | SMSF用户关键信息核查速率(个每秒) | 可选必选说明：可选参数<br>参数含义：该参数用于表示SMSF用户关键信息核查时的扫描速率。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~1000，单位是个每秒。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SMSFKEYCHECK查询当前参数配置值。<br>配置原则：无 |
| KEYCHECKPERIOD | SMSF用户关键信息核查周期(分钟) | 可选必选说明：可选参数<br>参数含义：该参数用于表示SMSF用户关键信息核查扫描周期。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~1440，单位是分钟。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SMSFKEYCHECK查询当前参数配置值。<br>配置原则：无 |
| VALIDTIMESW | SMSF用户关键信息有效时长开关 | 可选必选说明：可选参数<br>参数含义：该参数用于表示SMSF用户关键信息有效时长生效开关。<br>数据来源：本端规划<br>取值范围：<br>- “FUNC_ON（打开）”：功能开关打开<br>- “FUNC_OFF（关闭）”：功能开关关闭<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SMSFKEYCHECK查询当前参数配置值。<br>配置原则：无 |
| VALIDTIME | SMSF上用户关键信息数据的有效时长(分钟) | 可选必选说明：可选参数<br>参数含义：该参数用于表示SMSF上用户关键信息数据的有效时长。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~43200，单位是分钟。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SMSFKEYCHECK查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SMSFKEYCHECK]] · SMSF用户关键信息数据核查扫描参数（SMSFKEYCHECK）

## 使用实例

运营商希望设置“SMSF用户关键信息表核查功能开关”为“打开”，“SMSF用户关键信息核查速率(个每秒)”为“70”，“SMSF用户关键信息核查周期(分钟)”为“60”，“SMSF用户关键信息有效时长开关”为“打开”，“SMSF上用户关键信息数据的有效时长(分钟)”为“1440”，执行如下命令：

```
SET SMSFKEYCHECK: KEYCHECKSW=FUNC_ON, KEYCHECKRATE=70, KEYCHECKPERIOD=60, VALIDTIMESW=FUNC_ON, VALIDTIME=1440;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-SMSFKEYCHECK.md`
