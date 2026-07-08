---
id: UNC@20.15.2@MMLCommand@RMV N40MSGTEMP
type: MMLCommand
name: RMV N40MSGTEMP（删除N40消息属性模板）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: N40MSGTEMP
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 融合计费
- N40消息属性模板
status: active
---

# RMV N40MSGTEMP（删除N40消息属性模板）

## 功能

**适用NF：PGW-C、SMF**

该命令用于删除N40消息属性模板。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TEMPLATENAME | N40消息属性模板名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定N40消息字段模板名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@N40MSGTEMP]] · N40消息属性模板（N40MSGTEMP）

## 使用实例

删除名为“n40attr”的N40消息属性模板：

```
RMV N40MSGTEMP: TEMPLATENAME="n40attr";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-N40MSGTEMP.md`
