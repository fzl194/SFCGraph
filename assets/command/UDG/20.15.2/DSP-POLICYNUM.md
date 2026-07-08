---
id: UDG@20.15.2@MMLCommand@DSP POLICYNUM
type: MMLCommand
name: DSP POLICYNUM（查询策略数量）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: POLICYNUM
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- CSLB功能管理
- 业务管理
- 服务管理
- 策略
status: active
---

# DSP POLICYNUM（查询策略数量）

## 功能

该命令用于查询策略数量，策略指的是业务VNFC下发给CSLB的用于负载均衡的信息。

## 注意事项

- 本命令当前不支持查询存储在CSDB中的X元组策略，查询得到的数量始终显示为0个。X元组策略数量可以通过**[DSP DBTBL](../../../../CSDB功能管理/CSDB管理/数据表管理/查询CSDB数据表信息（DSP DBTBL）_29626992.md)**命令获取。
- 该命令批量下发可能导致执行超时。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PEERVNFCID | 服务VNFC ID | 可选必选说明：必选参数<br>参数含义：该参数用于指定业务VNFC的唯一标识，通过在业务VNFC下执行<br>**[LST NODE](../../../../单体服务公共功能管理/系统管理/基础参数/查询节点信息/查询节点信息（LST NODE）_27372977.md)**<br>获得，所得NODEID即为服务VNFC ID。<br>数据来源：本端规划<br>默认值：无<br>取值范围：0~4294967294 |
| DATATYPE | 数据类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定策略类型。<br>数据来源：本端规划<br>默认值：无<br>取值范围：<br>- “SRV_DATA_TYPE_LBPLY(负载均衡策略) ”<br>- “SRV_DATA_TYPE_NEXTHOP(下一跳) ”<br>- “SRV_DATA_TYPE_XTUPLE(X元组) ”<br>- “SRV_DATA_TYPE_ENEXTHOP(扩展下一跳) ”<br>- “SRV_DATA_TYPE_EXCHANGE(交换表) ”<br>- “SRV_DATA_TYPE_VPN(VPN) ” |
| POLICYID | 策略ID | 可选必选说明：可选参数<br>参数含义：该参数用于指定策略标识。<br>数据来源：本端规划<br>默认值：无<br>取值范围：整数类型，取值范围为0~FFFFFFFF |

## 操作的配置对象

- [[configobject/UDG/20.15.2/POLICYNUM]] · 策略数量（POLICYNUM）

## 使用实例

查询服务VNFC ID为4，数据类型为负载均衡策略的策略数量：

DSP POLICYNUM: PEERVNFCID=4, DATATYPE=SRV_DATA_TYPE_LBPLY;

```
%%DSP POLICYNUM: PEERVNFCID=4, DATATYPE=SRV_DATA_TYPE_LBPLY;%%
RETCODE = 0  操作成功
结果如下:
-------------------------
服务VNFC ID    数据类型        策略ID    记录数 
4              负载均衡策略    1         0      
4              负载均衡策略    3         0      
4              负载均衡策略    4         0      
4              负载均衡策略    0         5      
4              负载均衡策略    2         0      
(结果个数 = 5)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询策略数量（DSP-POLICYNUM）_29627053.md`
