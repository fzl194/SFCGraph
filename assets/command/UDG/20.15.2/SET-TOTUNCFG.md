---
id: UDG@20.15.2@MMLCommand@SET TOTUNCFG
type: MMLCommand
name: SET TOTUNCFG（设置TCP Tun接口配置）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: TOTUNCFG
command_category: 配置类
applicable_nf:
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 1
category_path:
- TCP优化服务管理
- TCP Tun接口配置
status: active
---

# SET TOTUNCFG（设置TCP Tun接口配置）

## 功能

**适用NF：UPF**

该命令用于设置TUN接口配置。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | TUNINGROSWITCH | TUNOUTGSOSWITCH | TUNSLEEPTIME |
| --- | --- | --- | --- |
| 初始值 | DISABLE | ENABLE | 0 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TUNINGROSWITCH | TUN_IN接口的GRO聚合功能开关 | 可选必选说明：可选参数<br>参数含义：是否开启TUN_IN接口的GRO聚合功能。<br>数据来源：本端规划<br>取值范围：<br>- ENABLE：使能。<br>- DISABLE：不使能。<br>默认值：无<br>配置原则：无 |
| TUNOUTGSOSWITCH | TUN_OUT接口的GSO聚合功能开关 | 可选必选说明：可选参数<br>参数含义：是否开启TUN_OUT接口的GSO聚合功能。<br>数据来源：本端规划<br>取值范围：<br>- ENABLE：使能。<br>- DISABLE：DISABLE。<br>默认值：无<br>配置原则：无 |
| TUNSLEEPTIME | 休眠时间 | 可选必选说明：可选参数<br>参数含义：控制报文转发处理线程的休眠时间。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围0～1000。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@TOTUNCFG]] · TCP Tun接口配置（TOTUNCFG）

## 使用实例

开启TUN_IN接口的GRO聚合功能、开启TUN_OUT接口的GSO聚合功能、设置控制报文转发处理线程的休眠时间为10毫秒：

```
SET TOTUNCFG: TUNINGROSWITCH=ENABLE, TUNOUTGSOSWITCH=ENABLE, TUNSLEEPTIME=10;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-TOTUNCFG.md`
