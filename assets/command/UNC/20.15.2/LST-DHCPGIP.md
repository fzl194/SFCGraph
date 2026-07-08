---
id: UNC@20.15.2@MMLCommand@LST DHCPGIP
type: MMLCommand
name: LST DHCPGIP（查询支持DHCP服务的GGSN IP地址）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: DHCPGIP
command_category: 查询类
applicable_nf:
- SGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- GTP-C接口管理
- GnGp-GGSN_S5_S8接口管理
- 支持DHCP服务的GGSN IP地址
status: active
---

# LST DHCPGIP（查询支持DHCP服务的GGSN IP地址）

## 功能

**适用网元：SGSN**

1. 该命令用于查询支持DHCP服务的GGSN IP地址。
2. SGSN支持用户采用DHCP方式接入，在采用DHCP接入方式时，不需要对APN进行DNS解析，只需要在SGSN中配置支持DHCP服务的GGSN IP地址即可。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPT | IP地址类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定IP地址类型<br>数据来源：整网规划<br>取值范围：<br>“IPV4(IPV4)”<br>、<br>“IPV6(IPV6)”<br>、<br>“IPV4V6(IPV4V6)”<br>默认值： 无 |
| IPV4 | GGSN IPv4地址 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定GGSN IPv4地址。<br>数据来源：整网规划<br>取值范围：0.0.0.0～255.255.255.255<br>默认值： 无 |
| IPV6 | GGSN IPv6地址 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定GGSN IPv6地址。<br>数据来源：整网规划<br>取值范围：::～FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值： 无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/DHCPGIP]] · 支持DHCP服务的GGSN IP地址（DHCPGIP）

## 使用实例

查询所有支持DHCP的GGSN IP地址：

LST DHCPGIP:;

```
%%LST DHCPGIP:;%%
RETCODE = 0  Execution succeeded

DHCP与GGSN IP地址的对应关系表
-----------------------------
     IP地址类型  =  IPV4
  GGSN IPv4地址  =  192.168.22.22
  GGSN IPv6地址  =  NULL
           描述  =  NULL
(结果个数  = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-DHCPGIP.md`
