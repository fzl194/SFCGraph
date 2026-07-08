# 删除VPN Target（RMV VPNTARGET）

- [命令功能](#ZH-CN_CONCEPT_0000001549961586__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000001549961586__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000001549961586__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000001549961586__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000001549961586__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0000001549961586)

该命令用于删除指定VPN地址族参数VPN Target。

#### [注意事项](#ZH-CN_CONCEPT_0000001549961586)

- 该命令执行后立即生效。
- 需要确保指定的VPN实例和地址族在设备上已创建。

#### [操作用户权限](#ZH-CN_CONCEPT_0000001549961586)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000001549961586)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VRFNAME | VPN实例名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定用户增加地址族的L3VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：使用LST L3VPNINST命令查看可用VPN。 |
| AFTYPE | 地址族类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定VPN实例下的地址族。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4uni：IPv4地址族。<br>- ipv6uni：IPv6地址族。<br>默认值：无 |
| VRFRTTYPE | VPN RT类型 | 可选必选说明：必选参数<br>参数含义：该参数用于设定VPN Target的类型为Import RT或者是Export RT。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- export_extcommunity：发布扩展团体属性。<br>- import_extcommunity：引入扩展团体属性。<br>默认值：无 |
| VRFRTVALUE | VPN RT的值 | 可选必选说明：必选参数<br>参数含义：该参数用于设定VPN Target值。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～21。取值范围是X.X.X.X:number<0-65535>、number<0-65535>:number<0-4294967295>、number<0-65535>.number<0-65535>:number<0-65535>或者number<65536-4294967295>:number<0-65535>，但不支持配置为0:0和0.0:0。<br>默认值：无 |

#### [使用实例](#ZH-CN_CONCEPT_0000001549961586)

删除名称为“vrf1”的VPN实例下的IPv4单播地址族的VPN Target：

```
RMV VPNTARGET:VRFNAME="vrf1", AFTYPE=ipv4uni, VRFRTTYPE=export_extcommunity,VRFRTVALUE="1:1";
```
