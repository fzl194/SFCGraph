---
id: UNC@20.15.2@MMLCommand@RMV OFCSRVTEMPLATE
type: MMLCommand
name: RMV OFCSRVTEMPLATE（删除离线业务模板）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: OFCSRVTEMPLATE
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
- 离线计费
- 业务级计费
- 业务计费模板
status: active
---

# RMV OFCSRVTEMPLATE（删除离线业务模板）

## 功能

**适用NF：PGW-C、SMF**

该命令用来删除离线业务模板的配置。

## 注意事项

- 该命令执行后立即生效。
- 该命令只对新业务生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TEMPLATENAME | 离线业务模板名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定离线业务模板名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不允许输入空格。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@OFCSRVTEMPLATE]] · 离线业务模板（OFCSRVTEMPLATE）

## 使用实例

删除名为“offlinetmp”的离线业务模板：

```
RMV OFCSRVTEMPLATE:TEMPLATENAME="offlinetmp";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-OFCSRVTEMPLATE.md`
