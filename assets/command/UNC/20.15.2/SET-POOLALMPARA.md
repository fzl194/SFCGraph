---
id: UNC@20.15.2@MMLCommand@SET POOLALMPARA
type: MMLCommand
name: SET POOLALMPARA（设置本地地址池使用率告警参数）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: POOLALMPARA
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
- GGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- UE地址管理
- UE地址池管理
- 地址池使用率告警配置
status: active
---

# SET POOLALMPARA（设置本地地址池使用率告警参数）

## 功能

**适用NF：PGW-C、SMF、GGSN**

为了即时监控地址池使用率，UNC提供了“地址池使用率超阈值”告警。该命令用于设置地址池使用率告警的产生阈值和恢复阈值。

## 注意事项

- 该命令执行后立即生效。

- 修改告警产生阈值和告警恢复阈值后，系统根据新配置的告警产生阈值和告警恢复阈值判断是否清除已上报告警。
- 若门限配置的不合理，配置过低，则可能会导致系统频繁告警；配置过高，则可能不能及时提醒地址可能即将用完，进而影响必要的扩容。
- 告警恢复阈值必须小于告警产生阈值。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| WARNTHRESH | RECVTHRESH | THRESHSW |
| --- | --- | --- |
| 80 | 70 | Disable |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| WARNTHRESH | 告警产生阈值 (%) | 可选必选说明：必选参数<br>参数含义：该参数用于指定本地地址池的使用率的告警产生阈值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~100，单位是百分比。<br>默认值：无。<br>配置原则：无 |
| RECVTHRESH | 告警恢复阈值 (%) | 可选必选说明：必选参数<br>参数含义：该参数用于指定本地地址池的使用率的告警恢复阈值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~100，单位是百分比。<br>默认值：无。<br>配置原则：无 |
| THRESHSW | 地址池资源过载告警开关 | 可选必选说明：必选参数<br>参数含义：该参数用来控制是否开启地址池资源过载告警。<br>数据来源：本端规划<br>取值范围：<br>- Disable（去使能）<br>- Enable（使能）<br>默认值：无。<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/POOLALMPARA]] · 本地地址池使用率告警参数（POOLALMPARA）

## 使用实例

设置本地地址池使用率告警的产生阈值和恢复阈值，执行命令如下：

```
SET POOLALMPARA:WARNTHRESH=81,RECVTHRESH=61,THRESHSW=Enable;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置本地地址池使用率告警参数（SET-POOLALMPARA）_92057522.md`
