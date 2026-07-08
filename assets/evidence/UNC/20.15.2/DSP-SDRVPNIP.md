# 查询SDRC中的VPNIP信息（DSP SDRVPNIP）

- [命令功能](#ZH-CN_MMLREF_0294730438__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0294730438__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0294730438__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0294730438__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0294730438__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0294730438)

该命令用于查询SDRC中的VPNIP信息，若命令不接任何参数，则该命令列出SDRC中所有VPNIP的信息，否则显示特定的VPNIP信息。

## [注意事项](#ZH-CN_MMLREF_0294730438)

无

#### [操作用户权限](#ZH-CN_MMLREF_0294730438)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0294730438)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VPNNAME | VPN名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示VPNIP策略的vpn名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~1024。<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0294730438)

显示SDRC中VPNNAME等于_public_的VPNIP信息

```
%%DSP SDRVPNIP:;%%
RETCODE = 0  操作成功

结果如下
--------
vpn名称  =  _public_
Address Family  =  0
源地址  =  "10.11.2.11"

---    END
```

## [输出结果说明](#ZH-CN_MMLREF_0294730438)

| 输出项名称 | 输出项解释 |
| --- | --- |
| VPN名称 | 该参数用于表示VPNIP策略的vpn名称。 |
| 地址族 | 该参数用于表示VPNIP策略的Address Family。 |
| 源地址 | 该参数用于表示VPNIP策略的源地址。 |
