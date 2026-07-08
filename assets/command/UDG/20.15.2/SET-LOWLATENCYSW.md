---
id: UDG@20.15.2@MMLCommand@SET LOWLATENCYSW
type: MMLCommand
name: SET LOWLATENCYSW（设置低时延业务开关）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: LOWLATENCYSW
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 1
category_path:
- 用户面服务管理
- 业务匹配策略
- 体验分级
- 体验分级全局参数
- 低时延业务开关
status: active
---

# SET LOWLATENCYSW（设置低时延业务开关）

## 功能

**适用NF：PGW-U、UPF**

该命令用于设置低时延业务开关。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | SWITCH |
| --- | --- |
| 初始值 | DISABLE |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SWITCH | 低时延业务开关 | 可选必选说明：可选参数<br>参数含义：该参数用于设置低时延业务功能是否使能。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能（关闭）。<br>- ENABLE：使能（开启）。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/LOWLATENCYSW]] · 低时延业务开关（LOWLATENCYSW）

## 使用实例

设置低时延业务开关使能：

```
SET LOWLATENCYSW: SWITCH=ENABLE;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置低时延业务开关（SET-LOWLATENCYSW）_69122707.md`
