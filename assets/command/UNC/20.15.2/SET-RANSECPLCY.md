---
id: UNC@20.15.2@MMLCommand@SET RANSECPLCY
type: MMLCommand
name: SET RANSECPLCY（设置RAN侧安全策略）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: RANSECPLCY
command_category: 配置类
applicable_nf:
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 会话协议参数管理
- 会话策略管理
- 5GC用户面安全策略管理
status: active
---

# SET RANSECPLCY（设置RAN侧安全策略）

## 功能

**适用NF：SMF**

该命令用来配置RAN侧用户面安全策略。策略用于明确是否需要对RAN侧用户面进行完整性保护和加密保护。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| UPINTEGRPLCY | UPINTEGRTIND | UPINTEGPDUPLCY | UPCONFIDPLCY | UPCONFIDIND |
| --- | --- | --- | --- | --- |
| SUBFIRST | PREFERRED | REDUCE | SUBFIRST | PREFERRED |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| UPINTEGRPLCY | 完整性保护策略 | 可选必选说明：可选参数<br>参数含义：该参数用于指定RAN侧用户面完整性保护策略。<br>数据来源：全网规划<br>取值范围：<br>- “SUBFIRST（优先从签约数据获取）”：优先从签约数据获取是否要RAN侧执行用户面保护策略，如果签约不提供该策略，则从本地配置获取。本地配置由参数UPINTEGRTIND和UPCONFIDIND指示。<br>- “LOCAL（从本地配置获取）”：根据本地配置的参数UPINTEGRTIND和UPCONFIDIND来指示RAN侧是否要执行用户面保护策略。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST RANSECPLCY查询当前参数配置值。<br>配置原则：无 |
| UPINTEGRTIND | 本地完整性保护指示 | 可选必选说明：可选参数<br>参数含义：该参数是本地配置，用于指示RAN侧是否要执行用户面完整性保护策略。<br>数据来源：全网规划<br>取值范围：<br>- “REQUIRED（需要）”：RAN侧需要执行该用户面保护。<br>- “PREFERRED（优选）”：RAN侧如果支持该用户面保护，则需要执行。<br>- “NOTNEEDED（不需要）”：RAN侧不需要执行该用户面保护。<br>- “NOTCARRY（不携带）”：本地不携带该用户面保护策略。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST RANSECPLCY查询当前参数配置值。<br>配置原则：<br>当“本地完整性保护指示”参数配置为NOTCARRY时，“本地加密保护指示”参数也建议配置为NOTCARRY。如果一个配置为NOTCARRY，另一个不为NOTCARRY时，另一个会被当做NOTCARRY处理。 |
| UPINTEGPDUPLCY | 完整性保护PDU策略 | 可选必选说明：可选参数<br>参数含义：该参数用于指定完整性保护指示为“REQUIRED”，但是会话AMBR大于UE支持的完整性保护最大速率时的处理策略。<br>数据来源：全网规划<br>取值范围：<br>- “DONOTHING（不做处理）”：保持会话AMBR大于UE支持的完整性保护最大速率。<br>- “CORRECT（纠正）”：将RAN侧需要执行用户面完整性保护纠正为RAN侧如果支持用户面完整性保护才执行。<br>- “REDUCE（限速）”：将会话AMBR降低至UE支持的完整性保护最大速率。<br>- “REJECT（拒绝）”：拒绝会话建立或者删除会话。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST RANSECPLCY查询当前参数配置值。<br>配置原则：无 |
| UPCONFIDPLCY | 加密保护策略 | 可选必选说明：可选参数<br>参数含义：该参数用于指定RAN侧用户面加密保护策略。<br>数据来源：全网规划<br>取值范围：<br>- “SUBFIRST（优先从签约数据获取）”：优先从签约数据获取是否要RAN侧执行用户面保护策略，如果签约不提供该策略，则从本地配置获取。本地配置由参数UPINTEGRTIND和UPCONFIDIND指示。<br>- “LOCAL（从本地配置获取）”：根据本地配置的参数UPINTEGRTIND和UPCONFIDIND来指示RAN侧是否要执行用户面保护策略。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST RANSECPLCY查询当前参数配置值。<br>配置原则：无 |
| UPCONFIDIND | 本地加密保护指示 | 可选必选说明：可选参数<br>参数含义：该参数是本地配置，用于指示RAN侧是否要执行用户面加密保护策略。<br>数据来源：全网规划<br>取值范围：<br>- “REQUIRED（需要）”：RAN侧需要执行该用户面保护。<br>- “PREFERRED（优选）”：RAN侧如果支持该用户面保护，则需要执行。<br>- “NOTNEEDED（不需要）”：RAN侧不需要执行该用户面保护。<br>- “NOTCARRY（不携带）”：本地不携带该用户面保护策略。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST RANSECPLCY查询当前参数配置值。<br>配置原则：<br>当“本地加密保护指示”参数配置为NOTCARRY时，“本地完整性保护指示”参数也建议配置为NOTCARRY。如果一个配置为NOTCARRY，另一个不为NOTCARRY时，另一个会被当做NOTCARRY处理。 |

## 操作的配置对象

- [RAN侧安全策略（RANSECPLCY）](configobject/UNC/20.15.2/RANSECPLCY.md)

## 使用实例

当用户需要配置全局无线侧安全策略参数为签约优先时，进行如下设置：

```
SET RANSECPLCY:UPINTEGRPLCY=SUBFIRST,UPINTEGRTIND=PREFERRED,UPINTEGPDUPLCY=REDUCE,UPCONFIDPLCY=SUBFIRST,UPCONFIDIND=PREFERRED;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置RAN侧安全策略（SET-RANSECPLCY）_09652638.md`
