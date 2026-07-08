---
id: UNC@20.15.2@MMLCommand@DSP DYNNGERRREC
type: MMLCommand
name: DSP DYNNGERRREC（查询域名查询失败的记录）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: DYNNGERRREC
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- NRF业务参数
- DNS客户端管理
status: active
---

# DSP DYNNGERRREC（查询域名查询失败的记录）

## 功能

**适用NF：AMF**

该命令用于向DNS服务器查询域名查询失败的记录，最多显示1000条。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QUERYCONDITION | 查询条件 | 可选必选说明：可选参数<br>参数含义：该参数用于基于FQDN或基于记录数的查询条件。<br>数据来源：本端规划<br>取值范围：<br>- BYDNSFQDN（基于FQDN）<br>- RECNUM（基于记录数）<br>默认值：无<br>配置原则：无 |
| DNSFQDN | DNS域名 | 可选必选说明：该参数在"QUERYCONDITION"配置为"BYDNSFQDN"时为条件可选参数。<br>参数含义：该参数用于表示查询失败的FQDN信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~256。<br>默认值：无<br>配置原则：无 |
| RECNUM | DNS域名记录数 | 可选必选说明：该参数在"QUERYCONDITION"配置为"RECNUM"时为条件可选参数。<br>参数含义：该参数用于表示最近失败的N个FQDN。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~1000。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/DYNNGERRREC]] · 域名查询失败的记录（DYNNGERRREC）

## 使用实例

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

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询域名查询失败的记录（DSP-DYNNGERRREC）_16634376.md`
