# 查询BGP VPN简要信息（DSP BGPVRF）

- [命令功能](#ZH-CN_CONCEPT_0000001549801930__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000001549801930__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000001549801930__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000001549801930__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000001549801930__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0000001549801930__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0000001549801930)

该命令用于查询BGP VPN简要信息。

#### [注意事项](#ZH-CN_CONCEPT_0000001549801930)

该命令执行后立即生效。

#### [操作用户权限](#ZH-CN_CONCEPT_0000001549801930)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000001549801930)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| AFTYPE | BGP地址族类型 | 可选必选说明：可选参数<br>参数含义：BGP地址族类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4uni：IPv4地址族。<br>- ipv4vpn：VPNv4地址族。<br>- ipv6uni：IPv6地址族。<br>- ipv6vpn：VPNv6地址族。<br>默认值：无 |
| VRFNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：使用LST L3VPNINST命令查看可用VPN。 |

#### [使用实例](#ZH-CN_CONCEPT_0000001549801930)

查询BGP VPN简要信息：

```
DSP BGPVRF:AFTYPE=ipv4uni;
```

```

RETCODE = 0  操作成功。

结果如下
------------------------
BGP VPN简要信息  =
VPN-Instance(IPv4-family):
VPN-Instance Name   _public_
Peer Num   1
Route Num   5

(结果个数 = 1)
---    END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0000001549801930)

| 输出项名称 | 输出项解释 |
| --- | --- |
| BGP VPN简要信息 | 用于查询BGP VPN简要信息。 |
