---
id: UDG@20.15.2@MMLCommand@ADD IPFARM
type: MMLCommand
name: ADD IPFARM（增加IPFarm）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: IPFARM
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 3600
category_path:
- 用户面服务管理
- DN管理
- IP Farm 管理
- IP Farm参数
status: active
---

# ADD IPFARM（增加IPFarm）

## 功能

**适用NF：PGW-U、UPF**

该命令用于配置重定向或p-cscf类型的IP farm。IP farm是若干个相同VPN的server集合。IP farm可以用于重定向，或p-cscf的连接状态检测机制。重定向类型的IP farm应用于captive portal动作，在动作执行时，会基于SET IPFARMGLOBAL配置的负荷分担模式选择状态正常的IP farm服务器作为重定向的目的服务器。p-cscf类型的IP farm主要用于检测PcscfGroup中各p-cscf的连接状态。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为3600。当配置记录数大于规格的90%时，会上报“ALM-135602215 配置数量超阈值”告警。当配置记录数小于等于配置规格90%时，恢复“ALM-135602215 配置数量超阈值”告警。阈值可以通过MOD CFGTHRESHOLD命令修改。
- 不允许将同一个virtual IP配置到不同的IP farm上，virtual IP与IP farm要唯一对应。
- IP farm支持IPv4和IPv6两种IP类型。当同一服务器支持双栈接入时，需要配置为两个IP farm，其中一个提供IPv4接入，另一个提供IPv6接入。
- 在不使能心跳检测时，IP farm下配置的参数VPN也需要和用户的vpn保持一致。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPFARMNAME | IP-Farm名称 | 可选必选说明：必选参数<br>参数含义：该参数用于设置IP farm名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| IPVERSION | IP协议版本 | 可选必选说明：必选参数<br>参数含义：该参数用于设置IP地址类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- IPV4：IPv4地址类型。<br>- IPV6：IPv6地址类型。<br>默认值：无<br>配置原则：无 |
| SERVERTYPE | 服务器类型 | 可选必选说明：可选参数<br>参数含义：该参数用于设置IP farm服务器类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- REDIRECT：指定为重定向。<br>- PCSCF：指定为P-CSCF。<br>- IPMS：指定为IPMS Server。<br>默认值：REDIRECT<br>配置原则：<br>- 如果运营商需要使用重定向或p-cscf的连接状态检测功能，需要配置该参数。<br>- 如果运营商需要使用重定向功能，则配置为REDIRECT。<br>- 如果运营商需要使用p-cscf的连接状态检测功能，则配置为PCSCF。 |
| VPNINSTANCE | VPN实例 | 可选必选说明：可选参数<br>参数含义：该参数用于设置VPN名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD VPNINST命令配置生成。 |
| HEALTHCHECKFLAG | 健康检查标记 | 可选必选说明：可选参数<br>参数含义：该参数用于设置健康检查标记。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能（关闭）。<br>- ENABLE：使能（开启）。<br>默认值：ENABLE<br>配置原则：<br>- 如果运营商需要使用IP Farm下的心跳检测功能，则需要配置该参数。<br>- 如果运营商希望开启心跳检测功能，则需要打开此开关，配置为ENABLE。<br>- 如果运营商希望关闭心跳检测功能，则需要关闭此开关，配置为DISABLE。 |
| VIRTUALIP | 虚拟IP地址 | 可选必选说明：条件可选参数<br>前提条件：该参数在“IPVERSION”配置为“IPV4”时为可选参数。<br>参数含义：该参数用于设置IP farm对应的虚拟IPv4地址，通过该虚拟IP地址关联到唯一的IP farm。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。采用点分十进制"X.X.X.X"格式。<br>默认值：无<br>配置原则：如果运营商需要使用FUI重定向功能，可能需要配置该参数。 |
| VIRTUALIPV6 | 虚拟IPv6地址 | 可选必选说明：条件可选参数<br>前提条件：该参数在“IPVERSION”配置为“IPV6”时为可选参数。<br>参数含义：该参数用于设置IP farm对应的虚拟IPv6地址，通过该虚拟IP地址关联到唯一的IP farm。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。采用冒号分十六进制X:X:X:X:X:X:X:X格式。<br>默认值：无<br>配置原则：如果运营商需要使用FUI重定向功能，可能需要配置该参数。 |
| INTERFACENAME | 心跳检测接口名称 | 可选必选说明：条件必选参数<br>前提条件：该参数在“HEALTHCHECKFLAG”配置为“ENABLE”时为必选参数。<br>可选必选说明：条件可选参数<br>前提条件：该参数在“HEALTHCHECKFLAG”配置为“DISABLE”时为可选参数。<br>参数含义：该参数用于设置心跳检测接口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：逻辑接口类型必须是phif。 |
| WPSELECTMODE | Web Proxy服务器选择模式 | 可选必选说明：条件可选参数<br>前提条件：该参数在“SERVERTYPE”配置为“REDIRECT”时为可选参数。<br>参数含义：该参数用于设置Web Proxy重定向类型IP farm服务器选择模式。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- INHERIT：继承全局软参BIT596和BIT1541的设置。<br>- SESSION_BASED：基于用户会话粒度选择不同的重定向服务器。<br>- FLOW_BASED：基于流粒度选择不同的重定向服务器。<br>默认值：INHERIT<br>配置原则：<br>- 如果是多流关联的业务，推荐配置SESSION_BASED。<br>- 如果业务流之间无关联关系，推荐配置FLOW_BASED。 |
| WPCONFLICTACT | Web Proxy服务器地址冲突动作 | 可选必选说明：条件可选参数<br>前提条件：该参数在“SERVERTYPE”配置为“REDIRECT”时为可选参数。<br>参数含义：该参数用于设置Web Proxy无法选到可用server时的缺省动作。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- BLOCK：Web Proxy无法选到可用server时，报文阻塞。<br>- PASS：Web Proxy无法选到可用server时，报文通过。<br>默认值：BLOCK<br>配置原则：<br>- 如果proxy server用于鉴权或分流，则建议配置为BLOCK。<br>- 如果proxy server仅用于业务加速，则建议配置为PASS。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/IPFARM]] · IPFarm（IPFARM）

## 关联任务

- [[UDG@20.15.2@Task@0-00087]]

## 使用实例

假设需要新增一个IPv4类型的IP farm，名字为test，虚拟地址为10.0.0.1，关闭心跳检测功能，做重定向业务，则按如下命令配置：

```
ADD IPFARM: IPFARMNAME="test", IPVERSION=IPV4, HEALTHCHECKFLAG=DISABLE, VIRTUALIP="10.0.0.1";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/ADD-IPFARM.md`
