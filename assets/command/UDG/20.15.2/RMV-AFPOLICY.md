---
id: UDG@20.15.2@MMLCommand@RMV AFPOLICY
type: MMLCommand
name: RMV AFPOLICY（删除防欺诈策略配置）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: AFPOLICY
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 业务防欺诈
- 防欺诈策略
status: active
---

# RMV AFPOLICY（删除防欺诈策略配置）

## 功能

**适用NF：PGW-U、UPF**

该命令用于删除判断出欺诈行为后的处理策略。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| AFPOLICYTYPE | 防欺诈策略类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定防欺诈策略类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DNS：指定DNS防欺诈。<br>- HTTP：指定HTTP防欺诈。<br>- HTTPS：指定HTTPS防欺诈。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/AFPOLICY]] · 防欺诈策略配置（AFPOLICY）

## 使用实例

如果运营商要删除在判断出DNS欺诈行为后处理策略，则配置命令如下：

```
RMV AFPOLICY:AFPOLICYTYPE=DNS;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-AFPOLICY.md`
