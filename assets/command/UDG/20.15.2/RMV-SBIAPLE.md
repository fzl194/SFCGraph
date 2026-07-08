---
id: UDG@20.15.2@MMLCommand@RMV SBIAPLE
type: MMLCommand
name: RMV SBIAPLE（删除服务化接口本端实体）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: SBIAPLE
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- HTTP功能管理
- SBI管理
- 服务化接口本端实体管理
status: active
---

# RMV SBIAPLE（删除服务化接口本端实体）

## 功能

![](删除服务化接口本端实体（RMV SBIAPLE）_84132108.assets/notice_3.0-zh-cn.png)

该命令用于删除服务化接口本端实体，该命令执行后系统中配置的服务化接口本端实体删除，对应的HTTP链路删除，影响基于该服务化接口的业务。

该命令用于删除服务化接口本端实体。

> **说明**
> - 该命令执行后立即生效。
>
> - 删除服务化接口本端实体后，基于该服务化接口的业务将中断。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INDEX | 索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定服务化接口本端实体的索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~128。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/SBIAPLE]] · 服务化接口本端实体（SBIAPLE）

## 使用实例

若运营商想删除索引是2的服务化接口本端实体，可以执行如下命令：

```
RMV SBIAPLE: INDEX=2;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除服务化接口本端实体（RMV-SBIAPLE）_84132108.md`
