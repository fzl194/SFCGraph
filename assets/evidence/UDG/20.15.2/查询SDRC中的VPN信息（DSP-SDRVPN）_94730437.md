# 查询SDRC中的VPN信息（DSP SDRVPN）

- [命令功能](#ZH-CN_MMLREF_0294730437__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0294730437__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0294730437__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0294730437__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0294730437__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0294730437)

该命令用于查询SDRC中的VPN信息，若命令不接任何参数，则该命令列出SDRC中所有VPN的信息，否则显示特定的VPN信息。

> **说明**
> 无

#### [操作用户权限](#ZH-CN_MMLREF_0294730437)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0294730437)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VPNNAME | VPN名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示vpn的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0294730437)

显示SDRC中VPNNAME等于_public_的VPN信息

```
%%DSP SDRVPN:;%%
RETCODE = 0  操作成功

结果如下
--------
VPN 名称  =  _public_
 SDR ID  =  1
 下行经过LB  =  是
VPN拓扑  =  instance_id:281492156580961 low_tb:1121 tp:2416123937  instance_id:281492156580949 low_tb:1109 tp:2416123937
(结果个数 = 1)

---    END
```

## [输出结果说明](#ZH-CN_MMLREF_0294730437)

| 输出项名称 | 输出项解释 |
| --- | --- |
| VPN名称 | 该参数用于表示vpn的名称。 |
| SDR ID | 该参数用于表示SDRC给该VPN分配的ID。 |
| 下行经过LB | 该参数用于表示该VPN是否关联CSLB。<br>取值说明：<br>- TRUE(TRUE)<br>- FALSE(FALSE) |
| VPN拓扑 | 该参数用于表示该VPN的TOPO信息。 |
