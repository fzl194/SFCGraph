---
id: UDG@20.15.2@MMLCommand@RMV SAMUTEPROTOCOL
type: MMLCommand
name: RMV SAMUTEPROTOCOL（删除SA EGN规则不启用协议）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: SAMUTEPROTOCOL
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 协议识别
- 特征库管理
- SA EGN规则生效控制
status: active
---

# RMV SAMUTEPROTOCOL（删除SA EGN规则不启用协议）

## 功能

**适用NF：PGW-U、UPF、GGSN**

该命令用于恢复指定SA EGN协议规则。

## 注意事项

该命令执行后60s生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROTOCOLNAME | 协议名称 | 可选必选说明：必选参数<br>参数含义：SA EGN规则不启用的协议。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：数据源为系统支持识别的所有类型的子协议，可以通过工程命令smctrldsp protocol-list查询。 |

## 操作的配置对象

- [SA EGN规则不启用协议（SAMUTEPROTOCOL）](configobject/UDG/20.15.2/SAMUTEPROTOCOL.md)

## 使用实例

恢复socks5协议规则：

```
RMV SAMUTEPROTOCOL:PROTOCOLNAME="socks5";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除SA-EGN规则不启用协议（RMV-SAMUTEPROTOCOL）_69450618.md`
