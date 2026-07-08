# 增加IP可达性检测自动化配置模板（ADD AUTOSCALINGIPREACH）

- [命令功能](#ZH-CN_CONCEPT_0000001600840617__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000001600840617__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000001600840617__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000001600840617__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000001600840617__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0000001600840617)

该命令用于添加IP可达性检测自动化配置模板，该模板自动化生成RU到网关的可达性检测配置。

#### [注意事项](#ZH-CN_CONCEPT_0000001600840617)

- 该命令执行后立即生效。
- 该命令最大记录数为64。
- 执行该命令前要保证通过ADD AUTOSCALINGBFD已配置指定的BFD自动化配置模板。
- 当引用参数SERVICENAME时，该参数由LST AUTOSCALINGSERVICE获取。
- 该命令在自动化配置开关为关闭的状态下才能执行，请先使用SET AUTOCONFIG命令关闭自动配置开关；生效配置，需要再次使用SET AUTOCONFIG命令开启自动配置开关。

#### [操作用户权限](#ZH-CN_CONCEPT_0000001600840617)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000001600840617)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SERVICENAME | 服务名称 | 可选必选说明：必选参数<br>参数含义：该参数用来表示接口自动化配置服务模板名称。该参数由ADD AUTOSCALINGSERVICE命令配置获得。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格和中文。<br>默认值：无 |
| IPVERSION | IP版本 | 可选必选说明：必选参数<br>参数含义：该参数用来表示IP版本。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- IPv4：IPv4地址族。<br>- IPv6：IPv6地址族。<br>默认值：IPv4 |
| DESTADDR4 | 目的地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IPVERSION”配置为“IPv4”时为必选参数。<br>参数含义：该参数用于表示对端网关的IPv4地址。<br>数据来源：对端协商<br>取值范围：IPv4地址类型。<br>默认值：无 |
| DESTADDR6 | 目的地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IPVERSION”配置为“IPv6”时为必选参数。<br>参数含义：该参数用于表示对端网关的IPv6地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。<br>默认值：无 |
| BFDTEMPLATENAME | BFD自动化配置模板名称 | 可选必选说明：必选参数<br>参数含义：该参数用来表示可达性检测需要联动的BFD自动化配置模板名称。该参数通过ADD AUTOSCALINGBFD命令配置获得。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～59。不支持空格和中文。<br>默认值：无 |

#### [使用实例](#ZH-CN_CONCEPT_0000001600840617)

增加一个IP可达性检测自动化配置模板：

```
ADD AUTOSCALINGIPREACH: SERVICENAME="service1",IPVERSION=IPv4,DESTADDR4="10.1.1.1",BFDTEMPLATENAME="bfdtemp1";
```
