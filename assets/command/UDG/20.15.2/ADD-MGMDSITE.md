---
id: UDG@20.15.2@MMLCommand@ADD MGMDSITE
type: MMLCommand
name: ADD MGMDSITE（添加IGMP全局配置）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: MGMDSITE
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
max_records: 65535
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP组播
- MGMD
- IGMP全局配置
status: active
---

# ADD MGMDSITE（添加IGMP全局配置）

## 功能

该命令用来创建IGMP全局配置。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为65535。
- 需要首先在公网或VPN实例下配置ADD MCASTENABLE命令。
- 该命令仅适用于非NP卡场景和NP卡非加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ADDRESSFAMILY | 地址族 | 可选必选说明：必选参数<br>参数含义：该参数用于表示地址族类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4unicast：IPv4单播。<br>默认值：无 |
| VRFNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用来指定VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：_public_<br>配置原则：通过LST L3VPNINST查看当前已存在的VPN实例。 |
| QUERYINTERVAL | 周期性普遍查询时间（s） | 可选必选说明：可选参数<br>参数含义：该参数用来指定周期性普遍查询时间。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～18000，单位是秒。<br>默认值：60 |
| QUERYRSPINTERVAL | 查询响应时间（s） | 可选必选说明：可选参数<br>参数含义：该参数用来指定查询响应时间。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～125，单位是秒。<br>默认值：10 |
| ROBUSTNESS | 鲁棒稳定系数 | 可选必选说明：可选参数<br>参数含义：该参数用来指定鲁棒稳定系数。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为2～5。<br>默认值：2 |
| LMQT | 特定组查询的周期性时间（s） | 可选必选说明：可选参数<br>参数含义：该参数用来指定特定组查询的周期性时间。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～25，单位是秒。<br>默认值：1 |
| OTHQUERIERPSTTIME | 其他查询器存在的时间（s） | 可选必选说明：可选参数<br>参数含义：该参数用来指定其他查询器存在的时间。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为60～300，单位是秒。<br>默认值：无<br>配置原则：如果不输入该参数，则表示其他查询器存在的时间的计算公式是：其他IGMP查询器的存活时间 ＝ 健壮系数 × IGMP普遍查询消息发送间隔 +（1/2）× 最大查询响应时间。当健壮系数、IGMP普遍查询消息发送间隔和最大查询响应时间都取缺省值时，其他IGMP查询器的存活时间的值为125秒。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/MGMDSITE]] · IGMP全局配置（MGMDSITE）

## 使用实例

创建IGMP全局配置鲁棒系数为3：

```
ADD MGMDSITE:VRFNAME="_public_",ADDRESSFAMILY=ipv4unicast,ROBUSTNESS=3;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/ADD-MGMDSITE.md`
