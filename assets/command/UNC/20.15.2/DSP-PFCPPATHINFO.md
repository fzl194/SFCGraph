---
id: UNC@20.15.2@MMLCommand@DSP PFCPPATHINFO
type: MMLCommand
name: DSP PFCPPATHINFO（显示PFCP链路相关数据）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: PFCPPATHINFO
command_category: 查询类
applicable_nf:
- SMF
- SGW-C
- PGW-C
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- PFCP接口管理
- PFCP路径管理
- PFCP路径查询
status: active
---

# DSP PFCPPATHINFO（显示PFCP链路相关数据）

## 功能

**适用NF：SMF、SGW-C、PGW-C、GGSN**

该命令用于查询PFCP链路相关数据，包括链路状态，进入迁移、去活的开始时间，以及本端对端地址等信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QUERYTYPE | 查询类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定查询类型。<br>数据来源：本端规划<br>取值范围：<br>- ALL（所有）<br>- UPINSTANCEID（UP实例标识）<br>- PATHIP（链路IP地址）<br>默认值：ALL<br>配置原则：无 |
| UPINSTANCEID | UP实例标识 | 可选必选说明：该参数在"QUERYTYPE"配置为"UPINSTANCEID"时为条件必选参数。<br>参数含义：该参数用于指定UPF的实例标识。当需要查询指定UPF的路径信息时，可以指定该参数。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~50。<br>默认值：无<br>配置原则：无 |
| IPTYPE | IP类型 | 可选必选说明：该参数在"QUERYTYPE"配置为"PATHIP"时为条件必选参数。<br>参数含义：该参数用于指示链路IP地址类型。<br>数据来源：本端规划<br>取值范围：<br>- IPV4（IPv4）<br>- IPV6（IPv6）<br>默认值：无<br>配置原则：无 |
| LOCALIPV4ADDR | 本端IPv4地址 | 可选必选说明：该参数在"IPTYPE"配置为"IPV4"时为条件必选参数。<br>参数含义：该参数用于指示本端IPv4地址（即CPPOINT命令中配置的IPv4地址）。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无 |
| LOCALIPV6ADDR | 本端IPv6地址 | 可选必选说明：该参数在"IPTYPE"配置为"IPV6"时为条件必选参数。<br>参数含义：该参数用于指示本端IPv6地址（即CPPOINT命令中配置的IPv6地址）。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |
| PEERIPV4ADDR | 对端IPv4地址 | 可选必选说明：该参数在"IPTYPE"配置为"IPV4"时为条件必选参数。<br>参数含义：该参数用于指示对端IPv4地址（即PNFPROFILE命令中配置的IPv4地址）。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无 |
| PEERIPV6ADDR | 对端IPv6地址 | 可选必选说明：该参数在"IPTYPE"配置为"IPV6"时为条件必选参数。<br>参数含义：该参数用于指示对端IPv6地址（即PNFPROFILE命令中配置的IPv6地址）。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |
| PODNAME | POD名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定需要查询的POD名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@PFCPPATHINFO]] · PFCP链路相关数据（PFCPPATHINFO）

## 使用实例

查询所有链路状态。DSP PFCPPATHINFO: QUERYTYPE=ALL;

```
%%DSP PFCPPATHINFO: QUERYTYPE=ALL;%%
RETCODE = 0  操作成功。

结果如下
------------------------
      UP实例标识  =  upf_instance_1
    本端IPv4地址  =  10.2.102.17
    本端IPv6地址  =  ::
      本端端口号  =  8805
    对端IPv4地址  =  192.168.208.11
    对端IPv6地址  =  ::
      对端端口号  =  8805
         VPN名称  =  _public_
        链路状态  =  故障
    去活开始时间  =  2021-02-08 12:04:31
    迁移开始时间  =  2021-02-08 11:50:31
惯性运行开始时间  =  2021-02-08 11:50:31
    惯性运行状态  =  true
   UPF支持的特性  =  FTUP;RATP;([16 0 0 0 0 0 16])
(结果个数 = 1)
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-PFCPPATHINFO.md`
