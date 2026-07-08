---
id: UNC@20.15.2@MMLCommand@RMV APPLYORIGIN
type: MMLCommand
name: RMV APPLYORIGIN（删除BGP路由信息的路由源设置）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: APPLYORIGIN
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- 路由策略管理
- 应用BGP路由信息的路由源
status: active
---

# RMV APPLYORIGIN（删除BGP路由信息的路由源设置）

## 功能

该命令用于删除BGP路由信息的路由源设置。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POLICYNAME | 路由策略名字 | 可选必选说明：必选参数<br>参数含义：该参数用来表示路由策略名字。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～200。<br>默认值：无 |
| NODESEQUENCE | 路由策略节点号 | 可选必选说明：必选参数<br>参数含义：该参数用来表示路由策略节点号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65535。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/APPLYORIGIN]] · BGP路由信息的路由源设置（APPLYORIGIN）

## 使用实例

删除policy路由策略10节点下的路由源类型：

```
RMV APPLYORIGIN:POLICYNAME="policy",NODESEQUENCE=10;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除BGP路由信息的路由源设置（RMV-APPLYORIGIN）_00441137.md`
