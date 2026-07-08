---
id: UDG@20.15.2@MMLCommand@SET TRFCDFDSWITCH
type: MMLCommand
name: SET TRFCDFDSWITCH（设置大流量攻击防护功能）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: TRFCDFDSWITCH
command_category: 配置类
applicable_nf:
- UPF
effect_mode: 立即生效
is_dangerous: true
max_records: 1
category_path:
- 用户面服务管理
- 业务安全防护
- 用户攻击防护
- DDoS防护
- 大流量攻击防护开关
status: active
---

# SET TRFCDFDSWITCH（设置大流量攻击防护功能）

## 功能

**适用NF：UPF**

![](设置大流量攻击防护功能（SET TRFCDFDSWITCH）_82837760.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，请确认Set TrfcDfdPara配置合理，否则可能导致用户丢包或去活。

该命令用来配置整机粒度是否开启大流量攻击检测功能。某一周期内某用户流量超过大流量攻击防护参数（SET TRFCDFDPARA）设定的阈值，则认为该用户存在大流量攻击行为。对这种大流量攻击行为的检测即为大流量攻击检测。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 使能该功能前，请检查Set TrfcDfdPara配置是否合理，否则开启后会被误识别为攻击流量，导致用户丢包或去活。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | UPSWITCH | DOWNSWITCH |
| --- | --- | --- |
| 初始值 | DISABLE | DISABLE |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| UPSWITCH | 上行大流量攻击检测开关 | 可选必选说明：必选参数<br>参数含义：该参数用于配置是否开启全局上行大流量攻击检测功能。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：ENABLE：使能，开启全局上行大流量攻击检测功能。 DISABLE：去使能，关闭全局上行大流量攻击检测功能。 |
| DOWNSWITCH | 下行大流量攻击检测开关 | 可选必选说明：必选参数<br>参数含义：该参数用于配置是否开启全局下行大流量攻击检测功能。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：ENABLE：使能，开启全局下行大流量攻击检测功能。 DISABLE：去使能，关闭全局下行大流量攻击检测功能。 |

## 操作的配置对象

- [大流量攻击防护配置（TRFCDFDSWITCH）](configobject/UDG/20.15.2/TRFCDFDSWITCH.md)

## 使用实例

当CPU达到设定的阈值需要开启大流量攻击检测的场景下，设置整机粒度上行大流量攻击检测功能开关为开启，下行大流量攻击检测功能开关为开启：

```
SET TRFCDFDSWITCH: UPSWITCH=ENABLE, DOWNSWITCH=ENABLE;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置大流量攻击防护功能（SET-TRFCDFDSWITCH）_82837760.md`
