---
id: UNC@20.15.2@MMLCommand@RMV S1PAGINGRULEALL
type: MMLCommand
name: RMV S1PAGINGRULEALL（删除所有S1寻呼规则）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: S1PAGINGRULEALL
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- S1接口管理
- S1寻呼规则管理
status: active
---

# RMV S1PAGINGRULEALL（删除所有S1寻呼规则）

## 功能

**适用网元：SGSN**

本命令用于删除所有S1寻呼规则。

## 注意事项

- 该命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| OPTION_TYPE | 操作类型 | 可选必选说明：必选参数<br>参数含义：操作类型<br>数据来源：整网规划<br>取值范围：ALL<br>默认值：ALL<br>配置原则：无 |

## 操作的配置对象

- [所有S1寻呼规则（S1PAGINGRULEALL）](configobject/UNC/20.15.2/S1PAGINGRULEALL.md)

## 使用实例

删除所有S1寻呼规则。

```
%%RMV S1PAGINGRULEALL: OPTION_TYPE=ALL;%% 
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除所有S1寻呼规则（RMV-S1PAGINGRULEALL）_15056745.md`
