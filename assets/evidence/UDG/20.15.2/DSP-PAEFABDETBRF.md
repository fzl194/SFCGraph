# 显示Fabric链路探测简要结果（DSP PAEFABDETBRF）

- [命令功能](#ZH-CN_MMLREF_0000002112631724__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000002112631724__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000002112631724__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000002112631724__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0000002112631724__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0000002112631724)

该命令用于查询Fabric平面链路状态探测简要结果。

> **说明**
> 探测任务中执行命令只支持查询目的端探测结果。

#### [操作用户权限](#ZH-CN_MMLREF_0000002112631724)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0000002112631724)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SRCPODNAME | 源Pod名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定本端Pod名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。<br>默认值：无<br>配置原则：<br>使用<br>[**DSP POD**](../../../操作维护/Pod管理/POD查询（DSP POD）_69830277.md)<br>获取Pod名称。 |
| DSTPODNAME | 目的Pod名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定远端Pod名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。<br>默认值：无<br>配置原则：<br>使用<br>[**DSP POD**](../../../操作维护/Pod管理/POD查询（DSP POD）_69830277.md)<br>获取Pod名称。 |
| SRCPORTNAME | 源端口名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定本端端口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~20。<br>默认值：无<br>配置原则：<br>使用<br>[**DSP PAEPORTINFO**](../端口/显示PAE端口基本信息（DSP PAEPORTINFO）_92520040.md)<br>获取探测端口名称（仅支持Fabric端口）。 |
| DSTPORTNAME | 目的端口名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定远端端口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~20。<br>默认值：无<br>配置原则：<br>使用<br>[**DSP PAEPORTINFO**](../端口/显示PAE端口基本信息（DSP PAEPORTINFO）_92520040.md)<br>获取探测端口名称（仅支持Fabric端口）。 |

## [使用实例](#ZH-CN_MMLREF_0000002112631724)

显示Fabric链路探测简要结果：

```
+++    UNC/*MEID:0 MENAME:UNC_z30062954_X86_20241226_1001*/        2024-12-26 15:59:46
O&M    #3308
%%DSP PAEFABDETBRF: SRCPODNAME="cslbip-pod-0", DSTPODNAME="vup-pod-0", SRCPORTNAME="eth2", DSTPORTNAME="eth2";%%
RETCODE = 0  操作成功

结果如下
--------
Pod名称       探测类型   发送报文数  接收报文数  

cslbip-pod-0  源端Pod    159         159         
vup-pod-0     目的端Pod  159         159         
(结果个数 = 2)

---    END
```

## [输出结果说明](#ZH-CN_MMLREF_0000002112631724)

| 输出项名称 | 输出项解释 |
| --- | --- |
| Pod名称 | 该参数用于表示fabric链路探测的Pod名称。 |
| 探测类型 | 该参数用于表示Pod的fabric链路探测类型。<br>取值说明：<br>- PODTYPE_SEND（源端Pod）<br>- PODTYPE_RECV（目的端Pod） |
| 发送报文数 | 该参数表示fabric链路探测Pod的发送成功的报文数。 |
| 接收报文数 | 该参数表示fabric链路探测Pod的发送接收的报文数。 |
