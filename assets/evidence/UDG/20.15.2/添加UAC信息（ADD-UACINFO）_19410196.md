# 添加UAC信息（ADD UACINFO）

- [命令功能](#ZH-CN_CONCEPT_0000203719410196__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000203719410196__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000203719410196__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000203719410196__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000203719410196__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0000203719410196)

**适用NF：PGW-U、UPF**

用于配置UAC服务器的地址信息。

#### [注意事项](#ZH-CN_CONCEPT_0000203719410196)

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 请在对接UAC服务器的专网设备上进行配置，其它设备上请勿配置该命令。

#### [操作用户权限](#ZH-CN_CONCEPT_0000203719410196)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000203719410196)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| UACNAME | UAC名称 | 可选必选说明：必选参数<br>参数含义：UAC名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| IPTYPE | IP地址类型 | 可选必选说明：必选参数<br>参数含义：该参数用来指定IP类型。<br>数据来源：对端协商<br>取值范围：枚举类型。<br>- IPV4：表示地址类型为IPv4。<br>- IPV6：表示地址类型为IPv6。<br>- IPVER_ALL：表示地址类型为IPv4和IPv6。<br>默认值：无<br>配置原则：无 |
| IPV4ADDRESS | UAC IPv4地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IPTYPE”配置为“IPV4” 或 “IPVER_ALL”时为必选参数。<br>参数含义：UAC的IPv4地址。<br>数据来源：对端协商<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：根据与当前UPF对接的MPF上通过ADD MPFLOGICINF命令配置的uacif1/0/0逻辑口的IPv4地址进行配置。 |
| IPV6ADDRESS | UAC IPv6地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IPTYPE”配置为“IPV6” 或 “IPVER_ALL”时为必选参数。<br>参数含义：UAC的IPv6地址。<br>数据来源：对端协商<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：根据与当前UPF对接的MPF上通过ADD MPFLOGICINF命令配置的uacif1/0/0逻辑口的IPv6地址进行配置。 |

#### [使用实例](#ZH-CN_CONCEPT_0000203719410196)

使用命令ADD UACINFO配置UAC IPv4地址：

```
ADD UACINFO: UACNAME="test", IPTYPE=IPV4, IPV4ADDRESS="192.168.0.10";
```
