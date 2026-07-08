---
id: UNC@20.15.2@MMLCommand@RMV ROUTEPOLICY
type: MMLCommand
name: RMV ROUTEPOLICY（删除路由策略）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: ROUTEPOLICY
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- 路由策略管理
- 路由策略
status: active
---

# RMV ROUTEPOLICY（删除路由策略）

## 功能

该命令用于删除路由策略。

## 注意事项

- 该命令执行后立即生效。
- 删除该路由策略时，要保证该路由策略被添加过。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POLICYNAME | 路由策略名字 | 可选必选说明：必选参数<br>参数含义：该参数用于指定路由策略的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～200。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/ROUTEPOLICY]] · 路由策略（ROUTEPOLICY）

## 使用实例

删除名称为a的路由策略：

```
RMV ROUTEPOLICY: POLICYNAME="a";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-ROUTEPOLICY.md`
