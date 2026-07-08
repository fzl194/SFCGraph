---
id: UNC@20.15.2@MMLCommand@MOD SFCPARA
type: MMLCommand
name: MOD SFCPARA（修改SFC参数）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: SFCPARA
command_category: 配置类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 感知业务管理
- 感知控制面功能参数
status: active
---

# MOD SFCPARA（修改SFC参数）

## 功能

**适用NF：AMF**

在部署感知的场景下，通过MOD SFCPARA修改SFC的参数（IP地址、端口号）。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SFCINSTANCEID | SFC实例ID | 可选必选说明：必选参数<br>参数含义：该参数用于指定SFC网元的实例ID。<br>数据来源：对端协商<br>取值范围：字符串类型，输入长度范围是1~64。只允许输入十进制数字（0-9），除0之外不能以0开头。对应十进制数取值范围是0~4294967295。<br>默认值：无<br>配置原则：无 |
| IPTYPE | IP类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SFC的地址的IP类型。<br>数据来源：对端协商<br>取值范围：<br>- “IPv4（IPv4）”：IPv4<br>- “IPv6（IPv6）”：IPv6<br>默认值：无<br>配置原则：无 |
| IPV4ADDRESS | IPv4地址 | 可选必选说明：该参数在"IPTYPE"配置为"IPv4"时为条件必选参数。<br>参数含义：该参数用于指定SFC的IPv4地址。<br>数据来源：对端协商<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无 |
| IPV6ADDRESS | IPv6地址 | 可选必选说明：该参数在"IPTYPE"配置为"IPv6"时为条件必选参数。<br>参数含义：该参数用于指定SFC的IPv6地址。<br>数据来源：对端协商<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |
| PORT | 端口号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SFC的端口号。<br>数据来源：对端协商<br>取值范围：整数类型，取值范围是1~65534。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SFCPARA]] · SFC参数（SFCPARA）

## 使用实例

若运营商要修改一条SFC的参数信息，SFC实例ID为1，IP类型为IPv4，地址为192.168.4.15，端口号为8080，可以用如下命令：

```
MOD SFCPARA: SFCINSTANCEID="1", IPTYPE=IPv4, IPV4ADDRESS="192.168.4.15", PORT=8080;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-SFCPARA.md`
