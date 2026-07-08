---
id: UNC@20.15.2@MMLCommand@ADD IPRESOURCE
type: MMLCommand
name: ADD IPRESOURCE（增加IP资源）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: IPRESOURCE
command_category: 配置类
applicable_nf:
- NCG
effect_mode: ''
is_dangerous: false
max_records: 512
category_path:
- 业务服务管理
- NCG业务及策略管理
- 计费管理
- 业务配置管理
- IP资源
status: active
---

# ADD IPRESOURCE（增加IP资源）

## 功能

**适用NF：NCG**

该命令用于增加CG侧话单接收、分发和备份时所使用的IP地址等信息，包含添加、删除、修改、查询IP资源命令。

以下应用情况时，需要增加IP资源：

1、接收对端网元发来的话单：CG配置一个IP地址用来接收话单。

2、将话单分发到计费中心：CG采用一个IP地址与计费中心通信。

3、将话单备份到第三方服务器/UDN服务器：CG采用一个IP地址与第三方服务器/UDN服务器通信。

## 注意事项

- 该命令执行后，需在“MML命令行 - UNC”窗口执行“[**RST VNFC**](../../../../../平台服务管理/单体服务公共功能管理/系统管理/复位系统/重启系统（RST VNFC）_59103634.md)”命令重新启动系统才能生效。
- 该命令最大记录数为512。
- 增加用于话单接收的IP资源前需确保用于话单接收的网口已接上网线，且网线的另一端连接到交换机上。
- 增加用于话单分发的IP资源前需确保用于话单分发的网口已接上网线，且网线的另一端连接到交换机上。
- 增加用于话单备份的IP资源前需确保用于话单备份的网口已接上网线，且网线的另一端连接到交换机或者第三方服务器/UDN服务器上。
- Bi、Omi、BiAndOmi接口，每一个RU必须配置一个而且只能配置一个IPv4和IPv6地址；当Bi地址和Omi地址分设时，每个RU都需要配置一个Bi地址和一个Omi地址，如果Bi地址和Omi地址合设，每个RU配置一个OmiAndBi地址；Ga接口，最多配置一个IPv4和一个IPv6地址。
- IPv4或者IPv6类型的Ga口地址，必须配置相应的接入控制模块之后，IP地址才能生效。
- NCG不支持IPv6以下格式地址下发：FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、::、::1、FE80::/10、FF00::/8、2001:X:X:X:X:X:: 。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPRID | IP资源标识 | 可选必选说明：必选参数<br>参数含义：用于表示一个IP资源对象，全局唯一。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32。<br>默认值：无<br>配置原则：<br>- 该参数只包含数字、字母和下划线。<br>- 增加话单分发的IP资源。 建议配置为：IP_Bi_CDRDistribution_1st。<br>- 增加话单备份的IP资源。 建议配置为：IP_Omi_CDRBackup_1st。<br>- 话单备份与分发采用同一IP资源。 建议配置为：IP_Backup_Distribution_1st。<br>- 增加话单接收的IP资源。 建议配置为：IP_Ga_CDRReceive_1st。 |
| IPRPURPOSE | IP资源用途 | 可选必选说明：必选参数<br>参数含义：IP资源用途。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- Bi：Bi。<br>- Omi：Omi。<br>- OmiAndBi：Omi&Bi。<br>- Ga：Ga。<br>默认值：无<br>配置原则：<br>- Bi- 计费接口，用于话单分发。当CG分发话单到计费中心或者计费中心到CG取话单时，选择此选项。<br>- Omi- 备份接口，用于话单备份。当CG需备份话单到第三方服务器/UDN服务器时，选择此选项。<br>- OmiAndBi- 计费和备份接口，用于话单分发和备份。当分发和备份采用同一IP资源时，选择此选项。<br>- Ga- Ga接口，用于接收话单。当CG需要从SMF网元接收话单时，选择此选项。 |
| RUID | RU的ID | 可选必选说明：条件必选参数<br>前提条件：该参数在“IPRPURPOSE”配置为“Bi”、“Omi” 或 “OmiAndBi”时为条件必选参数。<br>参数含义：RU的ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为64～4294967294。<br>默认值：无<br>配置原则：<br>- 该值需要执行[**LST SERVICERUSTATE**](../../../../../平台服务管理/单体服务编排功能管理/系统管理/资源管理/RU信息/查询RU的信息(LST SERVICERUSTATE)_29626965.md)命令，查询出存在的RU ID进行填写。 |
| IPTYPE | IP地址类型 | 可选必选说明：必选参数<br>参数含义：用于表示Ga、Bi、Omi、OmiAndBi口IP地址属于IPv4网络还是IPv6网络，需根据当前局点规划选择其中一种。<br>数据来源：对端协商<br>取值范围：枚举类型。<br>- IPV4：IPv4。<br>- IPV6：IPv6。<br>默认值：无<br>配置原则：当且仅当选择开关型参数“IP资源用途”的值为“Ga(Ga)”、“Bi(Bi)”、“Omi(Omi)”或“OmiAndBi(Omi&Bi)”时，此参数有效。 |
| IPV4 | IPv4地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IPTYPE”配置为“IPV4”时为条件必选参数。<br>参数含义：用于话单接收的IPv4地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。0.0.0.0-255.255.255.255。<br>默认值：无<br>配置原则：<br>- 业务地址不能配置为0.x.y.z、255.255.255.255和环回地址(127.x.y.z)。<br>- 业务地址必须是A、B或者C类地址。<br>- 不能配置与外联口IP地址相同的IP地址。 |
| IPV6 | IPv6地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IPTYPE”配置为“IPV6”时为条件必选参数。<br>参数含义：用于话单接收的IPv6地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。::～FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF。<br>默认值：无<br>配置原则：<br>- IPv6地址必须是全球单播地址，不能为::、FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、2001:X:X:X:X:X::、环回地址(::1)、链路本地地址(FE80::/10)和组播地址(FF00::/8)。<br>- 该参数的掩码缺省为FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF，不可更改。<br>- 不能配置与外联口IP地址相同的IP地址。 |
| VPNNAME | 虚拟网络名称 | 可选必选说明：可选参数<br>参数含义：该参数为VPN名称，是业务消息转发时的鉴权参数。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：_public_<br>配置原则：该参数区分大小写，不支持空格。 |

## 操作的配置对象

- [IP资源（IPRESOURCE）](configobject/UNC/20.15.2/IPRESOURCE.md)

## 使用实例

- 用于话单接收的IP资源示例：
  ```
  ADD IPRESOURCE: IPRID="IP_Ga_CDRReceive_1st", IPRPURPOSE=Ga, IPTYPE=IPV4, IPV4="10.31.14.3", VPNNAME="_public_";
  其中“IPRID”可以自定义,“IPRPURPOSE”、“IPTYPE”、“IPV4”、“VPNNAME”需要根据实际情况进行配置。
  ```
- 用于话单分发的IP资源示例：
  ```
  ADD IPRESOURCE: IPRID="IP_Bi_CDRDistribution_1st", IPRPURPOSE=Bi, RUID=66, IPTYPE=IPV4, IPV4="10.31.14.3", VPNNAME="_public_";
  其中“IPRID”可以自定义,“IPRPURPOSE”、“RUID”、“IPTYPE”、“IPV4”、“VPNNAME”需要根据实际情况进行配置。
  ```
- 用于话单备份的IP资源示例：
  ```
  ADD IPRESOURCE: IPRID="IP_Omi_CDRBackup_1st", IPRPURPOSE=Omi, RUID=66, IPTYPE=IPV4, IPV4="10.31.14.3", VPNNAME="_public_";
  其中“IPRID”可以自定义,“IPRPURPOSE”、“RUID”、“IPTYPE”、“IPV4”、“VPNNAME”需要根据实际情况进行配置。
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加IP资源（ADD-IPRESOURCE）_51174282.md`
