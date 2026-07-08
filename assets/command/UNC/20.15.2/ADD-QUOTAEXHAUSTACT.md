---
id: UNC@20.15.2@MMLCommand@ADD QUOTAEXHAUSTACT
type: MMLCommand
name: ADD QUOTAEXHAUSTACT（增加配额耗尽后的动作）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: QUOTAEXHAUSTACT
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
effect_mode: 对新用户生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 融合计费
- 配额耗尽处理动作
status: active
---

# ADD QUOTAEXHAUSTACT（增加配额耗尽后的动作）

## 功能

**适用NF：PGW-C、SMF**

该命令用于增加在线RG配额耗尽后的动作。

## 注意事项

- 该命令执行后只对新激活用户生效。

- 最多可输入101条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CCTMPLTNAME | 融合计费模板名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定融合计费模板的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。不区分大小写。<br>默认值：无<br>配置原则：<br>该参数使用<br>[**ADD CCT**](../融合计费模板/增加融合计费模板（ADD CCT）_09653176.md)<br>命令配置生成。 |
| ACTION | 在线RG配额耗尽后动作 | 可选必选说明：可选参数<br>参数含义：该参数用于指定在线RG配置耗尽后动作。<br>数据来源：本端规划<br>取值范围：不配置此参数时值默认为0，表示不下发在线RG配额耗尽后动作。<br>- “BLOCK（阻塞业务，使业务不能继续进行）”：阻塞业务，使业务不能继续进行。<br>- “REDIRECT（将当前业务重定向到指定的地址）”：将当前业务重定向到指定的地址。<br>- “FORWARD（允许继续转发业务）”：允许继续转发业务。<br>默认值：无<br>配置原则：<br>不配置此参数时值默认为0，表示不下发在线RG配置耗尽后动作。 |
| RDVIRTIP | 重定向IPv4地址 | 可选必选说明：该参数在"ACTION"配置为"REDIRECT"时为条件可选参数。<br>参数含义：该参数用于指定在线RG配额耗尽后重定向动作的IPv4地址。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：<br>不配置此参数时值默认为0.0.0.0。 |
| RDVIRTIPV6 | 重定向IPv6地址 | 可选必选说明：该参数在"ACTION"配置为"REDIRECT"时为条件可选参数。<br>参数含义：该参数用于指定在线RG配额耗尽后重定向动作的IPv6地址。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：<br>不配置此参数时值默认为::。 |

## 操作的配置对象

- [配额耗尽后的动作（QUOTAEXHAUSTACT）](configobject/UNC/20.15.2/QUOTAEXHAUSTACT.md)

## 使用实例

增加融合计费模板名为global的在线RG配额耗尽后动作为阻塞业务：

```
ADD QUOTAEXHAUSTACT: CCTMPLTNAME="global", ACTION=BLOCK;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加配额耗尽后的动作（ADD-QUOTAEXHAUSTACT）_95129686.md`
