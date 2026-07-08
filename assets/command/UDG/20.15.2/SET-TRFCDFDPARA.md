---
id: UDG@20.15.2@MMLCommand@SET TRFCDFDPARA
type: MMLCommand
name: SET TRFCDFDPARA（设置大流量攻击防护参数）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: TRFCDFDPARA
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
- 大流量攻击防护参数
status: active
---

# SET TRFCDFDPARA（设置大流量攻击防护参数）

## 功能

**适用NF：UPF**

![](设置大流量攻击防护参数（SET TRFCDFDPARA）_82837757.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，请确认上下行流量比例配置合理，否则可能导致用户丢包或去活。

该命令用于设置大流量攻击检测防护参数。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 对于大流量场景，如果不确定上下行流量的合理比例，不建议开启该检测功能，否则误配置后会被误识别为攻击流量，导致用户丢包或去活。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | UPCPUTHR | UPINTERVAL | UPRATIOTHR | UPCARCTL | UPRATINGTHR | DOWNCPUTHR | DOWNINTERVAL | DOWNRATIOTHR | DOWNCARCTL | DOWNRATINGTHR | ATKACT | LOGSW |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 初始值 | 0 | 5 | 10 | DISABLE | 10 | 0 | 5 | 10 | DISABLE | 10 | DROP | DISABLE |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| UPCPUTHR | 上行CPU阈值 | 可选必选说明：可选参数<br>参数含义：设置上行大流量攻击检测功能的CPU阈值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～100，单位是百分比。<br>默认值：无<br>配置原则：无 |
| UPINTERVAL | 上行报文探测周期 | 可选必选说明：可选参数<br>参数含义：设置上行大流量攻击检测周期。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～65。<br>默认值：无<br>配置原则：检测周期为UpInterval*1000包数。即当用户上行或下行包数大于等于UpInterval*1000时，统计本周期内对应方向上报文数的比例，判断是否存在攻击行为。统计后上下行报文数清零，开始下一周期的报文数统计。默认值为5，标识默认检测周期为5000包数。 |
| UPRATIOTHR | 上行报文比例阈值 | 可选必选说明：可选参数<br>参数含义：设置识别大流量攻击行为的上行报文数与下行报文数的比例。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～255。<br>默认值：无<br>配置原则：当某一周期用户上下行报文数之比大于UpRatioThr时， 认为该用户存在大流量攻击。 |
| UPCARCTL | 上行报文防护car控制开关 | 可选必选说明：可选参数<br>参数含义：设置是否在用户上行速率超过配置的PIR时再启动上行大流量攻击检测功能。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |
| UPRATINGTHR | 上行报文速率阈值 | 可选必选说明：可选参数<br>参数含义：设置上行大流量攻击检测功能的检测速率，单位kpps。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无<br>配置原则：当某一周期用户上行速率大于UpRatingThr时， 认为该用户存在大流量攻击。 |
| DOWNCPUTHR | 下行CPU阈值 | 可选必选说明：可选参数<br>参数含义：开启下行大流量攻击检测功能的CPU阈值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～100，单位是百分比。<br>默认值：无<br>配置原则：无 |
| DOWNINTERVAL | 下行报文探测周期 | 可选必选说明：可选参数<br>参数含义：设置下行大流量攻击检测周期。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～65。<br>默认值：无<br>配置原则：检测周期为DownInterval*1000包数。即当用户上行或下行包数大于等于DownInterval*1000时，统计本周期内对应方向上报文数的比例，判断是否存在攻击行为。统计后上下行报文数清零，开始下一周期的报文数统计。默认值为5，标识默认检测周期为5000包数。 |
| DOWNRATIOTHR | 下行报文比例阈值 | 可选必选说明：可选参数<br>参数含义：设置识别大流量攻击行为的下行报文数与上行报文数的比例。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～255。<br>默认值：无<br>配置原则：当某一周期用户下上行报文数之比大于DownRatioThr时， 认为该用户存在大流量攻击。 |
| DOWNCARCTL | 下行报文防护car控制开关 | 可选必选说明：可选参数<br>参数含义：设置是否在用户下行速率超过配置的PIR时再启动下行大流量攻击检测功能。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |
| DOWNRATINGTHR | 下行报文速率阈值 | 可选必选说明：可选参数<br>参数含义：设置下行大流量攻击检测功能的检测速率，单位kpps。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无<br>配置原则：当某一周期用户下行速率大于DownRatingThr时， 认为该用户存在大流量攻击。 |
| ATKACT | 报文防攻击动作 | 可选必选说明：可选参数<br>参数含义：设置识别大流量攻击行为后的处理动作。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DROP：丢包。<br>- DEACTIVE：承载去活。<br>- PASS：报文通过。<br>默认值：无<br>配置原则：无 |
| LOGSW | 日志开关 | 可选必选说明：可选参数<br>参数含义：设置识别大流量攻击行为后是否记录诊断日志。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@TRFCDFDPARA]] · 大流量攻击防护配置参数（TRFCDFDPARA）

## 使用实例

- 设置大流量攻击检测防护参数：
  ```
  SET TRFCDFDPARA: UPCPUTHR=80, DOWNCPUTHR=80, ATKACT=DROP, LOGSW=ENABLE;
  ```
- IPV4用户攻击记录的日志：
  ```
  find being attacked,ipid=1002,offset=0x4000,protocol=6,ueip=0xd6ffff01,serverip=0x01346adc8,sp=22,dp=10986,uppktnum=1,dnpktnum=1000.
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-TRFCDFDPARA.md`
