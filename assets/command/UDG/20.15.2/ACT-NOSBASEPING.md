---
id: UDG@20.15.2@MMLCommand@ACT NOSBASEPING
type: MMLCommand
name: ACT NOSBASEPING（NOS Base平面网络Ping功能）
nf: UDG
version: 20.15.2
verb: ACT
object_keyword: NOSBASEPING
command_category: 动作类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务公共功能管理
- 操作维护
- 系统调测
- 基础网络调测
status: active
---

# ACT NOSBASEPING（NOS Base平面网络Ping功能）

## 功能

该命令用于诊断不同节点间网络通断。PING是最常见的用于检测网络设备可访问性的调试工具，它使用ICMP报文来检测远程设备是否可用、远程主机通信的来回旅程的延迟以及包的丢失情况。

应用场景包括：

- 第一种场景：云设备内部，检测VNFC和VNFP的连通性。
- 第二种场景：设备的转发面，检测与其他配置IP业务设备的连通性。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定RU名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，区分大小写。<br>默认值：无<br>配置原则：当不输入时显示所有的RU的信息。使用<br>[**DSP RU**](../../../系统管理/资源管理/RU管理/显示资源单元信息（DSP RU）_59103857.md)<br>查看RU名称。 |
| IPVERSION | IP协议版本号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定发送ECHO-REQUEST报文的IP协议版本。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- IPv4：IPv4协议族。<br>- IPv6：IPv6协议族。<br>默认值：无<br>配置原则：无 |
| PACKETCOUNT | 发包数 | 可选必选说明：可选参数<br>参数含义：该参数用于指定发送ECHO-REQUEST报文次数。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～172800，单位是个数。<br>默认值：5<br>配置原则：无 |
| PACKETSIZE | 报文字节数 | 可选必选说明：可选参数<br>参数含义：该参数用于指定ECHO-REQUEST报文的有效载荷长度。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为20～9600，单位是字节。<br>默认值：56<br>配置原则：无 |
| SOURCEIPV4ADDRESS | 源IPv4地址 | 可选必选说明：条件可选参数，该参数在<br>“IPVERSION”<br>配置为<br>“IPv4”<br>时为可选参数。<br>参数含义：该参数用于指定发送ECHO-REQUEST报文的源IPv4地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无 |
| SOURCEIPV6ADDRESS | 源IPv6地址 | 可选必选说明：条件可选参数，该参数在<br>“IPVERSION”<br>配置为<br>“IPv6”<br>时为可选参数。<br>参数含义：该参数用于指定发送ECHO-REQUEST报文的源IPv6地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |
| DESTIPV4ADDRESS | 目的IPv4地址 | 可选必选说明：条件必选参数，该参数在<br>“IPVERSION”<br>配置为<br>“IPv4”<br>时为必选参数。<br>参数含义：该参数用于指定目的主机IPv4地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无 |
| DESTIPV6ADDRESS | 目的IPv6地址 | 可选必选说明：条件必选参数，该参数在<br>“IPVERSION”<br>配置为<br>“IPv6”<br>时为必选参数。<br>参数含义：该参数用于指定目的主机IPv6地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过<br>**LST VNFC**<br>命令获取。<br>默认值：无<br>配置原则：只能填写通过<br>**LST VNFC**<br>命令查询到的管理代理标识，但不能填写0，0表示VNFP。 |

## 操作的配置对象

- [NOS Base平面网络Ping功能（NOSBASEPING）](configobject/UDG/20.15.2/NOSBASEPING.md)

## 使用实例

检查IP地址为192.168.0.2的主机是否可达：

```
ACT NOSBASEPING: RUNAME="ACS_OM_RU_0001", IPVERSION=IPv4, PACKETCOUNT=1, DESTIPV4ADDRESS="192.168.0.2"
,SERVICEINSTANCE="ACS"
;
```

```
RETCODE = 99999  实时上报成功

仍有后续报告输出
---    END

RETCODE = 99999  实时上报成功

  PING 192.168.0.2: 56  字节

仍有后续报告输出
---    END

RETCODE = 99999  实时上报成功

    答复从 192.168.0.2：字节数=56 顺序号=1 生存时间=64 往返时间=0.032 毫秒

仍有后续报告输出
---    END

RETCODE = 0  操作成功

  --- 192.168.0.2 ping 统计 ---
    发送包数: 1
    接收包数: 1
    0.00% 包丢失
    往返时间 最小/平均/最大 = 0.032/0.032/0.032 毫秒

共有4个报告
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/NOS-Base平面网络Ping功能（ACT-NOSBASEPING）_59113817.md`
