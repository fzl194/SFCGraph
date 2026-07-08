---
id: UNC@20.15.2@MMLCommand@SET IULOAD
type: MMLCommand
name: SET IULOAD（设置SGP负荷配置）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: IULOAD
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- Iu接口管理
- Iu负荷配置
status: active
---

# SET IULOAD（设置SGP负荷配置）

## 功能

![](设置SGP负荷配置(SET IULOAD)_26305846.assets/notice_3.0-zh-cn_2.png)

如果未立即复位SGP，在后续的系统运行中如果发生部分SGP的复位，将会导致系统内的Iu接口负荷分担错误，导致负荷不均用户无法接入。

**适用网元：SGSN**

该命令用于设置Iu接口负荷在SGP进程间分担的控制参数。

## 注意事项

- 系统初次运行时，会执行系统初始设置值。
- 每个定时器的计量单位是不一样的，包括“分钟”和“秒”两种。
- “IUSHSPT”和“NTMR”需要复位SGP才能生效，其中“IUSHSPT”影响比较大，决定RANAP层是否负荷分担。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IUSHSPT | 是否支持Iu负荷分担 | 可选必选说明：可选参数<br>参数含义：该参数用于指定是否支持全系统内SGP进程的Iu负荷分担。<br>数据来源：整网规划<br>取值范围：<br>- “NO(否)”<br>- “YES(是)”<br>系统初始设置值：<br>“YES(是)”<br>说明：如果不启用全系统负荷分担，会导致负荷在不同的SGP进程上分担不均，可能导致在系统存在可用资源的情况下部分进程发送拥塞。 |
| NTMR | 周期性通知定时器长度（min） | 可选必选说明：可选参数<br>参数含义：该参数用于指定各个SGP进程之间状态周期性同步的时间间隔。<br>数据来源：整网规划<br>取值范围：1min~100min<br>系统初始设置值：5min |
| OVERLOADTMR | 发送OVERLOAD消息定时器长度（s） | 可选必选说明：可选参数<br>参数含义：该参数用于指定SGP进程过载之后，向RNC发送OVERLOAD消息的时间间隔。<br>数据来源：整网规划<br>取值范围：5s~250s<br>系统初始设置值：40s |
| LTHRESH | 保留参数1 | 可选必选说明：可选参数<br>参数含义：该参数为保留参数，暂未实现。<br>数据来源：整网规划<br>取值范围：1~100<br>系统初始设置值：无<br>说明：LTHRESH取值不能超过HTHRESH的值。 |
| HTHRESH | 保留参数2 | 可选必选说明：可选参数<br>参数含义：该参数为保留参数，暂未实现。<br>数据来源：整网规划<br>取值范围：1~100<br>系统初始设置值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/IULOAD]] · 用户Iu连接负荷状态（IULOAD）

## 使用实例

设置负荷配置：

SET IULOAD: IUSHSPT=YES, NTMR=5, OVERLOADTMR=40;

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-IULOAD.md`
