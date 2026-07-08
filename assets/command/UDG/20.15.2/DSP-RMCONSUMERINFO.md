---
id: UDG@20.15.2@MMLCommand@DSP RMCONSUMERINFO
type: MMLCommand
name: DSP RMCONSUMERINFO（查询路由管理消费者信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: RMCONSUMERINFO
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

# DSP RMCONSUMERINFO（查询路由管理消费者信息）

## 功能

该命令用来查询路由管理模块的消费者信息。

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

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@RMCONSUMERINFO]] · 路由管理消费者信息（RMCONSUMERINFO）

## 使用实例

查询路由管理模块的消费者信息：

```
DSP RMCONSUMERINFO:ADDRESSFAMILY=ipv4unicast;
```

```

RETCODE = 0  操作成功。

结果如下
--------
        Partner ID  =  0x6A0016
             VP ID  =  0x0
         VPN实例ID  =  0
        路由拓扑ID  =  0
            表名字  =  base
消费者订阅服务类型  =  IR
  路由引入处理状态  =  Normal
  单条路由订阅数量  =  0
      策略订阅状态  =  --
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-RMCONSUMERINFO.md`
