---
id: UNC@20.15.2@MMLCommand@SET ROAMMGMTPARA
type: MMLCommand
name: SET ROAMMGMTPARA（设置漫游管理参数）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: ROAMMGMTPARA
command_category: 配置类
applicable_nf:
- AMF
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 服务化接口管理
- 注册与服务发现
- 漫游参数管理
status: active
---

# SET ROAMMGMTPARA（设置漫游管理参数）

## 功能

**适用NF：AMF、SMF**

该命令用于配置漫游管理参数。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| IDENTGATEWAYSW | AVOIDNFMISUSESW |
| --- | --- |
| OFF | OFF |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IDENTGATEWAYSW | 识别关口局NF开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定漫游场景下是否根据对端NF的IP/FQDN识别是否为关口局NF。<br>数据来源：本端规划<br>取值范围：<br>- OFF（OFF）<br>- ON（ON）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST ROAMMGMTPARA查询当前参数配置值。<br>配置原则：<br>当存在NSA用户通过SA网络漫游接入时，需开启本开关。 |
| AVOIDNFMISUSESW | 避免网元混用开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定是否避免混用本网网元和异网网元。<br>数据来源：本端规划<br>取值范围：<br>- OFF（OFF）<br>- ON（ON）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST ROAMMGMTPARA查询当前参数配置值。<br>配置原则：<br>开启本开关后，本网用户只能从本地或缓存中发现本网网元，异网用户只能从本地或缓存中发现异网网元。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/ROAMMGMTPARA]] · 漫游管理参数（ROAMMGMTPARA）

## 使用实例

设置开启识别关口局NF开关。

```
SET ROAMMGMTPARA:IDENTGATEWAYSW=ON;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-ROAMMGMTPARA.md`
