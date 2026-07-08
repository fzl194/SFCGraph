---
id: UNC@20.15.2@MMLCommand@RMV SCTPENDPOINT
type: MMLCommand
name: RMV SCTPENDPOINT（删除SCTP端点）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: SCTPENDPOINT
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 计费和策略接口管理
- SCTP管理
- SCTP端点
status: active
---

# RMV SCTPENDPOINT（删除SCTP端点）

## 功能

**适用NF：PGW-C、SMF**

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

- [[UNC@20.15.2@ConfigObject@SCTPENDPOINT]] · SCTP端点（SCTPENDPOINT）

## 使用实例

根据网络规划，需要删除一个SCTP端点，则可以按如下配置：

```
RMV SCTPENDPOINT: ENDPOINTNAME="sctp_ep1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-SCTPENDPOINT.md`
