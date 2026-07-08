---
id: UNC@20.15.2@MMLCommand@ADD UNCVNFINFO
type: MMLCommand
name: ADD UNCVNFINFO（增加北向NF实例信息）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: UNCVNFINFO
command_category: 配置类
applicable_nf:
- AMF
- SMF
- NRF
- NSSF
- MME
- SMSF
- CHF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 性能统计管理
- 北向配置管理
status: active
---

# ADD UNCVNFINFO（增加北向NF实例信息）

## 功能

**适用NF：AMF、SMF、NRF、NSSF、MME、SMSF、CHF**

该命令用于增加北向NF实例信息。

## 注意事项

- 该命令执行后立即生效。

- 新增该配置，需要进入网管业务面，点击页面的Access键，进入后选择主拓扑，然后右键选择对应网元，将网元在网管上的状态为“调测”状态，并且完成相关配置和检查之后再对接北向OSS，否则可能导致北向OSS出现错误。

- 最多可输入1条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NRMNETYPE | 北向网元设备类型 | 可选必选说明：必选参数<br>参数含义：北向网元设备类型。<br>数据来源：本端规划<br>取值范围：<br>- “AMF（AMF）”：AMF<br>- “SMF（SMF）”：SMF，PGWC，SGWC，GGSNC<br>- “NRF（NRF）”：NRF<br>- “NSSF（NSSF）”：NSSF<br>- “MME（MME）”：MME<br>- “SMSF（SMSF）”：SMSF<br>- “CHF（CHF）”：CHF<br>- “AMF_MME_SGSN（AMF_MME_SGSN）”：AMF，MME，SGSN<br>- “AMF_MME（AMF_MME）”：AMF，MME<br>- “MME_SGSN（MME_SGSN）”：MME，SGSN<br>- “SMFONLY（SMFONLY）”：SMF<br>- “SMF_PGWC（SMF_PGWC）”：SMF，PGWC<br>- “SMF_PGWC_SGWC（SMF_PGWC_SGWC）”：SMF，PGWC，SGWC<br>- “PGWC_SGWC_GGSNC（PGWC_SGWC_GGSNC）”：PGWC，SGWC，GGSNC<br>- “ProxySGWC（ProxySGWC）”：ProxySGWC<br>- “CCG（CCG）”：CCG<br>- “SMF_SGWC（SMF_SGWC）”：SMF_SGWC<br>- “SAEGWC（SAEGWC）”：SAEGWC<br>- “ProxySMF_ProxySGWC_PGWC（ProxySMF_ProxySGWC_PGWC）”：ProxySMF，ProxySGWC，PGWC<br>- “SMF_PGWC_GGSNC（SMF_PGWC_GGSNC）”：SMF，PGWC，GGSNC<br>默认值：无<br>配置原则：无 |
| VNFINSTANCEID | 北向VNF实例号 | 可选必选说明：必选参数<br>参数含义：北向VNF实例号，该值从LCM通过VNF总览中选择对应的VNF，获取对应的VNF ID的值。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~64。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@UNCVNFINFO]] · 北向NF实例信息（UNCVNFINFO）

## 使用实例

新增UNC北向网元实例信息，其设备类型为AMF，VNF实例号为13204e79601644eb942eb4ae7dd6419b，执行以下命令：

```
ADD UNCVNFINFO: NRMNETYPE=AMF, VNFINSTANCEID="13204e79601644eb942eb4ae7dd6419b";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-UNCVNFINFO.md`
