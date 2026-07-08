---
id: UNC@20.15.2@MMLCommand@SET DRAUTOACTIVE
type: MMLCommand
name: SET DRAUTOACTIVE（设置冷备容灾自动升主功能）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: DRAUTOACTIVE
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 可靠性管理
- 微服务可靠性管理
status: active
---

# SET DRAUTOACTIVE（设置冷备容灾自动升主功能）

## 功能

该命令用于冷备容灾场景下，设置自动升主功能。

## 注意事项

- 该命令执行后立即生效。

- 此命令只在冷备容灾模式下生效。
- 此命令只能在配置主网元执行。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| ISAUTOACTIVE | STBYTOACTTIME | NOAUTOTIME |
| --- | --- | --- |
| TRUE | 15 | 60 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ISAUTOACTIVE | 是否自动升主 | 可选必选说明：可选参数<br>参数含义：该参数用于配置在冷备容灾模式首次协商持续失败场景下是否自动升为运行主状态。<br>数据来源：全网规划<br>取值范围：<br>- TRUE（是）<br>- FALSE（否）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST DRAUTOACTIVE查询当前参数配置值。<br>配置原则：无 |
| STBYTOACTTIME | 运行备升为运行主所需的持续时间（分钟） | 可选必选说明：该参数在"ISAUTOACTIVE"配置为"TRUE"时为条件可选参数。<br>参数含义：该参数用于配置当参数“ISAUTOACTIVE”设置为“TRUE”后，持续多长时间可升为运行主状态。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~120。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST DRAUTOACTIVE查询当前参数配置值。<br>配置原则：无 |
| NOAUTOTIME | 配置不自动升主容忍时间（分钟） | 可选必选说明：该参数在"ISAUTOACTIVE"配置为"FALSE"时为条件可选参数。<br>参数含义：该参数用于配置当参数“ISAUTOACTIVE”设置为“FALSE”后，持续多长时间后上报“ALM-100686 自动升主配置错误”告警。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~65535。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST DRAUTOACTIVE查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@DRAUTOACTIVE]] · 冷备容灾自动升主功能参数（DRAUTOACTIVE）

## 使用实例

配置冷备容灾首次协商失败是否自动升主为是，持续失败15min运行备升为运行主：

```
%%SET DRAUTOACTIVE: ISAUTOACTIVE=TRUE, STBYTOACTTIME=15;%%
RETCODE = 0  操作成功

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-DRAUTOACTIVE.md`
