---
id: UNC@20.15.2@MMLCommand@SET RRCINACTPARA
type: MMLCommand
name: SET RRCINACTPARA（设置RRC Inactive参数）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: RRCINACTPARA
command_category: 配置类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- RRC Inactive业务管理
- RRC Inactive参数
status: active
---

# SET RRCINACTPARA（设置RRC Inactive参数）

## 功能

**适用NF：AMF**

该命令用于设置RRC Inactive参数。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| LOCTMOUT |
| --- |
| FAILRSP |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LOCTMOUT | 位置获取超时 | 可选必选说明：可选参数<br>参数含义：该参数用于指定因UE进入RRC Inactive状态导致的获取位置信息超时，给周边网元的位置信息。<br>数据来源：全网规划<br>取值范围：<br>- “FAILRSP（失败响应）”：失败响应。<br>- “LASTLOC（上次位置）”：AMF中记录的上次位置。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST RRCINACTPARA查询当前参数配置值。<br>配置原则：<br>无。<br>说明：<br>若此参数配置为“FAILRSP（失败响应）”，会导致周边网元获取位置信息失败。<br>若此参数配置为“LASTLOC（上次位置）”，会导致周边网元无法获取实时位置。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/RRCINACTPARA]] · RRC Inactive参数（RRCINACTPARA）

## 使用实例

设置位置获取超时后给周边网元发送AMF中记录的上次位置，执行如下命令：

```
SET RRCINACTPARA: LOCTMOUT=LASTLOC;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-RRCINACTPARA.md`
