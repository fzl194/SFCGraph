---
id: UNC@20.15.2@MMLCommand@ADD ACTRL
type: MMLCommand
name: ADD ACTRL（增加接入控制）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: ACTRL
command_category: 配置类
applicable_nf:
- NCG
effect_mode: ''
is_dangerous: false
max_records: 256
category_path:
- 业务服务管理
- NCG业务及策略管理
- 计费管理
- 业务配置管理
- 接入控制
status: active
---

# ADD ACTRL（增加接入控制）

## 功能

**适用NF：NCG**

该命令用于增加接入控制模块采用的IP地址和端口号。本网元的接入控制功能，由资源管理模块RCM（Resource Control Management）和全局控制模块GACM（Global Access Control Module）共同完成。它的功能是通过与话单产生网元协商，将其发送的话单分配到网元不同的接入网元分组上进行处理，平衡负载，提高可靠性。

PS域网元的IP和端口号要根据实际配置。

## 注意事项

- 该命令执行后，需在“MML命令行 - UNC”窗口执行“[**RST VNFC**](../../../../../平台服务管理/单体服务公共功能管理/系统管理/复位系统/重启系统（RST VNFC）_59103634.md)”命令重新启动系统才能生效。
- 该命令最大记录数为256。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ACID | 接入控制标识 | 可选必选说明：必选参数<br>参数含义：用于在NCG中定义一条接入控制的数据记录。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32。<br>默认值：无<br>配置原则：不能输入的特殊字符请参考“<br>[**特殊字符表**](../话单稽核/增加话单稽核（ADD CDRAUDIT）_51174239.md#ZH-CN_CONCEPT_0251174239__table_0365FEF0)<br>”。 |
| AGID | 接入网元分组标识 | 可选必选说明：必选参数<br>参数含义：用于区分不同域的接入网元。<br>数据来源：对端协商<br>取值范围：字符串类型，输入长度范围为1～32。<br>默认值：无<br>配置原则：<br>- 该值需要执行[**LST CDRPROC**](../话单处理/查询话单处理（LST CDRPROC）_51174275.md)命令查询“接入网元分组标识”。如果没有符合要求的“接入网元分组标识”，还需执行[**ADD CDRPROC**](../话单处理/增加话单处理（ADD CDRPROC）_51174272.md)命令增加。<br>- 不能输入的特殊字符请参考“[**特殊字符表**](../话单稽核/增加话单稽核（ADD CDRAUDIT）_51174239.md#ZH-CN_CONCEPT_0251174239__table_0365FEF0)”。 |
| IPRID | IP资源标识 | 可选必选说明：必选参数<br>参数含义：用于表示IP资源。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32。<br>默认值：无<br>配置原则：<br>- 该值需要执行[**LST IPRESOURCE**](../IP资源/查询IP资源（LST IPRESOURCE）_51174285.md)命令查询“IP资源用途”为“Ga”的“IP资源标识”的值。<br>- 如果没有符合要求的IP资源，还需执行[**ADD IPRESOURCE**](../IP资源/增加IP资源（ADD IPRESOURCE）_51174282.md)命令增加。<br>- NCG采用此IP与话单产生网元通信。<br>- 不能输入的特殊字符请参考“[**特殊字符表**](../话单稽核/增加话单稽核（ADD CDRAUDIT）_51174239.md#ZH-CN_CONCEPT_0251174239__table_0365FEF0)”。 |
| PORT | 端口 | 可选必选说明：必选参数<br>参数含义：用于表示接入控制模块采用的端口。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65535。<br>默认值：无<br>配置原则：建议配置的端口号大于1024，防止和操作系统使用的端口号冲突。 |
| RIPTYPE | 重定向IP地址类型 | 可选必选说明：可选参数<br>参数含义：用于表示重定向IP地址属于IPv4网络还是IPv6网络，需根据当前局点规划选择其中一种。<br>数据来源：对端协商<br>取值范围：枚举类型。<br>- IPV4：IPv4。<br>- IPV6：IPv6。<br>默认值：无<br>配置原则：无 |
| RIPV4 | 重定向IPv4 | 可选必选说明：条件必选参数<br>前提条件：该参数在“RIPTYPE”配置为“IPV4”时为条件必选参数。<br>参数含义：用于表示接入控制模块采用的重定向IPv4地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：当“IP资源标识”指定的IP或端口故障时，可以切换到“重定向IP”和“重定向端口”。 |
| RIPV6 | 重定向IPv6 | 可选必选说明：条件必选参数<br>前提条件：该参数在“RIPTYPE”配置为“IPV6”时为条件必选参数。<br>参数含义：用于表示接入控制模块采用的重定向IPv6地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：<br>- 当“IP资源标识”指定的IP或端口故障时，可以切换到“重定向IP”和“重定向端口”。<br>- IPv6地址必须是全球单播地址，不能为::、FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、2001:X:X:X:X:X::、环回地址(::1)、链路本地地址(FE80::/10)和组播地址(FF00::/8)。<br>- 该参数的掩码缺省为FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF，不可更改。 |
| RPORT | 重定向端口 | 可选必选说明：可选参数<br>参数含义：用于接入控制模块采用的重定向端口。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65535。<br>默认值：无<br>配置原则：当“IP资源标识”指定的IP或端口故障时，可以切换到“重定向IP”和“重定向端口”。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/ACTRL]] · 接入控制（ACTRL）

## 使用实例

增加一个接入控制采用的IP示例：

```
ADD ACTRL: ACID="ps_actrl", AGID="PS_GROUP_1", IPRID="IP_Ga_CDRReceive_1st", PORT=9990, RIPTYPE=IPV4, RIPV4="192.168.3.5", RPORT=9999;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-ACTRL.md`
