---
id: UNC@20.15.2@MMLCommand@SET CACHEPLCY
type: MMLCommand
name: SET CACHEPLCY（设置缓存策略）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: CACHEPLCY
command_category: 配置类
applicable_nf:
- AMF
- SMF
- SMSF
- NCG
- NSSF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 服务化接口管理
- 注册与服务发现
- NF Cache管理
status: active
---

# SET CACHEPLCY（设置缓存策略）

## 功能

**适用NF：AMF、SMF、SMSF、NCG、NSSF**

该命令用于设置缓存策略。

## 注意事项

- 该命令执行后立即生效。

- 当缓存策略从其他模式切换到非白名单禁止模式时，不在白名单中的异网NF缓存数据将被删除。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| CACHEPOLICY | AGINGTIME |
| --- | --- |
| ALLCACHE | 600 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CACHEPOLICY | 缓存策略 | 可选必选说明：必选参数<br>参数含义：该参数用于设置缓存策略。<br>数据来源：本端规划<br>取值范围：<br>- “FORBIDDEN（非白名单禁止模式）”：不允许不在白名单中的异网NF数据缓存（白名单在CACHEWHITELST中配置）。<br>- “BESTEFFORT（非白名单尽力而为模式）”：未达到缓存规格上限时（缓存规格在CACHESPECS中配置），允许缓存不在白名单中的异网NF数据（白名单在CACHEWHITELST中配置）。<br>- “ALLCACHE（全部缓存模式）”：允许缓存所有NF数据。<br>默认值：无。<br>配置原则：<br>当缓存规格充足时，建议配置全部缓存模式；当缓存规格不足时，建议配置非白名单尽力而为模式；当异网NF数据异常时，建议配置非白名单禁止模式。 |
| AGINGTIME | 快速老化时间(秒) | 可选必选说明：该参数在"CACHEPOLICY"配置为"BESTEFFORT"时为条件可选参数。<br>参数含义：该参数用于指定快速老化时间。当缓存策略选择“非白名单尽力而为模式”，且缓存规格达到上限时，持续未被发现时间达到快速老化时间的不在白名单中的异网NF数据将会从缓存中删除。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~4294967295。目前该参数最小值为300秒（5分钟），最大值为259200秒（72小时）。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CACHEPLCY查询当前参数配置值。<br>配置原则：<br>当缓存策略选择“非白名单尽力而为模式”时可配置。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@CACHEPLCY]] · 缓存策略（CACHEPLCY）

## 使用实例

设置缓存策略为全部缓存模式。

```
SET CACHEPLCY: CACHEPOLICY=ALLCACHE;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-CACHEPLCY.md`
