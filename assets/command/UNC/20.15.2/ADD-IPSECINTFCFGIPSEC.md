---
id: UNC@20.15.2@MMLCommand@ADD IPSECINTFCFGIPSEC
type: MMLCommand
name: ADD IPSECINTFCFGIPSEC（增加IPsec隧道接口）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: IPSECINTFCFGIPSEC
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- IPSEC功能管理
- IP服务
- IP安全管理
- 互联网密钥交换
- IPsec接口配置
status: active
---

# ADD IPSECINTFCFGIPSEC（增加IPsec隧道接口）

## 功能

该命令用于增加IPsec隧道。

## 注意事项

- 该命令执行后立即生效。

- 此配置会将安全策略与接口进行绑定，若配置了空的安全策略，则不会进行记录，只有配置真实有效的安全策略才会生成IPsec隧道接口。

- 最多可输入512条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INTERFACENAME | 接口名称 | 可选必选说明：必选参数<br>参数含义：配置接口名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。<br>默认值：无<br>配置原则：无 |
| TNLTYPE | Tunnel口协议类型 | 可选必选说明：必选参数<br>参数含义：Tunnel口协议类型。<br>数据来源：本端规划<br>取值范围：<br>- “IPSEC（IPv4IP安全）”：IPv4IP安全<br>- “IPSEC6（IPv6IP安全）”：IPv6IP安全<br>默认值：无<br>配置原则：无 |
| POLICYNAME | 策略名称 | 可选必选说明：可选参数<br>参数含义：配置策略名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~15。不区分大小写。<br>默认值：无<br>配置原则：<br>策略名称与<br>[**ADD IPSECPOLICY**](../IPsec策略/增加IPsec策略（ADD IPSECPOLICY）_25912243.md)<br>/<br>[**ADD IPSECPOLICY6**](../IPsec策略IPv6/增加IPsec Ipv6策略（ADD IPSECPOLICY6）_68320981.md)<br>命令配置的策略名称保持一致。 |
| SRCIFNAME | 源接口名称 | 可选必选说明：可选参数<br>参数含义：地址借用接口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。<br>默认值：无<br>配置原则：<br>只支持配置环回口。 |

## 操作的配置对象

- [IPsec隧道接口（IPSECINTFCFGIPSEC）](configobject/UNC/20.15.2/IPSECINTFCFGIPSEC.md)

## 使用实例

增加接口名为“Tunnel1”的安全隧道：

```
ADD IPSECINTFCFGIPSEC:INTERFACENAME="Tunnel1",TNLTYPE=IPSEC,POLICYNAME="policy1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加IPsec隧道接口（ADD-IPSECINTFCFGIPSEC）_80910986.md`
