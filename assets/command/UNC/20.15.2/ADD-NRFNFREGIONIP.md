---
id: UNC@20.15.2@MMLCommand@ADD NRFNFREGIONIP
type: MMLCommand
name: ADD NRFNFREGIONIP（增加IP与NF区域映射关系配置）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: NRFNFREGIONIP
command_category: 配置类
applicable_nf:
- NRF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- NRF业务参数
- NF区域与IP映射关系配置管理
status: active
---

# ADD NRFNFREGIONIP（增加IP与NF区域映射关系配置）

## 功能

**适用NF：NRF**

该命令用于增加IP与NF区域的映射关系，用于在NF发现过程中，根据发现消费者与生产者的区域关系来执行对应的发现策略判断。

## 注意事项

- 该命令执行后立即生效。

- 最多可输入1024条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPTYPE | IP类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定NF客户端地址的IP类型。<br>数据来源：本端规划<br>取值范围：<br>- IPV4（IPv4地址）<br>- IPV6（IPv6地址）<br>默认值：无<br>配置原则：无 |
| IPV4 | IPv4地址 | 可选必选说明：该参数在"IPTYPE"配置为"IPV4"时为条件必选参数。<br>参数含义：该参数用于表示NF客户端的IPv4地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无 |
| IPV6 | IPv6地址 | 可选必选说明：该参数在"IPTYPE"配置为"IPV6"时为条件必选参数。<br>参数含义：该参数用于表示NF的客户端IPv6地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |
| NFREGION | NF归属区域 | 可选必选说明：必选参数<br>参数含义：该参数用于表示NF归属区域。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~36。该字段大小写不敏感 。<br>默认值：无<br>配置原则：<br>NF归属区域由运营商规划。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NRFNFREGIONIP]] · IP与NF区域映射关系配置（NRFNFREGIONIP）

## 使用实例

针对OCS已经打开区域关系精确匹配开关（SET NRFDISCREGNRULE的REGNEXTMACSW取为FUNC_ON）。 增加发现请求CHF的客户端IP和NF区域映射关系。CHF发现OCS过程中，NRF会根据请求IP映射到CHF的区域。如果CHF与OCS同区域，则发现结果响应大包，否则响应小包。

```
ADD NRFNFREGIONIP: IPTYPE=IPV4, IPV4="10.10.10.10", NFREGION="ff";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加IP与NF区域映射关系配置（ADD-NRFNFREGIONIP）_24796804.md`
