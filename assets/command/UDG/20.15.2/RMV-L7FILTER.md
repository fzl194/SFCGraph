---
id: UDG@20.15.2@MMLCommand@RMV L7FILTER
type: MMLCommand
name: RMV L7FILTER（删除七层过滤器）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: L7FILTER
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务匹配策略
- 业务过滤器管理
- 七层规则管理
- 七层过滤器
status: active
---

# RMV L7FILTER（删除七层过滤器）

## 功能

**适用NF：PGW-U、UPF**

此命令用于删除七层过滤器或子七层过滤器，支持批量删除所有的七层过滤器或指定七层过滤器下的所有子七层过滤器。当配置量较大时单次执行可能无法删除全部记录，需要多次执行。

## 注意事项

- 该命令执行后60s生效。
- 如果引用了该L7Filter的ProtBindFlowF的记录存在，则不允许删除该L7Filter实例。
- 如果该SubL7Filter绑定的L7Filter中还绑定了其他的SubL7Filter，即使该L7Filter被PROTBINDFLOWF绑定，这个SubL7Filter也允许被删除。
- 如果指定SUBL7FLTNAME参数，必须先指定L7FILTERNAME参数。
- 如果执行超时失败，需要重新执行，否则会存在部分记录未删除。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| L7FILTERNAME | 七层过滤器名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置L7Filter名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不区分大小写。<br>默认值：无<br>配置原则：无 |
| SUBL7FLTNAME | 子七层过滤器名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置该L7Filter的子七层过滤器名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/L7FILTER]] · 七层过滤器（L7FILTER）

## 使用实例

假设运营商需要删除一个七层过滤器中的某一个子七层过滤器。 删除七层过滤器中的子七层过滤器：

```
RMV L7FILTER: L7FILTERNAME="testl7filtername",SUBL7FLTNAME="testsubl7filtername";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除七层过滤器（RMV-L7FILTER）_82837399.md`
