---
id: UDG@20.15.2@MMLCommand@MOD VIRTUALIP
type: MMLCommand
name: MOD VIRTUALIP（修改浮动IP）
nf: UDG
version: 20.15.2
verb: MOD
object_keyword: VIRTUALIP
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 系统管理
- 路由管理
- 地址管理
status: active
---

# MOD VIRTUALIP（修改浮动IP）

## 功能

![](修改浮动IP (MOD VIRTUALIP)_01259710.assets/notice_3.0-zh-cn.png)

该类命令执行之后 **可能会导致OM Portal断链** 、网管断链以及VNFM断链，需使用修改后IP重新登录OM Portal，并重新对接网管以及修改VNFM侧对应网元的IP。该命令若执行不当， **会导致所有业务中断** 。

用于修改登录OM Portal的浮动IP地址。

> **说明**
> - IPv4单栈环境下的浮动IP类型不支持修改为IPv6类型，IPv6单栈环境下的浮动IP类型不支持修改为IPv4类型。
> - IPv4或IPv6单栈环境可以通过此命令变更为双栈环境。
> - 修改浮动IP时，需和物理IP保持相同网段。
> - 执行该命令修改浮动IP时，请参考网元的改造OM网络方案改造OM网络。

## 参数

| **参数标识** | **参数名称** | **参数说明** |
| --- | --- | --- |
| IPTYPE | 浮动IP类型 | 可选必选说明：必选参数<br>参数含义：浮动IP类型<br>取值范围：<br>- IPv4(IPv4类型)<br>- IPv6(IPv6类型)<br>默认值：无<br>配置原则：无 |
| IPV4ADDR | IPv4地址 | 可选必选说明：当浮动IP类型为IPv4时，此为必选参数<br>参数含义：IPv4地址<br>取值范围：有效的IPv4地址<br>默认值：无<br>配置原则：无 |
| IPV4GW | IPv4网关 | 可选必选说明：当浮动IP类型为IPv4时，此为必选参数<br>参数含义：IPv4网关<br>取值范围：有效的IPv4地址<br>默认值：无<br>配置原则：无 |
| NETMASK | 子网掩码 | 可选必选说明：当浮动IP类型为IPv4时，此为必选参数<br>参数含义：IPv4子网掩码<br>取值范围：有效的IPv4子网掩码<br>默认值：无<br>配置原则：无 |
| IPV6ADDR | IPv6地址 | 可选必选说明：当浮动IP类型为IPv6时，此为必选参数<br>参数含义：IPv6地址<br>取值范围：有效的IPv6地址<br>默认值：无<br>配置原则：无 |
| IPV6GW | IPv6网关 | 可选必选说明：当浮动IP类型为IPv6时，此为必选参数<br>参数含义：IPv6网关<br>取值范围：有效的IPv6地址<br>默认值：无<br>配置原则：无 |
| PREFIXLENGTH | 前缀长度 | 可选必选说明：当浮动IP类型为IPv6时，此为必选参数<br>参数含义：IPv6前缀长度<br>取值范围：0~128<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@VIRTUALIP]] · 浮动IP（VIRTUALIP）

## 使用实例

更新当前登录OM Portal的IP为:192.168.40.47，网关为:192.168.40.1，子网掩码为:255.255.255.0：

```
%%MOD VIRTUALIP: IPTYPE=IPv4, IPV4ADDR="192.168.40.47", IPV4GW="192.168.40.1", NETMASK="255.255.255.0";%%
RETCODE = 0  操作成功

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/MOD-VIRTUALIP.md`
