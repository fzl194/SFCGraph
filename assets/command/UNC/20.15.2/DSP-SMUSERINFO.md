---
id: UNC@20.15.2@MMLCommand@DSP SMUSERINFO
type: MMLCommand
name: DSP SMUSERINFO（显示会话管理的用户信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: SMUSERINFO
command_category: 查询类
applicable_nf:
- SGW-C
- PGW-C
- SMF
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 接入管理运维
- 查询用户信息
status: active
---

# DSP SMUSERINFO（显示会话管理的用户信息）

## 功能

![](显示会话管理的用户信息（DSP SMUSERINFO）_96805380.assets/notice_3.0-zh-cn_2.png)

执行该命令时，将可能产生大量详单信息。

执行该命令时，将可能会占用大量系统内存，短时间内连续执行该命令可能会影响系统业务正常运行。如果需要使用该命令请联系华为技术支持。

**适用NF：SGW-C、PGW-C、SMF、GGSN**

该命令用于查询SMF/PGW-C/SGW-C/GGSN-C的用户信息。

## 注意事项

查询的用户信息并不保障能查出所有会话。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN名称。表示查询该APN下用户上下文信息。使用用户请求的APN对应的上报属性中“上报给话统的APN名”参数的取值，即在SET APNREPORTATTR命令中设置的该APN的PERFORMANCE的取值，指定使用用户请求的APN还是真实的APN进行统计。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。<br>默认值：无<br>配置原则：无 |
| RATTYPE | 无线接入类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定无线接入类型。<br>数据来源：本端规划<br>取值范围：<br>- EUTRAN（演进型通用陆地无线接入网）<br>- HSPA（高速分组接入）<br>- WLAN（无线局域网）<br>- GAN（通用访问网络）<br>- EHRPD（演进的高速包数据网络）<br>- EUTRAN_NB_IOT（窄带物联网）<br>- UTRAN（通用陆地无线接入网）<br>- GERAN（GSM/EDGE无线接入网）<br>- NGRAN（5G无线接入网）<br>- REDCAP（轻量化5G）<br>默认值：无<br>配置原则：无 |
| ROAMING | 漫游状态 | 可选必选说明：可选参数<br>参数含义：该参数用于指定用户漫游状态。<br>数据来源：本端规划<br>取值范围：<br>- HOME（本地用户）<br>- ROAMING（漫游用户）<br>- VISITING（拜访用户）<br>默认值：无<br>配置原则：无 |
| SRUDRTYPE | Srudr类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SRUDR（Secondary RAT Usage Data Report ）类型。<br>数据来源：本端规划<br>取值范围：<br>- PGW_WITH_SRUDR（PGW接收到Secondary RAT Usage 5G流量上报的承载信息）<br>- SPGW_WITH_SRUDR（SPGW接收到Secondary RAT Usage 5G流量上报的承载信息）<br>- SGW_WITH_SRUDR（SGW接收到Secondary RAT Usage 5G流量上报的承载信息）<br>- SMF_WITH_SRUDR（SMF接收到Secondary RAT Usage 5G流量上报的承载信息）<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SMUSERINFO]] · 会话管理的用户信息（SMUSERINFO）

## 使用实例

显示APN为“huawei.com”的用户信息：

```
%%DSP SMUSERINFO: APN="huawei.com";%%
RETCODE = 0  操作成功

结果如下
--------
IMSI             IMEI  MSISDN         EBI或者NSAPI  PDU会话ID  用户IP类型  用户IPv4地址  用户IPv6地址  IPv4地址的域标识  POD名称  SMF网元形态  用户激活时间  AMF服务网络功能标识  UPF标识  无线接入类型  
    
123030005003087  NULL  8613900050030  NULL          5          IPv4        192.168.0.1   ::            NULL              sm2-pod-1  SMF          2023-08-31 15:45:56  d3e61349-aba7-0005-af06-db53ebeae81b  upf_instance_100  NGRAN
123030005005905  NULL  8613900050059  NULL          5          IPv4        192.168.0.1   ::            NULL              sm2-pod-1  SMF          2023-08-31 15:46:10  d3e61349-aba7-0005-af06-db53ebeae81b  upf_instance_100  NGRAN
(结果个数 = 2)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-SMUSERINFO.md`
