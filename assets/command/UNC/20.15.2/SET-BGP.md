---
id: UNC@20.15.2@MMLCommand@SET BGP
type: MMLCommand
name: SET BGP（设置BGP）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: BGP
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- BGP管理
- 设置BGP
status: active
---

# SET BGP（设置BGP）

## 功能

![](设置BGP（SET BGP）_00866001.assets/notice_3.0-zh-cn_2.png)

操作不当会去使能BGP，导致BGP功能不可用，并且所有历史BGP配置全部删除，请谨慎使用并联系华为技术支持协助操作。

该命令用于创建BGP协议并设置BGP协议参数。BGP是一种外部网关协议（EGP），与OSPF等内部网关协议（IGP）不同，其着眼点不在于发现和计算路由，而在于在AS之间选择最佳路由和控制路由的传播。BGP协议默认不开启认证，认证需要手动开启，否则会有风险。

## 注意事项

- 该命令执行后立即生效。
- 该命令参数GRACEFULRESTART 、BGPRIDAUTOSEL会导致BGP邻居复位。
- 新创建BGP必须至少配置ASNUM和BGPENABLE（取值为TRUE）两个参数。
- 如果去使能BGP，BGP进程将被删除。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| BGPENABLE | GRACEFULRESTART | TIMEWAITFORRIB | CONFEDNONSTANDED | CHECKFIRSTAS | BGPRIDAUTOSEL | KEEPALLROUTES | MEMORYLIMIT | GRPEERRESET | ISSHUTDOWN |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FALSE | FALSE | 600 | FALSE | TRUE | FALSE | FALSE | FALSE | FALSE | FALSE |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| BGPENABLE | 使能BGP | 可选必选说明：必选参数<br>参数含义：该参数用于使能BGP。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- FALSE：不使能。<br>- TRUE：使能。<br>默认值：无 |
| ASNUM | BGP自治域号 | 可选必选说明：条件可选参数<br>前提条件：该参数在“BGPENABLE”配置为“TRUE”时为可选参数。<br>参数含义：该参数用于指定BGP所在AS域。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～11。取值范围是number<1-4294967295>或者number<1-65535>.number<0-65535>。<br>默认值：无<br>配置原则：<br>- 输入单空格将删除该参数已有配置项。<br>- 此参数在使能BGP时必须配置。如需修改，需要先去使能再重新进行配置。修改已创建的BGP其它参数时，此参数可以不携带。 |
| GRACEFULRESTART | 使能GR能力 | 可选必选说明：条件可选参数<br>前提条件：该参数在“BGPENABLE”配置为“TRUE”时为可选参数。<br>参数含义：该参数用于表明是否使能GR能力。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：无 |
| TIMEWAITFORRIB | RIB结束时间（s） | 可选必选说明：条件可选参数<br>前提条件：该参数在“BGPENABLE”配置为“TRUE”时为可选参数。<br>参数含义：该参数指定重启时等待End-Of-Rib标记的时间。当建立或重建BGP会话时，应在此命令设置的时间内收到End-Of-RIB标记，如果收不到End-Of-RIB标记，则退出GR过程，从现有路由中选取最佳路由。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为3～3000，单位是秒。<br>默认值：无<br>配置原则：当GRACEFULRESTART配置为TRUE时，才能配置该命令。 |
| ASPATHLIMIT | 自治域路径上限 | 可选必选说明：条件可选参数<br>前提条件：该参数在“BGPENABLE”配置为“TRUE”时为可选参数。<br>参数含义：该参数设置AS Path属性中AS号的最大个数。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～2000。<br>默认值：无<br>配置原则：该命令会对所有BGP路由生效，在BGP路由属性AS数量超限的情况下会造成路由丢失，但是可以保护邻居不断连，实现网络稳定性。当配置成0时，当前配置被删除。 |
| CONFEDIDNUMBER | 联盟ID | 可选必选说明：条件可选参数<br>前提条件：该参数在“BGPENABLE”配置为“TRUE”时为可选参数。<br>参数含义：该参数设置BGP联盟的联盟ID。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～11。取值范围是number<1-4294967295>或者number<1-65535>.number<0-65535>。<br>默认值：无<br>配置原则：<br>- 输入单空格将删除该参数已有配置项。<br>- 联盟ID相当于整个自治系统的编号，其他相关外部AS在指定对等体所在的AS号时，要指定这个联盟ID。属于同一个联盟的所有子自治系统都必须指定相同的联盟ID。 |
| CONFEDNONSTANDED | 使能联盟 | 可选必选说明：条件可选参数<br>前提条件：该参数在“BGPENABLE”配置为“TRUE”时为可选参数。<br>参数含义：该参数用于指定是否与非标准的AS联盟兼容。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：无<br>配置原则：为了同采用非标准的设备互通，必须对联盟中所有路由器配置该命令。 |
| CHECKFIRSTAS | 使能检查第一个自治域号 | 可选必选说明：条件可选参数<br>前提条件：该参数在“BGPENABLE”配置为“TRUE”时为可选参数。<br>参数含义：该参数指定是否检查EBGP对等体发来的更新消息中AS_Path属性的第一个AS号。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：无 |
| BGPRIDAUTOSEL | 使能VPN路由器的ID为自动选择 | 可选必选说明：条件可选参数<br>前提条件：该参数在“BGPENABLE”配置为“TRUE”时为可选参数。<br>参数含义：该参数指定是否设置BGP路由器自动选择Router ID。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：无 |
| KEEPALLROUTES | 使能全部路由 | 可选必选说明：条件可选参数<br>前提条件：该参数在“BGPENABLE”配置为“TRUE”时为可选参数。<br>参数含义：该参数指定是否保存自BGP连接建立起来之后的所有来自指定对等体（组）的BGP路由更新信息，即使这些路由没有通过已配置的入口策略。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：无 |
| MEMORYLIMIT | 启用内存限制的前缀 | 可选必选说明：条件可选参数<br>前提条件：该参数在“BGPENABLE”配置为“TRUE”时为可选参数。<br>参数含义：该参数指定是否使能BGP内存保护，即当内存占用率达到过载阈值时，不再接收邻居发来的BGP路由，并生成日志。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：无 |
| GRPEERRESET | 使能GR能力重置BGP连接 | 可选必选说明：条件可选参数<br>前提条件：该参数在“BGPENABLE”配置为“TRUE”时为可选参数。<br>参数含义：该参数指配置路由器以GR方式复位BGP连接。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：无<br>配置原则：当GRACEFULRESTART为TRUE时，才可配置GRPEERRESET为TRUE。 |
| ISSHUTDOWN | 中断BGP对等体协议会话 | 可选必选说明：条件可选参数<br>前提条件：该参数在“BGPENABLE”配置为“TRUE”时为可选参数。<br>参数含义：该参数指定是否中断BGP对等体协议会话。使能此参数会中断所有BGP对等体的协议会话，请务必慎重使用。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：无 |

## 操作的配置对象

- [BGP（BGP）](configobject/UNC/20.15.2/BGP.md)

## 使用实例

使能AS号为100的BGP：

```
SET BGP:ASNUM="100", BGPENABLE=TRUE;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置BGP（SET-BGP）_00866001.md`
