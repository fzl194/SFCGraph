---
id: UDG@20.15.2@MMLCommand@SET MPLSSITE
type: MMLCommand
name: SET MPLSSITE（设置MPLS全局配置）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: MPLSSITE
command_category: 配置类
effect_mode: 立即生效
is_dangerous: true
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- MPLS管理
- MPLS基础
- MPLS全局配置
status: active
---

# SET MPLSSITE（设置MPLS全局配置）

## 功能

![](设置MPLS全局配置（SET MPLSSITE）_00600993.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，操作不当会去使能MPLS或LDP，导致MPLS或LDP功能不可用，并且所有历史MPLS或LDP配置全部删除，请谨慎使用并联系华为技术支持协助操作。

该命令用于设置MPLS全局配置。

## 注意事项

- 该命令执行后立即生效。
- 将MPLS开关或LDP开关置为DISABLE后，会导致MPLS或LDP功能不可用，并且所有历史MPLS或LDP配置全部删除。
- 如果修改LSR ID，所有与LSR ID相关的服务会更新。
- 可选参数至少选一项。
- 建议配置协议相关认证，增强协议安全性，否则可能存在协议安全风险。认证可以通过MOD LDPINSTANCE、ADD LDPPEERPOLICY或ADD LDPAUTHGROUP命令进行配置。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| MPLSLSRID | MPLSENABLE | LDPENABLE | NULLLABLETYPE |
| --- | --- | --- | --- |
| 0.0.0.0 | DISABLE | DISABLE | IMPLICIT_NULL |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MPLSLSRID | MPLS LSR ID | 可选必选说明：可选参数<br>参数含义：该参数用于指定设备的LSR ID，用于标识一个LSR。当下发0.0.0.0时表示LSR ID被删除。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：<br>- LSR ID用来在网络中唯一标识一个LSR。在网络中部署MPLS业务时，必须首先配置LSR ID。<br>- LSR没有缺省的LSR ID，必须手工配置。为了提高网络的可靠性，推荐使用LSR某个Loopback接口的地址作为LSR ID。<br>- 删除LSR ID会导致建立成功的LDP会话及LSP被删除，请谨慎执行。 |
| MPLSENABLE | MPLS能力 | 可选必选说明：可选参数<br>参数含义：该参数用于指定全局使能MPLS能力。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无 |
| LDPENABLE | LDP能力 | 可选必选说明：可选参数<br>参数含义：该参数用于指定全局使能MPLS LDP能力。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无 |
| NULLLABLETYPE | 空标签类型 | 可选必选说明：条件可选参数<br>前提条件：该参数在“MPLSENABLE”配置为“ENABLE”时为可选参数。<br>参数含义：该参数用于指定空标签类型，决定Egress向倒数第二跳分配的标签类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- EXPLICIT_NULL：显式空标签，为倒数第二跳分配0标签。<br>- IMPLICIT_NULL：隐式空标签，为倒数第二跳分配3标签。<br>- NON_NULL：不分配空标签，不为倒数第二跳分空标签。即标签值不小于16。<br>默认值：无<br>配置原则：配置后，仅在创建新的LSP时才会生效。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/MPLSSITE]] · MPLS全局配置（MPLSSITE）

## 使用实例

设置MPLS全局配置：

```
SET MPLSSITE:MPLSLSRID="192.168.1.1";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-MPLSSITE.md`
