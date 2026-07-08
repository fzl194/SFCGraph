---
id: UNC@20.15.2@MMLCommand@SET NGCHRSTORCFG
type: MMLCommand
name: SET NGCHRSTORCFG（设置AMF小范围CHR存储配置）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: NGCHRSTORCFG
command_category: 配置类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- CHR管理
- NG接入小范围CHR配置
status: active
---

# SET NGCHRSTORCFG（设置AMF小范围CHR存储配置）

## 功能

**适用NF：AMF**

该命令用于设置AMF小范围CHR存储配置。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| CHRSPESUBSAVE | CHRSAVEPATH |
| --- | --- |
| DISABLE | SAVE_OMU |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CHRSPESUBSAVE | 小范围CHR使能开关 | 可选必选说明：可选参数<br>参数含义：该参数用于控制是否开启小范围CHR功能。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE（不使能）<br>- ENABLE（使能）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NGCHRSTORCFG查询当前参数配置值。<br>配置原则：<br>当UCF未部署时选择存储到OMU，否则按需选择。 |
| CHRSAVEPATH | 小范围CHR存储路径 | 可选必选说明：该参数在"CHRSPESUBSAVE"配置为"ENABLE"时为条件可选参数。<br>参数含义：该参数用于控制小范围CHR存储路径。<br>数据来源：本端规划<br>取值范围：<br>- SAVE_OMU（保存到OMU）<br>- SAVE_UCF（保存到UCF）<br>- SAVE_OMU_AND_UCF（保存到OMU和UCF）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NGCHRSTORCFG查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NGCHRSTORCFG]] · AMF小范围CHR存储配置（NGCHRSTORCFG）

## 使用实例

若开启小范围CHR功能且保存路径为OMU，执行如下命令：

```
SET NGCHRSTORCFG: CHRSPESUBSAVE=ENABLE, CHRSAVEPATH=SAVE_OMU;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-NGCHRSTORCFG.md`
