---
id: UDG@20.15.2@MMLCommand@SET UPTCTIMER
type: MMLCommand
name: SET UPTCTIMER（设置TC定时器）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: UPTCTIMER
command_category: 配置类
applicable_nf:
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 1
category_path:
- 用户面服务管理
- Diameter管理
- Diameter公共参数
status: active
---

# SET UPTCTIMER（设置TC定时器）

## 功能

**适用NF：UPF**

该命令用于配置Diameter TC定时器。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 该命令相关的功能当前版本暂不支持。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | TCTIMERLEN | TCMODE |
| --- | --- | --- |
| 初始值 | 1 | MULTIPLY |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TCTIMERLEN | TC定时器时长（单位500ms） | 可选必选说明：必选参数<br>参数含义：该参数用于指定TC定时器时长。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～3600，单位是500毫秒。<br>默认值：无<br>配置原则：无 |
| TCMODE | 定时器模式 | 可选必选说明：可选参数<br>参数含义：该参数用于指定选择TC定时器的方式。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- FIXED：表示TC定时器为固定方式，即每次重建链间隔是固定的。<br>- MULTIPLY：表示TC定时器为累加方式，即每次重建链间隔是N*TcTimer时长，N表示重发建链请求消息的次数，N的最大值为20。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [TC定时器（UPTCTIMER）](configobject/UDG/20.15.2/UPTCTIMER.md)

## 使用实例

配置Diameter TC定时器，则可以按如下配置：

```
SET UPTCTIMER:TCTIMERLEN=3,TCMODE=FIXED;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置TC定时器（SET-UPTCTIMER）_45432682.md`
