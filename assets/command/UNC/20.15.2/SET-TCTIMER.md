---
id: UNC@20.15.2@MMLCommand@SET TCTIMER
type: MMLCommand
name: SET TCTIMER（设置TC定时器）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: TCTIMER
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
max_records: 1
category_path:
- 业务服务管理
- 接口管理
- 计费和策略接口管理
- Diameter管理
- 公共参数
- Diameter公共参数
status: active
---

# SET TCTIMER（设置TC定时器）

## 功能

**适用NF：PGW-C、SMF**

该命令用于配置Diameter TC定时器。设置定时器时长，用来控制当UNC与OCS等Diameter对端断链后，重建链接的间隔时长。当此定时器超时，UNC则会向OCS等Diameter对端重新发起建链请求。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
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
| TCMODE | 定时器模式 | 可选必选说明：可选参数<br>参数含义：该参数用于指定选择TC定时器的方式。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- FIXED：表示TC定时器为固定方式，即每次重建链间隔是固定的。<br>- MULTIPLY：表示TC定时器为累加方式，即每次重建链间隔是N*TcTimerr时长，N表示重发建链请求消息的次数，N的最大值为20。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/TCTIMER]] · TC定时器（TCTIMER）

## 使用实例

配置Diameter TC定时器，则可以按如下配置：

```
SET TCTIMER:TCTIMERLEN=3,TCMODE=FIXED;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置TC定时器（SET-TCTIMER）_09897236.md`
