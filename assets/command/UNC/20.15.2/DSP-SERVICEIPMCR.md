---
id: UNC@20.15.2@MMLCommand@DSP SERVICEIPMCR
type: MMLCommand
name: DSP SERVICEIPMCR（显示业务IP）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: SERVICEIPMCR
command_category: 查询类
applicable_nf:
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- MME链式备份管理
- 业务IP管理
- 业务IP
status: active
---

# DSP SERVICEIPMCR（显示业务IP）

## 功能

**适用网元：MME**

该命令用来显示实际生效的业务IP地址与VPN实例，以及VPN实例ID的所属关系。

## 注意事项

无

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPVERSION | IP版本 | 可选必选说明：可选参数<br>参数含义：该参数用于指定需要查询的业务IP地址的IP版本。<br>数据来源：本端规划<br>取值范围：<br>- “IPv4(IPv4地址)”<br>- “IPv6(IPv6地址)”<br>默认值：无<br>配置原则：<br>- 根据选择的IP版本，输入相应格式的IP地址。 |
| SERVICEIPV4 | 业务IPv4地址 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定需要查询的业务IPv4地址。<br>前提条件：该参数在<br>**IP版本**<br>配置为“IPv4(IPv4地址)”后生效。<br>数据来源：全网规划<br>取值范围：0.0.0.0~255.255.255.255<br>默认值：无<br>配置原则：<br>- 业务地址不能配置为0.0.0.0、255.255.255.255和环回地址(127.x.y.z)。<br>- 业务地址必须是A、B或者C类地址。<br>- 该参数的掩码缺省为255.255.255.255，不可更改。 |
| SERVICEIPV6 | 业务IPv6地址 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定需要查询的业务IPv6地址。<br>前提条件：该参数在<br>**IP版本**<br>配置为“IPv6(IPv6地址)”后生效。<br>数据来源：全网规划<br>取值范围：::~FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无<br>配置原则：<br>- IPv6地址必须是全球单播地址，不能为::、FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址(::1/128)、链路本地地址(FE80::/10)和组播地址(FF00::/8)。<br>- 该参数的掩码缺省为FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF，不可更改。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SERVICEIPMCR]] · 业务IP（SERVICEIPMCR）

## 使用实例

显示业务IP以及业务IP与VPN实例的所属关系的配置记录：

**DSP SERVICEIPMCR:;**

```
%%DSP SERVICEIPMCR: IPVERSION=IPv4;%%
RETCODE = 0  执行成功

操作结果如下
-------------------------
业务IPv4地址             业务IPv6地址          VPN实例名称      VPN实例ID      
192.168.57.1             ::                     _public_            0        
192.168.57.2             ::                     _public_            0        
(结果个数 = 2)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示业务IP(DSP-SERVICEIPMCR)_71731085.md`
