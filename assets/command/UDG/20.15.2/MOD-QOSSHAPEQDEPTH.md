---
id: UDG@20.15.2@MMLCommand@MOD QOSSHAPEQDEPTH
type: MMLCommand
name: MOD QOSSHAPEQDEPTH（修改Qos Shape缓存队列深度与流量速率的对应关系）
nf: UDG
version: 20.15.2
verb: MOD
object_keyword: QOSSHAPEQDEPTH
command_category: 配置类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 用户QOS控制
- 流量管理
- 整形队列深度
status: active
---

# MOD QOSSHAPEQDEPTH（修改Qos Shape缓存队列深度与流量速率的对应关系）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用于修改流量做shaping时的缓存队列深度与流量速率的对应关系。

## 注意事项

- 该命令执行后立即生效。
- 该命令只能用于修改已配置的速率对应的队列深度。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RATE | Qos Shape速率（千比特/秒） | 可选必选说明：必选参数<br>参数含义：指定shaping的流量速率。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295，单位是千比特每秒。<br>默认值：无<br>配置原则：无 |
| QDEPTH | Shape缓存队列深度（包） | 可选必选说明：必选参数<br>参数含义：做shaping时的缓存队列深度，即每个用户可以缓存的最大报文个数。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～2560。单位是个。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [Qos Shape缓存队列深度与流量速率的对应关系（QOSSHAPEQDEPTH）](configobject/UDG/20.15.2/QOSSHAPEQDEPTH.md)

## 使用实例

将128kbps的速率的缓存队列深度为32个报文修改成128kbps的速率的缓存队列深度为100个报文：

```
MOD QOSSHAPEQDEPTH:RATE=128,QDEPTH=100;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改Qos-Shape缓存队列深度与流量速率的对应关系（MOD-QOSSHAPEQDEPTH）_86528786.md`
