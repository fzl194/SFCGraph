---
id: UNC@20.15.2@MMLCommand@SET NRFDATACHK
type: MMLCommand
name: SET NRFDATACHK（设置NRF数据核查相关参数）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: NRFDATACHK
command_category: 配置类
applicable_nf:
- NRF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- NRF业务参数
- NRF数据一致性核查
status: active
---

# SET NRFDATACHK（设置NRF数据核查相关参数）

## 功能

**适用NF：NRF**

该命令用于设置NRF数据核查相关参数。通过此命令NRF可以对存储的NF Profile数据进行一致性校验。

## 注意事项

- 该命令执行后立即生效。

- 主备或双活组网的场景下，如果需要配置此命令，则两个NRF上均需执行此命令，且配置参数一致。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| CHECKFUNCSW | PERRIOD | ALARMSWITCH | HBRSPSWITCH |
| --- | --- | --- | --- |
| FUNC_OFF | 15 | FUNC_OFF | FUNC_OFF |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CHECKFUNCSW | 数据一致性核查功能开关 | 可选必选说明：可选参数<br>参数含义：该参数用于表示NF Profile数据一致性核查功能开关。当该开关打开时，NRF进行数据一致性核查。当该开关关闭时，NRF不进行数据一致性核查。<br>数据来源：本端规划<br>取值范围：<br>- FUNC_ON（打开）<br>- FUNC_OFF（关闭）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NRFDATACHK查询当前参数配置值。<br>配置原则：无 |
| PERRIOD | 核查周期(分) | 可选必选说明：可选参数<br>参数含义：该参数用于表示核查周期的时长。当NRF定时器针对某一NF进行计时，计时时长与随机偏移值累积达到核查周期后，开始对该NF进行数据核查，查看当前时间的NF数据与核查前的数据是否一致。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~1440，单位是分钟。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NRFDATACHK查询当前参数配置值。<br>配置原则：无 |
| ALARMSWITCH | 核查失败告警开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定是否上报告警"ALM-100279 数据一致性核查失败"。开关打开后，若连续三个核查周期核查该NF Profile。<br>数据一致性都失败时，会上报告警"ALM-100279 数据一致性核查失败"；开关关闭则不上报告警"ALM-100279 数据一致性核查失败"。<br>数据来源：本端规划<br>取值范围：<br>- FUNC_ON（打开）<br>- FUNC_OFF（关闭）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NRFDATACHK查询当前参数配置值。<br>配置原则：无 |
| HBRSPSWITCH | 回复心跳失败开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定核查失败情况下，NRF是否通过心跳响应回复404 Not Found，触发NF侧向NRF发起全量更新，使该NF的Profile数据刷新正确。开关打开时表示NRF回复404，反之NRF正常处理心跳。<br>数据来源：本端规划<br>取值范围：<br>- FUNC_ON（打开）<br>- FUNC_OFF（关闭）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NRFDATACHK查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NRFDATACHK]] · NRF数据一致性核查相关参数（NRFDATACHK）

## 使用实例

运营商希望在数据一致性核查功能打开时，NF Profile核查失败，只上报告警"ALM-100279 数据一致性核查失败"，不对该NF的心跳请求返回404，需要将HBRSPSWITCH设置为FUNC_OFF。

```
SET NRFDATACHK: HBRSPSWITCH=FUNC_OFF;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-NRFDATACHK.md`
