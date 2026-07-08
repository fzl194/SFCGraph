---
id: UNC@20.15.2@MMLCommand@SET MSFAULTTOLERANCE
type: MMLCommand
name: SET MSFAULTTOLERANCE（设置故障检测参数）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: MSFAULTTOLERANCE
command_category: 配置类
effect_mode: 立即生效
is_dangerous: true
category_path:
- 平台服务管理
- 可靠性管理
- 微服务可靠性管理
status: active
---

# SET MSFAULTTOLERANCE（设置故障检测参数）

## 功能

![](设置故障检测参数（SET MSFAULTTOLERANCE）_09587879.assets/notice_3.0-zh-cn_2.png)

本命令属于高危命令，配置小于默认值可能会导致业务故障，请谨慎使用并联系华为技术支持协助操作。

该命令用于设置正向监控和反向监控的超时时长，防脑裂自杀功能开关。

## 注意事项

- 该命令执行后立即生效。

- 当前版本参数PROCESSFORWARD，PROCESSREVERSE的配置不生效。
- 配置小于默认值可能会导致业务故障，建议保持默认值不变，如果要修改，建议配置不小于默认值。
- 超时时长(毫秒)等于超时周期数乘以心跳周期乘以100。
- 如需修改，要求进程级正向监控超时时长大于进程级反向监控超时时长，多连接正向监控超时时长大于多连接反向监控超时时长，多连接正向监控超时时长小于等于进程级正向监控超时时长，多连接反向监控超时时长小于等于进程级反向监控超时时长。
- 如需修改正反向监控超时时长，建议通过命令[**LST MCSWITCH**](查询多连接开关配置数据（LST MCSWITCH）_46243299.md)查询多连接开关，如果开关开启，建议配置多连接正反向监控超时时长，否则配置进程级正反向监控超时时长。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| HBTYPE | HBCYCLE | HBTIMEOUT | SWITCH |
| --- | --- | --- | --- |
| PROCESSFORWARD | 5 | 12 | OFF |
| PROCESSREVERSE | 5 | 10 | ON |
| DOMAINFORWARD | 5 | 26 | OFF |
| MCPROCESSFORWARD | 5 | 12 | OFF |
| MCPROCESSREVERSE | 5 | 10 | ON |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| HBTYPE | 故障检测类型 | 可选必选说明：必选参数<br>参数含义：该参数用于表示故障检测类型。<br>数据来源：本端规划<br>取值范围：<br>- “PROCESSFORWARD（进程级正向监控）”：该选项已废弃<br>- “PROCESSREVERSE（进程级反向监控）”：该选项已废弃<br>- “DOMAINFORWARD（区域级正向监控）”：该选项已废弃<br>- MCPROCESSFORWARD（多连接正向监控）<br>- MCPROCESSREVERSE（多连接反向监控）<br>默认值：无。<br>配置原则：<br>多连接开关关闭时，实现状态监控的服务主实例监控业务进程为进程级正向监控，业务进程反向监控实现状态监控的服务主实例为进程级反向监控。<br>多连接开关打开时，实现状态监控的所有服务实例监控业务进程为多连接正向监控，业务进程反向监控实现状态监控的所有服务实例为多连接反向监控。 |
| HBCYCLE | 心跳周期(100ms) | 可选必选说明：该参数在"HBTYPE"配置为"PROCESSFORWARD"、"PROCESSREVERSE"、"DOMAINFORWARD"、"MCPROCESSFORWARD"、"MCPROCESSREVERSE"时为条件必选参数。<br>参数含义：该参数用于表示心跳周期，单位为100ms。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~3600000。<br>默认值：无。<br>配置原则：无 |
| HBTIMEOUT | 心跳超时周期数 | 可选必选说明：该参数在"HBTYPE"配置为"PROCESSFORWARD"、"PROCESSREVERSE"、"DOMAINFORWARD"、"MCPROCESSFORWARD"、"MCPROCESSREVERSE"时为条件必选参数。<br>参数含义：该参数用于表示心跳超时周期数。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~4294967295。<br>默认值：无。<br>配置原则：无 |
| SWITCH | 自杀开关 | 可选必选说明：该参数在"HBTYPE"配置为"PROCESSREVERSE"、"MCPROCESSREVERSE"时为条件可选参数。<br>参数含义：该参数用于表示自杀功能开关是否打开。<br>数据来源：本端规划<br>取值范围：<br>- “ON（开启）”：自杀开关打开<br>- “OFF（关闭）”：自杀开关关闭<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST MSFAULTTOLERANCE查询当前参数配置值。<br>配置原则：<br>业务进程反向监控实现状态监控的服务实例超时时需要自杀则打开自杀开关，否则关闭自杀开关。 |

## 操作的配置对象

- [故障检测参数（MSFAULTTOLERANCE）](configobject/UNC/20.15.2/MSFAULTTOLERANCE.md)

## 使用实例

- 配置haf controller监控haf executor的心跳周期为5，即500ms，超时周期数为12，（12 * 500ms = 6s）。
  ```
  SET MSFAULTTOLERANCE: HBTYPE=DOMAINFORWARD, HBCYCLE=5, HBTIMEOUT=12;
  ```
- 配置实现状态监控的服务主实例监控业务进程的心跳周期为5，即500ms，超时周期数为12，（12 * 500ms = 6s）。
  ```
  SET MSFAULTTOLERANCE: HBTYPE=PROCESSFORWARD, HBCYCLE=5, HBTIMEOUT=12;
  ```
- 配置业务进程反向监控实现状态监控的服务主实例的心跳周期为5，即500ms，超时周期数为12，（12 * 500ms = 6s），防脑裂自杀功能打开。
  ```
  SET MSFAULTTOLERANCE: HBTYPE=PROCESSREVERSE, HBCYCLE=5, HBTIMEOUT=12, SWITCH=ON;
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置故障检测参数（SET-MSFAULTTOLERANCE）_09587879.md`
