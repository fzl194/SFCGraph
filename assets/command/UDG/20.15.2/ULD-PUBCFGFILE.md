---
id: UDG@20.15.2@MMLCommand@ULD PUBCFGFILE
type: MMLCommand
name: ULD PUBCFGFILE（上传绑定配置域信息）
nf: UDG
version: 20.15.2
verb: ULD
object_keyword: PUBCFGFILE
command_category: 调测类
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
- 公共命令配置域信息管理
status: active
---

# ULD PUBCFGFILE（上传绑定配置域信息）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

本命令用于将某一域的配置文件上传至FileServer。

## 注意事项

- 该命令执行后立即生效。
- 若执行该命令时与上次域核查之间有配置变动，则无法上传文件，需要重新核查之后才能上传。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| FILEPATH | CfgDomainName | 可选必选说明：必选参数<br>参数含义：FilePath。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/PUBCFGFILE]] · 上传绑定配置域信息（PUBCFGFILE）

## 使用实例

将域名为domain_a的配置文件上传到FileServer：

```
ULD PUBCFGFILE: FILEPATH="domain_a";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/上传绑定配置域信息（ULD-PUBCFGFILE）_68425110.md`
