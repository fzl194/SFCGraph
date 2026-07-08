---
id: UDG@20.15.2@MMLCommand@SET UPINITSETUP
type: MMLCommand
name: SET UPINITSETUP（主被动切换）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: UPINITSETUP
command_category: 配置类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 1
category_path:
- 用户面服务管理
- 路径管理
- PFCP路径管理
- UP信息管理
- UP主动被动建联开关
status: active
---

# SET UPINITSETUP（主被动切换）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用于设置是否主动发起建立偶联的消息。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 设置为主动发起建立偶联消息模式后，不处理SMF主动发起的建立偶联请求。
- 当SMF到UPF N4偶联已经建立，配置为U面主动发起建链的时候，UPF会释放已有的N4链路偶联，主动发起建链，并且不处理SMF发起的偶联建立请求。
- 设置主被动切换时，不需要去激活用户，也不需要删除SMF之间的偶联。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | UPSWITCH |
| --- | --- |
| 初始值 | DISABLE |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| UPSWITCH | UP切换 | 可选必选说明：必选参数<br>参数含义：主被动切换。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@UPINITSETUP]] · 主被动切换（UPINITSETUP）

## 使用实例

设置主动发起建立偶联：

```
SET UPINITSETUP: UPSWITCH=ENABLE;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-UPINITSETUP.md`
