---
id: UNC@20.15.2@MMLCommand@RMV NRFIPWHITELST
type: MMLCommand
name: RMV NRFIPWHITELST（删除NF IP白名单）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: NRFIPWHITELST
command_category: 配置类
applicable_nf:
- NRF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- NRF业务参数
- NF IP白名单管理
status: active
---

# RMV NRFIPWHITELST（删除NF IP白名单）

## 功能

![](删除NF IP白名单（RMV NRFIPWHITELST）_75909313.assets/notice_3.0-zh-cn_2.png)

客户端IP在被删除的IP段内的NF将无法正常注册、去注册、更新以及维持到NRF的心跳。

**适用NF：NRF**

该命令用于删除NF IP白名单内的IP段。

客户端IP在被删除的IP段内的NF将无法正常注册、去注册、更新以及维持到NRF的心跳。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPTYPE | IP类型 | 可选必选说明：必选参数<br>参数含义：该参数表示NF IP白名单内的IP段类型。<br>数据来源：本端规划<br>取值范围：<br>- IPV4（IPv4地址）<br>- IPV6（IPv6地址）<br>默认值：无<br>配置原则：无 |
| IPV4START | IPV4地址起始 | 可选必选说明：该参数在"IPTYPE"配置为"IPV4"时为条件必选参数。<br>参数含义：该参数表示NF IP白名单内的IPV4类型IP段起始值。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：<br>IPV4地址起始值必须小于等于IPV4地址结束值。 |
| IPV4END | IPV4地址结束 | 可选必选说明：该参数在"IPTYPE"配置为"IPV4"时为条件必选参数。<br>参数含义：该参数表示NF IP白名单内的IPV4类型IP段结束值。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无 |
| IPV6START | IPv6起始地址 | 可选必选说明：该参数在"IPTYPE"配置为"IPV6"时为条件必选参数。<br>参数含义：该参数表示NF IP白名单内的IPV6类型IP段起始值。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：<br>IPv6起始地址必须小于等于IPV6结束地址。 |
| IPV6END | IPV6结束地址 | 可选必选说明：该参数在"IPTYPE"配置为"IPV6"时为条件必选参数。<br>参数含义：该参数表示NF IP白名单内的IPV6类型IP段结束值。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NRFIPWHITELST]] · NF IP白名单（NRFIPWHITELST）

## 使用实例

将IP地址类型为IPV4，且IPV4地址起始值为10.1.1.1，IPV4地址结束为10.7.7.7的地址段从IP白名单中删除，执行如下命令：

```
RMV NRFIPWHITELST: IPTYPE=IPV4, IPV4START="10.1.1.1", IPV4END="10.7.7.7";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-NRFIPWHITELST.md`
