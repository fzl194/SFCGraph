---
id: UDG@20.15.2@MMLCommand@SET INNERTLSMODE
type: MMLCommand
name: SET INNERTLSMODE（设置TLS模式）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: INNERTLSMODE
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- TLS模式管理
status: active
---

# SET INNERTLSMODE（设置TLS模式）

## 功能

![](设置TLS模式（SET INNERTLSMODE）_63673351.assets/notice_3.0-zh-cn.png)

SERVICETYPE选择HAFETCD后，执行该命令会导致整系统复位。

该命令用于根据服务类型设置TLS模式。

> **说明**
> - 该命令执行后立即生效。
>
> - FusionStage裸机场景，本命令配置不生效。
>
> - 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：
>
> | SERVICETYPE | TLSMODE |
> | --- | --- |
> | HAFETCD | DEFAULT |
> | CMF | DEFAULT |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SERVICETYPE | 服务类型 | 可选必选说明：必选参数<br>参数含义：该参数用于表示服务类型。<br>数据来源：本端规划<br>取值范围：<br>- HAFETCD（HAFETCD）<br>- CMF（CMF）<br>默认值：无。<br>配置原则：无 |
| TLSMODE | TLS模式 | 可选必选说明：必选参数<br>参数含义：该参数用于表示TLS模式。<br>数据来源：本端规划<br>取值范围：<br>- HTTP（HTTP协议）<br>- HTTPS（HTTPS协议）<br>- DEFAULT（默认值）<br>默认值：无。<br>配置原则：<br>- DEFAULT代表TLSMODE以TOSCA模板中的VNF_TLS_MODE为准。<br>- 对安全要求较高的场景，可以设置为HTTPS，但会影响性能，需谨慎使用。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@INNERTLSMODE]] · TLS模式（INNERTLSMODE）

## 使用实例

设置hafetcd的TLS模式为http

```
SET INNERTLSMODE: SERVICETYPE=HAFETCD, TLSMODE=HTTP;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-INNERTLSMODE.md`
