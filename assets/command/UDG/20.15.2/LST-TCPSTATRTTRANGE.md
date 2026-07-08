---
id: UDG@20.15.2@MMLCommand@LST TCPSTATRTTRANGE
type: MMLCommand
name: LST TCPSTATRTTRANGE（查询TCP统计功能的RTT区间）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: TCPSTATRTTRANGE
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务运维
- 业务性能统计管理
- TcpStatRttRange
status: active
---

# LST TCPSTATRTTRANGE（查询TCP统计功能的RTT区间）

## 功能

**适用NF：PGW-U、UPF**

该命令用于查询TCP统计功能中的UE侧、SP侧RTT区间。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/TCPSTATRTTRANGE]] · TCP统计功能的RTT区间为初始值（TCPSTATRTTRANGE）

## 使用实例

如果运营商需要查询TCP统计功能中的UE侧、SP侧RTT区间：

```
LST TCPSTATRTTRANGE:;
```

```

RETCODE = 0  操作成功。

TCP统计的RTT区间信息
--------------------
UE侧RTT区间1最小值（毫秒）  =  6
UE侧RTT区间1最大值（毫秒）  =  16
UE侧RTT区间2最小值（毫秒）  =  26
UE侧RTT区间2最大值（毫秒）  =  36
UE侧RTT区间3最小值（毫秒）  =  46
UE侧RTT区间3最大值（毫秒）  =  56
UE侧RTT区间4最小值（毫秒）  =  66
UE侧RTT区间4最大值（毫秒）  =  76
SP侧RTT区间1最小值（毫秒）  =  8
SP侧RTT区间1最大值（毫秒）  =  18
SP侧RTT区间2最小值（毫秒）  =  28
SP侧RTT区间2最大值（毫秒）  =  38
SP侧RTT区间3最小值（毫秒）  =  48
SP侧RTT区间3最大值（毫秒）  =  58
SP侧RTT区间4最小值（毫秒）  =  68
SP侧RTT区间4最大值（毫秒）  =  78
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询TCP统计功能的RTT区间（LST-TCPSTATRTTRANGE）_74749243.md`
