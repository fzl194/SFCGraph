---
id: UDG@20.15.2@MMLCommand@LST SRROUTE6
type: MMLCommand
name: LST SRROUTE6（查询IPv6静态路由）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: SRROUTE6
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- 静态路由管理
- IPv6静态路由
status: active
---

# LST SRROUTE6（查询IPv6静态路由）

## 功能

该命令用于查询IPv6静态路由的配置情况。

静态路由是一种需要管理员手工配置的特殊路由。

当网络结构比较简单时，只需配置静态路由就可以使网络正常工作。当设备不能使用动态路由协议或者不能建立到达目的网络时，也可以使用静态路由。合理的静态路由可以改进网络性能，并为重要业务保证带宽。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| AFTYPE | 地址族 | 可选必选说明：可选参数<br>参数含义：该参数用于指定VPN实例的地址族信息。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv6unicast：IPv6单播。<br>默认值：ipv6unicast |
| VRFNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定VPN实例的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：公网需要输入_public_，默认查询所有VPN。 |
| PREFIX | 路由前缀 | 可选必选说明：可选参数<br>参数含义：该参数用于指定前缀信息。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。<br>默认值：无 |
| MASKLENGTH | 路由前缀长度 | 可选必选说明：可选参数<br>参数含义：该参数用于表示IPv6路由的前缀长度。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～128。<br>默认值：无<br>配置原则：不可单独以前缀长度查询路由。前缀长度需要和前缀一起配置。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/SRROUTE6]] · IPv6静态路由（SRROUTE6）

## 使用实例

查询IPv6静态路由的配置情况：

```
LST SRROUTE6:;
```

```

RETCODE = 0  操作成功

结果如下
-------------------------
         地址族  =  IPv6单播
    VPN实例名称  =  _public_
       路由前缀  =  2001:DB8::
   路由前缀长度  =  128
  下一跳VPN名字  =  _public_
 路由出接口名字  =  NULL0
     路由下一跳  =  2001:DB8::1
     路由优先级  =  60
动态BFD使能标识  =  FALSE
  静态BFD会话名  =  NULL
        路由tag  =  0
       路由描述  =  NULL
   DHCP使能标识  =  否
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-SRROUTE6.md`
