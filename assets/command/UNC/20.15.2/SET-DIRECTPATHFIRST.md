---
id: UNC@20.15.2@MMLCommand@SET DIRECTPATHFIRST
type: MMLCommand
name: SET DIRECTPATHFIRST（设置直连路径优先开关）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: DIRECTPATHFIRST
command_category: 配置类
applicable_nf:
- SGW-C
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
max_records: 1
category_path:
- 业务服务管理
- 接口管理
- 计费和策略接口管理
- Diameter管理
- 路由控制
- 路径选择控制
status: active
---

# SET DIRECTPATHFIRST（设置直连路径优先开关）

## 功能

**适用NF：SGW-C、PGW-C、SMF**

该命令用来配置diameter会话的CCR-U/T消息是否始终通过CCR-I的发送路径发送。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 该命令设定后的数据，需要通过LST DIRECTPATHFIRST命令进行查看。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | GXSWITCH |
| --- | --- |
| 初始值 | ENABLE |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GXSWITCH | Gx接口直连路径优先开关 | 可选必选说明：必选参数<br>参数含义：该参数用于控制diameter会话的CCR-U/T消息是否始终通过CCR-I的发送路径发送。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- DISABLE：否。<br>- ENABLE：是。<br>默认值：无<br>配置原则：<br>- 如果取值为enable，直连路径优先。<br>- 如果取值为disable，CCR-U/T消息始终通过CCR-I的发送路径发送。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/DIRECTPATHFIRST]] · 直连路径优先开关（DIRECTPATHFIRST）

## 使用实例

使能direct-path-first功能：

```
SET DIRECTPATHFIRST: GXSWITCH=ENABLE;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置直连路径优先开关（SET-DIRECTPATHFIRST）_09897318.md`
