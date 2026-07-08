---
id: UDG@20.15.2@MMLCommand@RMV PDNROUTETSTPATH
type: MMLCommand
name: RMV PDNROUTETSTPATH（删除UPF向PDN服务器发送探测消息的探测路径）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: PDNROUTETSTPATH
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 会话管理
- 会话连通性检测
- 网络侧连通性检测
- PDN侧路由探测
status: active
---

# RMV PDNROUTETSTPATH（删除UPF向PDN服务器发送探测消息的探测路径）

## 功能

**适用NF：PGW-U、UPF**

该命令用来删除UPF向PDN服务器自动发送探测消息的路径配置。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PATHNAME | 路径名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定用于连通性探测的路径名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：配置的路径名称应满足路径名称的取值范围。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@PDNROUTETSTPATH]] · UPF向PDN服务器发送探测消息的探测路径配置（PDNROUTETSTPATH）

## 使用实例

删除配置路径名称为test的探测路径配置：

```
RMV PDNROUTETSTPATH: PATHNAME="test";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-PDNROUTETSTPATH.md`
