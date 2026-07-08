---
id: UNC@20.15.2@MMLCommand@SET FAULTLNKDETCFG
type: MMLCommand
name: SET FAULTLNKDETCFG（设置故障链路探测功能）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: FAULTLNKDETCFG
command_category: 配置类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 扩展调测
- 平台调测
- 故障链路探测管理
status: active
---

# SET FAULTLNKDETCFG（设置故障链路探测功能）

## 功能

**适用网元：SGSN、MME**

该命令用于设置系统是否开启故障链路的TRACEROUTE探测功能，支持的链路包括：Diameter、S1AP、SGs、GTPC、M3UA、IP NS-VC、Ga、Dns类型的链路。本功能开启后，链路故障时系统自动获取链路本对端IP地址，并启动TRACEROUTE探测。

## 注意事项

- 系统初次运行时，会执行系统初始设置值。
- 该命令执行后立即生效。
- 故障探测链路不区分是否交叉路径，以平行链路进行探测。
- 如果周边设备不支持TRACEROUTE探测，或者ICMP报文达到流控，则可能导致产品接收不到TRACEROUTE探测响应报文。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SWITCH | 控制开关 | 可选必选说明：可选参数<br>参数含义：该参数控制系统是否开启对故障链路的TRACEROUTE探测功能。打开此功能之后，系统将自动把最近一段时间内收发的故障链路的TRACEROUTE探测结果保存在服务日志里(服务类型为LINK_DET，采集方法参考<br>[采集诊断日志](../../../../../../../../../网络运维/故障处理/UNC故障信息收集/通过OM Portal采集信息（存储正常期间）/采集诊断日志_04293376.md)<br>)，用于协助故障链路问题定位和分析。<br>数据来源：本端规划<br>取值范围：<br>- “OFF(关)”：关闭故障链路探测功能。<br>- “ON(开)”：打开故障链路探测功能。<br>系统初始设置值：<br>“ON(开)”<br>。<br>配置原则：<br>“为了提升系统在链路故障情况下的定位和分析能力，建议打开此开关”<br>。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/FAULTLNKDETCFG]] · 故障链路探测配置（FAULTLNKDETCFG）

## 使用实例

为了提升系统在链路故障情况下的定位和分析能力，建议打开故障链路的TRACEROUTE探测功能：

SET FAULTLNKDETCFG: SWITCH=ON;

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-FAULTLNKDETCFG.md`
