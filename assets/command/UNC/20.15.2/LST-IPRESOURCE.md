---
id: UNC@20.15.2@MMLCommand@LST IPRESOURCE
type: MMLCommand
name: LST IPRESOURCE（查询IP资源）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: IPRESOURCE
command_category: 查询类
applicable_nf:
- NCG
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NCG业务及策略管理
- 计费管理
- 业务配置管理
- IP资源
status: active
---

# LST IPRESOURCE（查询IP资源）

## 功能

**适用NF：NCG**

该命令用于查询IP资源的详细信息：

如果需要查询全部信息，请不要输入任何参数。

如果需要查询某方面的详细信息，请输入具体参数。例如，查询用于话单分发的IP资源的详细信息，请输入“IP资源用途”值为“Bi”。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPRID | IP资源标识 | 可选必选说明：可选参数<br>参数含义：用于表示一个IP资源对象，全局唯一。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32。<br>默认值：无<br>配置原则：无 |
| IPRPURPOSE | IP资源用途 | 可选必选说明：可选参数<br>参数含义：IP资源用途。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- Bi：Bi。<br>- Omi：Omi。<br>- OmiAndBi：Omi&Bi。<br>- Ga：Ga。<br>默认值：无<br>配置原则：无 |
| RUID | RU的ID | 可选必选说明：条件可选参数<br>前提条件：该参数在“IPRPURPOSE”配置为“Bi”、“Omi” 或 “OmiAndBi”时为条件可选参数。<br>参数含义：RU的ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为64～4294967294。<br>默认值：无<br>配置原则：该值需要执行<br>[**LST SERVICERUSTATE**](../../../../../平台服务管理/单体服务编排功能管理/系统管理/资源管理/RU信息/查询RU的信息(LST SERVICERUSTATE)_29626965.md)<br>命令，查询出存在的RU ID进行填写。 |
| IPTYPE | IP地址类型 | 可选必选说明：可选参数<br>参数含义：用于表示Ga、Bi、Omi、OmiAndBi口IP地址属于IPv4网络还是IPv6网络，需根据当前局点规划选择其中一种。<br>数据来源：对端协商<br>取值范围：枚举类型。<br>- IPV4：IPv4。<br>- IPV6：IPv6。<br>默认值：无<br>配置原则：无 |
| IPV4 | IPv4地址 | 可选必选说明：条件可选参数<br>前提条件：该参数在“IPTYPE”配置为“IPV4”时为条件可选参数。<br>参数含义：用于话单接收的IPv4地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。0.0.0.0-255.255.255.255。<br>默认值：无<br>配置原则：无 |
| IPV6 | IPv6地址 | 可选必选说明：条件可选参数<br>前提条件：该参数在“IPTYPE”配置为“IPV6”时为条件可选参数。<br>参数含义：用于话单接收的IPv6地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。::～FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF。<br>默认值：无<br>配置原则：无 |
| VPNNAME | 虚拟网络名称 | 可选必选说明：可选参数<br>参数含义：该参数为VPN名称，是业务消息转发时的鉴权参数。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@IPRESOURCE]] · IP资源（IPRESOURCE）

## 使用实例

查询用于话单分发或者备份的IP资源，示例如下：

```
LST IPRESOURCE:;
```

```
RETCODE = 0  操作成功。

结果如下:
--------
  IP资源标识  =  IP_CDR_Distribution_1st
  IP资源用途  =  Omi&Bi
      RU的ID  =  66
  IP地址类型  =  IPv4
    IPv4地址  =  192.168.20.37
    IPv6地址  =  ::
虚拟网络名称  =  _public_
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-IPRESOURCE.md`
