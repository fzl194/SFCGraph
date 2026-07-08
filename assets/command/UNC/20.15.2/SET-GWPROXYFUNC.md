---
id: UNC@20.15.2@MMLCommand@SET GWPROXYFUNC
type: MMLCommand
name: SET GWPROXYFUNC（设置网关Proxy功能）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: GWPROXYFUNC
command_category: 配置类
applicable_nf:
- PGW-C
- GGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- GGSN和P-GW Proxy
- 网关Proxy功能
status: active
---

# SET GWPROXYFUNC（设置网关Proxy功能）

## 功能

**适用NF：PGW-C、GGSN**

该命令用于设置网关Proxy功能配置。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| PROXYSW | RECOVERY |
| --- | --- |
| DISABLE | 0 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROXYSW | Proxy功能开关 | 可选必选说明：可选参数<br>参数含义：该参数用于控制是否打开网关Proxy功能。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE（不使能）<br>- ENABLE（使能）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST GWPROXYFUNC查询当前参数配置值。<br>配置原则：无 |
| RECOVERY | 重启计数器 | 可选必选说明：可选参数<br>参数含义：该参数用于控制Proxy GGSN/PGW在转发用户激活请求消息时将消息中的Recovery信元替换成本参数设置的值。该参数也适用于Echo消息。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~255。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST GWPROXYFUNC查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/GWPROXYFUNC]] · 网关Proxy功能配置（GWPROXYFUNC）

## 使用实例

打开网关proxy功能，并且设置重启计数器值为1：

```
SET GWPROXYFUNC:PROXYSW=ENABLE,RECOVERY=1;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置网关Proxy功能（SET-GWPROXYFUNC）_42853270.md`
