---
id: UNC@20.15.2@MMLCommand@SET R8QOSMAP
type: MMLCommand
name: SET R8QOSMAP（设置EPS QoS参数到Pre-R8 QoS参数映射规则）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: R8QOSMAP
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- QoS管理
- QoS兼容性管理
- EPS QoS参数到Pre-R8 QoS参数映射
status: active
---

# SET R8QOSMAP（设置EPS QoS参数到Pre-R8 QoS参数映射规则）

## 功能

**适用网元：MME**

此命令用于设置EPS QoS参数到Pre-R8 QoS参数的映射规则。在GUL互操作中，从4G网络向2/3G网络切换的时候，MME会根据配置的映射规则，将4G中使用的EPS QoS参数映射成适用于2/3G中使用的Pre-R8 QoS参数，以保证网络切换后，不影响业务服务质量。

## 注意事项

- 系统初次运行时，会执行系统初始设置值。
- 该命令执行后立即生效。
- 该命令仅支持范围在1～9、65～66、69～70之间的QCI到Pre-R8 QoS的映射，如果QCI不在此范围内，需要先通过[**ADD QCICONV**](../../EPS QoS/扩展QCI转换关系/增加扩展QCI转换关系(ADD QCICONV)_26306024.md)命令将扩展QCI映射为标准QCI(1～9)。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QCI | QoS 级别标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定映射规则所对应QoS的级别。<br>数据来源：整网规划<br>取值范围：1~254<br>系统初始设置值：请参考<br>[表1](#ZH-CN_MMLREF_0000001126146234__tab1)<br>。<br>配置原则：<br>- 1～9为标准QoS，10～254为扩展QoS。<br>- 1～3表示会话类业务。<br>- 4表示流类业务。<br>- 5～8表示交互类业务。<br>- 9表示背景类业务。<br>- 65表示公共安全PTT业务的语音业务。<br>- 66表示普通消费者PTT业务的语音业务。<br>- 69表示公共安全PTT业务的信令保障。<br>- 70表示公共安全数据业务。 |
| TC | 流量等级 | 可选必选说明：可选参数<br>参数含义：该参数用于指定映射后的QoS流量等级。<br>数据来源：整网规划<br>取值范围：<br>- “CC(Conversational class)”<br>- “SC(Streaming class)”<br>- “IC(Interactive class)”<br>- “BC(Background class)”<br>默认值：无<br>配置原则：建议值请参考<br>[表1](#ZH-CN_MMLREF_0000001126146234__tab1)<br>。 |
| MAXSDU | 最大SDU长度 | 可选必选说明：可选参数<br>参数含义：该参数用于指定映射后的最大服务数据单元的长度。<br>数据来源：整网规划<br>取值范围：1~153<br>默认值：无<br>配置原则：<br>- 1~150表示10~1500 octets。<br>- 151表示1502 octets。<br>- 152表示1510 octets。<br>- 153表示1520 octets。<br>- 建议值为150。 |
| DO | 发送次序 | 可选必选说明：可选参数<br>参数含义：该参数用于指定映射后的缺省QoS发送次序。<br>数据来源：整网规划<br>取值范围：<br>- “ORDER(With delivery order)”<br>- “NORDER(Without delivery order)”<br>默认值：无<br>配置原则：建议值为<br>“NORDER(Without delivery order)”<br>。 |
| RBER | 保留BER | 可选必选说明：可选参数<br>参数含义：该参数用于指定映射后的保留错误比特率。<br>数据来源：整网规划<br>取值范围：<br>- “E_RESIDUAL_BIT_ERR_RATIO_1(保留BER1)”：代表的比特率为5*10-2。<br>- “E_RESIDUAL_BIT_ERR_RATIO_2(保留BER2)”：代表的比特率为1*10-2。<br>- “E_RESIDUAL_BIT_ERR_RATIO_3(保留BER3)”：代表的比特率为5*10-3。<br>- “E_RESIDUAL_BIT_ERR_RATIO_4(保留BER4)”：代表的比特率为4*10-3。<br>- “E_RESIDUAL_BIT_ERR_RATIO_5(保留BER5)”：代表的比特率为1*10-3。<br>- “E_RESIDUAL_BIT_ERR_RATIO_6(保留BER6)”：代表的比特率为1*10-4。<br>- “E_RESIDUAL_BIT_ERR_RATIO_7(保留BER7)”：代表的比特率为1*10-5。<br>- “E_RESIDUAL_BIT_ERR_RATIO_8(保留BER8)”：代表的比特率为1*10-6。<br>- “E_RESIDUAL_BIT_ERR_RATIO_9(保留BER9)”：代表的比特率为6*10-8。<br>默认值：无<br>配置原则：建议值为<br>“E_RESIDUAL_BIT_ERR_RATIO_7(保留BER7 =7)”<br>。 |
| DESDU | 发送错误SDU | 可选必选说明：可选参数<br>参数含义：该参数用于指定映射后发送错误的服务数据单元。<br>数据来源：整网规划<br>取值范围：<br>- “NOT_DETECT(不检查)”：表示不需要侦查发送的服务数据单元是否有错。<br>- “ERR_SDU_DELIVERED(发送错误SDU)”：表示检测到发送的服务数据单元如果有错则需要上报。<br>- “ERR_SDU_NOT_DELIVERED(不发送错误SDU)”：表示检测到发送的服务数据单元如果有错不需要上报。<br>默认值：无<br>配置原则：建议值为<br>“NOT_DETECT(不检查)”<br>。 |
| SDUER | SDU误码率 | 可选必选说明：可选参数<br>参数含义：该参数用于指定映射后的缺省QoS SDU误码率。<br>数据来源：整网规划<br>取值范围：<br>- “SDUER1(1*10^-2)”<br>- “SDUER2(7*10^-3)”<br>- “SDUER3(1*10^-3)”<br>- “SDUER4(1*10^-4)”<br>- “SDUER5(1*10^-5)”<br>- “SDUER6(1*10^-6)”<br>- “SDUER7(1*10^-1)”<br>默认值：无<br>配置原则：建议值请参考<br>[表1](#ZH-CN_MMLREF_0000001126146234__tab1)<br>。 |
| THPRI | 发送控制优先级 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定映射后的缺省QoS发送控制优先级。<br>前提条件：该参数在<br>“TC(流量等级)”<br>配置为<br>“IC(Interactive class)”<br>后生效。<br>数据来源：整网规划<br>取值范围：<br>- “THPRI1(Priority level 1)”<br>- “THPRI2(Priority level 2)”<br>- “THPRI3(Priority level 3)”<br>默认值：无<br>配置原则：建议值请参考<br>[表1](#ZH-CN_MMLREF_0000001126146234__tab1)<br>。 |
| TD | 传递时延 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定映射后的缺省QoS传递时延。<br>前提条件：该参数在<br>“TC(流量等级)”<br>配置为<br>“CC(Conversational class)”<br>或<br>“SC(Streaming class)”<br>后生效。<br>数据来源：整网规划<br>取值范围：1~62（数值型）<br>默认值：无<br>配置原则：<br>- 1~15表示10~150ms，以10ms递增。<br>- 16~31表示200~950ms，以50ms递增。<br>- 32~62表示1000~4000ms，以100ms递增。<br>- 只在Traffic Class为实时类（Conversational，Streaming）时有效。<br>- 建议值请参考[表1](#ZH-CN_MMLREF_0000001126146234__tab1)。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/R8QOSMAP]] · EPS QoS参数到Pre-R8 QoS参数映射规则（R8QOSMAP）

## 使用实例

设置QCI为1的EPS QoS参数到Pre-R8 QoS参数映射规则：

SET R8QoSMAP: QCI=1, TC=CC, MAXSDU=1, DO=ORDER, RBER=E_RESIDUAL_BIT_ERR_RATIO_2, DESDU=ERR_SDU_DELIVERED, SDUER=SDUER1, TD=2;

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置EPS-QoS参数到Pre-R8-QoS参数映射规则（SET-R8QOSMAP）_26146234.md`
