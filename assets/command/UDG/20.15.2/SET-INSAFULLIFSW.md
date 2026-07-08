---
id: UDG@20.15.2@MMLCommand@SET INSAFULLIFSW
type: MMLCommand
name: SET INSAFULLIFSW（设置全量智能SA识别开关）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: INSAFULLIFSW
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: true
max_records: 1
category_path:
- 用户面服务管理
- 业务匹配策略
- 智能SA管理
- 全部流量智能识别功能开关
status: active
---

# SET INSAFULLIFSW（设置全量智能SA识别开关）

## 功能

**适用NF：PGW-U、UPF**

![](设置全量智能SA识别开关（SET INSAFULLIFSW）_56405098.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，当开启开关后，此命令会对ISU资源和性能影响产生极大挑战，开启后可能会发生CPU过载。

设置全量非可信流量上送TPU推理。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | INFERSWITCH |
| --- | --- |
| 初始值 | DISABLE |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INFERSWITCH | 全量推理开关 | 可选必选说明：必选参数<br>参数含义：该参数用于设置是否全量非可信流量使用智能识别。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE：全量非可信流量使用智能识别不使能。<br>- ENABLE：全量非可信流量使用智能识别使能。<br>默认值：无<br>配置原则：无 |
| CFGDOMAINNAME | 配置域名称 | 可选必选说明：可选参数<br>参数含义：该参数表示命令所属公共配置域的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/INSAFULLIFSW]] · 全量智能SA识别开关（INSAFULLIFSW）

## 使用实例

设置全量智能SA识别开关为开：

```
SET INSAFULLIFSW:INFERSWITCH=ENABLE;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-INSAFULLIFSW.md`
