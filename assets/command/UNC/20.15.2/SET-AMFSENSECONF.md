---
id: UNC@20.15.2@MMLCommand@SET AMFSENSECONF
type: MMLCommand
name: SET AMFSENSECONF（设置AMF感知配置）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: AMFSENSECONF
command_category: 配置类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 感知业务管理
- 感知核查管理
status: active
---

# SET AMFSENSECONF（设置AMF感知配置）

## 功能

**适用NF：AMF**

在部署感知的场景下，通过SET AMFSENSECONF命令设置AMF对感知的全局配置，例如感知能力核查消息开关、设置核查周期等功能。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| SFCCHKSW | SFCCHKPERIOD |
| --- | --- |
| DISABLE | 5 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SFCCHKSW | SFC基站感知能力核查开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定是否定时向SFC网元发送基站感知能力核查消息。<br>数据来源：本端规划<br>取值范围：<br>- ENABLE（开启）<br>- DISABLE（关闭）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST AMFSENSECONF查询当前参数配置值。<br>配置原则：无 |
| SFCCHKPERIOD | SFC基站感知能力核查消息发送周期(min) | 可选必选说明：可选参数<br>参数含义：该参数用于指定向SFC发送基站感知能力核查消息的间隔。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是5~30，单位是分钟。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST AMFSENSECONF查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@AMFSENSECONF]] · AMF感知配置（AMFSENSECONF）

## 使用实例

若运营商希望开启向SFC发送基站感知能力核查消息的功能，可以用如下命令：

```
SET AMFSENSECONF: SFCCHKSW=DISABLE;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-AMFSENSECONF.md`
