---
id: UDG@20.15.2@MMLCommand@RMV UPSCTPASSOC
type: MMLCommand
name: RMV UPSCTPASSOC（删除SCTP耦联测量对象）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: UPSCTPASSOC
command_category: 配置类
applicable_nf:
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- SCTP管理
- SCTP测量对象
status: active
---

# RMV UPSCTPASSOC（删除SCTP耦联测量对象）

## 功能

**适用NF：UPF**

此命令用于删除SCTP耦联测量对象。

## 注意事项

- 该命令执行后立即生效。
- 该命令相关的功能当前版本暂不支持。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| OBJECTID | SCTP偶联测量对象实例标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定SCTP耦联测量对象实例标识。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～200。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/UPSCTPASSOC]] · SCTP耦联信息（UPSCTPASSOC）

## 使用实例

根据网络规划，需要删除一个SCTP耦联测量对象，则可以按如下配置：

```
RMV UPSCTPASSOC: OBJECTID=1;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除SCTP耦联测量对象（RMV-UPSCTPASSOC）_45432726.md`
