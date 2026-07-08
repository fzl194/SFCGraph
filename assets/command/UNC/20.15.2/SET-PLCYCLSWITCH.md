---
id: UNC@20.15.2@MMLCommand@SET PLCYCLSWITCH
type: MMLCommand
name: SET PLCYCLSWITCH（设置冗余策略老化开关）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: PLCYCLSWITCH
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 服务通信管理
- 策略核查管理
status: active
---

# SET PLCYCLSWITCH（设置冗余策略老化开关）

## 功能

该命令用于设置冗余策略老化开关。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| SWITCH | AGINGTIMES |
| --- | --- |
| ON | 60 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SWITCH | 冗余策略老化开关 | 可选必选说明：必选参数<br>参数含义：该参数用于指示是否开启冗余策略老化。<br>数据来源：本端规划<br>取值范围：<br>- OFF（关闭）<br>- ON（打开）<br>默认值：无。<br>配置原则：无 |
| AGINGTIMES | 老化阈值 | 可选必选说明：该参数在"SWITCH"配置为"ON"时为条件必选参数。<br>参数含义：该参数用于设置老化阈值，单位：次数。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是3~9223372036854775807。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST PLCYCLSWITCH查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PLCYCLSWITCH]] · 冗余策略老化开关（PLCYCLSWITCH）

## 使用实例

设置冗余策略老化开关，ON表示开启，OFF表示关闭。

```
%%SET PLCYCLSWITCH: SWITCH=OFF;%%
RETCODE = 0  操作成功

---    结束
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置冗余策略老化开关（SET-PLCYCLSWITCH）_98081184.md`
