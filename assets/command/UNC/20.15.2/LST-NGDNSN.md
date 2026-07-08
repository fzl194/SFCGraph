---
id: UNC@20.15.2@MMLCommand@LST NGDNSN
type: MMLCommand
name: LST NGDNSN（查询DNS NAPTR记录）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NGDNSN
command_category: 查询类
applicable_nf:
- AMF
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- NRF业务参数
- DNS客户端管理
status: active
---

# LST NGDNSN（查询DNS NAPTR记录）

## 功能

**适用NF：AMF、SMF**

该命令用于查询FQDN与网元接口的对应关系。对于Proxy SGW特性，作为调测目的，可以通过添加网元类型为MME、接口类型为N26的记录来实现本地解析域名获取归属地PGW-C地址的功能。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| FQDN | FQDN | 可选必选说明：可选参数<br>参数含义：该参数用于表示由RAI、TAI、APN、MME等构建的域名，用来进行网元查询。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~255。该参数只能由字母（A-Z或者a-z）、数字（0-9）、连字符（-）和点（.）组成，大小写不敏感，FQDN不能以“.”开始，也不能以“.”结束。<br>默认值：无<br>配置原则：无 |
| HSINDEX | 主机名索引 | 可选必选说明：可选参数<br>参数含义：该参数用于指定主机名的索引。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~2048。<br>默认值：无<br>配置原则：无 |
| ENTITY | 网元类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定接口网元的类型。<br>数据来源：全网规划<br>取值范围：<br>- MME（MME）<br>- NG（5G网元）<br>默认值：无<br>配置原则：无 |
| INTYPE | 接口类型 | 可选必选说明：可选参数<br>参数含义：该参数用来指定接口对应的类型。<br>数据来源：全网规划<br>取值范围：<br>- N26（N26）<br>- SBI（SBI）<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [DNS NAPTR记录（NGDNSN）](configobject/UNC/20.15.2/NGDNSN.md)

## 使用实例

查询FQDN为“mmec22.mmegi8001.mme.epc.mnc123.mcc456.3gppnetwork.org”的记录结果：

```
%%LST NGDNSN: FQDN="mmec22.mmegi8001.mme.epc.mnc123.mcc456.3gppnetwork.org";%%
RETCODE = 0  操作成功

结果如下
--------
 FQDN                                                      主机名索引  网元类型  接口类型    优先级  权重    描述

 MMEC22.MMEGI8001.MME.EPC.MNC123.MCC456.3GPPNETWORK.ORG    1           MME       N26         0       100     To huawei MME
 MMEC22.MMEGI8001.MME.EPC.MNC123.MCC456.3GPPNETWORK.ORG    2           MME       N26         0       100     To huawei MME
 MMEC22.MMEGI8001.MME.EPC.MNC123.MCC456.3GPPNETWORK.ORG    3           5G网元    SBI         0       100     To huawei NG
(结果个数 = 3)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询DNS-NAPTR记录（LST-NGDNSN）_09653672.md`
