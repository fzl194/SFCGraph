---
id: UDG@20.15.2@MMLCommand@MOD GIREDIRECTPARA
type: MMLCommand
name: MOD GIREDIRECTPARA（修改单一Gi重定向信息）
nf: UDG
version: 20.15.2
verb: MOD
object_keyword: GIREDIRECTPARA
command_category: 配置类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 业务安全防护
- 用户攻击防护
- Gi重定向
- Gi重定向参数
status: active
---

# MOD GIREDIRECTPARA（修改单一Gi重定向信息）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用来修改指定VPN下的IPv4或IPv6 Gi重定向参数，在需要控制UE之间互访的恶意攻击报文和需要通过网关将报文重定向来保证网络的安全的场景下使用此命令。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VPNINSTANCE | 需绑定的VPN实例名 | 可选必选说明：必选参数<br>参数含义：该参数用于表示Gi重定向所绑定的VPN实例名。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，公网缺省VPN“_public_”不区分大小写，其它的VPN区分大小写。<br>默认值：无<br>配置原则：无 |
| IPTYPE | IP类型 | 可选必选说明：必选参数<br>参数含义：该参数用于表示重定向的目的地址类型。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- IPv4：表示地址类型为IPv4。<br>- IPv6：表示地址类型为IPv6。<br>默认值：无<br>配置原则：无 |
| V4REDIRIPTYPE | IPv4重定向动作 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IPTYPE”配置为“IPv4”时为必选参数。<br>参数含义：该参数用于表示IPv4重定向动作。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- BLACKHOLE：表示丢弃互访的报文，禁止UE互访。<br>- IPADDRESS：表示重定向到目的ip地址。<br>默认值：无<br>配置原则：无 |
| IPV4ADDRESS | IPv4重定向IP地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“V4REDIRIPTYPE”配置为“IPADDRESS”时为必选参数。<br>参数含义：该参数用于表示地址类型为IPv4的重定向的目的地址。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。必须是合法的ipv4地址，采用点分十进制"X.X.X.X"形式。<br>默认值：无<br>配置原则：无 |
| V6REDIRIPTYPE | IPv6重定向动作 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IPTYPE”配置为“IPv6”时为必选参数。<br>参数含义：该参数用于表示IPv6重定向动作。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- BLACKHOLE：表示丢弃互访的报文，禁止UE互访。<br>- IPADDRESS：表示重定向到目的ip地址。<br>默认值：无<br>配置原则：无 |
| IPV6ADDRESS | IPv6重定向IP地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“V6REDIRIPTYPE”配置为“IPADDRESS”时为必选参数。<br>参数含义：该参数用于表示地址类型为IPv6的重定向的目的地址。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。必须是合法的ipv6地址，16进制数，采用"X:X::X:X"形式。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [单一Gi重定向信息（GIREDIRECTPARA）](configobject/UDG/20.15.2/GIREDIRECTPARA.md)

## 使用实例

- 对缺省VPN的IPv4类型Gi重定向配置进行修改，把配置修改丢弃用户互访报文：
  ```
  MOD GIREDIRECTPARA:VPNINSTANCE="_public_",IPTYPE=IPv4,V4REDIRIPTYPE=BLACKHOLE;
  ```
- 对名为“vpn1”的VPN的IPv6类型Gi重定向配置进行修改，把配置修改为用户互访报文重定向到fe80:0000:0000:0000:0000:0000:0000:0000的目的地址上：
  ```
  MOD GIREDIRECTPARA:VPNINSTANCE="vpn1",IPTYPE=IPv6,V6REDIRIPTYPE=IPADDRESS,IPV6ADDRESS="fe80:0000:0000:0000:0000:0000:0000:0000";
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改单一Gi重定向信息（MOD-GIREDIRECTPARA）_82837770.md`
