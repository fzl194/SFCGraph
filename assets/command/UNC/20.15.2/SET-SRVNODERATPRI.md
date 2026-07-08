---
id: UNC@20.15.2@MMLCommand@SET SRVNODERATPRI
type: MMLCommand
name: SET SRVNODERATPRI（设置获取RAT Type的优先级）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: SRVNODERATPRI
command_category: 配置类
applicable_nf:
- GGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 接入控制
- 获取RAT管理
- 获取RAT方式的优先级
status: active
---

# SET SRVNODERATPRI（设置获取RAT Type的优先级）

## 功能

**适用NF：GGSN**

该命令用来配置获取RAT Type的两种方式的优先级。其执行的结果是覆盖式的。使用该命令配置了优先级顺序后，系统就按照此顺序来获取RAT类型，若高优先级失败，则使用低优先级的获取方式。

## 注意事项

- 该命令执行后立即生效。

- 若系统中尚未配置获取RAT类型的优先级，则使用默认的优先级；若系统中已配置获取RAT类型的优先级，执行本命令则修改已配置的获取RAT类型的优先级。
- RAT类型第一优先级和RAT类型第二优先级不能相同。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| NODETYPE | FIRSTPRIORITY | SECONDPRIORITY |
| --- | --- | --- |
| GGSN | RAT | SGSN_IP |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NODETYPE | 网元类型 | 可选必选说明：必选参数<br>参数含义：该参数表示当前配置的网元类型。<br>数据来源：本端规划<br>取值范围：<br>- GGSN（GGSN）<br>默认值：无。<br>配置原则：无 |
| FIRSTPRIORITY | RAT类型的第一优先级 | 可选必选说明：可选参数<br>参数含义：该参数用于指定获取RAT类型的两种方式的第一优先级。<br>数据来源：全网规划<br>取值范围：<br>- “RAT（RAT）”：表示从信令面消息中获取RAT type。<br>- “SGSN_IP（SGSNIP）”：表示从ADD SRVNODERAT命令配置中获取RAT type。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SRVNODERATPRI查询当前参数配置值。<br>配置原则：无 |
| SECONDPRIORITY | RAT类型的第二优先级 | 可选必选说明：可选参数<br>参数含义：该参数用于指定获取RAT类型的两种方式的第二优先级。<br>数据来源：全网规划<br>取值范围：<br>- “RAT（RAT）”：表示从信令面消息中获取RAT type。<br>- “SGSN_IP（SGSNIP）”：表示从ADD SRVNODERAT命令配置中获取RAT type。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SRVNODERATPRI查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SRVNODERATPRI]] · 获取RAT Type的优先级（SRVNODERATPRI）

## 使用实例

当从信令面消息中获取RAT类型的优先级高于根据信令面IP地址匹配到RAT类型优先级时，配置获取RAT Type的两种方式的优先级为：RAT>SGSN_IP：

```
SET SRVNODERATPRI:NODETYPE=GGSN,FIRSTPRIORITY=RAT,SECONDPRIORITY=SGSN_IP;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-SRVNODERATPRI.md`
