---
id: UDG@20.15.2@MMLCommand@RMV OSPFFRR
type: MMLCommand
name: RMV OSPFFRR（删除OSPF IP FRR配置）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: OSPFFRR
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- OSPF管理
- OSPF的FRR配置
status: active
---

# RMV OSPFFRR（删除OSPF IP FRR配置）

## 功能

该命令用于删除OSPF IP FRR（快速重路由）配置。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCID | OSPF进程号 | 可选必选说明：必选参数<br>参数含义：OSPF进程号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无 |

## 操作的配置对象

- [OSPF IP FRR配置（OSPFFRR）](configobject/UDG/20.15.2/OSPFFRR.md)

## 使用实例

删除OSPF进程号为1的IP FRR（快速重路由）配置：

```
RMV OSPFFRR: PROCID=1;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除OSPF-IP-FRR配置（RMV-OSPFFRR）_00601373.md`
