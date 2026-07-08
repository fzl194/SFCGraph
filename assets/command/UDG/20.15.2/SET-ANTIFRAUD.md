---
id: UDG@20.15.2@MMLCommand@SET ANTIFRAUD
type: MMLCommand
name: SET ANTIFRAUD（设置防欺诈配置）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: ANTIFRAUD
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 对新用户生效
is_dangerous: false
max_records: 1
category_path:
- 用户面服务管理
- 业务防欺诈
- 防欺诈参数
status: active
---

# SET ANTIFRAUD（设置防欺诈配置）

## 功能

**适用NF：PGW-U、UPF**

此命令用于配置当前系统的防欺诈相关参数，当用户需要开启或关闭防欺诈的相关配置时使用。包括DNS防欺诈开关、FUI防欺诈开关及HTTP防欺诈开关的开启状态。

## 注意事项

- 该命令执行后只对新激活用户生效。
- 该命令最大记录数为1。
- 启发式DNS防欺诈仅对之后发生承载更新的用户或者新激活用户生效，空记录和文本记录DNS防欺诈对未获取策略的业务流即时生效。
- 使用本命令时，对性能会产生一定影响。
- 该命令会导致用户匹配数发生变化，可能导致性能下降。执行命令前请评估对性能的影响，如果无法评估请联系华为技术支持。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | ISNULLRECEN | ISTEXTEN | ISHEURISTICEN | FUIAFSWITCH | HTTPAFSWITCH | URLREDAFSWITCH |
| --- | --- | --- | --- | --- | --- | --- |
| 初始值 | DISABLE | DISABLE | DISABLE | ENABLE | DISABLE | DISABLE |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ISNULLRECEN | 空记录DNS防欺诈开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定DNS空记录防欺诈开关。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能（关闭）。<br>- ENABLE：使能（开启）。<br>默认值：无<br>配置原则：<br>- 为了防止伪装DNS报文进行虚假计费，需要开启DNS空记录防欺诈开关。<br>- 如果运营商不希望开启DNS空记录防欺诈功能，则需要将此参数设为DISABLE。 |
| ISTEXTEN | 文本记录DNS防欺诈开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定DNS文本记录防欺诈开关。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能（关闭）。<br>- ENABLE：使能（开启）。<br>默认值：无<br>配置原则：<br>- 为了防止伪装DNS报文进行虚假计费，需要开启文本记录DNS防欺诈开关。<br>- 如果运营商不希望开启DNS文本记录防欺诈功能，则需要将此参数设为DISABLE。 |
| ISHEURISTICEN | 启发式DNS防欺诈开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定DNS启发式防欺诈开关。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能（关闭）。<br>- ENABLE：使能（开启）。<br>默认值：无<br>配置原则：<br>- 为了防止伪装DNS报文进行虚假计费，需要开启启发式DNS防欺诈开关。<br>- 如果运营商不希望开启DNS启发式防欺诈功能，则需要将此参数设为DISABLE。 |
| FUIAFSWITCH | FUI防欺诈开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定FUI防欺诈开关。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能（关闭）。<br>- ENABLE：使能（开启）。<br>默认值：无<br>配置原则：<br>- 为了防止伪装报文进行FUI重定向到充值页面从而实现虚假计费，需要开启FUI防欺诈开关。<br>- 如果运营商不希望开启FUI防欺诈功能，则需要将此参数设为DISABLE。 |
| HTTPAFSWITCH | HTTP防欺诈总开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定HTTP防欺诈开关。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能（关闭）。<br>- ENABLE：使能（开启）。<br>默认值：无<br>配置原则：<br>- 为了防止伪装HTTP报文进行虚假计费，需要开启HTTP防欺诈总开关。<br>- 如果运营商不希望开启HTTP防欺诈功能，则需要将此参数设为DISABLE。 |
| URLREDAFSWITCH | URL重定向防欺诈开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定URL重定向防欺诈开关。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能（关闭）。<br>- ENABLE：使能（开启）。<br>默认值：无<br>配置原则：<br>- 为了防止利用URL重定向来伪装报文进行虚假计费，需要开启URL重定向防欺诈开关。<br>- 如果运营商不希望开启URL重定向防欺诈功能，则需要将此参数设为DISABLE。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/ANTIFRAUD]] · 防欺诈配置（ANTIFRAUD）

## 使用实例

假如运营商需要开启DNS空记录防欺诈功能，关闭DNS启发式防欺诈功能，则配置命令如下：

```
SET ANTIFRAUD:ISNULLRECEN=ENABLE,ISHEURISTICEN=DISABLE;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置防欺诈配置（SET-ANTIFRAUD）_82837792.md`
