---
id: UDG@20.15.2@MMLCommand@SET HTTPFQDNSW
type: MMLCommand
name: SET HTTPFQDNSW（设置HTTP是否支持FQDN）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: HTTPFQDNSW
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- HTTP功能管理
- HTTP管理
- HTTP FQDN管理
status: active
---

# SET HTTPFQDNSW（设置HTTP是否支持FQDN）

## 功能

该命令用于设置HTTP是否支持FQDN。

- 当前应用场景：控制HTTP是否使用响应报文中Location字段携带的FQDN。

> **说明**
> - 该命令执行后立即生效。
>
> - 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：
>
> | GLOBALSW | INDIRECTSW |
> | --- | --- |
> | OFF | OFF |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GLOBALSW | 全局FQDN开关 | 可选必选说明：可选参数<br>参数含义：该参数用于全局控制HTTP是否使用响应报文中Location字段携带的FQDN。<br>数据来源：全网规划<br>取值范围：<br>- “ON（打开）”：打开<br>- “OFF（关闭）”：关闭<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST HTTPFQDNSW查询当前参数配置值。<br>配置原则：<br>- "GLOBALSW"打开，表示直连和间接路由场景都支持；间接路由场景不再受"INDIRECTSW"控制；<br>- "GLOBALSW"关闭，表示直连场景不支持；根据"INDIRECTSW"控制间接路由场景是否支持。 |
| INDIRECTSW | 间接路由场景FQDN开关 | 可选必选说明：可选参数<br>参数含义：该参数用于控制间接路由场景下HTTP是否使用响应报文中Location字段携带的FQDN。<br>数据来源：全网规划<br>取值范围：<br>- “ON（打开）”：打开<br>- “OFF（关闭）”：关闭<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST HTTPFQDNSW查询当前参数配置值。<br>配置原则：<br>- "INDIRECTSW"打开，表示间接路由场景支持；<br>- "INDIRECTSW"关闭，根据"GLOBALSW"控制间接路由场景是否支持。 |

## 操作的配置对象

- [HTTP是否支持FQDN（HTTPFQDNSW）](configobject/UDG/20.15.2/HTTPFQDNSW.md)

## 使用实例

打开HTTP的直连模式下FQDN开关，可以执行如下命令：

```
SET HTTPFQDNSW: GLOBALSW=ON;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置HTTP是否支持FQDN（SET-HTTPFQDNSW）_54530882.md`
