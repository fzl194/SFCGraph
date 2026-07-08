---
id: UNC@20.15.2@MMLCommand@SET IPPOOLALMTHD
type: MMLCommand
name: SET IPPOOLALMTHD（设置本地地址池组使用率告警阈值）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: IPPOOLALMTHD
command_category: 配置类
applicable_nf:
- PGW-C
- GGSN
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- UE地址管理
- UE地址池管理
- 地址池组使用率告警阈值
status: active
---

# SET IPPOOLALMTHD（设置本地地址池组使用率告警阈值）

## 功能

**适用NF：PGW-C、GGSN、SMF**

UNC支持将若干个地址池绑定为一个地址池组，并基于该地址池组为UE动态分配地址。为了即时监控地址池组中IP地址的使用率，UNC提供了“地址池组使用率超阈值”告警。该命令用于设置该地址池组使用率告警的产生阈值和恢复阈值。

## 注意事项

- 该命令执行后立即生效。

- 修改告警产生阈值和告警恢复阈值后，系统根据新配置的告警产生阈值和告警恢复阈值判断是否清除已上报告警。
- 若门限配置的不合理，配置过低，则可能会导致系统频繁告警；配置过高，则可能不能及时提醒地址可能即将用完，进而影响必要的扩容。
- 告警恢复阈值必须小于告警产生阈值。
- 当前版本不支持此命令。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| WARNTHRESH | RECVTHRESH |
| --- | --- |
| 80 | 70 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| WARNTHRESH | 告警产生阈值 (%) | 可选必选说明：必选参数<br>参数含义：该参数用于指定本地地址池组的使用率的告警产生阈值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~100，单位是百分比。<br>默认值：无。<br>配置原则：无 |
| RECVTHRESH | 告警恢复阈值 (%) | 可选必选说明：必选参数<br>参数含义：该参数用于指定本地地址池组的使用率的告警恢复阈值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~100，单位是百分比。<br>默认值：无。<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@IPPOOLALMTHD]] · 本地地址池组使用率告警阈值（IPPOOLALMTHD）

## 使用实例

设置本地地址池组使用率告警的产生阈值和恢复阈值，执行命令如下：

```
SET IPPOOLALMTHD:WARNTHRESH=81,RECVTHRESH=61;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-IPPOOLALMTHD.md`
