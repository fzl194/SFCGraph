---
id: UDG@20.15.2@MMLCommand@RMV SRVTLSPLY
type: MMLCommand
name: RMV SRVTLSPLY（删除TLS认证策略）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: SRVTLSPLY
command_category: 配置类
applicable_nf:
- UPF
- PGW-U
effect_mode: 对新流生效
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 媒体中继
- TLS认证策略
status: active
---

# RMV SRVTLSPLY（删除TLS认证策略）

## 功能

**适用NF：UPF、PGW-U**

该命令用于删除TLS认证策略。

## 注意事项

该命令执行后对新数据流生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PLYNAME | 策略名称 | 可选必选说明：必选参数<br>参数含义：该参数用于设置TLS认证策略描述。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~31。不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/SRVTLSPLY]] · TLS认证策略（SRVTLSPLY）

## 使用实例

删除TLS认证策略：

```
RMV SRVTLSPLY: PLYNAME="ply1";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-SRVTLSPLY.md`
