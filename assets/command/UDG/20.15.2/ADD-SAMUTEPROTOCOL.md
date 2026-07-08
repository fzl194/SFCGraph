---
id: UDG@20.15.2@MMLCommand@ADD SAMUTEPROTOCOL
type: MMLCommand
name: ADD SAMUTEPROTOCOL（增加SA EGN规则不启用协议）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: SAMUTEPROTOCOL
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
- GGSN
effect_mode: ''
is_dangerous: true
max_records: 256
category_path:
- 用户面服务管理
- 协议识别
- 特征库管理
- SA EGN规则生效控制
status: active
---

# ADD SAMUTEPROTOCOL（增加SA EGN规则不启用协议）

## 功能

**适用NF：PGW-U、UPF、GGSN**

![](增加SA EGN规则不启用协议（ADD SAMUTEPROTOCOL）_69212198.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，该命令用于设置指定SA EGN协议规则（如socks5）不启用。一般用于该规则不适用时，通过配置关闭。

该命令用于设置指定SA EGN协议规则不启用。一般用于该规则不适用时，通过配置关闭。

## 注意事项

- 该命令执行后60s生效。
- 该命令最大记录数为256。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROTOCOLNAME | 协议名称 | 可选必选说明：必选参数<br>参数含义：SA EGN规则不启用的协议。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：数据源为系统支持识别的所有类型的子协议，可以通过工程命令smctrldsp protocol-list查询。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/SAMUTEPROTOCOL]] · SA EGN规则不启用协议（SAMUTEPROTOCOL）

## 使用实例

关闭socks5协议规则：

```
ADD SAMUTEPROTOCOL:PROTOCOLNAME="socks5";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/ADD-SAMUTEPROTOCOL.md`
