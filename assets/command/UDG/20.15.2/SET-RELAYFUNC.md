---
id: UDG@20.15.2@MMLCommand@SET RELAYFUNC
type: MMLCommand
name: SET RELAYFUNC（设置媒体中继功能配置）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: RELAYFUNC
command_category: 配置类
applicable_nf:
- UPF
- PGW-U
effect_mode: 对新流生效
is_dangerous: true
max_records: 1
category_path:
- 用户面服务管理
- 业务控制策略
- 媒体中继
- 媒体中继功能
status: active
---

# SET RELAYFUNC（设置媒体中继功能配置）

## 功能

**适用NF：UPF、PGW-U**

![](设置媒体中继功能配置（SET RELAYFUNC）_64299160.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，删除该配置后，会导致媒体中继业务中断。

该命令用于配置媒体中继功能。

## 注意事项

- 该命令执行后对新数据流生效。
- 该命令最大记录数为1。
- 媒体中继功能关闭后，媒体中继的DNS代理功能关闭。用户可以使用已经获取到的媒体中继IP继续访问媒体中继业务，直到重新发起DNS请求。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | RELAYSW |
| --- | --- |
| 初始值 | DISABLE |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RELAYSW | 媒体中继功能开关 | 可选必选说明：必选参数<br>参数含义：该参数用于控制开启或关闭媒体中继功能。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能媒体中继功能开关。<br>- ENABLE：使能媒体中继功能开关。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/RELAYFUNC]] · 媒体中继功能配置（RELAYFUNC）

## 使用实例

开启媒体中继功能开关：

```
SET RELAYFUNC: RELAYSW=ENABLE;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置媒体中继功能配置（SET-RELAYFUNC）_64299160.md`
