---
id: UDG@20.15.2@MMLCommand@DSP SRVINSTSTAT
type: MMLCommand
name: DSP SRVINSTSTAT（查询LB服务实例统计）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: SRVINSTSTAT
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- CSLB功能管理
- 业务管理
- 服务实例管理
- 服务实例统计
status: active
---

# DSP SRVINSTSTAT（查询LB服务实例统计）

## 功能

该命令用于查询LB服务实例操作统计信息。

## 注意事项

该命令批量下发可能导致执行超时。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CONSUMERVNFCID | 服务VNFC ID | 可选必选说明：必选参数<br>参数含义：该参数用于指定业务VNFC的唯一标识，通过在业务VNFC下执行<br>**[LST NODE](../../../../单体服务公共功能管理/系统管理/基础参数/查询节点信息/查询节点信息（LST NODE）_27372977.md)**<br>获得，所得NODEID即为服务VNFC ID。<br>数据来源：本端规划<br>默认值：无<br>取值范围：0~4294967294 |
| SERVICEINDEX | 服务实例索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定服务实例索引，通过<br>**[DSP LBSRVINST](../服务实例/查询LB服务实例（DSP LBSRVINST）_29627060.md)**<br>获得。<br>数据来源：本端规划<br>默认值：无<br>取值范围：0~4294967294 |

## 操作的配置对象

- [LB服务实例统计（SRVINSTSTAT）](configobject/UDG/20.15.2/SRVINSTSTAT.md)

## 使用实例

查询负载均衡服务实例统计：

DSP SRVINSTSTAT: CONSUMERVNFCID=3, SERVICEINDEX=0;

```
%%DSP SRVINSTSTAT: CONSUMERVNFCID=3, SERVICEINDEX=0;%%
RETCODE = 0  操作成功
操作结果如下：
--------------
                 	 服务VNFC ID  =  3
                  服务实例索引  =  0
	  接收的上行IPv4报文数（千）  =  1261
    接收的上行IPv4报文流量（MB）  =  23443120
接收的上行需重组IPv4分片报文数  =  0
    重组失败的上行IPv4分片报文数  =  0
        重组成功的上行IPv4报文数  =  0
    匹配策略失败的上行IPv4报文数  =  0
      发送的上行IPv4报文数（千）  =  0
    发送的上行IPv4报文流量（MB）  =  0
      接收的下行IPv4报文数（千）  =  3336
    接收的下行IPv4报文流量（MB）  =  58361270
        寻址失败的下行IPv4报文数  =  0
    发送的下行IPv4报文数（千）  =  0
    发送的下行IPv4报文流量（MB）  =  0
      接收的上行IPv6报文数（千）  =  0
    接收的上行IPv6报文流量（MB）  =  0
接收的上行需重组IPv6分片报文数  =  0
    重组失败的上行IPv6分片报文数  =  0
        重组成功的上行IPv6报文数  =  0
    匹配策略失败的上行IPv6报文数  =  0
      发送的上行IPv6报文数（千）  =  0
    发送的上行IPv6报文流量（MB）  =  0
      接收的下行IPv6报文数（千）  =  0
    接收的下行IPv6报文流量（MB）  =  0
        寻址失败的下行IPv6报文数  =  0
      发送的下行IPv6报文数（千）  =  0
    发送的下行IPv6报文流量（MB）  =  0
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询LB服务实例统计（DSP-SRVINSTSTAT）_29627062.md`
