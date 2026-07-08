---
id: UNC@20.15.2@MMLCommand@RMV IPV4GPMEM
type: MMLCommand
name: RMV IPV4GPMEM（删除IPv4群组成员）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: IPV4GPMEM
command_category: 配置类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- 会话管理
- IP群组管理
- IP群组成员配置
status: active
---

# RMV IPV4GPMEM（删除IPv4群组成员）

## 功能

**适用网元：SGSN、MME**

该命令用于删除IP群组成员配置。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPGPID | IP群组标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定IP群组标识。<br>前提条件：“IP群组标识”已经通过<br>[**ADD IPGP**](../IP群组配置/增加IP群组(ADD IPGP)_18995796.md)<br>配置。<br>数据来源：本端规划<br>取值范围：1-255<br>默认值：无 |
| IPV4 | IPv4地址 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定IPv4地址。<br>数据来源：本端规划<br>取值范围：0.0.0.1～255.255.255.254<br>默认值：无<br>说明：“0.0.0.0”和“255.255.255.255”是无效的IP地址。<br>配置原则：<br>- IPv4地址不能为0.0.0.0、255.255.255.255和0.x.y.z。<br>- IPv4地址不能为组播地址（如：224.x.y.z）和环回地址（如：127.x.y.z）。<br>- IPv4地址必须是A、B或者C类地址。 |
| IPV4MSK | IPV4地址掩码 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定IPv4地址的掩码。<br>数据来源：全网规划<br>取值范围：0.0.0.1~255.255.255.255<br>默认值：无<br>配置原则：<br>- 输入的掩码要求对应的二进制值1和1之间不允许存在0。例如：“255.255.0.0”是有效掩码；“123.123.123.123”是无效掩码。因为123对应的二进制为“1111011”，1之间存在0。 |

## 操作的配置对象

- [IPv4群组成员（IPV4GPMEM）](configobject/UNC/20.15.2/IPV4GPMEM.md)

## 使用实例

删除IPv4群组成员，IP群组标识为1，IP地址为172.22.5.50，IPV4地址掩码为 255.255.255.0 ：

RMV IPV4GPMEM: IPGPID=1, IPV4="172.22.5.50", IPV4MSK="255.255.255.0";

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除IPv4群组成员(RMV-IPV4GPMEM)_26305528.md`
