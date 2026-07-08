---
id: UDG@20.15.2@MMLCommand@RMV QOSSHAPEQDEPTH
type: MMLCommand
name: RMV QOSSHAPEQDEPTH（删除Qos Shape缓存队列深度与流量速率的对应关系）
nf: UDG
version: 20.15.2
verb: RMV
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

# RMV QOSSHAPEQDEPTH（删除Qos Shape缓存队列深度与流量速率的对应关系）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用于清除配置的流量做shaping时的队列深度。执行删除命令需要指定速率，表示清除该速率所对应的队列深度。

## 注意事项

- 该命令执行后立即生效。
- 该命令只能用于清除已配置的速率对应的队列深度。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RATE | Qos Shape速率（千比特/秒） | 可选必选说明：必选参数<br>参数含义：指定shaping的流量速率。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295，单位是千比特每秒。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@QOSSHAPEQDEPTH]] · Qos Shape缓存队列深度与流量速率的对应关系（QOSSHAPEQDEPTH）

## 使用实例

清除128kbps速率的队列深度配置：

```
RMV QOSSHAPEQDEPTH:RATE=128;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-QOSSHAPEQDEPTH.md`
