---
id: UDG@20.15.2@MMLCommand@DSP RMCONSUMERSUBSCRIBE
type: MMLCommand
name: DSP RMCONSUMERSUBSCRIBE（查询路由管理消费者订阅信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: RMCONSUMERSUBSCRIBE
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- 路由基础调测
- 查询路由管理伙伴信息
status: active
---

# DSP RMCONSUMERSUBSCRIBE（查询路由管理消费者订阅信息）

## 功能

该命令用来查询路由管理模块的消费者订阅信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VPNNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示路由所属VPN的名字。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无 |
| VRFINDEX | VPN实例ID | 可选必选说明：可选参数<br>参数含义：该参数用于表示VPN实例ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无 |
| PARTNERID | Partner ID | 可选必选说明：可选参数<br>参数含义：该参数用于表示Partner ID。<br>数据来源：本端规划<br>取值范围：十六进制整数类型，取值范围为0x0～0xFFFFFFFF。<br>默认值：无 |
| VPID | VP ID | 可选必选说明：可选参数<br>参数含义：该参数用于表示VP ID。<br>数据来源：本端规划<br>取值范围：十六进制整数类型，取值范围为0x0～0xFFFFFFFF。<br>默认值：无 |
| ADDRESSFAMILY | 地址族 | 可选必选说明：必选参数<br>参数含义：该参数用于表示路由所属VPN的地址族。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4unicast：IPv4单播。<br>- ipv6unicast：IPv6单播。<br>默认值：无 |
| ALL | 所有实例 | 可选必选说明：可选参数<br>参数含义：该参数用于表示是否查询所有实例。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：FALSE |
| PREFIX | 路由前缀 | 可选必选说明：可选参数<br>参数含义：该参数用于表示路由前缀。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～41。IPv4地址格式是点分十进制格式，格式为X.X.X.X，IPv6地址格式是32位16进制数，格式为X:X:X:X:X:X:X:X。<br>默认值：无 |
| MASKLEN | 路由掩码长度 | 可选必选说明：可选参数<br>参数含义：IPv4场景，该参数用于表示路由的掩码长度；IPv6场景，该参数用于表示路由的前缀长度。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～128。ADDRESSFAMILY为ipv4unicast时取值范围0～32，ADDRESSFAMILY为ipv6unicast时取值范围0～128。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/RMCONSUMERSUBSCRIBE]] · 路由管理消费者订阅信息（RMCONSUMERSUBSCRIBE）

## 使用实例

查询路由管理模块的消费者订阅信息：

```
DSP RMCONSUMERSUBSCRIBE:ADDRESSFAMILY=ipv4unicast;
```

```

RETCODE = 0  操作成功。

结果如下
--------
           VPN实例ID  =  0
          Partner ID  =  0x700007
          路由拓扑ID  =  0
              表名字  =  base
               VP ID  =  0x1
            路由前缀  =  10.1.1.0
        路由掩码长度  =  32
        当前处理状态  =  normal
            订阅模式  =  forRely
        路由协议名字  =  所有路由
            子协议ID  =  NO_SUB_PROTOCOL
          路由进程ID  =  0
最近更新使用的事务号  =  0x0
        订阅路由数量  =  1
        更新打包标志  =  TRUE
            更新时间  =  2018-02-13 15:12:25
  目的IP地址订阅结果  =  0.0.0.0
    掩码长度订阅结果  =  255
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询路由管理消费者订阅信息（DSP-RMCONSUMERSUBSCRIBE）_00866217.md`
