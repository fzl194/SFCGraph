# 删除EpRpDyn对象本端IP地址或者删除远端IP地址段（RMV EPRPDYNIP）

- [命令功能](#ZH-CN_CONCEPT_0182837841__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0182837841__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0182837841__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0182837841__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0182837841__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0182837841)

**适用NF：SGW-U、PGW-U、UPF**

该命令用于删除EpRpDyn对象的本端IP地址或者对端IP地址段。

#### [注意事项](#ZH-CN_CONCEPT_0182837841)

- 该命令执行后立即生效。
- 删除本端IP地址时，如果不输入参数，则删除该EPRPDYN对象所有本端IP地址。
- 删除远端地址段时，如果不输入参数，则删除该EPRPDYN对象所有对端地址段。

#### [操作用户权限](#ZH-CN_CONCEPT_0182837841)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0182837841)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| EPRPDYNNAME | 对象名称 | 可选必选说明：必选参数<br>参数含义：对象名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格以及特殊字符：“_”、“#”、“$”等。<br>默认值：无<br>配置原则：无 |
| IPVERSION | IP地址版本类型 | 可选必选说明：必选参数<br>参数含义：该参数用来指定IP地址版本类型。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- IPV4：表示地址类型为IPv4。<br>- IPV6：表示地址类型为IPv6。<br>默认值：无<br>配置原则：无 |
| IPV4DIRECTION | IPv4方向 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IPVERSION”配置为“IPV4”时为必选参数。<br>参数含义：IPv4地址的方向。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- LOCAL_IP：本端IP地址。<br>- FAR_IP：对端IP地址段。<br>默认值：无<br>配置原则：无 |
| IPV4ADDR | IPv4地址 | 可选必选说明：条件可选参数<br>前提条件：该参数在“IPV4DIRECTION”配置为“FAR_IP” 或 “LOCAL_IP”时为可选参数。<br>参数含义：本端IPv4地址或者对端IPv4地址段。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。点分十进制格式，新配置的本端IPv4地址或者对端IPv4地址段不会覆盖已有的本端IPv4地址或者对端IPv4地址段。<br>默认值：无<br>配置原则：无 |
| FARIPV4MASKLEN | IPv4掩码长度 | 可选必选说明：条件可选参数<br>前提条件：该参数在“IPV4DIRECTION”配置为“FAR_IP”时为可选参数。<br>参数含义：对端IPv4地址段掩码。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～32。<br>默认值：无<br>配置原则：无 |
| IPV6DIRECTION | IPv6方向 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IPVERSION”配置为“IPV6”时为必选参数。<br>参数含义：IPv6地址的方向。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- LOCAL_IP：本端IP地址。<br>- FAR_IP：对端IP地址段。<br>默认值：无<br>配置原则：无 |
| IPV6ADDR | IPv6地址 | 可选必选说明：条件可选参数<br>前提条件：该参数在“IPV6DIRECTION”配置为“FAR_IP” 或 “LOCAL_IP”时为可选参数。<br>参数含义：本端IPv6地址或者对端IPv6地址段。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。冒号分十六进制格式，新配置的本端IPv6地址或者对端IPv6地址段不会覆盖已有的本端IPv6地址或者对端IPv6地址段。<br>默认值：无<br>配置原则：无 |
| FARIPV6MASKLEN | IPv6掩码长度 | 可选必选说明：条件可选参数<br>前提条件：该参数在“IPV6DIRECTION”配置为“FAR_IP”时为可选参数。<br>参数含义：对端IPv6地址段掩码。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～128。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0182837841)

- 删除EPRPDYN对象pgw1的本端IP地址192.168.12.11：
  ```
  RMV EPRPDYNIP:EPRPDYNNAME="pgw1",IPVERSION=IPV4,IPV4DIRECTION=LOCAL_IP,IPV4ADDR="192.168.12.11";
  ```
- 删除EPRPDYN对象pgw1的所有本端IP地址：
  ```
  RMV EPRPDYNIP:EPRPDYNNAME="pgw1",IPVERSION=IPV4,IPV4DIRECTION=LOCAL_IP;
  ```
- 删除EPRPDYN对象pgw1的对端IP地址段192.168.1.0：
  ```
  RMV EPRPDYNIP:EPRPDYNNAME="pgw1",IPVERSION=IPV4,IPV4DIRECTION=FAR_IP,IPV4ADDR="192.168.1.0";
  ```
- 删除EPRPDYN对象pgw1的所有对端IP地址段：
  ```
  RMV EPRPDYNIP:EPRPDYNNAME="pgw1",IPVERSION=IPV4,IPV4DIRECTION=FAR_IP;
  ```
