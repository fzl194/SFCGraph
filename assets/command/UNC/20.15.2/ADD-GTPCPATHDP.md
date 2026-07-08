---
id: UNC@20.15.2@MMLCommand@ADD GTPCPATHDP
type: MMLCommand
name: ADD GTPCPATHDP（增加GTP-C路径管理自定义策略）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: GTPCPATHDP
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- GTP-C接口管理
- GTP-C协议管理
- GTP-C路径管理自定义策略
status: active
---

# ADD GTPCPATHDP（增加GTP-C路径管理自定义策略）

## 功能

**适用网元：SGSN**

该命令用于增加GTP-C路径管理自定义策略。

该命令引入一个系数钝化GTP-C路径故障的判定，每次T3*N3探测为一个判定周期，需要连续X个判定周期的Echo探测都没有响应后，才判定为GTP-C路径故障。

引入的这个系数会较大地钝化GTP-C路径故障的判定，若闪断频繁发生，钝化GTP-C路径故障判定条件会掩盖闪断的问题，此时GTP-C路径故障告警定位为反映对端长时间故障不通的问题。若未出现GTP-C路径故障告警但出现激活成功率下降，可以通过GTP-C接口跟踪，或者将故障判定条件调得更加灵敏来临时定位。

使用场景举例：

漫游路径的GTP-C路径故障告警较多，故障状态的GTP-C路径持续时长90%在4~10分钟内分布。通过调大漫游路径的故障判定条件高于10分钟，减少GTP-C路径故障告警。

## 注意事项

- 该命令目前只支持配置“路径范围”为“ROAMING（漫游路径）”的记录，且支持配置一条。
- 该命令执行后，“故障判定钝化系数”对新的故障判定生效，“漫游路径告警ID控制”对新产生的告警生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RANGE | 路径范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定该配置影响的GTP-C路径范围。<br>数据来源：本端规划<br>取值范围：<br>- ROAMING（漫游路径）<br>默认值：无<br>配置原则：<br>- 漫游路径是指Gp接口的GTP-C路径。 |
| PAS_COE | 故障判定钝化系数 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定判定GTP-C路径故障的钝化系数。设置钝化系数后，GTP-C路径故障的判定条件为：正常状态路径的Echo探测在（T3*N3）时长后未收到响应计为1组Echo探测无响应，连续X（X = 钝化系数值）组Echo探测无响应后，GTP-C路径状态才从正常变为故障。<br>比如，钝化系数设置为2，“1”表示Echo探测收到响应，“0”表示一组Echo探测未收到响应，GTP-C路径状态的结果如下：<br>11111 —— 正常<br>10101 —— 正常<br>11101 —— 正常<br>11100 —— 故障<br>11000 —— 故障<br>前提条件：在<br>“RANGE”<br>配置为<br>“ROAMING（漫游路径）”<br>时，才需要配置本参数。<br>数据来源：本端规划<br>取值范围：1~20<br>默认值：无<br>配置原则：<br>- 建议对于“漫游路径”调高该参数值，减少GTP-C路径故障告警的数量。 |
| GP_ALMID | 漫游路径告警ID控制 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定Gp接口GTP-C路径故障告警上报的告警ID是否与其他接口上报的告警ID相同。<br>数据来源：本端规划<br>取值范围：<br>- INDEP（独立告警ID）：Gp接口的GTP-C路径上报故障告警的ID为**ALM-80656 Gp接口GTPC路径故障**。<br>- COMMON（公共告警ID）：Gp接口的GTP-C路径上报故障告警的ID为**ALM-80610 GTPC路径故障**。<br>默认值：INDEP（独立告警ID）<br>配置原则：<br>- 前提条件：当“路径范围”为“ROAMING（漫游路径）”时，才需要配置。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/GTPCPATHDP]] · GTP-C路径管理自定义策略（GTPCPATHDP）

## 使用实例

配置漫游路径的钝化系数为3，使用独立的告警ID

ADD GTPCPATHDP: RANGE=ROAMING, PAS_COE=3, GP_ALMID=INDEP;

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-GTPCPATHDP.md`
