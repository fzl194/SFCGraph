---
id: UDG@20.15.2@MMLCommand@SET MSSTBMFILTER
type: MMLCommand
name: SET MSSTBMFILTER（设置MSS表项开关过滤规则）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: MSSTBMFILTER
command_category: 配置类
effect_mode: 立即生效
is_dangerous: true
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- MSS
- 表项管理统计查询
status: active
---

# SET MSSTBMFILTER（设置MSS表项开关过滤规则）

## 功能

![](设置MSS表项开关过滤规则（SET MSSTBMFILTER）_50281626.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，操作不当会导致性能下降，请谨慎使用并联系华为技术支持协助操作。

该命令用于设置过滤规则，是诊断开关命令；通过开关设置过滤规则，记录指定表项的刷表轨迹，协助问题定位；用户打开开关后对下表性能有影响，2小时后会自动关闭。

## 注意事项

- 该命令执行后立即生效。
- 本命令用于开启TBM过滤规则开关，开启后会降低性能。开关将在2小时后自动关闭。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：必选参数<br>参数含义：该参数用于表示的RU名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，区分大小写。<br>默认值：无<br>配置原则：使用DSP RU查看RU名称。 |
| ENABLE | 开关使能 | 可选必选说明：必选参数<br>参数含义：该参数用于表示开关使能。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- FALSE：关闭。<br>- TRUE：打开。<br>默认值：无 |
| TABLEID | 表ID | 可选必选说明：条件可选参数<br>前提条件：该参数在“ENABLE”配置为“TRUE”时为可选参数。<br>参数含义：该参数用于表示表ID。如果不设置该参数，则表示匹配所有的表ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无 |
| TABLETYPE | 表项类型 | 可选必选说明：条件可选参数<br>前提条件：该参数在“ENABLE”配置为“TRUE”时为可选参数。<br>参数含义：该参数用于表示表类型。如果不设置该参数，则表示匹配所有的表类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- linear：线性表。<br>- hash：哈希表。<br>- fib4：FIB4表。<br>- fib6：FIB6表。<br>- invalid：无效表类型。<br>默认值：无 |
| LINEARINDEX | 线性索引值 | 可选必选说明：条件必选参数<br>前提条件：该参数在“TABLETYPE”配置为“linear”时为必选参数。<br>参数含义：该参数用于表示线性索引值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无 |
| HASHKEY | 哈希关键字 | 可选必选说明：条件必选参数<br>前提条件：该参数在“TABLETYPE”配置为“hash”时为必选参数。<br>参数含义：该参数用于表示哈希关键字值。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～256。十六进制字符。<br>默认值：无 |
| VPNID | 虚拟专用网号 | 可选必选说明：条件必选参数<br>前提条件：该参数在“TABLETYPE”配置为“fib4” 或 “fib6”时为必选参数。<br>参数含义：该参数用于表示虚拟专用网号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无 |
| IPV4 | IPv4地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“TABLETYPE”配置为“fib4”时为必选参数。<br>参数含义：该参数用于表示IPv4地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无 |
| IPV4MASK | IPv4掩码长度 | 可选必选说明：条件必选参数<br>前提条件：该参数在“TABLETYPE”配置为“fib4”时为必选参数。<br>参数含义：该参数用于表示IPv4掩码长度。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～32。<br>默认值：无 |
| IPV6 | IPv6地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“TABLETYPE”配置为“fib6”时为必选参数。<br>参数含义：该参数用于表示IPv6地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。<br>默认值：无 |
| IPV6MASK | IPv6掩码长度 | 可选必选说明：条件必选参数<br>前提条件：该参数在“TABLETYPE”配置为“fib6”时为必选参数。<br>参数含义：该参数用于表示IPv6掩码长度。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～128。<br>默认值：无 |

## 操作的配置对象

- [MSS表项开关过滤状态（MSSTBMFILTER）](configobject/UDG/20.15.2/MSSTBMFILTER.md)

## 使用实例

设置表过滤规则：

```
SET MSSTBMFILTER:RUNAME="VNODE_VNRS_VNFC_IPU_0064",ENABLE=TRUE,TABLETYPE=linear, LINEARINDEX=1;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置MSS表项开关过滤规则（SET-MSSTBMFILTER）_50281626.md`
