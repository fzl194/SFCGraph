---
id: UNC@20.15.2@MMLCommand@SET MCSWITCH
type: MMLCommand
name: SET MCSWITCH（设置多连接开关）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: MCSWITCH
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 可靠性管理
- 微服务可靠性管理
status: active
---

# SET MCSWITCH（设置多连接开关）

## 功能

当前版本配置此命令不生效。

该命令用于配置多连接开关，开关打开，客户端与域内全部服务端连接，开关关闭，客户端只与域内主服务端连接。一个域内有一个主服务端与多个非主服务端。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| SWITCH |
| --- |
| ON |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SWITCH | 多连接开关 | 可选必选说明：必选参数<br>参数含义：该参数用于表示多连接开关。<br>数据来源：本端规划<br>取值范围：<br>- “ON（开启）”：多连接开关打开<br>- “OFF（关闭）”：多连接开关关闭<br>默认值：无。<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@MCSWITCH]] · 多连接开关配置数据（MCSWITCH）

## 使用实例

- 打开多连接开关。
  ```
  SET MCSWITCH: SWITCH=ON;
  ```
- 关闭多连接开关。
  ```
  SET MCSWITCH: SWITCH=OFF;
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-MCSWITCH.md`
