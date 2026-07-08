---
id: UNC@20.15.2@MMLCommand@LST NGDNSLE
type: MMLCommand
name: LST NGDNSLE（查询DNS本端实体）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NGDNSLE
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- NRF业务参数
- DNS客户端管理
status: active
---

# LST NGDNSLE（查询DNS本端实体）

## 功能

**适用NF：AMF**

该命令用于查看配置的DNS本端实体信息，DNS本端实体包含了DNS本端的IP地址。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPTYPE | IP地址类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定DNS本端实体的IP地址类型。<br>数据来源：全网规划<br>取值范围：<br>- IPV4（IPv4）<br>- IPV6（IPv6）<br>默认值：无<br>配置原则：无 |
| IPV4 | IPv4地址 | 可选必选说明：该参数在"IPTYPE"配置为"IPV4"时为条件必选参数。<br>参数含义：该参数用于指定DNS本端实体的IPv4地址。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无 |
| IPV6 | IPv6地址 | 可选必选说明：该参数在"IPTYPE"配置为"IPV6"时为条件必选参数。<br>参数含义：该参数用于指定DNS本端实体的IPv6地址。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |
| VPNNAME | VPN名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定DNS本端实体到DNS服务器间的链路所用的VPN名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~31。<br>默认值：无<br>配置原则：无 |
| LENAME | DNS本端实体名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定DNS本端实体的名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~32。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [DNS本端实体（NGDNSLE）](configobject/UNC/20.15.2/NGDNSLE.md)

## 使用实例

- 查询IP地址类型为IPv4，IP地址为192.168.101.100的DNS本端实体。
  ```
  %%LST NGDNSLE: IPTYPE=IPV4, IPV4="192.168.101.100";%%
  RETCODE = 0  操作成功

  操作结果如下
  ------------
             IP地址类型  =  IPv4
               IPv4地址  =  192.168.101.100
               IPv6地址  =  ::
                VPN名称  =  NULL
        DNS本端实体名称  =  dnsle01
  (结果个数 = 1)

  ---    END
  ```
- 查询所有DNS本端实体。
  ```
  %%LST NGDNSLE:;%%
  RETCODE = 0  操作成功

  操作结果如下
  ------------
  IP地址类型       IPv4地址         IPv6地址   VPN名称  DNS本端实体名称  

  IPv4             192.168.101.100  ::         NULL     dnsle01          
  IPv4             192.168.101.111  ::         NULL     dnsle02          
  (结果个数 = 2)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询DNS本端实体（LST-NGDNSLE）_25120887.md`
