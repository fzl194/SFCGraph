---
id: UNC@20.15.2@MMLCommand@SET SESSNCHRSTORECFG
type: MMLCommand
name: SET SESSNCHRSTORECFG（设置CHR存储配置）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: SESSNCHRSTORECFG
command_category: 配置类
applicable_nf:
- SGW-C
- PGW-C
- SMF
- GGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- CHR管理
- CHR存储配置
status: active
---

# SET SESSNCHRSTORECFG（设置CHR存储配置）

## 功能

**适用NF：SGW-C、PGW-C、SMF、GGSN**

该命令用于设置CHR存储配置。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| CHRFAILSAVE | CHRALLSAVE | CHRSPESUBSAVE | CHRSAVEPATH |
| --- | --- | --- | --- |
| ENABLE | DISABLE | ENABLE | SAVE_OMU |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CHRFAILSAVE | UCF保存异常CHR开关 | 可选必选说明：可选参数<br>参数含义：该参数用于控制UCF是否保存异常CHR单据。本参数和CHRALLSAVE参数中任意一个使能时异常CHR单据均可以保存在UCF中。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE（不使能）<br>- ENABLE（使能）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SESSNCHRSTORECFG查询当前参数配置值。<br>配置原则：无 |
| CHRALLSAVE | UCF保存整系统CHR开关 | 可选必选说明：可选参数<br>参数含义：该参数用于控制UCF是否保存整系统CHR单据。本参数和CHRFAILSAVE参数中任意一个使能时异常CHR单据均可以保存在UCF中。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE（不使能）<br>- ENABLE（使能）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SESSNCHRSTORECFG查询当前参数配置值。<br>配置原则：无 |
| CHRSPESUBSAVE | 小范围CHR使能开关 | 可选必选说明：可选参数<br>参数含义：该参数用于控制是否开启小范围CHR功能。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE（不使能）<br>- ENABLE（使能）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SESSNCHRSTORECFG查询当前参数配置值。<br>配置原则：无 |
| CHRSAVEPATH | 小范围CHR存储路径 | 可选必选说明：该参数在"CHRSPESUBSAVE"配置为"ENABLE"时为条件必选参数。<br>参数含义：该参数用于控制小范围CHR单据的存储路径。<br>数据来源：本端规划<br>取值范围：<br>- SAVE_OMU（保存到OMU）<br>- SAVE_UCF（保存到UCF）<br>- SAVE_OMU_AND_UCF（保存到OMU和UCF）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SESSNCHRSTORECFG查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SESSNCHRSTORECFG]] · CHR存储配置（SESSNCHRSTORECFG）

## 使用实例

设置CHR存储方式，异常流程单据存盘开关关闭，整系统CHR单据存盘开关打开：

```
SET SESSNCHRSTORECFG: CHRFAILSAVE=DISABLE, CHRALLSAVE=ENABLE;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-SESSNCHRSTORECFG.md`
