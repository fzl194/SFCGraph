---
id: UDG@20.15.2@MMLCommand@ADD GIREDIRECTPARA
type: MMLCommand
name: ADD GIREDIRECTPARA（添加单一Gi重定向信息）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: GIREDIRECTPARA
command_category: 配置类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 8194
category_path:
- 用户面服务管理
- 业务安全防护
- 用户攻击防护
- Gi重定向
- Gi重定向参数
status: active
---

# ADD GIREDIRECTPARA（添加单一Gi重定向信息）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用来配置指定VPN下的IPv4或IPv6报文Gi重定向参数，在需要控制UE之间互访的恶意攻击报文和需要通过网关将报文重定向来保证网络的安全的场景下使用此命令。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为8194。
- 任何一条VPN只支持配1条IPv4和1条IPv6重定向配置，由于VPN的配置最大值是4096，VPN实例IPv4和IPv6重定向配置最多支持均为各4096条。
- 在配置某一VPN实例的重定向功能前，需先执行ADD VPNINST命令添加该VPN实例，若配置重定向功能输入的VPN实例名不存在，则无法正确配置。
- 执行该命令配置IPV4ADDRESS参数/IPV6ADDRESS参数时，需要确保对应路由存在，否则业务无法重定向到指定ip地址对应的设备，GI重定向功能不生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VPNINSTANCE | 需绑定的VPN实例名 | 可选必选说明：必选参数<br>参数含义：该参数用于表示Gi重定向所绑定的VPN实例名。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，公网缺省VPN“_public_”不区分大小写，其它的VPN区分大小写。<br>默认值：无<br>配置原则：Gi重定向绑定的VPN，绑定VPN时需确保该VPN已经配置。 |
| IPTYPE | IP类型 | 可选必选说明：必选参数<br>参数含义：该参数用于表示重定向的目的地址类型。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- IPv4：表示地址类型为IPv4。<br>- IPv6：表示地址类型为IPv6。<br>默认值：无<br>配置原则：无 |
| V4REDIRIPTYPE | IPv4重定向动作 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IPTYPE”配置为“IPv4”时为必选参数。<br>参数含义：该参数用于表示IPv4重定向动作。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- BLACKHOLE：表示丢弃互访的报文，禁止UE互访。<br>- IPADDRESS：表示重定向到目的ip地址。<br>默认值：无<br>配置原则：无 |
| IPV4ADDRESS | IPv4重定向IP地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“V4REDIRIPTYPE”配置为“IPADDRESS”时为必选参数。<br>参数含义：该参数用于表示地址类型为IPv4的重定向的目的地址。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。必须是合法的ipv4地址，采用点分十进制"X.X.X.X"形式。<br>默认值：无<br>配置原则：无 |
| V6REDIRIPTYPE | IPv6重定向动作 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IPTYPE”配置为“IPv6”时为必选参数。<br>参数含义：该参数用于表示IPv6重定向动作。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- BLACKHOLE：表示丢弃互访的报文，禁止UE互访。<br>- IPADDRESS：表示重定向到目的ip地址。<br>默认值：无<br>配置原则：无 |
| IPV6ADDRESS | IPv6重定向IP地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“V6REDIRIPTYPE”配置为“IPADDRESS”时为必选参数。<br>参数含义：该参数用于表示地址类型为IPv6的重定向的目的地址。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。必须是合法的ipv6地址，16进制数，采用"X:X::X:X"形式。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/GIREDIRECTPARA]] · 单一Gi重定向信息（GIREDIRECTPARA）

## 使用实例

- 开启缺省VPN的Gi重定向，对缺省VPN用户，全部重定向至地址类型为IPv4的192.168.0.1的目的地址上：
  ```
  ADD GIREDIRECTPARA:VPNINSTANCE="_public_",IPTYPE=IPv4,V4REDIRIPTYPE=IPADDRESS,IPV4ADDRESS="192.168.0.1";
  ```
- 禁止名为“vpn1”的VPN下的IPv6用户互访：
  ```
  ADD GIREDIRECTPARA:VPNINSTANCE="vpn1",IPTYPE=IPv6,V6REDIRIPTYPE=BLACKHOLE;
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/添加单一Gi重定向信息（ADD-GIREDIRECTPARA）_82837767.md`
