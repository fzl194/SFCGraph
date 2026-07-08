---
id: UNC@20.15.2@MMLCommand@ADD RESERVEDIP
type: MMLCommand
name: ADD RESERVEDIP（增加预留IP资源）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: RESERVEDIP
command_category: 配置类
applicable_nf:
- NCG
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NCG业务及策略管理
- 计费管理
- 业务系统管理
- 预留IP资源
status: active
---

# ADD RESERVEDIP（增加预留IP资源）

## 功能

**适用NF：NCG**

该命令用于IP资源预埋，以便新增RU后有IP资源可以迁移到新RU上，减少用户对接NCG新规划RU的工作 。

以下情况时，需要增加预留IP资源：

新开局只配置了少量RU，为后续扩容需要预埋IP资源。

## 注意事项

- 该命令生效需在“MML命令行 - UNC”窗口执行“SET IPCONVERGENCE”命令开启IP收敛功能。
- 该命令执行后，需在“MML命令行 - UNC”窗口执行“[**RST VNFC**](../../../../../平台服务管理/单体服务公共功能管理/系统管理/复位系统/重启系统（RST VNFC）_59103634.md)”命令重新启动系统才能生效。
- 增加用于话单接收的预留IP资源前需确保用于话单接收的网口已接上网线，且网线的另一端连接到交换机上。
- NCG不支持IPv6以下格式地址下发：FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、::、::1、FE80::/10、FF00::/8、2001:X:X:X:X:X:: 。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPRID | 预留IP资源标识 | 可选必选说明：必选参数<br>参数含义：用于表示一个预留IP资源对象，全局唯一。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32。<br>默认值：无<br>配置原则：该参数只包含数字、字母和下划线 |
| IPV4 | IPv4地址 | 可选必选说明：条件必选参数<br>参数含义：用于话单接收的IPv4地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。0.0.0.0-255.255.255.255。<br>默认值：无<br>配置原则：<br>- IPV4地址与IPV6地址至少配置一个<br>- 同一RU的预留IP资源和IP资源总数不能超过32<br>- 业务地址不能配置为0.x.y.z、255.255.255.255和环回地址(127.x.y.z)。<br>- 业务地址必须是A、B或者C类地址。<br>- 不能与IPRESOURCE中配置的地址相同。 |
| IPV6 | IPv6地址 | 可选必选说明：条件必选参数<br>参数含义：用于话单接收的IPv6地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。::～FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF。<br>默认值：无<br>配置原则：<br>- IPV4地址与IPV6地址至少配置一个<br>- 同一RU的预留IP资源和IP资源总数不能超过32<br>- IPv6地址必须是全球单播地址，不能为::、FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、2001:X:X:X:X:X::、环回地址(::1)、链路本地地址(FE80::/10)和组播地址(FF00::/8)。<br>- 该参数的掩码缺省为FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF，不可更改。<br>- 不能与IPRESOURCE中配置的地址相同。 |
| IPRPURPOSE | 预留IP资源用途 | 可选必选说明：必选参数<br>参数含义：预留IP资源用途。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- Bi：Bi<br>- Omi：Omi<br>- OmiAndBi：Omi&Bi<br>默认值：无<br>配置原则：<br>- 同一个RU的IP资源（包括RESERVEDIP和IPRESOURCE）不能重复。<br>- Bi：计费接口，用于话单分发。当CG分发话单到计费中心或者计费中心到CG取话单时，选择此选项。<br>- Omi：备份接口，用于话单备份。当CG需备份话单到第三方服务器/UDN服务器时，选择此选项。<br>- OmiAndBi：计费和备份接口，用于话单分发和备份。当分发和备份采用同一IP资源时，选择此选项。 |
| PRFNAME | 格式引擎包名 | 可选必选说明：必选参数<br>参数含义：格式引擎包定义了CG话单处理的业务规则，主要包括话单字段过滤配置、分拣条件配置、通道配置、话单处理脚本等。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～255。<br>默认值：无<br>配置原则：<br>- “格式引擎包名”可以通过[DSP FEMPACKET](../../业务配置管理/格式引擎包/显示格式引擎配置信息（DSP FEMPACKET）_51174306.md)命令获取，其他名称无法生效。<br>- 多个“格式引擎包名”使用“\|”分割<br>- 最多不能超过4个“格式引擎包名” |
| MNAME | 模块名称 | 可选必选说明：可选参数<br>参数含义：预留IP资源对应的模块。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～255。<br>默认值：默认反填当前最大RU加1的模块名<br>配置原则：<br>- 该参数输入格式固定为'AP'接RUID_APID，APID值为1~4。例如：RUID为66时，该参数可以是“AP66_1”、“AP66_2”、“AP66_3”、“AP66_4”。<br>- 不能输入的特殊字符请参考“[**特殊字符表**](../../业务配置管理/话单存储/增加话单存储（ADD CDRSTOR）_51174277.md#ZH-CN_CONCEPT_0251174277__table_0365FEF0)”<br>- 多个“模块名称”使用“\|”分割<br>- “模块名称”反填个数与“格式引擎包名”个数一致 |
| RUID | RU的ID | 可选必选说明：可选参数<br>参数含义：RU的ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为64～4294967294。<br>默认值：默认反填当前最少IP资源和预留IP资源RU的ID<br>配置原则：<br>- 该值需要执行[**LST SERVICERUSTATE**](../../../../../平台服务管理/单体服务编排功能管理/系统管理/资源管理/RU信息/查询RU的信息(LST SERVICERUSTATE)_29626965.md)命令，查询出存在的RU ID进行填写。 |
| VPNNAME | 虚拟网络名称 | 可选必选说明：可选参数<br>参数含义：该参数为VPN名称，是业务消息转发时的鉴权参数。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@RESERVEDIP]] · 预留IP资源（RESERVEDIP）

## 使用实例

添加标识为IP_66_Reserved_1st的预留IP资源，示例如下：

```
ADD RESERVEDIP: IPRID="IP_66_Reserved_1st", IPV4="10.31.14.3", IPRPURPOSE=Bi, PRFNAME="PS_R15_VF80_Unicom.tar.gz", 
VPNNAME="_public_";
其中“IPRID”可以自定义,“IPV4”、“IPRPURPOSE”、“PRFNAME”需要根据实际情况进行配置。
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-RESERVEDIP.md`
