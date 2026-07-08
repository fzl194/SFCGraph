---
id: UNC@20.15.2@MMLCommand@RMV LACGROUP
type: MMLCommand
name: RMV LACGROUP（删除LAC组）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: LACGROUP
command_category: 配置类
applicable_nf:
- GGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 虚拟APN映射管理
- 基于LAC位置的虚拟APN映射管理
- 虚拟APN映射的LAC组
status: active
---

# RMV LACGROUP（删除LAC组）

## 功能

**适用NF：GGSN**

该命令用来删除指定的LAC组。当LAC组下绑定LAC号段时，同时可以删除该LAC组下的所有绑定的LAC号段。

## 注意事项

- 该命令执行后立即生效。

- 当LAC组被作为映射规则在ADD VIRTUALAPNRULE命令中配置的时候，如果需要删除这个LAC组，需要先使用RMV VIRTUALAPNRULE命令解除该LAC组对应的所有虚拟APN映射关系，再删除该LAC组，否则删除命令执行失败。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LACGROUPNAME | LAC组名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定TAC组名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~32。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@LACGROUP]] · LAC组（LACGROUP）

## 使用实例

假设运营商需要去删除一个本地已经配置的“LAC组名”为“beijing”的LAC组：

```
RMV LACGROUP:LACGROUPNAME="beijing";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-LACGROUP.md`
