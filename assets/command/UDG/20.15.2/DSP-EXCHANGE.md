---
id: UDG@20.15.2@MMLCommand@DSP EXCHANGE
type: MMLCommand
name: DSP EXCHANGE（查询负载均衡交换表）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: EXCHANGE
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- CSLB功能管理
- 操作维护
- 系统调测
- 策略调测
- 交换信息
status: active
---

# DSP EXCHANGE（查询负载均衡交换表）

## 功能

查询负载均衡交换表的详细信息

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CONSUMERVNFCID | 服务VNFC ID | 可选必选说明：必选参数<br>参数含义：该参数用于指定业务VNFC的唯一标识，通过在业务VNFC下执行<br>**[LST NODE](../../../../../单体服务公共功能管理/系统管理/基础参数/查询节点信息/查询节点信息（LST NODE）_27372977.md)**<br>获得，所得NODEID即为服务VNFC ID。<br>默认值：无<br>取值范围：0~4294967294 |
| EXCHANGEID | 交换ID | 可选必选说明：必选参数<br>参数含义：交换ID<br>数据来源：可通过执行<br>**[DSP POLICYNUM](../../../../业务管理/服务管理/策略/查询策略数量（DSP POLICYNUM）_29627053.md)**<br>查询到。<br>默认值：无<br>取值范围：0~4294967294 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/EXCHANGE]] · 负载均衡交换表（EXCHANGE）

## 使用实例

查询服务VNFC ID为4，交换ID为18的负载均衡交换表信息的命令如下：

DSP EXCHANGE: CONSUMERVNFCID=4, EXCHANGEID=18;

```
%%DSP EXCHANGE: CONSUMERVNFCID=4, EXCHANGEID=18;%%
RETCODE = 0  操作成功

结果如下:
-------------------------
服务VNFC ID    交换ID    交换前数据    交换后数据 
4              18        1             71         
4              18        2             72         
4              18        3             73         
(结果个数 = 3)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询负载均衡交换表（DSP-EXCHANGE）_29627119.md`
