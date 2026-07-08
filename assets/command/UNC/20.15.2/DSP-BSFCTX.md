---
id: UNC@20.15.2@MMLCommand@DSP BSFCTX
type: MMLCommand
name: DSP BSFCTX（显示UE IP对应的PCF信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: BSFCTX
command_category: 查询类
applicable_nf:
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 接入管理运维
- 显示UE IP对应的PCF信息
status: active
---

# DSP BSFCTX（显示UE IP对应的PCF信息）

## 功能

**适用NF：SMF**

该命令用于显示UE IP对应的PCF信息。

## 注意事项

在以IPv4地址作为查询条件的时候，如果该IPv4地址绑定了IP Domain信息，则查询条件里必须同时指定对应的IP Domain信息，否则无法查询到记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| UEIPTYPE | UE IP的类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定UE IP的类型。<br>数据来源：全网规划<br>取值范围：<br>- IPV4（IPV4）<br>- IPV6（IPV6）<br>默认值：无<br>配置原则：无 |
| UEIPV4ADDR | UE的IPv4地址 | 可选必选说明：该参数在"UEIPTYPE"配置为"IPV4"时为条件必选参数。<br>参数含义：该参数用于表示UE的IPv4地址。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无 |
| UEIPV6PREFIX | UE的IPv6前缀 | 可选必选说明：该参数在"UEIPTYPE"配置为"IPV6"时为条件必选参数。<br>参数含义：该参数用于指定UE的IPv6前缀。仅前64位有效。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |
| IPDOMAIN | IPv4地址的域标识 | 可选必选说明：该参数在"UEIPTYPE"配置为"IPV4"时为条件可选参数。<br>参数含义：该参数用于指定IPv4地址的域标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [UE IP对应的PCF信息（BSFCTX）](configobject/UNC/20.15.2/BSFCTX.md)

## 使用实例

显示UE IP为192.168.2.1的PCF信息：

```
DSP BSFCTX:UEIPTYPE=IPV4, UEIPV4ADDR="192.168.2.1";
RETCODE = 0 操作成功

结果如下
------------------------
                                             UE IP的类型  =  IPV4
                                            UE的IPv4地址  =  192.168.2.1
                                            UE的IPv6前缀  =  ::
                                        IPv4地址的域标识  =  NULL
                                     UE IP对应用户的SUPI  =  imsi-123032900100001
                                     UE IP对应用户的GPSI  =  msisdn-8613529000001
                                             UE的MAC地址  =  NULL
                                            数据网络名称  =  HUAWEI.COM
会话对应PCF或者Npcf_PolicyAuthorization服务对应PCF的FQDN  =  pnfservice.fqdn.pcf0.huawei.com
                                     PCF N7接口 IPv4地址  =  192.168.2.10
                                     PCF N7接口 IPv6地址  =  NULL
                                    PCF N7接口传输层协议  =  TransportProtocolTCP
                                          PCF N7接口端口  =  5060
                                  PCF Rx接口Diameter主机  =  huawei.com
                                  PCF Rx接口Diameter域名  =  huawei.com
                                                切片标识  =  Sst:1 Sd:010101
                                                 POD名称  =  sm2-pod-0
(结果数目 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示UE-IP对应的PCF信息（DSP-BSFCTX）_09652292.md`
