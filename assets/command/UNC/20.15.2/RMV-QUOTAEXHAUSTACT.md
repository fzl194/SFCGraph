---
id: UNC@20.15.2@MMLCommand@RMV QUOTAEXHAUSTACT
type: MMLCommand
name: RMV QUOTAEXHAUSTACT（删除配额耗尽后的动作）
nf: UNC
version: 20.15.2
verb: RMV
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

# RMV QUOTAEXHAUSTACT（删除配额耗尽后的动作）

## 功能

**适用NF：PGW-C、SMF**

该命令用于删除在线RG配额耗尽后的动作。

## 注意事项

该命令执行后只对新激活用户生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CCTMPLTNAME | 融合计费模板名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定融合计费模板的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。不区分大小写。<br>默认值：无<br>配置原则：<br>该参数使用<br>[**ADD CCT**](../融合计费模板/增加融合计费模板（ADD CCT）_09653176.md)<br>命令配置生成。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@QUOTAEXHAUSTACT]] · 配额耗尽后的动作（QUOTAEXHAUSTACT）

## 使用实例

删除融合计费模板名为global的在线RG配额耗尽后动作为阻塞业务：

```
RMV QUOTAEXHAUSTACT: CCTMPLTNAME="global";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-QUOTAEXHAUSTACT.md`
