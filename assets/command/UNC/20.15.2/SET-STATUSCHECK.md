---
id: UNC@20.15.2@MMLCommand@SET STATUSCHECK
type: MMLCommand
name: SET STATUSCHECK（设置状态核查参数）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: STATUSCHECK
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 可靠性管理
- 微服务可靠性管理
status: active
---

# SET STATUSCHECK（设置状态核查参数）

## 功能

当前版本配置此命令不生效。

该命令用于设置状态核查开关和核查周期。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| SWITCH | CYCLE |
| --- | --- |
| ON | 30 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SWITCH | 状态核查开关 | 可选必选说明：必选参数<br>参数含义：该命令用于设置状态核查开关。<br>数据来源：本端规划<br>取值范围：<br>- “ON（开启）”：状态核查开关打开<br>- “OFF（关闭）”：状态核查开关关闭<br>默认值：无。<br>配置原则：无 |
| CYCLE | 状态核查周期(分钟) | 可选必选说明：该参数在"SWITCH"配置为"ON"时为条件必选参数。<br>参数含义：该命令用于设置状态核查周期。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是10~4294967295，单位是分钟。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST STATUSCHECK查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [状态核查参数（STATUSCHECK）](configobject/UNC/20.15.2/STATUSCHECK.md)

## 使用实例

- 配置状态核查开关为开启，周期为50，即每50分钟进行状态核查。
  ```
  SET STATUSCHECK: SWITCH=ON, CYCLE=50;
  ```
- 配置状态核查开关为关闭，即不进行状态核查。
  ```
  SET STATUSCHECK: SWITCH=OFF;
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置状态核查参数（SET-STATUSCHECK）_50456771.md`
