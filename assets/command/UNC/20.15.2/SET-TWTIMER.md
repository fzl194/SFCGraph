---
id: UNC@20.15.2@MMLCommand@SET TWTIMER
type: MMLCommand
name: SET TWTIMER（设置TW定时器）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: TWTIMER
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
effect_mode: ''
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

# SET TWTIMER（设置TW定时器）

## 功能

**适用NF：PGW-C、SMF**

该命令用于配置Diameter TW定时器。当该定时器超时后，UNC会向OCS等Diameter对端发送DWR消息。并能控制DWR消息响应超时次数达到上限后，是否复位UNC和对端之间的链接。

## 注意事项

- 该命令需要重新建链后才能生效。
- 该命令最大记录数为1。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | TWTIMERLEN | TWNORESPTIMES | TWRSTTCP |
| --- | --- | --- | --- |
| 初始值 | 30 | 3 | DISABLE |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TWTIMERLEN | TW定时器时长（秒） | 可选必选说明：必选参数<br>参数含义：该参数用于指定TW定时器时长。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～180，单位是秒。<br>默认值：无<br>配置原则：无 |
| TWNORESPTIMES | DWR消息响应超时次数上限 | 可选必选说明：可选参数<br>参数含义：该参数用于指定DWR消息响应超时次数上限。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～3。<br>默认值：无<br>配置原则：无 |
| TWRSTTCP | 超时次数达到上限复位连接 | 可选必选说明：可选参数<br>参数含义：该参数用于指定超时次数达到上限是否复位连接。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不复位TCP。<br>- ENABLE：复位TCP。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/TWTIMER]] · TW定时器（TWTIMER）

## 使用实例

配置Diameter TW定时器，则可按如下配置：

```
SET TWTIMER:TWTIMERLEN=3,TWNORESPTIMES=3,TWRSTTCP=ENABLE;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-TWTIMER.md`
