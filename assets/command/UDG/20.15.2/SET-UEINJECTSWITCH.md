---
id: UDG@20.15.2@MMLCommand@SET UEINJECTSWITCH
type: MMLCommand
name: SET UEINJECTSWITCH（设置UE灌包开关）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: UEINJECTSWITCH
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
- 会话管理
- 会话连通性检测
- UE侧连通性检测
- UE灌包功能
status: active
---

# SET UEINJECTSWITCH（设置UE灌包开关）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用于配置UE下行灌包功能。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 此命令不支持配置恢复，若整机重启则需要重新配置。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | SWITCH |
| --- | --- |
| 初始值 | DISABLE |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SWITCH | 开关标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定是否使能UE灌包功能。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/UEINJECTSWITCH]] · UE灌包开关（UEINJECTSWITCH）

## 使用实例

使能UE下行灌包功能：

```
SET UEINJECTSWITCH: SWITCH=ENABLE;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置UE灌包开关（SET-UEINJECTSWITCH）_82837095.md`
