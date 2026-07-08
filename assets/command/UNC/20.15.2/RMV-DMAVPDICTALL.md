---
id: UNC@20.15.2@MMLCommand@RMV DMAVPDICTALL
type: MMLCommand
name: RMV DMAVPDICTALL（删除所有Diameter AVP表）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: DMAVPDICTALL
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 扩展调测
- 业务调测
- Diameter AVP表
status: active
---

# RMV DMAVPDICTALL（删除所有Diameter AVP表）

## 功能

**适用网元：SGSN**

本命令用于删除所有Diameter数据字典中的AVP表。

## 注意事项

- 该命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| OPTION_TYPE | 操作类型 | 可选必选说明：必选参数<br>参数含义：操作类型<br>数据来源：整网规划<br>取值范围：ALL<br>默认值：ALL<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/DMAVPDICTALL]] · 所有Diameter AVP表（DMAVPDICTALL）

## 使用实例

删除所有Diameter数据字典中的AVP表。

```
%%RMV DMAVPDICTALL: OPTION_TYPE=ALL;%% 
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-DMAVPDICTALL.md`
