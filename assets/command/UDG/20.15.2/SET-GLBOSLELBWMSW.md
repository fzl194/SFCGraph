---
id: UDG@20.15.2@MMLCommand@SET GLBOSLELBWMSW
type: MMLCommand
name: SET GLBOSLELBWMSW（设置整机操作系统级带宽管理开关）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: GLBOSLELBWMSW
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 1
category_path:
- 用户面服务管理
- 业务控制策略
- 带宽控制
- 整机操作系统级带宽管理
status: active
---

# SET GLBOSLELBWMSW（设置整机操作系统级带宽管理开关）

## 功能

**适用NF：PGW-U、UPF**

该命令用来设置整机下操作系统级带宽管理开关。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 此命令的生效范围为整机，开启后可能导致性能下降明显。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | ISENABLE |
| --- | --- |
| 初始值 | DISABLE |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ISENABLE | 整机操作系统级带宽管理开关 | 可选必选说明：必选参数<br>参数含义：整机操作系统级带宽管理开关。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能（关闭）。<br>- ENABLE：使能（开启）。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [整机操作系统级带宽管理开关（GLBOSLELBWMSW）](configobject/UDG/20.15.2/GLBOSLELBWMSW.md)

## 使用实例

假如运营商需使能整机的操作系统BWM功能：

```
SET GlbOSLELBWMSW:ISENABLE=ENABLE;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置整机操作系统级带宽管理开关（SET-GLBOSLELBWMSW）_82837501.md`
