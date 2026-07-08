---
id: UDG@20.15.2@MMLCommand@RMV PUBCFGDOMAIN
type: MMLCommand
name: RMV PUBCFGDOMAIN（删除公共配置域名称）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: PUBCFGDOMAIN
command_category: 配置类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 业务运维
- 集中配置管理
- 公共配置域管理
status: active
---

# RMV PUBCFGDOMAIN（删除公共配置域名称）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

本命令用于将网元从某一配置域中删除。配置域也称之为集中配置管理组。

## 注意事项

- 该命令执行后立即生效。
- 当网元中有配置在引用该域，则该域无法删除。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CFGDOMAINNAME | 域名称 | 可选必选说明：必选参数<br>参数含义：配置域名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@PUBCFGDOMAIN]] · 公共配置域名称（PUBCFGDOMAIN）

## 使用实例

将网元从名为domain_a的域中删除：

```
RMV PUBCFGDOMAIN: CFGDOMAINNAME="domain_a";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-PUBCFGDOMAIN.md`
