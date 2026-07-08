---
id: UDG@20.15.2@MMLCommand@RMV TOPOLICYCFG
type: MMLCommand
name: RMV TOPOLICYCFG（删除TCP优化策略配置）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: TOPOLICYCFG
command_category: 配置类
applicable_nf:
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- TCP优化服务管理
- TCP策略配置
status: active
---

# RMV TOPOLICYCFG（删除TCP优化策略配置）

## 功能

**适用NF：UPF**

该命令用于删除TCP优化策略配置。

## 注意事项

该命令执行后只对之后发生承载更新的用户或者新激活用户生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POLICYID | 策略ID | 可选必选说明：必选参数<br>参数含义：策略ID。<br>数据来源：本端规划<br>取值范围：整数类型,取值范围为1~7。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/TOPOLICYCFG]] · TCP优化策略配置（TOPOLICYCFG）

## 使用实例

运营商需要删除策略ID为1的TCP优化策略：

```
RMV TOPOLICYCFG: POLICYID=1;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除TCP优化策略配置（RMV-TOPOLICYCFG）_93175451.md`
