---
id: UDG@20.15.2@MMLCommand@RMV OSPFV3HOSTNAME
type: MMLCommand
name: RMV OSPFV3HOSTNAME（删除OSPFv3主机名配置）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: OSPFV3HOSTNAME
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- OSPFv3管理
- OSPFv3主机名配置
status: active
---

# RMV OSPFV3HOSTNAME（删除OSPFv3主机名配置）

## 功能

该命令用于删除OSPFv3主机名。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCID | OSPFv3进程号 | 可选必选说明：必选参数<br>参数含义：OSPFv3进程号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无 |

## 操作的配置对象

- [OSPFv3主机名配置（OSPFV3HOSTNAME）](configobject/UDG/20.15.2/OSPFV3HOSTNAME.md)

## 使用实例

OSPFv3进程1下删除主机名：

```
RMV OSPFV3HOSTNAME:PROCID=1;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除OSPFv3主机名配置（RMV-OSPFV3HOSTNAME）_49801718.md`
