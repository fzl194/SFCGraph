---
id: UDG@20.15.2@MMLCommand@SET DCSLIVEPARAS
type: MMLCommand
name: SET DCSLIVEPARAS（设置DCS直播参数）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: DCSLIVEPARAS
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- MML命令
- 系统资源配置
status: active
---

# SET DCSLIVEPARAS（设置DCS直播参数）

## 功能

该命令用于设置DCS直播参数。

> **说明**
> - 该命令执行后立即生效。
>
> - 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：
>
> | READBEHINDTHRES | PUBTIMEOUT | PUBVERIFYPERIOD | SUBVERIFYPERIOD | LIVEAGINGPERIOD |
> | --- | --- | --- | --- | --- |
> | 3 | 200 | 30 | 30 | 30 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| READBEHINDTHRES | 读滞后阈值（MB） | 可选必选说明：可选参数<br>参数含义：该参数用于表示允许直播读取数据落后最新数据的量的最大值，超过该阈值将启动视频读取加速。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~5，单位是兆字节。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST DCSLIVEPARAS查询当前参数配置值。<br>配置原则：无 |
| PUBTIMEOUT | 回源超时阈值（ms） | 可选必选说明：可选参数<br>参数含义：该参数用于表示回源超时阈值，回源指从源头CDN拉取视频数据。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是10~30000，单位是毫秒。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST DCSLIVEPARAS查询当前参数配置值。<br>配置原则：无 |
| PUBVERIFYPERIOD | 回源超时检查周期（s） | 可选必选说明：可选参数<br>参数含义：该参数用于表示回源超时检查周期。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~4294967295，单位是秒。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST DCSLIVEPARAS查询当前参数配置值。<br>配置原则：无 |
| SUBVERIFYPERIOD | 订阅关系核查周期（Min） | 可选必选说明：可选参数<br>参数含义：该参数用于表示订阅关系核查周期，避免UE去订阅直播未通知给DCS，导致订阅关系残留。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~720，单位是分钟。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST DCSLIVEPARAS查询当前参数配置值。<br>配置原则：无 |
| LIVEAGINGPERIOD | 直播资源老化周期（s） | 可选必选说明：可选参数<br>参数含义：该参数用于表示直播资源老化周期，直播资源老化用于回收已结束的或无人订阅的直播资源。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~720，单位是秒。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST DCSLIVEPARAS查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [DCS直播参数（DCSLIVEPARAS）](configobject/UDG/20.15.2/DCSLIVEPARAS.md)

## 使用实例

设置DCS直播参数，其中读滞后阈值取值为3，回源超时阈值取值为200，回源超时检查周期取值为1，订阅关系核查周期取值为30，直播资源老化周期取值为30。

```
%%SET DCSLIVEPARAS: READBEHINDTHRES=3, PUBTIMEOUT=200, PUBVERIFYPERIOD=1, SUBVERIFYPERIOD=30, LIVEAGINGPERIOD=30;%%
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置DCS直播参数（SET-DCSLIVEPARAS）_76129918.md`
