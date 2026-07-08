---
id: UNC@20.15.2@MMLCommand@SET FWDFCPARA
type: MMLCommand
name: SET FWDFCPARA（设置转发面流控参数）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: FWDFCPARA
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- CSLB功能管理
- 操作维护
- 系统调测
- 转发面流控参数
status: active
---

# SET FWDFCPARA（设置转发面流控参数）

## 功能

![](设置转发面流控参数（SET FWDFCPARA）_59903035.assets/notice_3.0-zh-cn_2.png)

可能会影响流控设置，请谨慎使用并联系华为技术支持协助操作。

该命令用于设置CSLB转发面流控参数。

## 注意事项

- 该命令执行后立即生效。
- 该命令执行时，FCTHDLEVLE1，FCTHDLEVEL2参数必须选择一个及以上才能执行，否则执行失败（错误码：0x1ce3）。仅设置FCTHDLEVEL1时，FCTHDLEVEL1值更新，FCTHDLEVEL2保持原有值不变；仅设置FCTHDLEVEL2时，FCTHDLEVEL2值更新，FCTHDLEVEL1保持原有值不变。
- 该命令仅适用于非NP卡场景和NP卡非加速模式场景。
- 该命令存在系统初始记录，参数的初始设置值如下表：
  | FCTYPE | FCTHDLEVEL1 | FCTHDLEVEL2 |
  | --- | --- | --- |
  | ICMP | 1024 | 60 |
  | IPS_DETECT | 3200 | 800 |
  | TCP_SYN | 200 | 10 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| FCTYPE | 流控类型 | 可选必选说明：必选参数<br>参数含义：该参数用于表示流控类型。<br>数据来源：本端规划<br>取值范围：枚举类型:<br>- ICMP ：对ICMP协议报文的流控；<br>- IPS_DETECT ：对IPS主动探测报文的流控；<br>- TCP_SYN ：对TCP协议SYN报文的流控；<br>默认值：无<br>配置原则：无 |
| FCTHDLEVEL1 | 一级流控阈值(pps) | 可选必选说明：该参数在FCTYPE为ICMP、IPS_DETECT或TCP_SYN时为可选参数。<br>参数含义：一级流控阈值。<br>- FCTYPE为ICMP时，为每个RU每秒能通过的ICMP报文数。<br>- FCTYPE为IPS_DETECT时，为每个RU每秒能通过的IPS探测报文数。<br>- FCTYPE为TCP_SYN时，为每个RU每秒能通过的TCP协议SYN报文数。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65535，单位是包每秒(pps)。其中，0代表不限制。<br>默认值：无<br>配置原则：无 |
| FCTHDLEVEL2 | 二级流控阈值(pps) | 可选必选说明：该参数在FCTYPE为ICMP、IPS_DETECT或TCP_SYN时为可选参数。<br>参数含义：二级流控阈值。<br>- FCTYPE为ICMP时，为每个ICMP流（源IP、目的IP、协议类型）每秒能通过的报文数。<br>- FCTYPE为IPS_DETECT时，为每个IPS探测链路（源IP、目的IP、协议类型）每秒能通过的报文数。<br>- FCTYPE为TCP_SYN时，为每个TCP连接（源IP、目的IP、源端口、目的端口、协议类型）每秒能通过的SYN报文数。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65535，单位是包每秒（pps）。其中，0代表不限制。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [转发面流控参数（FWDFCPARA）](configobject/UNC/20.15.2/FWDFCPARA.md)

## 使用实例

设置ICMP协议报文的流控，对每个RU设置流控级别为2000pps，对每个流设置流控级别为60pps，命令如下：

```
SET FWDFCPARA: FCTYPE=ICMP, FCTHDLEVEL1=2000, FCTHDLEVEL2=60;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置转发面流控参数（SET-FWDFCPARA）_59903035.md`
