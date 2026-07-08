# 查询域名查询失败的记录（DSP DYNNGERRREC）

- [命令功能](#ZH-CN_MMLREF_0216634376__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0216634376__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0216634376__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0216634376__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0216634376__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0216634376)

**适用NF：AMF**

该命令用于向DNS服务器查询域名查询失败的记录，最多显示1000条。

## [注意事项](#ZH-CN_MMLREF_0216634376)

无

#### [操作用户权限](#ZH-CN_MMLREF_0216634376)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0216634376)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QUERYCONDITION | 查询条件 | 可选必选说明：可选参数<br>参数含义：该参数用于基于FQDN或基于记录数的查询条件。<br>数据来源：本端规划<br>取值范围：<br>- BYDNSFQDN（基于FQDN）<br>- RECNUM（基于记录数）<br>默认值：无<br>配置原则：无 |
| DNSFQDN | DNS域名 | 可选必选说明：该参数在"QUERYCONDITION"配置为"BYDNSFQDN"时为条件可选参数。<br>参数含义：该参数用于表示查询失败的FQDN信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~256。<br>默认值：无<br>配置原则：无 |
| RECNUM | DNS域名记录数 | 可选必选说明：该参数在"QUERYCONDITION"配置为"RECNUM"时为条件可选参数。<br>参数含义：该参数用于表示最近失败的N个FQDN。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~1000。<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0216634376)

查询域名查询失败的记录：

```
DSP DYNNGERRREC: QUERYCONDITION=BYDNSFQDN, DNSFQDN=" mmec22.mmegi8001.mme.epc.mnc000.mcc000.3gppnetwork.org";
%%DSP DYNNGERRREC: QUERYCONDITION=BYDNSFQDN, DNSFQDN=" mmec22.mmegi8001.mme.epc.mnc000.mcc000.3gppnetwork.org";%%
RETCODE = 0  操作成功

结果如下
------------------------
             DNS域名  =  mmec22.mmegi8001.mme.epc.mnc000.mcc000.3gppnetwork.org
       DNS域名记录数  =  1
            查询类型  =  NAPTR类型
            错误来源  =  LINK
  第一次查询失败时间  =  2019-12-23 22:06:17.168173899 +0800 CST m=+34.705799359
最近一次失败参考信息  =  link rsp time out, current wait time is 3s
最近一次查询失败时间  =  2019-12-23 22:08:22.049450558 +0800 CST m=+159.587075759
        查询失败次数  =  3
(结果个数 = 1)
```

## [输出结果说明](#ZH-CN_MMLREF_0216634376)

| 输出项名称 | 输出项解释 |
| --- | --- |
| DNS域名 | 该参数用于表示查询失败的FQDN信息。 |
| DNS域名记录数 | 该参数用于表示最近失败的N个FQDN。 |
| 查询类型 | 该参数用于表示DNS客户端向DNS服务器查询的类型。<br>取值说明：<br>- NAPTR（NAPTR类型）<br>- A（A类型）<br>- AAAA（AAAA类型） |
| 错误来源 | 该参数用于表示错误来源。<br>取值说明：<br>- LINK（LINK）<br>- DNSSERVER（DNSSERVER） |
| 第一次查询失败时间 | 该参数用于表示第一次检查出DNS查询失败的时间。 |
| 最近一次失败参考信息 | 该参数用于表示最近一次查询失败的原因。 |
| 最近一次查询失败时间 | 该参数用于表示最近一次检查出DNS查询失败的时间。 |
| 查询失败次数 | 该参数用于表示检查出该域名DNS查询失败的次数。 |
