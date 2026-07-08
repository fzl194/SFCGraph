---
id: UNC@20.15.2@MMLCommand@SET IPALLOCBYLOCSW
type: MMLCommand
name: SET IPALLOCBYLOCSW（设置基于位置区地址分配的开关）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: IPALLOCBYLOCSW
command_category: 配置类
applicable_nf:
- PGW-C
- GGSN
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- UE地址管理
- UE地址池管理
- 基于位置区地址分配开关配置
status: active
---

# SET IPALLOCBYLOCSW（设置基于位置区地址分配的开关）

## 功能

**适用NF：PGW-C、GGSN、SMF**

该命令用于设置基于位置区地址分配开关。

## 注意事项

- 该命令执行后立即生效。

- “开关”为“INHERIT”时，按照基于位置区组地址分配的全局开关的配置进行地址分配，不为“INHERIT”时，按照基于位置区组地址分配的开关配置进行地址分配。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LOCATIONGRPTYPE | 位置区组类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定位置区组类型。<br>数据来源：本端规划<br>取值范围：<br>- LAC（LAC）<br>- TAC（TAC）<br>默认值：无。<br>配置原则：<br>- 配置类型为TAC，LOCATIONGRPNAME必须由ADD ADDRTACGROUP新增。<br>- 配置类型为LAC，LOCATIONGRPNAME必须由ADD ADDRLACGROUP新增。 |
| LOCATIONGRPNAME | 位置区组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于标识位置区组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~32。<br>默认值：无。<br>配置原则：<br>该参数使用ADD ADDRTACGROUP或ADD ADDRLACGROUP命令配置生成。 |
| SWITCH | IPv4开关 | 可选必选说明：必选参数<br>参数含义：该参数用于指定基于位置区分配IPv4地址的开关。<br>数据来源：本端规划<br>取值范围：<br>- “DISABLE（去使能）”：不使用UPF所在的群组标识作为地址分配规则的匹配条件。<br>- “INHERIT（继承）”：继承SET IPALLOCBYUPFGLBSW命令的“基于UPF地址分配的全局开关”。<br>- “ENABLE（使能）”：使用UPF所在的群组标识作为地址分配规则的匹配条件。<br>默认值：无。<br>配置原则：无 |
| IPV6SWITCH | IPv6开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定基于位置区分配IPv6地址的开关。<br>数据来源：本端规划<br>取值范围：<br>- “DISABLE（去使能）”：不使用UPF所在的群组标识作为地址分配规则的匹配条件。<br>- “INHERIT（继承）”：继承SET IPALLOCBYUPFGLBSW命令的“基于UPF地址分配的全局开关”。<br>- “ENABLE（使能）”：使用UPF所在的群组标识作为地址分配规则的匹配条件。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST IPALLOCBYLOCSW查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/IPALLOCBYLOCSW]] · 基于位置区地址分配的开关（IPALLOCBYLOCSW）

## 使用实例

禁止名为tac1的TAC-Group基于位置区地址分配：

```
SET IPALLOCBYLOCSW: LOCATIONGRPTYPE=TAC, LOCATIONGRPNAME="tac1", SWITCH=DISABLE, IPV6SWITCH=DISABLE;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置基于位置区地址分配的开关（SET-IPALLOCBYLOCSW）_49644934.md`
