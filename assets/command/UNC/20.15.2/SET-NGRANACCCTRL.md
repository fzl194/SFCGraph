---
id: UNC@20.15.2@MMLCommand@SET NGRANACCCTRL
type: MMLCommand
name: SET NGRANACCCTRL（设置5G基站接入控制策略）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: NGRANACCCTRL
command_category: 配置类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- N2接口管理
- NGRAN接入管理控制
status: active
---

# SET NGRANACCCTRL（设置5G基站接入控制策略）

## 功能

![](设置5G基站接入控制策略（SET NGRANACCCTRL）_58492657.assets/notice_3.0-zh-cn_2.png)

功能开启前，需要对已接入基站的TAC进行检查，确认是否在规划范围内，避免功能开启后，已接入的基站断链后无法再次接入，导致业务受损。

**适用NF：AMF**

此命令用于配置5G基站接入控制参数，根据基站所在的TAC区域，控制是否允许基站接入。当希望只允许在白名单TAC区的基站接入时，可执行此命令。

## 注意事项

- 该命令执行后立即生效。

- 功能开启前，需要提前规划好允许基站接入的TAC全集，并通过ADD NGTAGP、ADD NGTAGPMEM进行配置。
- 功能开启前，需要对已接入基站的TAC进行检查，确认是否在规划范围内，避免功能开启后，已接入的基站断链后无法再次接入，导致业务受损。
- 功能开启后，AMF对于不满足TAC区域规划且已接入的基站不主动断链，在基站下次建链时进行限制。
- 基站建链消息中携带的任意一个TAC只要在配置范围内则允许建链。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| NGRANACCSW | NGTAGPID |
| --- | --- |
| OFF | 0 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NGRANACCSW | 基于位置区基站接入限制开关 | 可选必选说明：可选参数<br>参数含义：该参数用于设置是否开启基于位置区基站接入限制功能。<br>数据来源：本端规划<br>取值范围：<br>- “ON（开启）”：开启基于位置区基站接入限制功能<br>- “OFF（关闭）”：关闭基于位置区基站接入限制功能<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NGRANACCCTRL查询当前参数配置值。<br>配置原则：<br>当运营商希望只允许指定TAC区（通过ADD NGTAGP、ADD NGTAGPMEM进行配置）的基站与AMF建链时，将本参数设置为“ON（开启）”。 |
| NGTAGPID | 跟踪区群组标识 | 可选必选说明：该参数在"NGRANACCSW"配置为"ON"时为条件必选参数。<br>参数含义：该参数用于指定跟踪区群组标识。该参数已经通过ADD NGTAGP命令中的NGTAGPID参数配置。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~256。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NGRANACCCTRL查询当前参数配置值。<br>配置原则：<br>该参数需在ADD NGTAGP中配置。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NGRANACCCTRL]] · 5G基站接入控制策略（NGRANACCCTRL）

## 使用实例

运营商希望只允许TAC组ID为1的基站接入AMF，可执行如下命令。

```
SET NGRANACCCTRL: NGRANACCSW=ON, NGTAGPID=1;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-NGRANACCCTRL.md`
