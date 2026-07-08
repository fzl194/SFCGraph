---
id: UNC@20.15.2@MMLCommand@LST UNCVNFINFO
type: MMLCommand
name: LST UNCVNFINFO（查询北向NF实例信息）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: UNCVNFINFO
command_category: 查询类
applicable_nf:
- AMF
- SMF
- NRF
- NSSF
- MME
- SMSF
- CHF
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 性能统计管理
- 北向配置管理
status: active
---

# LST UNCVNFINFO（查询北向NF实例信息）

## 功能

**适用NF：AMF、SMF、NRF、NSSF、MME、SMSF、CHF**

该命令用于查询北向NF实例信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NRMNETYPE | 北向网元设备类型 | 可选必选说明：可选参数<br>参数含义：北向网元设备类型。<br>数据来源：本端规划<br>取值范围：<br>- “AMF（AMF）”：AMF<br>- “SMF（SMF）”：SMF，PGWC，SGWC，GGSNC<br>- “NRF（NRF）”：NRF<br>- “NSSF（NSSF）”：NSSF<br>- “MME（MME）”：MME<br>- “SMSF（SMSF）”：SMSF<br>- “CHF（CHF）”：CHF<br>- “AMF_MME_SGSN（AMF_MME_SGSN）”：AMF，MME，SGSN<br>- “AMF_MME（AMF_MME）”：AMF，MME<br>- “MME_SGSN（MME_SGSN）”：MME，SGSN<br>- “SMFONLY（SMFONLY）”：SMF<br>- “SMF_PGWC（SMF_PGWC）”：SMF，PGWC<br>- “SMF_PGWC_SGWC（SMF_PGWC_SGWC）”：SMF，PGWC，SGWC<br>- “PGWC_SGWC_GGSNC（PGWC_SGWC_GGSNC）”：PGWC，SGWC，GGSNC<br>- “ProxySGWC（ProxySGWC）”：ProxySGWC<br>- “CCG（CCG）”：CCG<br>- “SMF_SGWC（SMF_SGWC）”：SMF_SGWC<br>- “SAEGWC（SAEGWC）”：SAEGWC<br>- “ProxySMF_ProxySGWC_PGWC（ProxySMF_ProxySGWC_PGWC）”：ProxySMF，ProxySGWC，PGWC<br>- “SMF_PGWC_GGSNC（SMF_PGWC_GGSNC）”：SMF，PGWC，GGSNC<br>默认值：无<br>配置原则：无 |
| VNFINSTANCEID | 北向VNF实例号 | 可选必选说明：可选参数<br>参数含义：北向VNF实例号，该值从LCM通过VNF总览中选择对应的VNF，获取对应的VNF ID的值。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~64。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [北向NF实例信息（UNCVNFINFO）](configobject/UNC/20.15.2/UNCVNFINFO.md)

## 使用实例

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

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询北向NF实例信息（LST-UNCVNFINFO）_09651753.md`
