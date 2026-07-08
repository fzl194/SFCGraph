---
id: UNC@20.15.2@MMLCommand@SET SMSCHRSTORCFG
type: MMLCommand
name: SET SMSCHRSTORCFG（设置SMS小范围CHR存储配置）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: SMSCHRSTORCFG
command_category: 配置类
applicable_nf:
- SMSF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- SMSF业务管理
- CHR管理
status: active
---

# SET SMSCHRSTORCFG（设置SMS小范围CHR存储配置）

## 功能

**适用NF：SMSF**

该命令用于设置SMS小范围CHR存储配置。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| CHRSPESUBSAVE | CHRSAVEPATH |
| --- | --- |
| FUNC_OFF | SAVE_OMU |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CHRSPESUBSAVE | 小范围CHR使能开关 | 可选必选说明：可选参数<br>参数含义：该参数用于表示小范围CHR使能开关。<br>数据来源：本端规划<br>取值范围：<br>- “FUNC_ON（打开）”：功能开关打开<br>- “FUNC_OFF（关闭）”：功能开关关闭<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SMSCHRSTORCFG查询当前参数配置值。<br>配置原则：无 |
| CHRSAVEPATH | 小范围CHR存储路径 | 可选必选说明：该参数在"CHRSPESUBSAVE"配置为"FUNC_ON"时为条件可选参数。<br>参数含义：该参数用于表示小范围CHR存储路径。<br>数据来源：本端规划<br>取值范围：<br>- “SAVE_OMU（保存到OMU）”：表示保存到OMU。<br>- “SAVE_UCF（保存到UCF）”：表示保存到UCF。<br>- “SAVE_OMU_AND_UCF（保存到OMU和UCF）”：表示保存到OMU和UCF。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SMSCHRSTORCFG查询当前参数配置值。<br>配置原则：<br>当前只支持“SAVE_OMU(保存到OMU)”。 |

## 操作的配置对象

- [SMS小范围CHR存储配置（SMSCHRSTORCFG）](configobject/UNC/20.15.2/SMSCHRSTORCFG.md)

## 使用实例

运营商希望设置“小范围CHR使能开关”为“打开”，“小范围CHR存储路径”为“保存到OMU”的SMS小范围CHR存储配置，执行如下命令：

```
SET SMSCHRSTORCFG:CHRSPESUBSAVE=FUNC_ON, CHRSAVEPATH=SAVE_OMU;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置SMS小范围CHR存储配置（SET-SMSCHRSTORCFG）_04281145.md`
