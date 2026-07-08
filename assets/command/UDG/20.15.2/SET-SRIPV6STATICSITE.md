---
id: UDG@20.15.2@MMLCommand@SET SRIPV6STATICSITE
type: MMLCommand
name: SET SRIPV6STATICSITE（设置IPv6静态路由全局属性）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: SRIPV6STATICSITE
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- 静态路由管理
- IPv6静态路由全局属性管理
status: active
---

# SET SRIPV6STATICSITE（设置IPv6静态路由全局属性）

## 功能

该命令用来设置IPv6路由全局属性。

## 注意事项

- 该命令执行后立即生效。
- 可选参数至少选一项。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| IPV6PREFERENCE | MINRXINTERVAL6 | MINTXINTERVAL6 | MULTIPLIER6 |
| --- | --- | --- | --- |
| 60 | 200 | 200 | 3 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPV6PREFERENCE | 全局默认优先级 | 可选必选说明：可选参数<br>参数含义：该参数用于指定IPv6静态路由的全局默认优先级。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～255。<br>默认值：无 |
| MINRXINTERVAL6 | BFD最小接收间隔（ms） | 可选必选说明：可选参数<br>参数含义：该参数用于指定期望从对端接收IPv6 BFD报文的缺省最小接收间隔。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为30～1000，单位是毫秒。<br>默认值：无 |
| MINTXINTERVAL6 | BFD最小传输间隔（ms） | 可选必选说明：可选参数<br>参数含义：该参数用于指定向对端发送IPv6 BFD报文的缺省最小传输间隔。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为30～1000，单位是毫秒。<br>默认值：无 |
| MULTIPLIER6 | 本地检测倍数 | 可选必选说明：可选参数<br>参数含义：该参数用于指定会话检测倍数，如果BFD会话在设置的检测周期内没有收到对端发来的BFD报文，则认为链路发生了故障，BFD会话的状态将会置为Down。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为3～50。<br>默认值：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@SRIPV6STATICSITE]] · IPv6静态路由全局属性（SRIPV6STATICSITE）

## 使用实例

设置IPv6静态路由全局属性：

```
SET SRIPV6STATICSITE:IPV6PREFERENCE=5,MINRXINTERVAL6=300,MINTXINTERVAL6=350,MULTIPLIER6=45;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-SRIPV6STATICSITE.md`
