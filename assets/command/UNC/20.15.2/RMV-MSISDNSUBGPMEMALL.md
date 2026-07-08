---
id: UNC@20.15.2@MMLCommand@RMV MSISDNSUBGPMEMALL
type: MMLCommand
name: RMV MSISDNSUBGPMEMALL（删除所有MSISDN用户群成员）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: MSISDNSUBGPMEMALL
command_category: 配置类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 移动性管理
- 区域漫游限制管理
- MSISDN用户群成员管理
status: active
---

# RMV MSISDNSUBGPMEMALL（删除所有MSISDN用户群成员）

## 功能

**适用网元：SGSN、MME**

本命令用于删除所有MSISDN用户群成员。

## 注意事项

- 该命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBID | 用户群标识 | 可选必选说明：必选参数<br>参数含义：用户群标识<br>数据来源：整网规划<br>取值范围：1~100<br>默认值：1<br>配置原则：无 |
| OPTION_TYPE | 操作类型 | 可选必选说明：必选参数<br>参数含义：操作类型<br>数据来源：整网规划<br>取值范围：ALL<br>默认值：ALL<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/MSISDNSUBGPMEMALL]] · 所有MSISDN用户群成员（MSISDNSUBGPMEMALL）

## 使用实例

删除所有MSISDN用户群成员。

```
%%RMV MSISDNSUBGPMEMALL: OPTION_TYPE=ALL, SUBID=1;%% 
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除所有MSISDN用户群成员（RMV-MSISDNSUBGPMEMALL）_14340897.md`
