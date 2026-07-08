---
id: UDG@20.15.2@MMLCommand@SET TCPKEEPALIVECFG
type: MMLCommand
name: SET TCPKEEPALIVECFG（设置TCP保活参数）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: TCPKEEPALIVECFG
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- IPAPM功能管理
- TWAMP
- TCP保活配置
status: active
---

# SET TCPKEEPALIVECFG（设置TCP保活参数）

## 功能

该命令用于设置TWAMP的Full模式TCP保活参数配置。

> **说明**
> - 该命令执行后在TCP链路重建时生效。
>
> - 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：
>
> | KEEPALIVETIME | INTERVAL | RETRY |
> | --- | --- | --- |
> | 90 | 30 | 9 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| KEEPALIVETIME | 保活时间 | 可选必选说明：可选参数<br>参数含义：保活时间是在空闲条件下两次保活传输之间的持续时间。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是30~7200，单位是秒。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST TCPKEEPALIVECFG查询当前参数配置值。<br>配置原则：无 |
| INTERVAL | 保活间隔 | 可选必选说明：可选参数<br>参数含义：保活间隔是两次连续保活重传之间的持续时间，如果没有收到对上一次保活传输的确认。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是10~300，单位是秒。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST TCPKEEPALIVECFG查询当前参数配置值。<br>配置原则：无 |
| RETRY | 保活重试 | 可选必选说明：可选参数<br>参数含义：保活重试是在声明远程端不可用之前要执行的重传次数。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是3~20，单位是次。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST TCPKEEPALIVECFG查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/TCPKEEPALIVECFG]] · TCP保活参数（TCPKEEPALIVECFG）

## 关联任务

- [[UDG@20.15.2@Task@0-00229]]

## 使用实例

设置TCP保活参数配置的实例：

```
SET TCPKEEPALIVECFG: KEEPALIVETIME=90, INTERVAL=30, RETRY=8;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置TCP保活参数（SET-TCPKEEPALIVECFG）_27102484.md`
