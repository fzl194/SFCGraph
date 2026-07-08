---
id: UNC@20.15.2@MMLCommand@RMV SCTPTEMPLATE
type: MMLCommand
name: RMV SCTPTEMPLATE（删除SCTP模板）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: SCTPTEMPLATE
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 计费和策略接口管理
- SCTP管理
- SCTP模板
status: active
---

# RMV SCTPTEMPLATE（删除SCTP模板）

## 功能

**适用NF：PGW-C、SMF**

此命令用于删除SCTP模板，根据现网规划，当UNC不需要使用SCTP承载逻辑接口信令时，可以使用此命令删除SCTP模板。

## 注意事项

命令执行后对新建立的SCTP链路生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SCTPTEMPLNAME | SCTP模板名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定SCTP模板的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [SCTP模板（SCTPTEMPLATE）](configobject/UNC/20.15.2/SCTPTEMPLATE.md)

## 使用实例

根据网络规划，需要删除一个SCTP模板，则可以按如下配置：

```
RMV SCTPTEMPLATE: SCTPTEMPLNAME="sctp_tp1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除SCTP模板（RMV-SCTPTEMPLATE）_09897334.md`
