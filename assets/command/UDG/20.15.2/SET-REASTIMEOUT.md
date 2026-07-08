---
id: UDG@20.15.2@MMLCommand@SET REASTIMEOUT
type: MMLCommand
name: SET REASTIMEOUT（设置IPv4报文重组超时配置）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: REASTIMEOUT
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP协议栈
- IPv4管理
- IPv4报文重组超时配置
status: active
---

# SET REASTIMEOUT（设置IPv4报文重组超时配置）

## 功能

为了提高路由设备的性能，防止攻击，使用该命令设置IPv4分片报文适当的重组超时时间，可以使长时间等待重组完成的重组队列及时被老化。缺省情况下，IPv4分片报文的重组超时时间是30秒。

## 注意事项

- 该命令执行后立即生效。
- 该命令仅适用于非NP卡场景和NP卡非加速模式场景。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| TIMEOUT |
| --- |
| 30 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TIMEOUT | IPv4报文重组超时时间（s） | 可选必选说明：必选参数<br>参数含义：该参数表示IPv4重组超时时间。太长的超时时间，可能会造成有大量分片报文存储在路由设备中等待重组完成，会造成资源的持续占用，降低路由器的性能，同时可能会遭受网络攻击。所以不建议将超时时间设置的过大。过短的超时时间，将可能导致有分片报文未进行重组，最终重组失败。推荐使用缺省值30秒。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为5～120，单位是秒。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/REASTIMEOUT]] · IPv4报文重组超时配置（REASTIMEOUT）

## 使用实例

设置IPv4报文充重组超时时间为5秒 ：

```
SET REASTIMEOUT: TIMEOUT=5;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-REASTIMEOUT.md`
