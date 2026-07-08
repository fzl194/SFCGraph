---
id: UDG@20.15.2@MMLCommand@SET DRGROUPABLEMENT
type: MMLCommand
name: SET DRGROUPABLEMENT（设置是否使能热备容灾组）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: DRGROUPABLEMENT
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 可靠性管理
- 微服务可靠性管理
status: active
---

# SET DRGROUPABLEMENT（设置是否使能热备容灾组）

## 功能

该命令用于设置是否使能热备容灾组。

> **说明**
> - 该命令执行后立即生效。
>
> - 该命令只用于在UEG-M/UEG网元采用主备（热备）容灾模式下执行。
>
> - 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：
>
> | DRGROUPABLEMENT | ISAUTOACTIVE |
> | --- | --- |
> | DISABLE | FALSE |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DRGROUPABLEMENT | 是否使能热备容灾组 | 可选必选说明：必选参数<br>参数含义：该参数用于是否使能热备容灾组。<br>数据来源：全网规划<br>取值范围：<br>- ENABLE（使能热备容灾功能）<br>- DISABLE（去使能热备容灾功能）<br>默认值：无。<br>配置原则：无 |
| ISAUTOACTIVE | 是否自动升主 | 可选必选说明：可选参数<br>参数含义：该参数用于配置在热备容灾模式首次协商持续失败场景下是否自动升为运行主状态。<br>数据来源：全网规划<br>取值范围：<br>- TRUE（是）<br>- FALSE（否）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST DRGROUPABLEMENT查询当前参数配置值。<br>配置原则：<br>热备容灾使能若配置为不自动升主，容灾控制通道异常时，通过<br>[**SWAP DR**](容灾实例主备倒换（SWAP DR）_23235166.md)<br>命令强制升主。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@DRGROUPABLEMENT]] · 是否使能热备容灾组（DRGROUPABLEMENT）

## 使用实例

使能热备容灾组:

```
%%SET DRGROUPABLEMENT: DRGROUPABLEMENT=ENABLE;%%
RETCODE = 0  操作成功

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-DRGROUPABLEMENT.md`
