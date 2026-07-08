---
id: UDG@20.15.2@MMLCommand@RMV HTTPSTATOBJ
type: MMLCommand
name: RMV HTTPSTATOBJ（删除基于对端结点的性能统计测量对象信息）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: HTTPSTATOBJ
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- HTTP功能管理
- HTTP管理
- HTTP统计管理
status: active
---

# RMV HTTPSTATOBJ（删除基于对端结点的性能统计测量对象信息）

## 功能

删除基于对端结点的性能统计测量对象信息。当测量对象无法正常老化时，可通过该命令删除。

> **说明**
> 该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PTYPE | 对端网元类型 | 可选必选说明：必选参数<br>参数含义：用于标识通信对端结点的类型，对于服务化接口的消息统计，标识对端NFTYPE。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~128。<br>默认值：无<br>配置原则：无 |
| PADDR | 对端IP地址 | 可选必选说明：必选参数<br>参数含义：用于标识通信对端结点的IP，对于服务化接口的消息统计，标识对端IP。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~128。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [基于对端结点的性能统计测量对象信息（HTTPSTATOBJ）](configobject/UDG/20.15.2/HTTPSTATOBJ.md)

## 使用实例

如果想删除基于对端结点的性能统计测量对象信息，可以用如下命令：

```
RMV HTTPSTATOBJ: PTYPE="AMF", PADDR="192.168.111.222";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除基于对端结点的性能统计测量对象信息（RMV-HTTPSTATOBJ）_86240312.md`
