---
id: UDG@20.15.2@MMLCommand@MOD OSPFDEFAULTROUTE
type: MMLCommand
name: MOD OSPFDEFAULTROUTE（修改OSPF默认宣告路由配置）
nf: UDG
version: 20.15.2
verb: MOD
object_keyword: OSPFDEFAULTROUTE
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- OSPF管理
- OSPF默认宣告路由配置
status: active
---

# MOD OSPFDEFAULTROUTE（修改OSPF默认宣告路由配置）

## 功能

该命令用于修改普通OSPF区域的缺省路由。

## 注意事项

- 该命令执行后立即生效。
- 只有在配置了OSPF进程后才能使用此命令。
- OSPF缺省路由发布的方式取决于引入缺省路由的区域类型，该命令仅用于发布缺省路由到普通OSPF区域。
- 对于Stub区域、Totally Stub区域、Totally NSSA区域，缺省路由自动发布。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCID | 进程号 | 可选必选说明：必选参数<br>参数含义：OSPF进程号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无<br>配置原则：OSPF进程必须已经存在。请使用LST OSPF命令查看可用的OSPF进程。 |
| TOPOID | 拓扑标识 | 可选必选说明：必选参数<br>参数含义：拓扑标识。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为0。<br>默认值：无<br>配置原则：目前只支持默认拓扑0。 |
| CONFIGCOST | 使能度量 | 可选必选说明：可选参数<br>参数含义：使能缺省路由度量值。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- FALSE：不使能。<br>- TRUE：使能。<br>默认值：无 |
| COST | 外部LSA开销值 | 可选必选说明：条件必选参数<br>前提条件：该参数在“CONFIGCOST”配置为“TRUE”时为必选参数。<br>参数含义：ASE LSA的开销值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～16777214。<br>默认值：无<br>配置原则：<br>- 到第一类外部路由的开销值＝本设备到相应的ASBR的开销值＋ASBR到该路由目的地址的开销值。<br>- 到第二类外部路由的开销值＝ASBR到该路由目的地址的开销值。<br>- 如果不配置此参数，则实际取值为1。 |
| CONFIGTYPE | 缺省路由使能类型 | 可选必选说明：可选参数<br>参数含义：缺省路由使能类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- FALSE：不使能。<br>- TRUE：使能。<br>默认值：无 |
| ROUTETYPE | 引入外部路由类型 | 可选必选说明：条件必选参数<br>前提条件：该参数在“CONFIGTYPE”配置为“TRUE”时为必选参数。<br>参数含义：引入外部路由类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- Type1：外部路由类型1。<br>- Type2：外部路由类型2。<br>默认值：无<br>配置原则：如果不配置此参数，则实际取值为Type2。 |
| DELAYTIMER | 延迟发布聚合路由的时间（s） | 可选必选说明：可选参数<br>参数含义：发布延迟时间。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～65535，单位是秒。<br>默认值：无 |
| CONFIGFLAG | 默认路由发布标志 | 可选必选说明：可选参数<br>参数含义：指定默认路由发布模式。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DefRtAdv：用于引入外部路由的缺省路由，引入其他协议产生的缺省路由并发布到整个普通OSPF区域。<br>- Always：无论本机是否存在激活的非本OSPF进程的缺省路由，都会产生并发布一个描述缺省路由的LSA。<br>- Summary：发布指定缺省路由的Type 3 summary LSA。<br>默认值：无 |
| PERMCALCOTHER | 计算默认路由 | 可选必选说明：可选参数<br>参数含义：计算默认路由。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：无<br>配置原则：如果没有配置PERMCALCOTHER参数，也没有配置CONFIGFLAG参数为Always，则：本机存在激活的非OSPF缺省路由，则设备不再计算来自其他设备的缺省路由；本机不存在激活的非OSPF缺省路由，则设备仍然计算来自于其他设备的缺省路由。 |
| ROUTEPOLICYNAME | 路由策略 | 可选必选说明：可选参数<br>参数含义：路由策略名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～200。<br>默认值：无<br>配置原则：<br>- 输入单空格将删除该参数已有配置项。<br>- 区分大小写。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/OSPFDEFAULTROUTE]] · OSPF默认宣告路由配置（OSPFDEFAULTROUTE）

## 使用实例

修改OSPF进程1的缺省路由Cost值为100：

```
MOD OSPFDEFAULTROUTE:PROCID=1,TOPOID=0,CONFIGCOST=TRUE,COST=100;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改OSPF默认宣告路由配置（MOD-OSPFDEFAULTROUTE）_50121834.md`
