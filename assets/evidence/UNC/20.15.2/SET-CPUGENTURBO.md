# 设置CPU睿频开关（SET CPUGENTURBO）

- [命令功能](#ZH-CN_MMLREF_0000001951335405__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001951335405__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001951335405__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001951335405__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0000001951335405)

![](设置CPU睿频开关（SET CPUGENTURBO）_51335405.assets/notice_3.0-zh-cn_2.png)

如果配置不合理会导致权重计算产生偏差。

**适用NF：SGW-C、PGW-C、SMF、GGSN**

该命令用于设置不同CPU代际的睿频开关。

## [注意事项](#ZH-CN_MMLREF_0000001951335405)

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| CPUGENERATION | TURBOSWITCH |
| --- | --- |
| Icelake | - |
| Skylake | - |
| Broadwell | - |
| Haswell | - |
| CascadeLake | - |

#### [操作用户权限](#ZH-CN_MMLREF_0000001951335405)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001951335405)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CPUGENERATION | CPU代际类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定CPU代际类型。<br>数据来源：本端规划<br>取值范围：<br>- Icelake（Icelake代际）<br>- Skylake（kylake代际）<br>- Broadwell（Broadwell代际）<br>- Haswell（Haswell代际）<br>- CascadeLake（CascadeLake代际）<br>默认值：无。<br>配置原则：无 |
| TURBOSWITCH | 睿频开关 | 可选必选说明：必选参数<br>参数含义：该参数用于设置睿频的开关。<br>数据来源：本端规划<br>取值范围：<br>- OFF（OFF）<br>- ON（ON）<br>默认值：无。<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0000001951335405)

查询CPU代际类型为Icelake的代际开关：

```
SET CPUGENTURBO:CPUGENERATION=Icelake,TURBOSWITCH=ON;
```
