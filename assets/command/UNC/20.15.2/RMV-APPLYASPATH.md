---
id: UNC@20.15.2@MMLCommand@RMV APPLYASPATH
type: MMLCommand
name: RMV APPLYASPATH（删除AS路径设置）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: APPLYASPATH
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- 路由策略管理
- 应用替换AS路径
status: active
---

# RMV APPLYASPATH（删除AS路径设置）

## 功能

该命令删除AS路径属性的操作。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POLICYNAME | 路由策略名字 | 可选必选说明：必选参数<br>参数含义：该参数用于指定路由策略名字。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～200。<br>默认值：无 |
| NODESEQUENCE | 路由策略节点号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定路由策略节点号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65535。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/APPLYASPATH]] · AS路径设置（APPLYASPATH）

## 使用实例

删除AS路径属性的操作：

```
RMV APPLYASPATH:POLICYNAME="bbb",NODESEQUENCE=10;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除AS路径设置（RMV-APPLYASPATH）_49802118.md`
