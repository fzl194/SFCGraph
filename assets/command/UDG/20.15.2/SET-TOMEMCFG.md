---
id: UDG@20.15.2@MMLCommand@SET TOMEMCFG
type: MMLCommand
name: SET TOMEMCFG（设置TCP Socket缓存配置）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: TOMEMCFG
command_category: 配置类
applicable_nf:
- UPF
effect_mode: 对新流生效
is_dangerous: false
max_records: 1
category_path:
- TCP优化服务管理
- TCP Socket缓存配置
status: active
---

# SET TOMEMCFG（设置TCP Socket缓存配置）

## 功能

**适用NF：UPF**

该命令用于设置TCP Socket缓存配置。

## 注意事项

- 该命令执行后对新数据流生效。
- 该命令最大记录数为1。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | TCPRMEMMIN | TCPRMEMDEFAULT | TCPRMEMMAX | TCPWMEMMIN | TCPWMEMDEFAULT | TCPWMEMMAX | TCPADVWINSCALE |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 初始值 | 131072 | 1048576 | 2097152 | 131072 | 1048576 | 2097152 | 2 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TCPRMEMMIN | 为TCP socket预留的接收缓存大小的最小值 | 可选必选说明：可选参数<br>参数含义：设置为TCP Socket预留的接收缓存大小的最小值。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围4096～100000000。<br>默认值：无<br>配置原则：无 |
| TCPRMEMDEFAULT | 为TCP socket预留的接收缓存大小的默认值 | 可选必选说明：可选参数<br>参数含义：设置为TCP Socket预留的接收缓存大小的默认值。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围4096～100000000。<br>默认值：无<br>配置原则：无 |
| TCPRMEMMAX | 为TCP socket预留的发送缓存大小的最大值 | 可选必选说明：可选参数<br>参数含义：设置为TCP Socket预留的接收缓存大小的最大值。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围4096～100000000。<br>默认值：无<br>配置原则：无 |
| TCPWMEMMIN | 为TCP socket预留的发送缓存大小的最小值 | 可选必选说明：可选参数<br>参数含义：设置为TCP Socket预留的发送缓存大小的最小值。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围4096～100000000。<br>默认值：无<br>配置原则：无 |
| TCPWMEMDEFAULT | 为TCP socket预留的发送缓存大小的默认值 | 可选必选说明：可选参数<br>参数含义：设置为TCP Socket预留的发送缓存大小的默认值。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围4096～100000000。<br>默认值：无<br>配置原则：无 |
| TCPWMEMMAX | 为TCP socket预留的发送缓存的大小最大值 | 可选必选说明：可选参数<br>参数含义：设置为TCP Socket预留的发送缓存的大小最大值。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围4096～100000000。<br>默认值：无<br>配置原则：无 |
| TCPADVWINSCALE | 应用层缓存开销的计算因子 | 可选必选说明：可选参数<br>参数含义：设置应用层缓存开销的计算因子，应用层缓存开销大小等于总的缓存大小/2^tcp_adv_win_scale。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围0~10。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [TCP Socket缓存配置（TOMEMCFG）](configobject/UDG/20.15.2/TOMEMCFG.md)

## 使用实例

设置TCP socket预留的接收缓存大小的最小值为1310720字节，TCP socket预留的接收缓存大小的初始值为10485760字节，TCP socket预留的接收缓存大小的最大值为20971520字节，TCP socket预留的发送缓存大小的最小值为1310720字节，TCP socket预留的发送缓存大小的初始值为10485760字节，TCP socket预留的发送缓存大小的最大值为20971520字节，应用层缓存开销的计算因子为5：

```
SET TOMEMCFG: TCPRMEMMIN=1310720, TCPRMEMDEFAULT=10485760, TCPRMEMMAX=20971520, TCPWMEMMIN=1310720, TCPWMEMDEFAULT=10485760, TCPWMEMMAX=20971520, TCPADVWINSCALE=5;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置TCP-Socket缓存配置（SET-TOMEMCFG）_31379097.md`
