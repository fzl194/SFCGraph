# 删除北向NF实例信息（RMV UNCVNFINFO）

- [命令功能](#ZH-CN_MMLREF_0209652514__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0209652514__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0209652514__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0209652514__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0209652514)

**适用NF：AMF、SMF、NRF、NSSF、MME、SMSF、CHF**

该命令用于删除北向NF实例信息。

## [注意事项](#ZH-CN_MMLREF_0209652514)

- 该命令执行后立即生效。

- 删除北向实例会导致该网元不上报北向数据，请谨慎操作。

#### [操作用户权限](#ZH-CN_MMLREF_0209652514)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0209652514)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NRMNETYPE | 北向网元设备类型 | 可选必选说明：必选参数<br>参数含义：北向网元设备类型。<br>数据来源：本端规划<br>取值范围：<br>- “AMF（AMF）”：AMF<br>- “SMF（SMF）”：SMF，PGWC，SGWC，GGSNC<br>- “NRF（NRF）”：NRF<br>- “NSSF（NSSF）”：NSSF<br>- “MME（MME）”：MME<br>- “SMSF（SMSF）”：SMSF<br>- “CHF（CHF）”：CHF<br>- “AMF_MME_SGSN（AMF_MME_SGSN）”：AMF，MME，SGSN<br>- “AMF_MME（AMF_MME）”：AMF，MME<br>- “MME_SGSN（MME_SGSN）”：MME，SGSN<br>- “SMFONLY（SMFONLY）”：SMF<br>- “SMF_PGWC（SMF_PGWC）”：SMF，PGWC<br>- “SMF_PGWC_SGWC（SMF_PGWC_SGWC）”：SMF，PGWC，SGWC<br>- “PGWC_SGWC_GGSNC（PGWC_SGWC_GGSNC）”：PGWC，SGWC，GGSNC<br>- “ProxySGWC（ProxySGWC）”：ProxySGWC<br>- “CCG（CCG）”：CCG<br>- “SMF_SGWC（SMF_SGWC）”：SMF_SGWC<br>- “SAEGWC（SAEGWC）”：SAEGWC<br>- “ProxySMF_ProxySGWC_PGWC（ProxySMF_ProxySGWC_PGWC）”：ProxySMF，ProxySGWC，PGWC<br>- “SMF_PGWC_GGSNC（SMF_PGWC_GGSNC）”：SMF，PGWC，GGSNC<br>默认值：无<br>配置原则：无 |
| VNFINSTANCEID | 北向VNF实例号 | 可选必选说明：必选参数<br>参数含义：北向VNF实例号，该值从LCM通过VNF总览中选择对应的VNF，获取对应的VNF ID的值。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~64。<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0209652514)

删除UNC北向网元实例信息，其设备类型为AMF，VNF实例号为13204e79601644eb942eb4ae7dd6419b，执行以下命令：

```
RMV UNCVNFINFO: NRMNETYPE=AMF, VNFINSTANCEID="13204e79601644eb942eb4ae7dd6419b";
```
