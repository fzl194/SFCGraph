---
id: UDG@20.15.2@MMLCommand@MOD IKEPEER6
type: MMLCommand
name: MOD IKEPEER6（修改IPv6 IKE对等体）
nf: UDG
version: 20.15.2
verb: MOD
object_keyword: IKEPEER6
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- IPSEC功能管理
- IP服务
- IP安全管理
- 互联网密钥交换
- IKE对等体IPv6
status: active
---

# MOD IKEPEER6（修改IPv6 IKE对等体）

## 功能

该命令用于修改IKE对等体的配置。

> **说明**
> - 该命令执行后立即生效。
>
> - IKEV1是不安全的协议，建议使用IKEV2。
> - IKEv1国密IPSEC仅支持主模式。
> - IKEv1国密IPSEC不支持NAT穿越。
> - IKEv1国密IPSEC不支持主备隧道。
> - IKEv1仅支持国密数字信封，不支持除此之外的认证方式。
> - IP-disable仅支持IKEv1。
> - 证书字段和场景字段不能同时配置。
> - 参数LOCALIDTYPE配置为Fqdn_ipv6（Fqdn_Ipv6）或User_fqdn_ipv6（User_fqdn_ipv6）时，参数REMOTEID必须进行配置。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PEERNAME | IKE对等体名称 | 可选必选说明：必选参数<br>参数含义：对端名字。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~15。不区分大小写。<br>默认值：无<br>配置原则：无 |
| PRESHAREDKEY | 预共享密钥 | 可选必选说明：可选参数<br>参数含义：预共享密钥。<br>数据来源：对端协商<br>取值范围：Pwd，取值范围是1~127。<br>默认值：无<br>配置原则：无 |
| EXCHANGEMODE | 交换模式 | 可选必选说明：可选参数<br>参数含义：交换模式。<br>数据来源：对端协商<br>取值范围：<br>- “Main（主模式）”：主模式<br>- “Aggressive（野蛮模式）”：野蛮模式<br>默认值：无<br>配置原则：无 |
| NATTRAVERSAL | Nat穿越 | 可选必选说明：可选参数<br>参数含义：Nat穿越。<br>数据来源：本端规划<br>取值范围：<br>- TRUE(TRUE)<br>- FALSE(FALSE)<br>默认值：无<br>配置原则：无 |
| PROPOSAL | 安全提议 | 可选必选说明：可选参数<br>参数含义：IKE提议。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~4294967295。101不支持配置，但可以查询。<br>默认值：无<br>配置原则：无 |
| LOCALIDTYPE | 本地ID类型 | 可选必选说明：可选参数<br>参数含义：本地ID的类型。<br>数据来源：本端规划<br>取值范围：<br>- “IPv6（IPv6）”：IPv6<br>- “Fqdn_ipv6（Fqdn_Ipv6）”：Fqdn_Ipv6<br>- “User_fqdn_ipv6（User_fqdn_ipv6）”：User_fqdn_ipv6<br>- “Dn_ipv6（Dn_ipv6）”：Dn_ipv6<br>- “Ip_disable（IP-disable）”：关闭local ip的IP校验<br>默认值：无<br>配置原则：无 |
| REMOTEID | 远端ID | 可选必选说明：可选参数<br>参数含义：远端ID。<br>数据来源：对端协商<br>取值范围：字符串类型，输入长度范围是1~255。<br>默认值：无<br>配置原则：无 |
| VERSION2 | IKE版本2 | 可选必选说明：可选参数<br>参数含义：IKE版本2。<br>数据来源：对端协商<br>取值范围：<br>- TRUE(TRUE)<br>- FALSE(FALSE)<br>默认值：无<br>配置原则：<br>该参数用于配置ike版本，TRUE代表使用IKE版本2，FALSE代表使用IKE版本1。 |
| LOWREMOTEADDR | 远端地址 | 可选必选说明：可选参数<br>参数含义：远端地址。<br>数据来源：对端协商<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |
| INVRFNAME | SA绑定VPN名称 | 可选必选说明：可选参数<br>参数含义：SA绑定的VPN名字。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~47。<br>默认值：无<br>配置原则：无 |
| OUTVRFNAME | 远端地址VPN名称 | 可选必选说明：可选参数<br>参数含义：远端地址的VPN。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~47。<br>默认值：无<br>配置原则：无 |
| AUTHADDRESS | 低位认证地址 | 可选必选说明：可选参数<br>参数含义：IKE远端认证地址。<br>数据来源：对端协商<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |
| AUTHENDADDRESS | 高位认证地址 | 可选必选说明：可选参数<br>参数含义：IKE远端认证结尾地址。<br>数据来源：对端协商<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |
| CERTLOCALFILE | 证书文件名 | 可选必选说明：可选参数<br>参数含义：签名证书文件名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~127。<br>默认值：无<br>配置原则：无 |
| DPDHASHSEQ | DPD载荷顺序 | 可选必选说明：可选参数<br>参数含义：IKEv1 DPD载荷顺序。<br>数据来源：本端规划<br>取值范围：<br>- “Hash_notify（DPD载荷顺序先hash后notify）”：DPD载荷顺序先hash后notify<br>- “Notify_hash（DPD载荷顺序先notify后hash）”：DPD载荷顺序先notify后hash<br>默认值：无<br>配置原则：无 |
| IKEMSGSYNC | 使能IKE消息序列号同步 | 可选必选说明：可选参数<br>参数含义：使能IKE消息序列号同步。<br>数据来源：本端规划<br>取值范围：<br>- Disable（不使能）<br>- Enable（使能）<br>默认值：无<br>配置原则：无 |
| IPSECMSGSYNC | 使能IPSEC消息序列号同步 | 可选必选说明：可选参数<br>参数含义：使能IPSEC消息序列号同步。<br>数据来源：本端规划<br>取值范围：<br>- Disable（不使能）<br>- Enable（使能）<br>默认值：无<br>配置原则：无 |
| ENCCERTLOCFILE | 加密证书名称 | 可选必选说明：可选参数<br>参数含义：加密证书文件名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~127。<br>默认值：无<br>配置原则：无 |
| CERTSCENARIO | 签名证书场景名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定签名证书绑定的场景名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~192。<br>默认值：无<br>配置原则：无 |
| ENCCERTSCENARIO | 加密证书场景名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定v1国密加密证书绑定的场景名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~192。<br>默认值：无<br>配置原则：无 |
| CUSTOMPARA | 自定义参数 | 可选必选说明：可选参数<br>参数含义：自定义参数。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~4294967295。<br>默认值：0<br>配置原则：<br>bit0为1：国密数字信封场景协商时不校验接收到的Transfrom ID。bit0为0：国密数字信封场景协商时校验接收到的Transfrom ID。<br>bit1为1：国密数字信封场景协商时不校验SM4算法中的Key Length字段。bit1为0：国密数字信封场景协商时校验SM4算法中的Key Length字段。<br>bit2位1：国密数字信封场景DPD报文中SPI size为16。bit2位0：国密数字信封场景DPD报文中SPI size为0。<br>bit3为1：国密数字信封场景一阶段HASH计算方式与国密协议保持一致。bit3为0：国密数字信封场景一阶段HASH计算方式以IKEv1协议规定方式计算。<br>bit4为1：国密数字信封场景二阶段HASH计算方式与国密协议保持一致。bit4为0：国密数字信封场景二阶段HASH计算方式以IKEv1协议规定方式计算。<br>bit5~bit8：控制国密数字信封场景哪一端作为发起端。<br>bit9为1：国密ESP认证算法使用的HMAC_SM3算法选择HMAC_SM3_128。<br>bit10为1：国密ESP认证算法使用的HMAC_SM3算法选择HMAC_SM3_256。<br>bit9和bit10均为0或者均为1：国密ESP认证算法使用的HMAC_SM3算法选择HMAC_SM3_96。<br>默认值：0。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/IKEPEER6]] · IPv6 IKE对等体（IKEPEER6）

## 使用实例

修改名称为“peer1”的IKE对等体的交换模式为aggressive模式：

```
MOD IKEPEER6:PEERNAME="peer1",EXCHANGEMODE=Aggressive;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/MOD-IKEPEER6.md`
