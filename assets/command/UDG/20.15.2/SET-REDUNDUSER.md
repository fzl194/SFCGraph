---
id: UDG@20.15.2@MMLCommand@SET REDUNDUSER
type: MMLCommand
name: SET REDUNDUSER（配置静态地址用户路由冗余功能）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: REDUNDUSER
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: true
max_records: 1
category_path:
- 用户面服务管理
- 会话管理
- 会话地址管理
- 静态地址用户路由冗余
- 路由冗余开关
status: active
---

# SET REDUNDUSER（配置静态地址用户路由冗余功能）

## 功能

**适用NF：PGW-U、UPF**

![](配置静态地址用户路由冗余功能（SET REDUNDUSER）_71074367.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，改此配置前先确认是否存在静态地址冗余用户，否则可能导致此部分用户业务不通。

该命令用来配置静态地址用户路由冗余功能。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 修改此配置前需要保证无正在使用或者准备使用静态地址路由冗余的用户，否则可能导致此部分用户业务不通。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | SWITCH |
| --- | --- |
| 初始值 | DISABLE |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SWITCH | 开关 | 可选必选说明：必选参数<br>参数含义：配置静态地址用户路由冗余功能是否使能。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/REDUNDUSER]] · 静态地址用户路由冗余功能（REDUNDUSER）

## 关联任务

- [[UDG@20.15.2@Task@0-00064]]

## 使用实例

配置当前设备支持静态地址用户路由冗余功能：

```
SET REDUNDUSER: SWITCH=ENABLE;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/配置静态地址用户路由冗余功能（SET-REDUNDUSER）_71074367.md`
