---
id: UDG@20.15.2@MMLCommand@SET TCPSTATRTTRANGE
type: MMLCommand
name: SET TCPSTATRTTRANGE（设置TCP统计功能的RTT区间）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: TCPSTATRTTRANGE
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 1
category_path:
- 用户面服务管理
- 业务运维
- 业务性能统计管理
- TcpStatRttRange
status: active
---

# SET TCPSTATRTTRANGE（设置TCP统计功能的RTT区间）

## 功能

**适用NF：PGW-U、UPF**

该命令用于设置TCP统计功能中的UE侧、SP侧RTT区间。通过观察网络中TCP业务流的UE侧、SP侧RTT比例分布，可以评估网络的传输质量。基于业务的TCP统计功能支持根据UE侧RTT区间、SP侧RTT区间统计TCP流数；如UE侧RTT区间为0到20ms的TCP流数，SP侧RTT区间为0到3ms的TCP流数。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 不允许RTT区间有重叠。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | UERANGE1MIN | UERANGE1MAX | UERANGE2MIN | UERANGE2MAX | UERANGE3MIN | UERANGE3MAX | UERANGE4MIN | UERANGE4MAX | SPRANGE1MIN | SPRANGE1MAX | SPRANGE2MIN | SPRANGE2MAX | SPRANGE3MIN | SPRANGE3MAX | SPRANGE4MIN | SPRANGE4MAX |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 初始值 | 0 | 20 | 20 | 60 | 60 | 150 | 150 | 65535 | 0 | 3 | 3 | 20 | 20 | 50 | 50 | 65535 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| UERANGE1MIN | UE侧RTT区间1最小值（毫秒） | 可选必选说明：可选参数<br>参数含义：该参数用于指定UE侧RTT区间1的最小值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65535，单位是毫秒。该参数必须小于UERange1Max。<br>默认值：无<br>配置原则：无 |
| UERANGE1MAX | UE侧RTT区间1最大值（毫秒） | 可选必选说明：可选参数<br>参数含义：该参数用于指定UE侧RTT区间1的最大值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65535，单位是毫秒。该参数必须大于UERange1Min，并且小于等于UERange2Min。<br>默认值：无<br>配置原则：无 |
| UERANGE2MIN | UE侧RTT区间2最小值（毫秒） | 可选必选说明：可选参数<br>参数含义：该参数用于指定UE侧RTT区间2的最小值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65535，单位是毫秒。该参数必须大于等于UERange1Max，并且小于UERange2Max。<br>默认值：无<br>配置原则：无 |
| UERANGE2MAX | UE侧RTT区间2最大值（毫秒） | 可选必选说明：可选参数<br>参数含义：该参数用于指定UE侧RTT区间2的最大值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65535，单位是毫秒。该参数必须大于UERange2Min，并且小于等于UERange3Min。<br>默认值：无<br>配置原则：无 |
| UERANGE3MIN | UE侧RTT区间3最小值（毫秒） | 可选必选说明：可选参数<br>参数含义：该参数用于指定UE侧RTT区间3的最小值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65535，单位是毫秒。该参数必须大于等于UERange2Max，并且小于UERange3Max。<br>默认值：无<br>配置原则：无 |
| UERANGE3MAX | UE侧RTT区间3最大值（毫秒） | 可选必选说明：可选参数<br>参数含义：该参数用于指定UE侧RTT区间3的最大值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65535，单位是毫秒。该参数必须大于UERange3Min，并且小于等于UERange4Min。<br>默认值：无<br>配置原则：无 |
| UERANGE4MIN | UE侧RTT区间4最小值（毫秒） | 可选必选说明：可选参数<br>参数含义：该参数用于指定UE侧RTT区间4的最小值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65535，单位是毫秒。该参数必须大于等于UERange3Max，并且小于UERange4Max。<br>默认值：无<br>配置原则：无 |
| UERANGE4MAX | UE侧RTT区间4最大值（毫秒） | 可选必选说明：可选参数<br>参数含义：该参数用于指定UE侧RTT区间4的最大值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65535，单位是毫秒。该参数必须大于UERange4Min。<br>默认值：无<br>配置原则：无 |
| SPRANGE1MIN | SP侧RTT区间1最小值（毫秒） | 可选必选说明：可选参数<br>参数含义：该参数用于指定SP侧RTT区间1的最小值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65535，单位是毫秒。该参数必须小于SPRange1Max。<br>默认值：无<br>配置原则：无 |
| SPRANGE1MAX | SP侧RTT区间1最大值（毫秒） | 可选必选说明：可选参数<br>参数含义：该参数用于指定SP侧RTT区间1的最大值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65535，单位是毫秒。该参数必须大于SPRange1Min，并且小于等于SPRange2Min。<br>默认值：无<br>配置原则：无 |
| SPRANGE2MIN | SP侧RTT区间2最小值（毫秒） | 可选必选说明：可选参数<br>参数含义：该参数用于指定SP侧RTT区间2的最小值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65535，单位是毫秒。该参数必须大于等于SPRange1Max，并且小于SPRange2Max。<br>默认值：无<br>配置原则：无 |
| SPRANGE2MAX | SP侧RTT区间2最大值（毫秒） | 可选必选说明：可选参数<br>参数含义：该参数用于指定SP侧RTT区间2的最大值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65535，单位是毫秒。该参数必须大于SPRange2Min，并且小于等于SPRange3Min。<br>默认值：无<br>配置原则：无 |
| SPRANGE3MIN | SP侧RTT区间3最小值（毫秒） | 可选必选说明：可选参数<br>参数含义：该参数用于指定SP侧RTT区间3的最小值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65535，单位是毫秒。该参数必须大于等于SPRange2Max，并且小于SPRange3Max。<br>默认值：无<br>配置原则：无 |
| SPRANGE3MAX | SP侧RTT区间3最大值（毫秒） | 可选必选说明：可选参数<br>参数含义：该参数用于指定SP侧RTT区间3的最大值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65535，单位是毫秒。该参数必须大于SPRange3Min，并且小于等于SPRange4Min。<br>默认值：无<br>配置原则：无 |
| SPRANGE4MIN | SP侧RTT区间4最小值（毫秒） | 可选必选说明：可选参数<br>参数含义：该参数用于指定SP侧RTT区间4的最小值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65535，单位是毫秒。该参数必须大于等于SPRange3Max，并且小于SPRange4Max。<br>默认值：无<br>配置原则：无 |
| SPRANGE4MAX | SP侧RTT区间4最大值（毫秒） | 可选必选说明：可选参数<br>参数含义：该参数用于指定SP侧RTT区间4的最大值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65535，单位是毫秒。该参数必须大于SPRange4Min。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/TCPSTATRTTRANGE]] · TCP统计功能的RTT区间为初始值（TCPSTATRTTRANGE）

## 使用实例

如果运营商需要把UE侧的RTT区间1设置为[6,16)，区间2设置为[26,36)，区间3设置为[46,56)，区间4设置为[66,76)：

```
SET TCPSTATRTTRANGE: UERANGE1MIN=6, UERANGE1MAX=16, UERANGE2MIN=26, UERANGE2MAX=36, UERANGE3MIN=46, UERANGE3MAX=56, UERANGE4MIN=66, UERANGE4MAX=76;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-TCPSTATRTTRANGE.md`
