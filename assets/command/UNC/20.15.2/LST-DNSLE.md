---
id: UNC@20.15.2@MMLCommand@LST DNSLE
type: MMLCommand
name: LST DNSLE（查询DNS Client IP与DNS实体的绑定关系）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: DNSLE
command_category: 查询类
applicable_nf:
- SGSN
- MME
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- GTP-C接口管理
- DNS
- DNS本端实体管理
status: active
---

# LST DNSLE（查询DNS Client IP与DNS实体的绑定关系）

## 功能

**适用网元：SGSN、MME** **、AMF**

该命令用于查看配置的DNS本端实体信息，DNS本端实现体包含了DNS本端的IP地址、端口和VPN名称。

## 注意事项

- 该命令执行后立即生效。
- 如果不输入参数，则查询所有记录。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPT | IP地址类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定IP地址类型。<br>数据来源：整网规划<br>取值范围：<br>- “IPV4(IPV4)”<br>- “IPV6(IPV6)”<br>默认值：无 |
| IPV4 | IPv4地址 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定IPv4地址。<br>前提条件：当<br>“IP地址类型”<br>设置为<br>“IPV4(IPV4)”<br>时，该参数有效。<br>数据来源：整网规划<br>取值范围：0.0.0.0～255.255.255.255<br>默认值：无 |
| IPV6 | IPv6地址 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定IPv6地址。<br>前提条件：当<br>“IP地址类型”<br>设置为<br>“IPV6(IPV6)”<br>时，该参数有效。<br>数据来源：整网规划<br>取值范围：::～FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无 |
| LOCPORT | 本地端口号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定本端端口号。<br>数据来源：整网规划<br>取值范围：15000~65535<br>默认值：无 |
| VPNNAME | VPN名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定DNS本端实体到DNS服务器间的链路所用的VPN名称。<br>数据来源：整网规划<br>取值范围：0~31个字符。<br>默认值：无 |
| LENAME | DNS本端实体名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定DNS本端实体的名称。<br>数据来源：整网规划<br>取值范围：0~32个字符。<br>默认值：无 |

## 操作的配置对象

- [DNS Client IP与DNS实体的绑定关系（DNSLE）](configobject/UNC/20.15.2/DNSLE.md)

## 使用实例

查询所有DNS本端实体：

LST DNSLE:;

```
%%LST DNSLE:;%%
RETCODE = 0  操作成功。

操作结果如下
-------------------------
IP地址类型          IP地址            本地端口号          VPN名称     DNS本端实体名称 

IPV4               192.168.97.26      15001               _abc_       Dnsle26     
IPV4               192.168.97.26      15013               _abc_       NULL        
(结果个数 = 2)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询DNS-Client-IP与DNS实体的绑定关系(LST-DNSLE)_72345489.md`
