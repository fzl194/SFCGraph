---
id: UDG@20.15.2@MMLCommand@ADD QOSSHAPEQDEPTH
type: MMLCommand
name: ADD QOSSHAPEQDEPTH（添加Qos Shape缓存队列深度与流量速率的对应关系）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: QOSSHAPEQDEPTH
command_category: 配置类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 100
category_path:
- 用户面服务管理
- 业务控制策略
- 用户QOS控制
- 流量管理
- 整形队列深度
status: active
---

# ADD QOSSHAPEQDEPTH（添加Qos Shape缓存队列深度与流量速率的对应关系）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用于配置流量做shaping时的缓存队列深度与流量速率的对应关系。用户流量速率与这个对应关系表进行比较得到缓存队列深度。队列深度，即最多缓存的报文个数。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为100。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RATE | Qos Shape速率（千比特/秒） | 可选必选说明：必选参数<br>参数含义：指定shaping的流量速率。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295，单位是千比特每秒。<br>默认值：无<br>配置原则：<br>- 向上取最接近的速率的配置值，如果向上取不到，则取系统根据RATE计算的一个推荐值，即：- 当PIR不在本命令配置的RATE范围之内，则取系统根据RATE计算出的推荐值。<br>- 当PIR表示的速率有对应QDEPTH配置，则取这个配置值。<br>- 当PIR表示的速率没有对应QDEPTH配置，但是在本命令配置的RATE范围之内，则取这个RATE范围的上限值对应的QDEPTH的配置。<br>- 例如：配置了5个对应关系（速率分别是5M，32M，48M，64M，96M）。现有3个流量，速率分别是A，B，C，其中，A小于5M，B在48M与64M之间，C大于96M，则A流量的QDEPTH取值以5M的对应关系获得，B流量的QDEPTH取值以64M的对应关系获得，C流量的QDEPTH取值以系统根据C计算得到的推荐值获得。<br>- 用户可以缓存的报文个数取决于报文速率、报文大小和缓存队列深度。报文缓存只要满足如下条件之一就停止缓存：1、网关根据速率计算出可以缓存的最大流量A，即RATE*3（秒），报文缓存后将超过A；2、缓存队列已满。 |
| QDEPTH | Shape缓存队列深度（包） | 可选必选说明：必选参数<br>参数含义：做shaping时的缓存队列深度，即每个用户可以缓存的最大报文个数。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～2560。单位是个。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/QOSSHAPEQDEPTH]] · Qos Shape缓存队列深度与流量速率的对应关系（QOSSHAPEQDEPTH）

## 使用实例

配置128kbps的速率的缓存队列深度为32个报文：

```
ADD QOSSHAPEQDEPTH:RATE=128,QDEPTH=32;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/ADD-QOSSHAPEQDEPTH.md`
