---
id: UNC@20.15.2@MMLCommand@MOD NGDNSN
type: MMLCommand
name: MOD NGDNSN（修改DNS NAPTR记录）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: NGDNSN
command_category: 配置类
applicable_nf:
- AMF
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- NRF业务参数
- DNS客户端管理
status: active
---

# MOD NGDNSN（修改DNS NAPTR记录）

## 功能

![](修改DNS NAPTR记录（MOD NGDNSN）_09653687.assets/notice_3.0-zh-cn_2.png)

本次修改可能会更新本主机名的其他关联记录。可通过LST NGIPV4DNSH、LST NGIPV6DNSH查询。

**适用NF：AMF、SMF**

该命令用于修改FQDN与网元接口的对应关系。

对于Proxy SGW特性，作为调测目的，可以通过添加网元类型为MME、接口类型为N26的记录来实现本地解析域名获取归属地PGW-C地址的功能。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| FQDN | FQDN | 可选必选说明：必选参数<br>参数含义：该参数用于表示由RAI、TAI、APN、MME等构建的域名，用来进行网元查询。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~255。该参数只能由字母（A-Z或者a-z）、数字（0-9）、连字符（-）和点（.）组成，大小写不敏感，FQDN不能以“.”开始，也不能以“.”结束。<br>默认值：无<br>配置原则：无 |
| HSINDEX | 主机名索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定主机名的索引。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~2048。<br>默认值：无<br>配置原则：<br>该参数需要先通过ADD NGIPV4DNSH或ADD NGIPV6DNSH命令完成配置。 |
| ENTITY | 网元类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定接口网元的类型。<br>数据来源：全网规划<br>取值范围：<br>- MME（MME）<br>- NG（5G网元）<br>默认值：无<br>配置原则：无 |
| INTYPE | 接口类型 | 可选必选说明：必选参数<br>参数含义：该参数用来指定接口对应的类型。<br>数据来源：全网规划<br>取值范围：<br>- N26（N26）<br>- SBI（SBI）<br>默认值：无<br>配置原则：<br>网元类型和接口类型间存在配置约束关系如下，具体配置哪种接口需要依据组网情况而定：<br>- “MME”:“N26”。<br>- “NG”：“SBI”。 |
| PRIORITY | 优先级 | 可选必选说明：可选参数<br>参数含义：该参数用来指定接口网元对应的优先级。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~65535。<br>默认值：无<br>配置原则：<br>- 优先级数值配置越小，代表优先级越高。<br>- IP地址的优先级越高，则顺序越靠前。 |
| WEIGHT | 权重 | 可选必选说明：可选参数<br>参数含义：该参数用来指定接口网元对应的权重。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~65535。<br>默认值：无<br>配置原则：<br>- 权重数值配置越大，代表权重越大。<br>- 对于同优先级的IP地址，进行随机选择，IP地址的权重越大，被选中的概率就越高。 |
| DESC | 描述 | 可选必选说明：可选参数<br>参数含义：该参数用于描述该命令的文字说明，目的是在配置的时候可以将对象属性、配置原因、背景等进行描述，以便在查询时能够在大量配置数据中清晰的掌握配置的原因。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~1024。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [DNS NAPTR记录（NGDNSN）](configobject/UNC/20.15.2/NGDNSN.md)

## 使用实例

修改FQDN为mmec22.mmegi8001.mme.epc.mnc123.mcc456.3gppnetwork.org，HSINDEX为100，网元类型MME，接口类型为N26的一条NAPTR记录，将该记录优先级修改为2，权重修改为50，描述改为“到华为的MME02”：

```
MOD NGDNSN: FQDN="mmec22.mmegi8001.mme.epc.mnc123.mcc456.3gppnetwork.org", HSINDEX=100, ENTITY=MME, INTYPE=N26, PRIORITY=2, WEIGHT=50, DESC="To huawei MME02";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改DNS-NAPTR记录（MOD-NGDNSN）_09653687.md`
