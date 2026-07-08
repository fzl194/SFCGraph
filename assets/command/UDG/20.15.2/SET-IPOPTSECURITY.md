---
id: UDG@20.15.2@MMLCommand@SET IPOPTSECURITY
type: MMLCommand
name: SET IPOPTSECURITY（设置IP选项安全配置）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: IPOPTSECURITY
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP协议栈
- IPv4管理
- IP选项安全配置
status: active
---

# SET IPOPTSECURITY（设置IP选项安全配置）

## 功能

该命令用于设置带路由选项的IP报文的安全配置。

通常情况下带路由选项的IP报文用于网络路径的故障诊断和特殊业务的临时传送。但是路由选项可能被网络攻击者利用，探测网络结构并发动攻击。所以需要利用命令行控制系统是否处理这些带路由选项的IP报文。

缺省情况下，设备处理带路由选项的IP报文。当为了防止针对这种报文的攻击时，可以去使能系统处理带路由选项IP报文的功能。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| OPTIONTYPE | IP选项类型 | 可选必选说明：必选参数<br>参数含义：该参数表示IP选项的类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- routeAlert：系统处理带路由告警选项IP报文的功能。<br>- routeRecord：系统处理带记录路由选项IP报文的功能。<br>- sourceRoute：系统处理带源路由选项IP报文的功能。该选项控制报文传输路径。<br>- timeStamp：系统处理带记录时间戳选项IP报文的功能。该选项用于计算报文传输/处理时消耗的时间。<br>默认值：无 |
| SWITCHOP | IP选项配置开关 | 可选必选说明：必选参数<br>参数含义：该参数表示使能或去使能对应选项报文的处理能力。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- disable：去使能。<br>- enable：使能。<br>默认值：无 |

## 操作的配置对象

- [IP选项安全配置（IPOPTSECURITY）](configobject/UDG/20.15.2/IPOPTSECURITY.md)

## 使用实例

使能系统处理带路由选项IP报文的功能：

```
SET IPOPTSECURITY: OPTIONTYPE=routeRecord, SWITCHOP=enable;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置IP选项安全配置（SET-IPOPTSECURITY）_00865745.md`
