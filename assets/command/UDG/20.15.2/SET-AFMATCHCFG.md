---
id: UDG@20.15.2@MMLCommand@SET AFMATCHCFG
type: MMLCommand
name: SET AFMATCHCFG（设置软参欺诈场景功能开关）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: AFMATCHCFG
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 1
category_path:
- 用户面服务管理
- 业务防欺诈
- HTTP欺诈场景的匹配情况统计
status: active
---

# SET AFMATCHCFG（设置软参欺诈场景功能开关）

## 功能

**适用NF：PGW-U、UPF**

此命令用于配置软参场景欺诈统计功能开关。

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
| SWITCH | 软参欺诈场景功能开关 | 可选必选说明：必选参数<br>参数含义：该参数用于开启或者关闭软参欺诈场景统计功能。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能（关闭）。<br>- ENABLE：使能（开启）。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [软参欺诈场景开关状态（AFMATCHCFG）](configobject/UDG/20.15.2/AFMATCHCFG.md)

## 使用实例

开启软参场景欺诈统计功能，则配置命令如下：

```
SET AFMATCHCFG:SWITCH=ENABLE;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置软参欺诈场景功能开关（SET-AFMATCHCFG）_82837812.md`
