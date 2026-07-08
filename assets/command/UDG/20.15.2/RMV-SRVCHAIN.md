---
id: UDG@20.15.2@MMLCommand@RMV SRVCHAIN
type: MMLCommand
name: RMV SRVCHAIN（删除业务链）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: SRVCHAIN
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- SFIP管理
- 业务链配置
status: active
---

# RMV SRVCHAIN（删除业务链）

## 功能

**适用NF：PGW-U、UPF**

该命令用于删除业务链配置。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SRVCHAINNAME | 业务链名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置业务链名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [业务链（SRVCHAIN）](configobject/UDG/20.15.2/SRVCHAIN.md)

## 使用实例

如果运营商想要删除业务链名称为TestSrvChain的业务链配置。命令如下：

```
RMV SRVCHAIN:SRVCHAINNAME="TestSrvChain";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除业务链（RMV-SRVCHAIN）_42287013.md`
