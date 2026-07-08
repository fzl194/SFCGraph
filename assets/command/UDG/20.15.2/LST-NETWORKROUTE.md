---
id: UDG@20.15.2@MMLCommand@LST NETWORKROUTE
type: MMLCommand
name: LST NETWORKROUTE（查询引入路由指定前缀和掩码长度）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: NETWORKROUTE
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- BGP管理
- 引入路由指定前缀和掩码长度
status: active
---

# LST NETWORKROUTE（查询引入路由指定前缀和掩码长度）

## 功能

该命令用于查询设备上BGP VPN实例下所引入的network路由信息。

## 注意事项

- 该命令执行后立即生效。
- 如果未指定具体路由信息，将查询指定BGP VPN实例下所引入的network路由信息。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VRFNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定用户增加引入network路由的BGP VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无 |
| AFTYPE | 地址族类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定BGP VPN实例下的地址族。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4uni：IPv4地址族。<br>- ipv6uni：IPv6地址族。<br>默认值：无 |
| NETWORKADDRESS | IPv4路由前缀地址 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv4uni”时为可选参数。<br>参数含义：该参数用于指定引入IPv4路由的前缀信息。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：配置该参数时，需要同时配置MASKLEN指定路由的掩码长度。 |
| MASKLEN | IPv4掩码长度 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv4uni”时为可选参数。<br>参数含义：该参数用于指定引入外部IPv4路由的掩码长度。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～32。<br>默认值：无<br>配置原则：配置NETWORKADDRESS参数时，需要配置本参数指定引入路由的掩码长度，AFTYPE参数为ipv4uni时，掩码长度范围为0~32。 |
| NETWORKADDRESSV6 | IPv6路由前缀地址 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv6uni”时为可选参数。<br>参数含义：该参数用于指定引入IPv6路由的前缀信息。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：配置该参数时，需要同时配置MASKLENV6指定路由的前缀长度。 |
| MASKLENV6 | IPv6掩码长度 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv6uni”时为可选参数。<br>参数含义：该参数用于指定引入外部IPv6路由的前缀长度。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～128。<br>默认值：无<br>配置原则：配置NETWORKADDRESSV6参数时，需要配置本参数指定引入路由的前缀长度，前缀长度范围为0~128。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/NETWORKROUTE]] · 引入路由指定前缀和掩码长度（NETWORKROUTE）

## 使用实例

- 查询名称为“vrf1”的BGP VPN实例下所引入的IPv4 network路由的信息：
  ```
  LST NETWORKROUTE:VRFNAME="vrf1", AFTYPE=ipv4uni;
  ```
  ```

  RETCODE = 0  操作成功。

  结果如下
  --------
       VPN实例名称  =  vrf1
        地址族类型  =  IPv4uni
  IPv4路由前缀地址  =  192.168.2.0
      IPv4掩码长度  =  24
  IPv6路由前缀地址  =  ::
      IPv6掩码长度  =  0
          策略名称  =  NULL
  (结果个数 = 1)
  ---    END
  ```
- 查询名称为“vrf1”的BGP VPN实例下所引入的IPv6 network路由的信息：
  ```
  LST NETWORKROUTE:VRFNAME="vrf1", AFTYPE=ipv6uni;
  ```
  ```

  RETCODE = 0  操作成功。

  结果如下
  --------
       VPN实例名称  =  vrf1
        地址族类型  =  IPv6uni
  IPv4路由前缀地址  =  0.0.0.0
      IPv4掩码长度  =  0
  IPv6路由前缀地址  =  2001:db8:1:1:1:1:1:1
      IPv6掩码长度  =  32
          策略名称  =  NULL
  (结果个数 = 1)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-NETWORKROUTE.md`
