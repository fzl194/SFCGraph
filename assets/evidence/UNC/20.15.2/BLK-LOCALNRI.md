# 闭塞本局NRI配置信息(BLK LOCALNRI)

- [命令功能](#ZH-CN_MMLREF_0000001126305910__1.3.1.1)
- [注意事项](#ZH-CN_MMLREF_0000001126305910__1.3.2.1)
- [本地用户权限](#ZH-CN_MMLREF_0000001126305910__1.3.3.1)
- [网管用户权限](#ZH-CN_MMLREF_0000001126305910__1.3.4.1)
- [参数说明](#ZH-CN_MMLREF_0000001126305910__1.3.5.1)
- [使用实例](#ZH-CN_MMLREF_0000001126305910__1.3.6.1)

#### [命令功能](#ZH-CN_MMLREF_0000001126305910)

**适用网元：SGSN**

该命令用于闭塞本局NRI配置信息。本局NRI被闭塞之后，从 “NRI起始值” 开始的N个NRI都将处于BLOCKED状态（其中N为 [**ADD LOCALNRI**](增加本局NRI配置信息(ADD LOCALNRI)_72345699.md) 命令中输入的 “NRI个数” ），SGSN在新分配PTMSI时，将不使用BLOCKED状态的NRI值，但是可以正确识别该NRI值为本局NRI。

#### [注意事项](#ZH-CN_MMLREF_0000001126305910)

- 该命令执行立即生效。
- 该命令输入的“NRI起始值”必须为[**ADD LOCALNRI**](增加本局NRI配置信息(ADD LOCALNRI)_72345699.md)命令中输入的“NRI起始值”。

#### [本地用户权限](#ZH-CN_MMLREF_0000001126305910)

manage-ug；system-ug

#### [网管用户权限](#ZH-CN_MMLREF_0000001126305910)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_MMLREF_0000001126305910)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POOLID | POOL区标识 | 可选必选说明：必选参数<br>参数含义：该参数用于POOL区标识。<br>数据来源：整网规划<br>取值范围：0～4095<br>默认值：无 |
| NRIVBGN | NRI起始值 | 可选必选说明：必选参数<br>参数含义：该参数用于NRI起始值，参数值需与<br>[**ADD LOCALNRI**](增加本局NRI配置信息(ADD LOCALNRI)_72345699.md)<br>中的<br>“NRI起始值”<br>相同，NRI（Net Resource Identify），网络资源标识，用于标识一个CN节点。RAN根据NRI将MS的消息路由到对应的SGSN。<br>数据来源：整网规划<br>取值范围：0～1023<br>默认值： 无<br>说明：- NRI的取值范围在0～(2n-1)，n为本Pool的NRI长度。<br>- 若POOL表的NRI长度为10，则LOCALNRI表的NRI个数必须大于等于4， NRI起始值小于等于1020。 |

#### [使用实例](#ZH-CN_MMLREF_0000001126305910)

闭塞一条POOLID为1，NRI的起始值为10的本局NRI配置信息：

BLK LOCALNRI: POOLID=1, NRIVBGN=10;
