---
id: UDG@20.15.2@MMLCommand@SET USRTRCPLY
type: MMLCommand
name: SET USRTRCPLY（设置用户跟踪策略）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: USRTRCPLY
command_category: 配置类
applicable_nf:
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 1
category_path:
- 用户面服务管理
- 业务运维
- 业务跟踪管理
- 用户跟踪策略配置
status: active
---

# SET USRTRCPLY（设置用户跟踪策略）

## 功能

**适用NF：UPF**

该命令用于设置用户跟踪策略。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 匿名化开关默认开启，建议运营商遵从所在国家的相关法律关闭。为更好地保护用户个人隐私，请及时开启匿名化开关。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | LOCALFILEDAYS | ANONYMOUSSWITCH |
| --- | --- | --- |
| 初始值 | 7 | ENABLE |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LOCALFILEDAYS | 最大保留天数 | 可选必选说明：可选参数<br>参数含义：跟踪存盘文件最大保留天数，本地时间3:00定时删除超期文件。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～720，单位是天。<br>默认值：无<br>配置原则：无 |
| ANONYMOUSSWITCH | 匿名化开关 | 可选必选说明：可选参数<br>参数含义：跟踪存盘文件匿名化策略开关。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ENABLE：使能。<br>- DISABLE：不使能。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/USRTRCPLY]] · 用户跟踪策略（USRTRCPLY）

## 使用实例

设置跟踪文件删除策略为7天：

```
SET USRTRCPLY: LOCALFILEDAYS=7;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-USRTRCPLY.md`
