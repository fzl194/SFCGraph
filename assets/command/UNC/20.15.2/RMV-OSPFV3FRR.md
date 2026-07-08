---
id: UNC@20.15.2@MMLCommand@RMV OSPFV3FRR
type: MMLCommand
name: RMV OSPFV3FRR（删除OSPFv3 IP FRR配置）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: OSPFV3FRR
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- OSPFv3管理
- OSPFv3 FRR配置
status: active
---

# RMV OSPFV3FRR（删除OSPFv3 IP FRR配置）

## 功能

该命令用于删除OSPFv3 IP FRR（快速重路由）配置。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCID | OSPFv3进程号 | 可选必选说明：必选参数<br>参数含义：OSPFv3进程号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/OSPFV3FRR]] · OSPFv3 IP FRR配置（OSPFV3FRR）

## 使用实例

删除OSPFv3进程号为1的IP FRR（快速重路由）配置：

```
RMV OSPFV3FRR: PROCID=1;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-OSPFV3FRR.md`
