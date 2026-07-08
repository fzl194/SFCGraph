# 查询L3VPN实例地址族（LST VPNINSTAF）

- [命令功能](#ZH-CN_CONCEPT_0000001550121422__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000001550121422__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000001550121422__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000001550121422__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000001550121422__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0000001550121422__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0000001550121422)

该命令用于查询设备上VPN实例下配置的地址族信息。

#### [注意事项](#ZH-CN_CONCEPT_0000001550121422)

- 该命令执行后立即生效。
- 如果未设定VPN实例，将查询设备上所有实例下的地址族；如果未设定地址族，将查询指定VPN实例下的所有地址族。

#### [操作用户权限](#ZH-CN_CONCEPT_0000001550121422)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000001550121422)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VRFNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定L3VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无 |
| AFTYPE | 地址族类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定VPN实例下的地址族。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4uni：IPv4地址族。<br>- ipv6uni：IPv6地址族。<br>默认值：无 |

#### [使用实例](#ZH-CN_CONCEPT_0000001550121422)

查询设备上所有VPN实例的地址族，其中VPN实例_public_为公网实例，表示相对于私网的公网概念：

```
LST VPNINSTAF:;
```

```
RETCODE = 0  操作成功。

结果如下
-------------------------
VPN实例名称          地址族类型           路由标识             引入路由策略名称            可更改本地交叉下一跳   发布路由策略名称     路由上送时首先添加ERT     实例的标签分配模式   隧道策略名称   实例的标签值       FRR使能
_public_             IPv4uni              NULL                 NULL                        FALSE                  NULL                 FALSE                     每路由每标签         NULL           NULL               FALSE
_public_             IPv6uni              NULL                 NULL                        FALSE                  NULL                 FALSE                     每路由每标签         NULL           NULL               FALSE
__mpp_vpn_inner__    IPv4uni              NULL                 NULL                        FALSE                  NULL                 FALSE                     每路由每标签         NULL           NULL               FALSE
vpn1                 IPv4uni              NULL                 NULL                        FALSE                  NULL                 FALSE                     每路由每标签         NULL           NULL               FALSE
(结果个数 = 4)
---    END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0000001550121422)

参见ADD VPNINSTAF的参数说明。
