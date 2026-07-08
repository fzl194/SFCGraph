---
id: UNC@20.15.2@MMLCommand@SET TRUSTEDWLANFUNC
type: MMLCommand
name: SET TRUSTEDWLANFUNC（设置可信Non-3GPP接入开关）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: TRUSTEDWLANFUNC
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
effect_mode: 对新用户生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 接入控制
- WLAN控制管理
status: active
---

# SET TRUSTEDWLANFUNC（设置可信Non-3GPP接入开关）

## 功能

**适用NF：PGW-C、SMF**

该命令用于设置可信Non-3GPP接入开关。

## 注意事项

- 该命令执行后只对新激活用户生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| ACCSW |
| --- |
| DISABLE |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ACCSW | 可信Non-3GPP接入开关 | 可选必选说明：可选参数<br>参数含义：本参数用于控制是否使能可信Non-3GPP接入功能。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE（不使能）<br>- ENABLE（使能）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST TRUSTEDWLANFUNC查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/TRUSTEDWLANFUNC]] · 可信Non-3GPP接入开关（TRUSTEDWLANFUNC）

## 使用实例

设置可信Non-3GPP接入开关：

```
SET TRUSTEDWLANFUNC: ACCSW=ENABLE;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置可信Non-3GPP接入开关（SET-TRUSTEDWLANFUNC）_78871396.md`
