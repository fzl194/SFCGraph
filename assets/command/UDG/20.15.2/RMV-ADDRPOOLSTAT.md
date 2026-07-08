---
id: UDG@20.15.2@MMLCommand@RMV ADDRPOOLSTAT
type: MMLCommand
name: RMV ADDRPOOLSTAT（删除地址池统计配置）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: ADDRPOOLSTAT
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 业务运维
- 业务性能统计管理
- 地址池统计配置
status: active
---

# RMV ADDRPOOLSTAT（删除地址池统计配置）

## 功能

**适用NF：PGW-U、UPF**

该命令用于删除已经配置的地址池性能统计对象。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POOLSTATNAME | 地址池统计名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定地址池统计配置的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～79。由“_”、“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/ADDRPOOLSTAT]] · 地址池统计配置（ADDRPOOLSTAT）

## 使用实例

删除配置名称为“stat1”的地址池性能统计对象：

```
RMV ADDRPOOLSTAT: POOLSTATNAME="stat1";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除地址池统计配置（RMV-ADDRPOOLSTAT）_26921002.md`
