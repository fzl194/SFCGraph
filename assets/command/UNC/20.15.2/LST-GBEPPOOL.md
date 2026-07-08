---
id: UNC@20.15.2@MMLCommand@LST GBEPPOOL
type: MMLCommand
name: LST GBEPPOOL（查询地址池中信息）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: GBEPPOOL
command_category: 查询类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- Gb接口管理
- Gb自动配置管理
- Gb地址池管理
status: active
---

# LST GBEPPOOL（查询地址池中信息）

## 功能

**适用网元：SGSN**

此命令用于显示地址池中信息。

## 注意事项

- 此命令执行后立即生效。
- 若不输入参数，则查询地址池中所有信息。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPTYPE | IP类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定待查询的IP地址类型。<br>取值范围：<br>- “IPV4(IPv4)”<br>- “IPV6(IPv6)”<br>默认值：无 |
| IPV4 | IPv4地址 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定地址池中待查询的IPv4地址。<br>前提条件：该参数在<br>“ IP类型 ”<br>设置为<br>“IPV4(IPv4)”<br>时生效。<br>取值范围：0.0.0.1～255.255.255.254<br>默认值：无<br>配置原则：<br>- 有效的IPV4地址不能为环回地址(127.x.y.z)。<br>- 有效的IPV4地址必须是A、B或者C类地址。 |
| IPV6 | IPv6地址 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定地址池中待查询的IPv6地址。<br>前提条件：该参数在<br>“ IP类型 ”<br>设置为<br>“IPV6(IPv6)”<br>时生效。<br>取值范围：::～FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无<br>配置原则：IPV6地址必须是全球单播地址，不能为::、FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址(::1)、链路本地地址(FE80::/10)和组播地址(FF00::/8)。 |

## 操作的配置对象

- [地址池中IP地址（GBEPPOOL）](configobject/UNC/20.15.2/GBEPPOOL.md)

## 使用实例

1. 查询地址池中的所有信息：
  LST GBEPPOOL:;
  ```
  %%LST GBEPPOOL:;%%
  RETCODE = 0  操作成功。

  操作结果如下
  --------------
   本端实体标识  IP类型  IP地址         描述信息    vpn名称    组号                         

    0            IPv4    192.168.4.102  GBEPPool1   _abc_    0                        
    1            IPv4    192.168.4.103  GBEPPool2   _abc_    0                         
  (结果个数 = 2)

  ---    END
  ```
2. 查询 “IP类型” 为 “IPV4(IPv4)” 且 “IPv4地址” 值为 “192.168.4.102” 的记录：
  LST GBEPPOOL: IPTYPE=IPV4, IPV4="192.168.4.102";
  ```
  %%LST GBEPPOOL: IPTYPE=IPV4, IPV4="192.168.4.102";%%
  RETCODE = 0  操作成功。

  操作结果如下
  --------------
  本端实体标识  =  0
        IP类型  =  IPv4
        IP地址  =  192.168.4.102
      描述信息  =  GBEPPool1
      VPN名称   =  _abc_
         组号 = 0
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询地址池中信息(LST-GBEPPOOL)_26305808.md`
