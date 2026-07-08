# 查询北向NF实例信息（LST UNCVNFINFO）

- [命令功能](#ZH-CN_MMLREF_0209651753__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0209651753__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0209651753__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0209651753__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0209651753__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0209651753)

**适用NF：AMF、SMF、NRF、NSSF、MME、SMSF、CHF**

该命令用于查询北向NF实例信息。

## [注意事项](#ZH-CN_MMLREF_0209651753)

无

#### [操作用户权限](#ZH-CN_MMLREF_0209651753)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0209651753)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NRMNETYPE | 北向网元设备类型 | 可选必选说明：可选参数<br>参数含义：北向网元设备类型。<br>数据来源：本端规划<br>取值范围：<br>- “AMF（AMF）”：AMF<br>- “SMF（SMF）”：SMF，PGWC，SGWC，GGSNC<br>- “NRF（NRF）”：NRF<br>- “NSSF（NSSF）”：NSSF<br>- “MME（MME）”：MME<br>- “SMSF（SMSF）”：SMSF<br>- “CHF（CHF）”：CHF<br>- “AMF_MME_SGSN（AMF_MME_SGSN）”：AMF，MME，SGSN<br>- “AMF_MME（AMF_MME）”：AMF，MME<br>- “MME_SGSN（MME_SGSN）”：MME，SGSN<br>- “SMFONLY（SMFONLY）”：SMF<br>- “SMF_PGWC（SMF_PGWC）”：SMF，PGWC<br>- “SMF_PGWC_SGWC（SMF_PGWC_SGWC）”：SMF，PGWC，SGWC<br>- “PGWC_SGWC_GGSNC（PGWC_SGWC_GGSNC）”：PGWC，SGWC，GGSNC<br>- “ProxySGWC（ProxySGWC）”：ProxySGWC<br>- “CCG（CCG）”：CCG<br>- “SMF_SGWC（SMF_SGWC）”：SMF_SGWC<br>- “SAEGWC（SAEGWC）”：SAEGWC<br>- “ProxySMF_ProxySGWC_PGWC（ProxySMF_ProxySGWC_PGWC）”：ProxySMF，ProxySGWC，PGWC<br>- “SMF_PGWC_GGSNC（SMF_PGWC_GGSNC）”：SMF，PGWC，GGSNC<br>默认值：无<br>配置原则：无 |
| VNFINSTANCEID | 北向VNF实例号 | 可选必选说明：可选参数<br>参数含义：北向VNF实例号，该值从LCM通过VNF总览中选择对应的VNF，获取对应的VNF ID的值。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~64。<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0209651753)

查询所有UNC北向网元实例信息:

```
%%LST UNCVNFINFO:;%%
RETCODE = 0  操作成功

结果如下
--------
北向网元设备类型  =  AMF
   北向VNF实例号  =  13204e79601644eb942eb4ae7dd6419b
(结果个数 = 1)

---    END
```

## [输出结果说明](#ZH-CN_MMLREF_0209651753)

| 输出项名称 | 输出项解释 |
| --- | --- |
| 北向网元设备类型 | 北向网元设备类型。 |
| 北向VNF实例号 | 北向VNF实例号，该值从LCM通过VNF总览中选择对应的VNF，获取对应的VNF ID的值。 |
