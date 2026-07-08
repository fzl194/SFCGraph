---
id: UDG@20.15.2@MMLCommand@SET APPPOLICYPARA
type: MMLCommand
name: SET APPPOLICYPARA（设置应用策略参数）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: APPPOLICYPARA
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 1
category_path:
- 用户面服务管理
- 业务匹配策略
- 业务匹配公共配置
- 业务公共参数管理
- 应用策略开关参数
status: active
---

# SET APPPOLICYPARA（设置应用策略参数）

## 功能

**适用NF：PGW-U、UPF**

该命令用于设置APP策略参数。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | ACLSWITCH | BWALLOCATION | DNSREDSWITCH |
| --- | --- | --- | --- |
| 初始值 | DISABLE | DISABLE | DISABLE |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ACLSWITCH | 黑白名单开关 | 可选必选说明：可选参数<br>参数含义：该参数用于设置是否启用黑白名单策略。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能（关闭）。<br>- ENABLE：使能（开启）。<br>默认值：无<br>配置原则：配置使能时，仅白名单内的用户允许访问业务，黑名单不允许。 |
| BWALLOCATION | 应用带宽策略开关 | 可选必选说明：可选参数<br>参数含义：该参数用于设置是否支持app带宽策略。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能（关闭）。<br>- ENABLE：使能（开启）。<br>默认值：无<br>配置原则：配置使能时，对访问APP的上下行数据流做带宽控制。 |
| DNSREDSWITCH | DNS重定向开关 | 可选必选说明：可选参数<br>参数含义：该参数用于设置DNS重定向开关。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能（关闭）。<br>- ENABLE：使能（开启）。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [应用策略参数（APPPOLICYPARA）](configobject/UDG/20.15.2/APPPOLICYPARA.md)

## 使用实例

使能黑白名单策略控制开关、APP带宽策略控制开关和DNS重定向策略控制开关：

```
SET APPPOLICYPARA: ACLSWITCH=ENABLE, BWALLOCATION=ENABLE, DNSREDSWITCH=ENABLE;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置应用策略参数（SET-APPPOLICYPARA）_64015284.md`
