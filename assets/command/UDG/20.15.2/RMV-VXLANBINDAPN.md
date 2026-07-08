---
id: UDG@20.15.2@MMLCommand@RMV VXLANBINDAPN
type: MMLCommand
name: RMV VXLANBINDAPN（删除VXLAN隧道组绑定APN）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: VXLANBINDAPN
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: true
category_path:
- 用户面服务管理
- 路径管理
- VXLAN路径管理
- VXLAN隧道绑定APN
status: active
---

# RMV VXLANBINDAPN（删除VXLAN隧道组绑定APN）

## 功能

**适用NF：PGW-U、UPF**

![](删除VXLAN隧道组绑定APN（RMV VXLANBINDAPN）_81234594.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，删除配置会导致匹配到对应规则的数据报文无法转发给MEP。

该命令用于删除VXLAN隧道组与APN的绑定关系。

## 注意事项

- 该命令执行后立即生效。
- 执行该命令时，会删除Vxlan组和APN的绑定关系，将改变业务数据转发流程，数据报文由转发给MEP修改为直接路由转发。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN实例名。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [VXLAN隧道组绑定APN（VXLANBINDAPN）](configobject/UDG/20.15.2/VXLANBINDAPN.md)

## 使用实例

删除所有VXLAN隧道组与apn1的绑定关系：

```
RMV VXLANBINDAPN: APN="apn1";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除VXLAN隧道组绑定APN（RMV-VXLANBINDAPN）_81234594.md`
