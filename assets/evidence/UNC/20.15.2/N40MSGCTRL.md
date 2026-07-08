# 设置N40接口消息的控制参数（SET N40MSGCTRL）

- [命令功能](#ZH-CN_MMLREF_0000001878393532__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001878393532__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001878393532__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001878393532__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0000001878393532)

**适用NF：PGW-C、SMF、GGSN**

该命令用于设置N40接口消息的控制参数。

## [注意事项](#ZH-CN_MMLREF_0000001878393532)

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| ROAMOFFSTARTSW | UPFID23G | PRAINFO23G | SLICINGINFO23G | SSCMODE23G | DNNSELMODE23G | STOPINDICTR23G | UCITIMER23G |
| --- | --- | --- | --- | --- | --- | --- | --- |
| DISABLE | ENABLE | ENABLE | ENABLE | ENABLE | ENABLE | ENABLE | ENABLE |

#### [操作用户权限](#ZH-CN_MMLREF_0000001878393532)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001878393532)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ROAMOFFSTARTSW | 国际漫游场景更新流程中仅离线新业务预申请上报CHF开关 | 可选必选说明：可选参数<br>参数含义：该参数用于控制国际漫游场景下SMF与CHF的更新流程仅离线新业务预申请时是否上报CHF。<br>数据来源：本端规划<br>取值范围：<br>- “DISABLE（不使能）”：国际漫游场景更新流程中仅离线新业务预申请时上报CHF。<br>- “ENABLE（使能）”：国际漫游场景更新流程中仅离线新业务预申请时不上报CHF。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST N40MSGCTRL查询当前参数配置值。<br>配置原则：无 |
| UPFID23G | GERAN/UTRAN接入场景携带UPFID | 可选必选说明：可选参数<br>参数含义：该参数用于控制GERAN/UTRAN接入场景是否携带UPFID。<br>数据来源：本端规划<br>取值范围：<br>- “DISABLE（不使能）”：GERAN/UTRAN接入场景不携带UPFID。<br>- “ENABLE（使能）”：GERAN/UTRAN接入场景携带UPFID。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST N40MSGCTRL查询当前参数配置值。<br>配置原则：无 |
| PRAINFO23G | GERAN/UTRAN接入场景携带Presence Reporting Area Information | 可选必选说明：可选参数<br>参数含义：该参数用于控制GERAN/UTRAN接入场景是否携带Presence Reporting Area Information。<br>数据来源：本端规划<br>取值范围：<br>- “DISABLE（不使能）”：GERAN/UTRAN接入场景不携带Presence Reporting Area Information。<br>- “ENABLE（使能）”：GERAN/UTRAN接入场景携带Presence Reporting Area Information。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST N40MSGCTRL查询当前参数配置值。<br>配置原则：无 |
| SLICINGINFO23G | GERAN/UTRAN接入场景携带Network Slicing Information | 可选必选说明：可选参数<br>参数含义：该参数用于控制GERAN/UTRAN接入场景是否携带Network Slicing Information。<br>数据来源：本端规划<br>取值范围：<br>- “DISABLE（不使能）”：GERAN/UTRAN接入场景不携带Network Slicing Information。<br>- “ENABLE（使能）”：GERAN/UTRAN接入场景携带Network Slicing Information。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST N40MSGCTRL查询当前参数配置值。<br>配置原则：无 |
| SSCMODE23G | GERAN/UTRAN接入场景携带SSC Mode | 可选必选说明：可选参数<br>参数含义：该参数用于控制GERAN/UTRAN接入场景是否携带SSC Mode。<br>数据来源：本端规划<br>取值范围：<br>- “DISABLE（不使能）”：GERAN/UTRAN接入场景不携带SSC Mode。<br>- “ENABLE（使能）”：GERAN/UTRAN接入场景携带SSC Mode。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST N40MSGCTRL查询当前参数配置值。<br>配置原则：无 |
| DNNSELMODE23G | GERAN/UTRAN接入场景携带DNN Selection Mode | 可选必选说明：可选参数<br>参数含义：该参数用于控制GERAN/UTRAN接入场景是否携带DNN Selection Mode。<br>数据来源：本端规划<br>取值范围：<br>- “DISABLE（不使能）”：GERAN/UTRAN接入场景不携带DNN Selection Mode。<br>- “ENABLE（使能）”：GERAN/UTRAN接入场景携带DNN Selection Mode。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST N40MSGCTRL查询当前参数配置值。<br>配置原则：无 |
| STOPINDICTR23G | GERAN/UTRAN接入场景携带Session Stop Indicator | 可选必选说明：可选参数<br>参数含义：该参数用于控制GERAN/UTRAN接入场景是否携带Session Stop Indicator。<br>数据来源：本端规划<br>取值范围：<br>- “DISABLE（不使能）”：GERAN/UTRAN接入场景不携带Session Stop Indicator。<br>- “ENABLE（使能）”：GERAN/UTRAN接入场景携带Session Stop Indicator。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST N40MSGCTRL查询当前参数配置值。<br>配置原则：无 |
| UCITIMER23G | GERAN/UTRAN接入场景携带Unit Count Inactivity Timer | 可选必选说明：可选参数<br>参数含义：该参数用于控制GERAN/UTRAN接入场景是否携带Unit Count Inactivity Timer。<br>数据来源：本端规划<br>取值范围：<br>- “DISABLE（不使能）”：GERAN/UTRAN接入场景不携带Unit Count Inactivity Timer。<br>- “ENABLE（使能）”：GERAN/UTRAN接入场景携带Unit Count Inactivity Timer。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST N40MSGCTRL查询当前参数配置值。<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0000001878393532)

设置国际漫游场景下在更新流程中仅离线新业务预申请不需要上报CHF：

```
SET N40MSGCTRL: ROAMOFFSTARTSW=ENABLE;
```
