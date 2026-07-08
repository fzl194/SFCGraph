---
id: UNC@20.15.2@MMLCommand@SET HSMFCHGCTRL
type: MMLCommand
name: SET HSMFCHGCTRL（设置漫游用户在归属地的计费方式和漫游参数的协商方式）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: HSMFCHGCTRL
command_category: 配置类
applicable_nf:
- SMF
- PGW-C
- GGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 融合计费
- QBC计费控制
status: active
---

# SET HSMFCHGCTRL（设置漫游用户在归属地的计费方式和漫游参数的协商方式）

## 功能

**适用NF：SMF、PGW-C、GGSN**

该命令用于控制漫游用户在归属地的计费方式和Roaming Charging Profile的协商方式。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| CHGMODE | FBCNEGRCPSW | LOCALRCPSELMODE |
| --- | --- | --- |
| FBC | DISABLE | LOCALCFG |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CHGMODE | 计费模式 | 可选必选说明：可选参数<br>参数含义：该参数用于设置漫游用户在归属地的计费方式。<br>数据来源：全网规划<br>取值范围：<br>- “FBC（FBC计费）”：漫游用户在归属地使用FBC计费。<br>- “QBC（QBC计费）”：漫游用户在归属地使用QBC计费。<br>- “NOCHG（不计费）”：漫游用户在归属地不做计费功能。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST HSMFCHGCTRL查询当前参数配置值。<br>配置原则：无 |
| FBCNEGRCPSW | FBC计费漫游参数协商开关 | 可选必选说明：可选参数<br>参数含义：该参数用于设置漫游用户在归属地做FBC计费时是否和H-CHF进行Roaming Charging Profile的协商。<br>数据来源：全网规划<br>取值范围：<br>- “DISABLE（不使能）”：不和H-CHF协商Roaming Charging Profile。<br>- “ENABLE（使能）”：和H-CHF协商Roaming Charging Profile。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST HSMFCHGCTRL查询当前参数配置值。<br>配置原则：<br>该配置为全局配置，当ADD VPLMNCHGMODE的CHGMODE参数配置成FBC计费时，也受本参数控制。 |
| LOCALRCPSELMODE | 本地漫游参数获取方式 | 可选必选说明：可选参数<br>参数含义：该参数用于设置漫游用户在归属地未从H-CHF获取到Roaming Charging Profile时，Roaming Charging Profile协商结果的获取方式。<br>数据来源：全网规划<br>取值范围：<br>- “LOCALCFG（使用本地配置）”：使用本地配置生成Roaming Charging Profile。<br>- “VSMF（使用V-SMF携带的参数）”：使用V-SMF携带的Roaming Charging Profile。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST HSMFCHGCTRL查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@HSMFCHGCTRL]] · 漫游用户在归属地的计费方式和漫游参数的协商方式（HSMFCHGCTRL）

## 使用实例

设置漫游用户在归属地的计费方式为QBC，未从H-CHF获取到Roaming Charging Profile时，使用本地配置生成：

```
SET HSMFCHGCTRL: CHGMODE=QBC, LOCALRCPSELMODE=LOCALCFG;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-HSMFCHGCTRL.md`
