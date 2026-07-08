---
id: UDG@20.15.2@MMLCommand@SET IPSQMQDEPTH
type: MMLCommand
name: SET IPSQMQDEPTH（设置IPSQM缓存队列深度）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: IPSQMQDEPTH
command_category: 配置类
applicable_nf:
- SGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 1
category_path:
- 用户面服务管理
- 业务控制策略
- IPSQM控制
- IPSQM整形队列深度
status: active
---

# SET IPSQMQDEPTH（设置IPSQM缓存队列深度）

## 功能

**适用NF：SGW-U、UPF**

该命令用于配置整形队列深度。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 配置DEPTH参数时推荐按照如下算法估算出队列深度：QUEDEPTH = rate*RTT/pktlen。其中，rate是参数RATE的值转换成字节每秒，RTT（Round-Trip Time）需要根据网络情况估算（单位是秒），pktlen是报文的平均长度（单位是字节）。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | DEPTH |
| --- | --- |
| 初始值 | 20 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DEPTH | 队列深度（报文个数） | 可选必选说明：必选参数<br>参数含义：IPSQM整形PDP缓存队列深度，即可以缓存报文的个数。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～1024。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [IPSQM缓存队列深度（IPSQMQDEPTH）](configobject/UDG/20.15.2/IPSQMQDEPTH.md)

## 关联任务

- [[UDG@20.15.2@Task@0-00232]]

## 使用实例

配置整形队列深度：

```
SET IPSQMQDEPTH: DEPTH=256;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置IPSQM缓存队列深度（SET-IPSQMQDEPTH）_21392220.md`
