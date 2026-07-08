---
id: UNC@20.15.2@MMLCommand@SET N4CHGMSGCTRL
type: MMLCommand
name: SET N4CHGMSGCTRL（设置N4接口计费消息相关控制参数）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: N4CHGMSGCTRL
command_category: 配置类
applicable_nf:
- SMF
- PGW-C
- GGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 融合计费
- 全局配置
status: active
---

# SET N4CHGMSGCTRL（设置N4接口计费消息相关控制参数）

## 功能

**适用NF：SMF、PGW-C、GGSN**

该命令用于配置N4接口计费消息相关控制参数。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| MSGCACHEEPDSW | CACHEFULLACT |
| --- | --- |
| DISABLE | TERMINATE |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MSGCACHEEPDSW | 消息缓存池扩展开关 | 可选必选说明：可选参数<br>参数含义：该参数用于控制单个会话的N4计费消息缓存池满时（20条消息），是否扩展消息缓存池规格到40条消息，最多支持100个会话进行扩展。如果该会话已缓存的N4计费消息中存在丢中间消息时，该会话不可以扩展。<br>数据来源：本端规划<br>取值范围：<br>- “DISABLE（不使能）”：关闭消息缓存池扩展功能。<br>- “ENABLE（使能）”：开启消息缓存池扩展功能。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST N4CHGMSGCTRL查询当前参数配置值。<br>配置原则：无 |
| CACHEFULLACT | 缓存池满的动作 | 可选必选说明：可选参数<br>参数含义：该参数用于控制单个会话的N4计费消息缓存池满时动作。该参数配置为Continue时，如果FAILHANDLING配置（或CHF下发）的动作不是CONTINUE，该参数不生效，按TERMINATE处理。如果此时已出现丢包，按去激活处理。<br>数据来源：本端规划<br>取值范围：<br>- “CONTINUE（允许业务继续进行）”：允许业务继续进行，不再进行配额管理。<br>- “TERMINATE（去活会话）”：去活PDU会话。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST N4CHGMSGCTRL查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/N4CHGMSGCTRL]] · N4接口计费消息相关控制参数（N4CHGMSGCTRL）

## 使用实例

配置N4接口计费消息相关控制参数消息缓存池扩展功能使能、缓存池满的动作为用户转离线：

```
SET N4CHGMSGCTRL: 
MSGCACHEEPDSW=ENABLE,
CACHEFULLACT=CONTINUE;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-N4CHGMSGCTRL.md`
