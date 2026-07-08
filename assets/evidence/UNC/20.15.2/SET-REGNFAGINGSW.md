# 设置NF实例老化开关（SET REGNFAGINGSW）

- [命令功能](#ZH-CN_MMLREF_0209652581__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0209652581__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0209652581__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0209652581__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0209652581)

**适用NF：NRF**

该命令用于设置NRF老化功能相关配置。

## [注意事项](#ZH-CN_MMLREF_0209652581)

- 该命令执行后立即生效。

- 主备或双活组网的场景下，如果需要配置此命令，则两个NRF上均需执行此命令，且配置参数一致。
- 当NF处于SUSPENDED状态，且NF实例老化开关为打开状态时，NRF会对该NF实例进行老化处理。
- 当超过配置的老化时长后，NRF会将该NF实例信息从NRF上删除。
- 当打开老化通知开关时，NRF会向所有订阅此NF实例的NF发送去注册事件通知。
- 双活容灾组网下，若数据备份状态为容灾通道故障状态，老化功能不触发。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| SWITCH | AGEINGTIMER | NRFAGINGNTFYSW |
| --- | --- | --- |
| SWITCH_ON | 1440 | SWITCH_ON |

#### [操作用户权限](#ZH-CN_MMLREF_0209652581)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0209652581)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SWITCH | 开关状态 | 可选必选说明：必选参数<br>参数含义：该参数用于表示NF实例的老化开关状态。开关打开，NRF会对所有NF实例进行老化处理；开关关闭，则NRF不对NF实例进行老化处理。<br>数据来源：本端规划<br>取值范围：<br>- SWITCH_ON（开启）<br>- SWITCH_OFF（关闭）<br>默认值：无。<br>配置原则：无 |
| AGEINGTIMER | 老化时长(分) | 可选必选说明：该参数在"SWITCH"配置为"SWITCH_ON"时为条件必选参数。<br>参数含义：该参数用于表示NF实例的老化时长。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~2880。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST REGNFAGINGSW查询当前参数配置值。<br>配置原则：无 |
| NRFAGINGNTFYSW | NRF老化通知开关 | 可选必选说明：该参数在"SWITCH"配置为"SWITCH_ON"时为条件可选参数。<br>参数含义：该参数用于控制当NF实例的老化开关状态设置为"SWITCH_ON"，NRF老化该NF实例时，是否发送去注册事件的通知消息。开关设置为"SWITCH_ON"时，NRF会发送通知消息，当开关设置"SWITCH_OFF"时，不发送通知消息。<br>数据来源：本端规划<br>取值范围：<br>- SWITCH_ON（开启）<br>- SWITCH_OFF（关闭）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST REGNFAGINGSW查询当前参数配置值。<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0209652581)

- 运营商希望关闭NF实例的老化开关时，配置此命令。配置完成后，将不会对NF实例进行老化处理。
  ```
  SET REGNFAGINGSW:SWITCH=SWITCH_OFF;
  ```
- 运营商希望重新配置NF实例的老化时长时，配置此命令。配置完成后，将会对所有NF以新的老化时长生效。
  ```
  SET REGNFAGINGSW: SWITCH=SWITCH_ON, AGEINGTIMER=60;
  ```
- 当运营商希望NRF老化NF实例时，NRF会向所有订阅此NF实例的NF发送去注册事件通知，配置此命令。
  ```
  SET REGNFAGINGSW: SWITCH=SWITCH_ON, AGEINGTIMER=60, NRFAGINGNTFYSW=SWITCH_ON;
  ```
