---
id: UNC@20.15.2@MMLCommand@SET LSPVGLOBALCFG
type: MMLCommand
name: SET LSPVGLOBALCFG（设置LSPV全局属性）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: LSPVGLOBALCFG
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 系统管理
- 系统维护
- Ping和Tracert
- LSPV
status: active
---

# SET LSPVGLOBALCFG（设置LSPV全局属性）

## 功能

该命令用于配置LSPV全局属性。

当设备作为标签转发路径检测的响应端时，可能收到大量MPLS ECHO-REQUEST报文需要处理，可以执行SET LSPVGLOBALCFG命令使能设备LSPV模块和配置LSPV模块的MPLS ECHO-REQUEST报文处理速率，从而保证设备能够接收MPLS ECHO-REQUEST报文，并回应MPLS ECHO-REPLY报文。

## 注意事项

- 该命令执行后立即生效。
- 配置速率较小时可能会导致LSP Ping丢包。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| LSPV | MAXRATE |
| --- | --- |
| ENABLE | 1000 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LSPV | LSPV响应端 | 可选必选说明：必选参数<br>参数含义：该参数用于使能，去使能LSPV响应端。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ENABLE：使能。<br>- DISABLE：去使能。<br>默认值：无 |
| MAXRATE | 最大速率（pps） | 可选必选说明：条件可选参数<br>前提条件：该参数在“LSPV”配置为“ENABLE”时为可选参数。<br>参数含义：该参数用于指定MPLS echo request报文防攻击的限速值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为10～65535。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/LSPVGLOBALCFG]] · LSPV全局属性（LSPVGLOBALCFG）

## 使用实例

LSPV响应端：

```
SET LSPVGLOBALCFG:LSPV=ENABLE,MAXRATE=1000;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-LSPVGLOBALCFG.md`
