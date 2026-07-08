# 删除BGP对等体组地址族（RMV BGPPEERGROUPAF）

- [命令功能](#ZH-CN_CONCEPT_0000001600866169__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000001600866169__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000001600866169__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000001600866169__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000001600866169__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0000001600866169)

该命令用于删除BGP对等体组地址族。

#### [注意事项](#ZH-CN_CONCEPT_0000001600866169)

该命令执行后立即生效。

#### [操作用户权限](#ZH-CN_CONCEPT_0000001600866169)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000001600866169)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VRFNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：_public_<br>配置原则：使用LST L3VPNINST命令查看可用VPN。 |
| AFTYPE | 地址族类型 | 可选必选说明：必选参数<br>参数含义：该参数用于给定VRF的地址族类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4uni：IPv4地址族。<br>- ipv4vpn：VPNv4地址族。<br>- ipv6uni：IPv6地址族。<br>- ipv6vpn：VPNv6地址族。<br>默认值：无 |
| GROUPNAME | 对等体组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定相应的对等体组。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～47。<br>默认值：无<br>配置原则：使用LST BGPPEERGROUP命令查看可用对等体组名。 |

#### [使用实例](#ZH-CN_CONCEPT_0000001600866169)

- 删除相应对等体组的IPv4地址族：
  ```
  RMV BGPPEERGROUPAF:VRFNAME="_public_",GROUPNAME="asdf",AFTYPE=ipv4uni;
  ```
- 删除相应对等体组的IPv6地址族：
  ```
  RMV BGPPEERGROUPAF:VRFNAME="_public_",GROUPNAME="asdf",AFTYPE=ipv6uni;
  ```
