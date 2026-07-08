---
id: UDG@20.15.2@MMLCommand@SET CPTEIDUALLOC
type: MMLCommand
name: SET CPTEIDUALLOC（配置CP分配TEID-U开关）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: CPTEIDUALLOC
command_category: 配置类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: 对新用户生效
is_dangerous: false
max_records: 1
category_path:
- 用户面服务管理
- 会话管理
- GTP隧道管理
- CP分配TEID-U控制
status: active
---

# SET CPTEIDUALLOC（配置CP分配TEID-U开关）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用于配置是否支持CP分配TEID-U功能。当前产品仅支持UP本地分配TEID-U，不支持CP分配TEID-U，如果配置错误，可能导致用户激活失败。

## 注意事项

- 该命令执行后只对新激活用户生效。
- 该命令最大记录数为1。
- 系统是否支持CP分配TEID-U的配置一般不要修改，如需修改，例如组网变化，需要执行DSP SESSIONNUMBER确认是否存在用户，如果存在，请执行DEA SESSION先去活所有用户，用户下线后再修改此配置。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | SWITCH |
| --- | --- |
| 初始值 | DISABLE |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SWITCH | 开关标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定系统是否支持CP分配TEID-U。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：表示不支持CP分配TEID-U功能。<br>- ENABLE：表示支持CP分配TEID-U功能。当前产品不支持该功能。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/CPTEIDUALLOC]] · CP分配TEID-U开关（CPTEIDUALLOC）

## 关联任务

- [[UDG@20.15.2@Task@0-00219]]

## 使用实例

使能UP分配TEID-U功能：

```
SET CPTEIDUALLOC: SWITCH=DISABLE;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/配置CP分配TEID-U开关（SET-CPTEIDUALLOC）_82837177.md`
