---
id: UDG@20.15.2@MMLCommand@RMV OSPFDNBITSET
type: MMLCommand
name: RMV OSPFDNBITSET（删除DN比特位配置）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: OSPFDNBITSET
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- OSPF管理
- OSPF DN比特位配置
status: active
---

# RMV OSPFDNBITSET（删除DN比特位配置）

## 功能

该命令用于恢复OSPF LSA的DN位默认配置。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCID | 进程号 | 可选必选说明：必选参数<br>参数含义：OSPF进程号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/OSPFDNBITSET]] · DN比特位配置（OSPFDNBITSET）

## 使用实例

恢复OSPF进程1下DN位的默认配置：

```
RMV OSPFDNBITSET:PROCID=1;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-OSPFDNBITSET.md`
