---
id: UNC@20.15.2@MMLCommand@ADD IPOPTSECURITYIF
type: MMLCommand
name: ADD IPOPTSECURITYIF（增加接口IP选项安全配置）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: IPOPTSECURITYIF
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
max_records: 65535
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP协议栈
- IPv4管理
- 接口下IP选项安全配置
status: active
---

# ADD IPOPTSECURITYIF（增加接口IP选项安全配置）

## 功能

该命令用于添加指定接口上带路由选项的IP报文的安全配置。接口名称可以通过LST INTERFACE命令获取。

通常情况下带路由选项的IP报文用于网络路径的故障诊断和特殊业务的临时传送。但是路由选项可能被网络攻击者利用，探测网络结构并发动攻击。缺省情况下，设备处理带路由选项的IP报文。为了防止针对这种报文的攻击，可以使用该命令去使能系统处理带路由选项IP报文的功能。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为65535。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| OPTIONTYPE | IP选项类型 | 可选必选说明：必选参数<br>参数含义：该参数表示IP选项的类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- routeAlert：系统处理带路由告警选项IP报文的功能。<br>- routeRecord：系统处理带记录路由选项IP报文的功能。<br>- sourceRoute：系统处理带源路由选项IP报文的功能。该选项控制报文传输路径。<br>- timeStamp：系统处理带记录时间戳选项IP报文的功能。该选项用于计算报文传输/处理时消耗的时间。<br>默认值：无 |
| SWITCHOP | IP选项配置开关 | 可选必选说明：必选参数<br>参数含义：该参数表示使能或去使能对应选项报文的处理能力。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- disable：去使能。<br>- enable：使能。<br>默认值：无 |
| IFNAME | 接口名称 | 可选必选说明：必选参数<br>参数含义：该参数用于表示接口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。接口名称由接口类型+接口编号组成。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/IPOPTSECURITYIF]] · 接口IP选项安全配置（IPOPTSECURITYIF）

## 使用实例

添加记录路由选项routeRecord的配置实例：

```
ADD IPOPTSECURITYIF: OPTIONTYPE=routeRecord, SWITCHOP=enable, IFNAME="Ethernet66/0/4";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-IPOPTSECURITYIF.md`
