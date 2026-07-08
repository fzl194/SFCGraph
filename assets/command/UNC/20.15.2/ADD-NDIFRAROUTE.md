---
id: UNC@20.15.2@MMLCommand@ADD NDIFRAROUTE
type: MMLCommand
name: ADD NDIFRAROUTE（增加接口上ND RA路由配置信息）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: NDIFRAROUTE
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
max_records: 17
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP协议栈
- IPv6管理
- IPv6 ND RA路由信息
status: active
---

# ADD NDIFRAROUTE（增加接口上ND RA路由配置信息）

## 功能

该命令用于增加IPv6接口上RA路由配置信息。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为17。
- 执行该命令行前需要先在接口使能IPv6。
- 接口名称可以通过LST INTERFACE命令获取。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IFNAME | 接口名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定接口名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：请使用LST INTERFACE命令查看可用接口。 |
| PREFIX | IPv6地址前缀 | 可选必选说明：必选参数<br>参数含义：该参数用于指定IPv6地址前缀。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。<br>默认值：无 |
| PREFIXLENGTH | 前缀长度 | 可选必选说明：必选参数<br>参数含义：该参数用于指定前缀长度。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为0～128。<br>默认值：无 |
| LIFETIME | 路由存活时间（s） | 可选必选说明：必选参数<br>参数含义：该参数用于指定路由存活时间。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295，单位是秒。<br>默认值：无 |
| PREFERENCE | 路由器优先级 | 可选必选说明：可选参数<br>参数含义：该参数用于指定路由器优先级。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- LOW：低优先级。<br>- MEDIUM：中优先级。<br>- HIGH：高优先级。<br>默认值：MEDIUM |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NDIFRAROUTE]] · 接口上ND RA路由配置信息（NDIFRAROUTE）

## 使用实例

增加接口上ND RA路由配置信息：

```
ADD NDIFRAROUTE: IFNAME="Ethernet65/0/8",PREFIX="2001:db8::11",PREFIXLENGTH=70,LIFETIME=888,PREFERENCE=LOW;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-NDIFRAROUTE.md`
