---
id: UDG@20.15.2@MMLCommand@SET EXTOTTMATCHSW
type: MMLCommand
name: SET EXTOTTMATCHSW（OTT业务规则匹配功能是否使能）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: EXTOTTMATCHSW
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: true
max_records: 1
category_path:
- 用户面服务管理
- 业务匹配策略
- 百万级业务规则库
- 全局OTT开关
status: active
---

# SET EXTOTTMATCHSW（OTT业务规则匹配功能是否使能）

## 功能

**适用NF：PGW-U、UPF**

该命令用来设置OTT业务规则匹配功能是否使能。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 本命令属于高危命令，操作不当会导致性能下降明显，请谨慎使用并联系华为技术支持协助操作。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | IPV4MATCH | IPV6MATCH |
| --- | --- | --- |
| 初始值 | DISABLE | DISABLE |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPV4MATCH | IPv4流量OTT业务规则匹配功能开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定是否支持ISU VM外置匹配基于IPv4的OTT业务。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能（关闭）。<br>- ENABLE：使能（开启）。<br>默认值：无<br>配置原则：当需要对ipv4业务流量与OTT业务规则库做匹配时，需要设置为开启。 |
| IPV6MATCH | IPv6流量OTT业务规则匹配功能开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定是否支持ISU VM外置匹配基于IPv6的OTT业务。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能（关闭）。<br>- ENABLE：使能（开启）。<br>默认值：无<br>配置原则：当需要对ipv6业务流量与OTT业务规则库做匹配时，需要设置为开启。 |

## 操作的配置对象

- [OTT业务规则匹配功能是否使能（EXTOTTMATCHSW）](configobject/UDG/20.15.2/EXTOTTMATCHSW.md)

## 关联任务

- [0-00093](task/UDG/20.15.2/0-00093.md)

## 使用实例

如设置支持ISU VM外置匹配基于IPv4和IPv6的OTT业务，命令如下：

```
SET EXTOTTMATCHSW: IPV4MATCH=ENABLE, IPV6MATCH=ENABLE;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/OTT业务规则匹配功能是否使能（SET-EXTOTTMATCHSW）_06453258.md`
