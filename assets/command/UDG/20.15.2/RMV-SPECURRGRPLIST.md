---
id: UDG@20.15.2@MMLCommand@RMV SPECURRGRPLIST
type: MMLCommand
name: RMV SPECURRGRPLIST（删除特殊URR组列表）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: SPECURRGRPLIST
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 计费控制
- 特殊使用率上报规则组列表
status: active
---

# RMV SPECURRGRPLIST（删除特殊URR组列表）

## 功能

**适用NF：PGW-U、UPF**

该命令用于根据输入删除特殊URR组列表配置。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| URRGROUPNAME | URR组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于设置特殊使用量上报规则组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@SPECURRGRPLIST]] · 特殊URR组列表（SPECURRGRPLIST）

## 使用实例

删除已经配置的特殊URR组列表：

```
RMV SPECURRGRPLIST: URRGROUPNAME="cp_token";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-SPECURRGRPLIST.md`
