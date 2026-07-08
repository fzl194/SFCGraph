---
id: UNC@20.15.2@MMLCommand@SET VLRFUNCSW
type: MMLCommand
name: SET VLRFUNCSW（设置VLR功能开关）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: VLRFUNCSW
command_category: 配置类
applicable_nf:
- SMSF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- VLR业务管理
- VLR功能开关
status: active
---

# SET VLRFUNCSW（设置VLR功能开关）

## 功能

**适用NF：SMSF**

该命令用于设置VLR短信业务功能开关。运营商可以根据需要设置VLR的不同功能。

## 注意事项

- 该命令执行后立即生效。

- 双活组网的场景下，如果需要配置此命令，则两个VLR上均需执行此命令，且配置参数一致。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| TMSIASSIGNSW | VLRREGRCSW | FORCEUPHLRSW | METRICSSTATSW | PURGEMSSW | HOMECHARGINGSW | FOREIGNCHARGSW |
| --- | --- | --- | --- | --- | --- | --- |
| FUNC_OFF | FUNC_OFF | FUNC_OFF | FUNC_ON | FUNC_ON | FUNC_OFF | FUNC_OFF |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TMSIASSIGNSW | VLR用户位置更新时分配TMSI开关 | 可选必选说明：可选参数<br>参数含义：该参数用于表示VLR用户进行位置更新时VLR分配TMSI的功能开关。<br>数据来源：本端规划<br>取值范围：<br>- “FUNC_ON（打开）”：功能开关打开<br>- “FUNC_OFF（关闭）”：功能开关关闭<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST VLRFUNCSW查询当前参数配置值。<br>配置原则：无 |
| VLRREGRCSW | VLR向注册中心注册开关 | 可选必选说明：可选参数<br>参数含义：该参数用于表示VLR向注册中心注册的功能开关。<br>数据来源：本端规划<br>取值范围：<br>- “FUNC_ON（打开）”：功能开关打开<br>- “FUNC_OFF（关闭）”：功能开关关闭<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST VLRFUNCSW查询当前参数配置值。<br>配置原则：无 |
| FORCEUPHLRSW | VLR向HLR强制更新开关 | 可选必选说明：可选参数<br>参数含义：该命令用于表示VLR用户位置更新流程中VLR向HLR强制更新的功能开关。<br>数据来源：本端规划<br>取值范围：<br>- “FUNC_ON（打开）”：功能开关打开<br>- “FUNC_OFF（关闭）”：功能开关关闭<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST VLRFUNCSW查询当前参数配置值。<br>配置原则：无 |
| METRICSSTATSW | VLR内部统计功能开关 | 可选必选说明：可选参数<br>参数含义：该参数用于表示VLR内部统计功能开关。<br>数据来源：本端规划<br>取值范围：<br>- “FUNC_ON（打开）”：功能开关打开<br>- “FUNC_OFF（关闭）”：功能开关关闭<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST VLRFUNCSW查询当前参数配置值。<br>配置原则：无 |
| PURGEMSSW | PURGE MS消息开关 | 可选必选说明：可选参数<br>参数含义：该参数用于表示VLR向HLR发送PURGE MS消息的功能开关。开关设置为FUNC_ON时，RMV VLRCTX命令执行后，会向HLR发送删除用户消息。开关设置为FUNC_OFF时，RMV VLRCTX命令不生效。<br>数据来源：本端规划<br>取值范围：<br>- “FUNC_ON（打开）”：功能开关打开<br>- “FUNC_OFF（关闭）”：功能开关关闭<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST VLRFUNCSW查询当前参数配置值。<br>配置原则：无 |
| HOMECHARGINGSW | 本网用户计费开关 | 可选必选说明：可选参数<br>参数含义：该参数用于控制本网用户计费开关，对于本网用户，打开开关后可以对短信的MO/MT发起计费请求。<br>数据来源：对端协商<br>取值范围：<br>- “FUNC_ON（打开）”：功能开关打开<br>- “FUNC_OFF（关闭）”：功能开关关闭<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST VLRFUNCSW查询当前参数配置值。<br>配置原则：无 |
| FOREIGNCHARGSW | 外网用户计费开关 | 可选必选说明：可选参数<br>参数含义：该参数用于控制外网用户计费开关，对于外网漫入到MSC/VLR的用户，打开开关后可以对短信的MO/MT发起计费请求。<br>数据来源：对端协商<br>取值范围：<br>- “FUNC_ON（打开）”：功能开关打开<br>- “FUNC_OFF（关闭）”：功能开关关闭<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST VLRFUNCSW查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [VLR功能开关（VLRFUNCSW）](configobject/UNC/20.15.2/VLRFUNCSW.md)

## 使用实例

运营商希望设置“VLR用户位置更新时分配TMSI开关”为“打开”，“VLR向注册中心注册开关”为“打开”，“VLR向HLR强制更新开关”为“打开”，“VLR内部统计功能开关”为“打开”时，执行如下命令：

```
SET VLRFUNCSW: TMSIASSIGNSW=FUNC_OFF, VLRREGRCSW=FUNC_OFF, FORCEUPHLRSW=FUNC_OFF, METRICSSTATSW=FUNC_OFF;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置VLR功能开关（SET-VLRFUNCSW）_53641466.md`
