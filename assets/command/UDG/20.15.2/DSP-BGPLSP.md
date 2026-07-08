---
id: UDG@20.15.2@MMLCommand@DSP BGPLSP
type: MMLCommand
name: DSP BGPLSP（查询BGP LSP信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: BGPLSP
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- BGP管理
- 查询BGP LSP信息
status: active
---

# DSP BGPLSP（查询BGP LSP信息）

## 功能

该命令用户查询BGP LSP信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VRFNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无 |
| AFTYPE | BGP地址族类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定BGP地址族类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4uni：IPv4地址族。<br>- ipv6uni：IPv6地址族。<br>默认值：无 |
| LSPQUERYTYPE | BGP LSP查询方式 | 可选必选说明：可选参数<br>参数含义：该参数用于指定BGP LSP查询方式。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- exclude：不包含FEC的IP地址和掩码。<br>- include：包含FEC的IP地址和掩码。<br>默认值：无 |
| IPV4ADDR | FEC IPv4地址 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv4uni”时为可选参数。<br>参数含义：该参数用于指定FEC IPv4地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无 |
| IPV4MASKLEN | FEC IPv4掩码长度 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv4uni”时为可选参数。<br>参数含义：该参数用于指定FEC IPv4地址的掩码长度。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～32。<br>默认值：无 |
| IPV6ADDR | FEC IPv6地址 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv6uni”时为可选参数。<br>参数含义：该参数用于指定FEC IPv6地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。<br>默认值：无 |
| IPV6MASKLEN | FEC IPv6掩码长度 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv6uni”时为可选参数。<br>参数含义：该参数用于指定FEC IPv6地址的前缀长度。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～128。<br>默认值：无 |
| LSRTYPE | LSR类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定LSR类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ingress：入节点。<br>- transit：中间节点。<br>- egress：出节点。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/BGPLSP]] · BGP LSP信息（BGPLSP）

## 使用实例

查询BGP LSP信息：

```
DSP BGPLSP:;
```

```

RETCODE = 0  操作成功。

结果如下
--------
VPN实例名称    路由标识（RD）    BGP地址族类型    FEC IP地址     FEC掩码长度    下一跳IP地址    入标签    出标签    入接口    出接口    LSP编号    LSP主备状态    出分片编号    LSR类型    出隧道编号    标签操作    LSP MTU    LSP时间戳    优先级模式

vrf1           1:152             IPv4uni          10.1.1.1       32             192.168.1.1     32769     NULL      NULL      NULL      32769      主             0             出节点     0x0           弹出标签    0          0            无
vrf1           1:152             IPv4uni          10.1.1.2       32             192.168.1.1     32768     NULL      NULL      NULL      32768      主             0             出节点     0x0           弹出标签    0          0            无
vrf1           2:152             IPv6uni          2001:db8::     128            2001:db8::1     32770     NULL      NULL      NULL      32770      主             0             出节点     0x0           弹出标签    0          0            无
(结果个数 = 3)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询BGP-LSP信息（DSP-BGPLSP）_00866093.md`
