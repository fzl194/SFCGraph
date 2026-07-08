---
id: UDG@20.15.2@MMLCommand@MOD VTEP
type: MMLCommand
name: MOD VTEP（修改VXLAN隧道端点）
nf: UDG
version: 20.15.2
verb: MOD
object_keyword: VTEP
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 路径管理
- VXLAN路径管理
- VXLAN隧道端点配置
status: active
---

# MOD VTEP（修改VXLAN隧道端点）

## 功能

**适用NF：PGW-U、UPF**

该命令用于修改VXLAN隧道端点IP。

## 注意事项

- 该命令执行后立即生效。
- 在5G LAN业务中，地址类型只支持配置为IPv4。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VTEPNAME | VXLAN隧道端点名称 | 可选必选说明：必选参数<br>参数含义：该参数用于配置VXLAN隧道端点名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不区分大小写，不支持空格。<br>默认值：无<br>配置原则：无 |
| IPVERSION | IP协议版本 | 可选必选说明：必选参数<br>参数含义：该参数用于设置VTEP IP地址类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- IPV4：IPv4地址类型。<br>- IPV6：IPv6地址类型。<br>默认值：无<br>配置原则：无 |
| VTEPIPV4 | 隧道对端端点的IPv4地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IPVERSION”配置为“IPV4”时为必选参数。<br>参数含义：该参数用于配置VXLAN隧道端点IPv4地址。<br>数据来源：对端协商<br>取值范围：IPv4地址类型。有效的IP地址。采用点分十进制"X.X.X.X"格式，不能是全0全1，不能是组播IP，不能是环回IP。<br>默认值：无<br>配置原则：根据环境的网络规划进行配置，点分十进制格式。除A、B、C类地址合法外，其余都为非法地址。 |
| VTEPIPV6 | 隧道对端端点的IPv6地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IPVERSION”配置为“IPV6”时为必选参数。<br>参数含义：该参数用于配置VXLAN隧道端点IPv6地址。<br>数据来源：对端协商<br>取值范围：IPv6地址类型。采用冒号分十六进制X:X:X:X:X:X:X:X格式。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/VTEP]] · VXLAN隧道端点（VTEP）

## 使用实例

修改VTEP Name为vtep1的隧道端点IP为192.168.1.2：

```
MOD VTEP: VTEPNAME="vtep1", IPVERSION=IPV4, VTEPIPV4="192.168.1.2";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/MOD-VTEP.md`
