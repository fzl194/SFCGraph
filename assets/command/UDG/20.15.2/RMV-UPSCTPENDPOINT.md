---
id: UDG@20.15.2@MMLCommand@RMV UPSCTPENDPOINT
type: MMLCommand
name: RMV UPSCTPENDPOINT（删除SCTP端点）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: UPSCTPENDPOINT
command_category: 配置类
applicable_nf:
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- SCTP管理
- SCTP端点
status: active
---

# RMV UPSCTPENDPOINT（删除SCTP端点）

## 功能

**适用NF：UPF**

此命令用于删除SCTP端点信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ENDPOINTNAME | 端点名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定SCTP端点名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/UPSCTPENDPOINT]] · SCTP端点（UPSCTPENDPOINT）

## 使用实例

根据网络规划，需要删除一个SCTP端点，则可以按如下配置：

```
RMV UPSCTPENDPOINT: ENDPOINTNAME="sctp_ep1";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除SCTP端点（RMV-UPSCTPENDPOINT）_97314589.md`
