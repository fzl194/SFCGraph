---
id: UNC@20.15.2@MMLCommand@RMV MVNONETALL
type: MMLCommand
name: RMV MVNONETALL（删除所有MVNO网络配置信息）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: MVNONETALL
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 网络管理
- 归属网络运营商管理
- MVNO管理
- MVNO网络标识配置表
status: active
---

# RMV MVNONETALL（删除所有MVNO网络配置信息）

## 功能

**适用网元：SGSN**

本命令用于删除所有MVNO网络配置信息。

## 注意事项

- 该命令执行后立即生效。
- RMV MVNONETALL命令无法删除带IMSI参数的配置

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| OPTION_TYPE | 操作类型 | 可选必选说明：必选参数<br>参数含义：操作类型<br>数据来源：整网规划<br>取值范围：ALL<br>默认值：ALL<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/MVNONETALL]] · 所有MVNO网络配置信息（MVNONETALL）

## 使用实例

删除所有MVNO网络配置信息。

```
%%RMV MVNONETALL: OPTION_TYPE=ALL;%% 
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除所有MVNO网络配置信息（RMV-MVNONETALL）_14719677.md`
