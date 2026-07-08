---
id: UNC@20.15.2@MMLCommand@RMV RDSACCTATTTEMP
type: MMLCommand
name: RMV RDSACCTATTTEMP（删除计费消息属性模板）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: RDSACCTATTTEMP
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- RADIUS管理
- RADIUS计费管理
- RADIUS计费信元模板
status: active
---

# RMV RDSACCTATTTEMP（删除计费消息属性模板）

## 功能

**适用NF：PGW-C、SMF**

该命令用来删除计费消息属性模板。

## 注意事项

- 该命令执行后立即生效。
- 若该模板已被RADIUS抄送服务器绑定，则无法删除。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ATTRTEMPNAME | 计费消息属性模板名字 | 可选必选说明：必选参数<br>参数含义：该参数用于指定计费消息属性模板名字。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@RDSACCTATTTEMP]] · 计费消息属性模板（RDSACCTATTTEMP）

## 使用实例

删除名为“RDSACCTATTTEMP”的计费消息属性模板：

```
RMV RDSACCTATTTEMP: ATTRTEMPNAME="RDSACCTATTTEMP";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-RDSACCTATTTEMP.md`
