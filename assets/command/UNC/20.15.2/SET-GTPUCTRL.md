---
id: UNC@20.15.2@MMLCommand@SET GTPUCTRL
type: MMLCommand
name: SET GTPUCTRL（设置用户面控制参数）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: GTPUCTRL
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
- 数据转发管理
- GTP-U
- GTP-U参数管理
status: active
---

# SET GTPUCTRL（设置用户面控制参数）

## 功能

**适用网元：SGSN、MME**

该命令用于设置用户面控制参数。用户面控制参数包括GTPU协议参数表定时器参数、流量更新时是否上报PDP信息到用户跟踪的开关。

## 注意事项

- 系统初次运行时，会执行系统初始设置值。
- 该命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NSSTDDT | 新SGSN开始下行时间（100ms） | 可选必选说明：可选参数<br>参数含义：该参数用来表示Inter-Rau切换时，新侧的SGSN首先要缓存下行数据，并启动此定时器控制何时发送缓存的数据。<br>数据来源：本端规划<br>取值范围：1~255<br>系统初始设置值：<br>“2”<br>。<br>配置原则：<br>- 该参数设置时长要小于“停止接收切换数据时间(s)”设置的时长。<br>- 该参数一般不需要设置。<br>说明：本参数配置后对当前已经启动的定时器无效，只对后续启动的定时器有效。 |
| NSSTHDT | 停止接收切换数据时间（s） | 可选必选说明：可选参数<br>参数含义：该参数用来表示Inter RAU切换时，若该定时器超时，SGSN停止接收切换数据。<br>数据来源：本端规划<br>取值范围：3~120<br>系统初始设置值：<br>“11”<br>。<br>配置原则：<br>- 该参数设置时长要大于“新SGSN开始下行时间(100ms)”设置的时长。<br>- 该参数一般不需要设置。<br>说明：本参数配置后对当前已经启动的定时器无效，只对后续启动的定时器有效。 |
| DPDPTIME | GTP-U路径断后多久去活PDP （s） | 可选必选说明：可选参数<br>参数含义：该参数定义了GTP-U路径断后，隔多少秒去激活PDP。<br>数据来源：本端规划<br>取值范围：0~864000<br>系统初始设置值：<br>“0”<br>。<br>配置原则：该参数一般不需要设置。 |
| PDPTRCFORPFFLUX | 流量更新时是否将PDP信息上报到用户跟踪开关 | 可选必选说明：可选参数<br>参数含义：该参数用于控制在流量更新时是否将PDP信息上报到用户跟踪。<br>数据来源：本端规划<br>取值范围：<br>- “OFF(关闭)”<br>- “ON(打开)”<br>系统初始设置值：<br>“OFF(关闭)”<br>。<br>配置原则：该参数一般不要设置。 |
| SPTSPCSRVEXT | 2G支持特殊业务类型扩展头 | 可选必选说明：可选参数<br>参数含义：2G支持特殊业务类型扩展头。 此参数只针对2G用户，控制<br>UNC<br>是否支持来自GGSN的下行报文中的特殊业务类型扩展头的处理，提取业务信息。否则，剥去该扩展头。<br>取值范围：<br>- “NOT_SUPPORT(不支持)”<br>- “SUPPORT(支持)”<br>系统初始设置值：<br>“NOT_SUPPORT(不支持)”<br>。 |
| FWDSPCSRVEXT | 3G透传特殊业务类型扩展头 | 可选必选说明：可选参数<br>参数含义：3G透传特殊业务类型扩展头。 此参数只针对3G用户，控制<br>UNC<br>是否透传GGSN的下行报文中的特殊业务类型扩展头给RNC。否则，剥去该扩展头。<br>取值范围：<br>- “REMOVE(剥去)”<br>- “FORWARD(透传)”<br>系统初始设置值：<br>“REMOVE(剥去)”<br>。 |

## 操作的配置对象

- [用户面控制参数（GTPUCTRL）](configobject/UNC/20.15.2/GTPUCTRL.md)

## 使用实例

1. 设置“新SGSN开始下行时间”为500毫秒，“停止接收切换数据时间”为80秒：
  SET GTPUCTRL: NSSTDDT=5, NSSTHDT=80;
2. 设置“GTP-U路径断后多久去活PDP”为50秒：
  SET GTPUCTRL:DPDPTIME=50;
3. 设置“2G支持特殊业务类型扩展头”为“支持”：
  SET GTPUCTRL: SPTSPCSRVEXT=SUPPORT;
4. 设置“3G透传特殊业务类型扩展头”为“透传”：
  SET GTPUCTRL: FWDSPCSRVEXT=FORWARD;

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置用户面控制参数(SET-GTPUCTRL)_26305648.md`
