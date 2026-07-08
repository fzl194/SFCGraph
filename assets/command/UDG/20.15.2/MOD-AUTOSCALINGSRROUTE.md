---
id: UDG@20.15.2@MMLCommand@MOD AUTOSCALINGSRROUTE
type: MMLCommand
name: MOD AUTOSCALINGSRROUTE（修改静态路由自动化配置模板）
nf: UDG
version: 20.15.2
verb: MOD
object_keyword: AUTOSCALINGSRROUTE
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 自动部署
- 静态路由自动化配置
status: active
---

# MOD AUTOSCALINGSRROUTE（修改静态路由自动化配置模板）

## 功能

该命令用于修改静态路由自动化配置模板。

## 注意事项

- 该命令执行后立即生效。
- 修改该静态路由自动化配置模板时，要保证该模板添加过。
- 如果地址族取值为IPv4，则路由掩码长度取值范围为0到32，如果地址族取值为IPv6，则路由掩码长度取值范围为0到128。
- 该命令在自动化配置开关为关闭的状态下才能执行，请先使用SET AUTOCONFIG命令关闭自动配置开关；生效配置，需要再次使用SET AUTOCONFIG命令开启自动配置开关。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SERVICENAME | 服务名称 | 可选必选说明：必选参数<br>参数含义：该参数用来表示接口自动化配置服务模板名称。要求和ADD AUTOSCALINGSERVICE命令中配置的SERVICENAME参数保持一致。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格和中文。<br>默认值：无 |
| VRFNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用来指定VPN实例的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格和中文。<br>默认值：无<br>配置原则：<br>- 输入单空格将删除该参数已有配置项。<br>- 不配置时默认为_public_。<br>- _public_表示公网。<br>- 该参数不支持修改。 |
| IPVERSION | 地址族 | 可选必选说明：必选参数<br>参数含义：该参数用来指定VPN实例的地址族信息。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- IPv4：IPv4地址族。<br>- IPv6：IPv6地址族。<br>默认值：无<br>配置原则：该参数不支持修改。 |
| PREFIX4 | 路由前缀IPv4 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IPVERSION”配置为“IPv4”时为必选参数。<br>参数含义：该参数用来指定IPv4前缀信息。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：该参数不支持修改。 |
| PREFIX6 | 路由前缀IPv6 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IPVERSION”配置为“IPv6”时为必选参数。<br>参数含义：该参数用来指定IPv6前缀信息。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：该参数不支持修改。 |
| MASKLENGTH | 路由掩码长度 | 可选必选说明：必选参数<br>参数含义：IPv4场景，该参数用于表示路由的掩码长度；IPv6场景，该参数用于表示路由的前缀长度。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～128。<br>默认值：无<br>配置原则：该参数不支持修改。 |
| NEXTHOPALLOCTYPE4 | IPv4路由下一跳分配方式 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IPVERSION”配置为“IPv4”时为必选参数。<br>参数含义：该参数用于指定IPv4路由下一跳的获取方式。用户配置方式是指用户配置静态路由的下一跳；DHCP方式是指静态路由下一跳支持DHCP联动。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- CONFIG：用户配置方式。<br>- DHCP：DHCP分配方式。<br>默认值：无<br>配置原则：该参数不支持修改。 |
| NEXTHOPALLOCTYPE6 | IPv6路由下一跳分配方式 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IPVERSION”配置为“IPv6”时为必选参数。<br>参数含义：该参数用于指定IPv6路由下一跳的获取方式。用户配置方式是指用户配置静态路由的下一跳；DHCP方式是指静态路由下一跳支持DHCP联动。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- CONFIG：用户配置方式。<br>- DHCP：DHCP分配方式。<br>默认值：无<br>配置原则：该参数不支持修改。 |
| NEXTHOP4 | 路由下一跳IPv4 | 可选必选说明：条件必选参数<br>前提条件：该参数在“NEXTHOPALLOCTYPE4”配置为“CONFIG”时为必选参数。<br>参数含义：该参数用来指定IPv4下一跳IP地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：该参数不支持修改。 |
| NEXTHOP6 | 路由下一跳IPv6 | 可选必选说明：条件必选参数<br>前提条件：该参数在“NEXTHOPALLOCTYPE6”配置为“CONFIG”时为必选参数。<br>参数含义：该参数用来指定IPv6下一跳IP地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：该参数不支持修改。 |
| PREFERENCE | 路由优先级 | 可选必选说明：可选参数<br>参数含义：该参数用来指定路由优先级。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～255。<br>默认值：无 |
| BFDENABLE | BFD使能标识 | 可选必选说明：可选参数<br>参数含义：BFD使能标识。为静态路由模板使能BFD，若使能静态路由动态BFD则依赖ADD AUTOSCALINGSRBFD命令配置，若使能静态路由静态BFD，则依赖ADD AUTOSCALINGBFD命令且配置BFDTYPE为Static。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- FALSE：否。<br>- TRUE：是。<br>默认值：无 |
| TAG | 路由tag | 可选必选说明：可选参数<br>参数含义：该参数用来指定路由的tag。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无 |
| DESCRIPTION | 路由描述 | 可选必选说明：可选参数<br>参数含义：该参数用来指定路由的描述信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～35。不支持中文。<br>默认值：无<br>配置原则：输入单空格将删除该参数已有配置项。 |
| BFDTEMPLATENAME | BFD模板名称 | 可选必选说明：条件可选参数<br>前提条件：该参数在“BFDENABLE”配置为“TRUE”时为可选参数。<br>参数含义：该参数用来指定BFD自动化配置模板名称。该参数由ADD AUTOSCALINGBFD命令配置获得。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～59。不支持空格和中文。<br>默认值：无<br>配置原则：输入单空格将删除该参数已有配置项。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@AUTOSCALINGSRROUTE]] · 静态路由自动化配置模板（AUTOSCALINGSRROUTE）

## 使用实例

- 修改一个IPv4的静态路由自动化配置模板：
  ```
  MOD AUTOSCALINGSRROUTE:SERVICENAME="abc",IPVERSION=IPv4,PREFIX4="192.168.0.1",MASKLENGTH=32,VRFNAME="_public_",NEXTHOPALLOCTYPE4=CONFIG,NEXTHOP4="192.168.0.3",BFDENABLE=TRUE,DESCRIPTION="DPU STATIC ROUTE";
  ```
- 修改一个IPv6的静态路由自动化配置模板：
  ```
  MOD AUTOSCALINGSRROUTE:SERVICENAME="service1",NEXTHOPALLOCTYPE6=CONFIG,IPVERSION=IPv6,PREFIX6="2001:DB8::1",MASKLENGTH=64,VRFNAME="_public_",NEXTHOP6="2001:DB8::10",BFDENABLE=TRUE,DESCRIPTION="modified";
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/MOD-AUTOSCALINGSRROUTE.md`
