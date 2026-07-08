---
id: UNC@20.15.2@MMLCommand@MOD NFABILITY
type: MMLCommand
name: MOD NFABILITY（修改配置NF的能力信息）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: NFABILITY
command_category: 配置类
applicable_nf:
- NRF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- 对端NF管理
- NF信息管理
- NF能力信息管理
status: active
---

# MOD NFABILITY（修改配置NF的能力信息）

## 功能

**适用NF：NRF**

该命令用于修改配置NF的能力信息。

## 注意事项

- 该命令执行后立即生效。

- 主备或双活组网的场景下，如果需要配置此命令，则两个NRF上均需执行此命令，且配置参数一致。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFIDTYPE | NF标识类型 | 可选必选说明：必选参数<br>参数含义：该参数用于表示NF标识类型。<br>数据来源：全网规划<br>取值范围：<br>- NF_ID（NF实例标识）<br>- NF_IP（NF IP地址）<br>默认值：无<br>配置原则：无 |
| IPTYPE | IP类型 | 可选必选说明：该参数在"NFIDTYPE"配置为"NF_IP"时为条件必选参数。<br>参数含义：该参数用于指定NF的客户端地址的IP类型。<br>数据来源：全网规划<br>取值范围：<br>- IPV4（IPv4地址）<br>- IPV6（IPv6地址）<br>默认值：无<br>配置原则：无 |
| NFINSTANCEID | NF实例标识 | 可选必选说明：该参数在"NFIDTYPE"配置为"NF_ID"时为条件必选参数。<br>参数含义：该参数用于表示NF实例标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~40。该参数只能由字母（A-Z或者a-z）、数字（0-9）、中划线（-）组成。不区分大小写。<br>默认值：无<br>配置原则：无 |
| IPV4 | IPv4地址 | 可选必选说明：该参数在"IPTYPE"配置为"IPV4"时为条件必选参数。<br>参数含义：该参数用于表示NF的客户端IPv4地址。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无 |
| IPV6 | IPv6地址 | 可选必选说明：该参数在"IPTYPE"配置为"IPV6"时为条件必选参数。<br>参数含义：该参数用于表示NF的客户端IPv6地址。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |
| ABILITY | NF支持的能力 | 可选必选说明：可选参数<br>参数含义：该参数用于表示NF支持的能力。<br>数据来源：全网规划<br>取值范围：<br>- “INCCACHE（增量构建缓存）”：代表NF支持增量缓存能力。增量缓存能力是指NF侧在缓存有效期内针对同一个生产者NF的多次发现结果的部分Profile信息进行累加。<br>- “NOCACHE（无缓存）”：代表NF不具备缓存能力。<br>默认值：无<br>配置原则：<br>当NF配置为增量构建缓存（INCCACHE）时，此时需与SET NRFFUNCSW的DISCFILTEREXSW参数进行配合使用，详细请参考DISCFILTEREXSW参数说明。<br>当NF配置为无缓存能力（NOCACHE）时，针对该NF发起的服务发现时返回精确匹配报文。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NFABILITY]] · 配置NF的能力信息（NFABILITY）

## 使用实例

运营商网络规划变更时，运营商希望在NRF上修改NF实例标识为123e4567-e89b-12d3-a456-426655440000的NF配置的能力信息，执行此命令。

```
MOD NFABILITY: ABILITY=INCCACHE-1&NOCACHE-0, NFIDTYPE=NF_ID, NFINSTANCEID="123e4567-e89b-12d3-a456-426655440000";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改配置NF的能力信息（MOD-NFABILITY）_44007369.md`
