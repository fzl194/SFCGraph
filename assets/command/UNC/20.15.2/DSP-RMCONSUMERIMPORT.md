---
id: UNC@20.15.2@MMLCommand@DSP RMCONSUMERIMPORT
type: MMLCommand
name: DSP RMCONSUMERIMPORT（查询路由管理消费者引入信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: RMCONSUMERIMPORT
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

# DSP RMCONSUMERIMPORT（查询路由管理消费者引入信息）

## 功能

该命令用来查询路由管理模块的消费者引入信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PARTNERID | Partner ID | 可选必选说明：可选参数<br>参数含义：该参数用于表示Partner ID。<br>数据来源：本端规划<br>取值范围：十六进制整数类型，取值范围为0x0～0xFFFFFFFF。<br>默认值：无 |
| VPID | VP ID | 可选必选说明：可选参数<br>参数含义：该参数用于表示VP ID。<br>数据来源：本端规划<br>取值范围：十六进制整数类型，取值范围为0x0～0xFFFFFFFF。<br>默认值：无 |
| VPNNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示路由所属VPN的名字。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无 |
| VRFINDEX | VPN实例ID | 可选必选说明：可选参数<br>参数含义：该参数用于表示VPN实例ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无 |
| ADDRESSFAMILY | 地址族 | 可选必选说明：必选参数<br>参数含义：该参数用于表示路由所属VPN的地址族。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4unicast：IPv4单播。<br>- ipv6unicast：IPv6单播。<br>默认值：无 |
| ALL | 所有实例 | 可选必选说明：可选参数<br>参数含义：该参数用于表示是否查询所有实例。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：无 |

## 操作的配置对象

- [路由管理消费者引入信息（RMCONSUMERIMPORT）](configobject/UNC/20.15.2/RMCONSUMERIMPORT.md)

## 使用实例

查询路由管理模块的消费者引入信息：

```
DSP RMCONSUMERIMPORT:ADDRESSFAMILY=ipv4unicast;
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
            通告的前缀数量  =  4
             通告的IID数量  =  3
          被流控的前缀数量  =  0
           被流控的IID数量  =  0
上次批量更新通告的前缀数量  =  4
 上次批量更新通告的IID数量  =  3
      最近一次平滑开始时间  =  2016-11-11 07:41:04
      最近一次平滑结束时间  =  2016-11-11 07:41:04
      最近一次对帐开始时间  =  0000-00-00 00:00:00
      最近一次对帐结束时间  =  0000-00-00 00:00:00
          路由引入处理状态  =  normal
                  引入标识  =  0x1
          前缀批量更新状态  =  normal
           IID批量更新状态  =  normal
                  引入规则  =  PREFIX_INCLUDE_NOADV/IID/LOCAL
                 协议类型1  =  所有路由
                 协议类型2  =  所有路由
                 协议类型3  =  所有路由
                 协议类型4  =  所有路由
                 协议类型5  =  所有路由
                 协议类型6  =  所有路由
                 协议类型7  =  所有路由
                 协议类型8  =  所有路由
                 协议类型9  =  所有路由
                协议类型10  =  所有路由
               子协议类型1  =  NO_SUB_PROTOCOL
               子协议类型2  =  NO_SUB_PROTOCOL
               子协议类型3  =  NO_SUB_PROTOCOL
               子协议类型4  =  NO_SUB_PROTOCOL
               子协议类型5  =  NO_SUB_PROTOCOL
               子协议类型6  =  NO_SUB_PROTOCOL
               子协议类型7  =  NO_SUB_PROTOCOL
               子协议类型8  =  NO_SUB_PROTOCOL
               子协议类型9  =  NO_SUB_PROTOCOL
              子协议类型10  =  NO_SUB_PROTOCOL
                   进程ID1  =  0
                   进程ID2  =  0
                   进程ID3  =  0
                   进程ID4  =  0
                   进程ID5  =  0
                   进程ID6  =  0
                   进程ID7  =  0
                   进程ID8  =  0
                   进程ID9  =  0
                  进程ID10  =  0
                   策略ID1  =  4294967295
                   策略ID2  =  0
                   策略ID3  =  0
                   策略ID4  =  0
                   策略ID5  =  0
                   策略ID6  =  0
                   策略ID7  =  0
                   策略ID8  =  0
                   策略ID9  =  0
                  策略ID10  =  0
                   版本号1  =  0
                   版本号2  =  0
                   版本号3  =  0
                   版本号4  =  0
                   版本号5  =  0
                   版本号6  =  0
                   版本号7  =  0
                   版本号8  =  0
                   版本号9  =  0
                  版本号10  =  0
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询路由管理消费者引入信息（DSP-RMCONSUMERIMPORT）_49961134.md`
