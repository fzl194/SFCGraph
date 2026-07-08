---
id: UNC@20.15.2@MMLCommand@LST NRFIGNDISCPARA
type: MMLCommand
name: LST NRFIGNDISCPARA（查询NF服务发现忽略参数规则）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NRFIGNDISCPARA
command_category: 查询类
applicable_nf:
- NRF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- NRF业务参数
- NF服务发现忽略参数处理规则
status: active
---

# LST NRFIGNDISCPARA（查询NF服务发现忽略参数规则）

## 功能

**适用NF：NRF**

该命令用于查询NF服务发现忽略参数配置。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFTYPE | 网元类型 | 可选必选说明：可选参数<br>参数含义：该参数用于表示忽略发现参数规则对应的目标NF类型。其中，ALL表示适用于所有目标NF类型。<br>数据来源：本端规划<br>取值范围：<br>- ALL（表示适用于所有NF类型）<br>- NRF（NRF）<br>- UDM（UDM）<br>- AMF（AMF）<br>- SMF（SMF）<br>- AUSF（AUSF）<br>- NEF（NEF）<br>- PCF（PCF）<br>- SMSF（SMSF）<br>- NSSF（NSSF）<br>- UDR（UDR）<br>- LMF（LMF）<br>- GMLC（GMLC）<br>- EIR_5G（EIR_5G）<br>- SEPP（SEPP）<br>- UPF（UPF）<br>- N3IWF（N3IWF）<br>- AF（AF）<br>- UDSF（UDSF）<br>- BSF（BSF）<br>- CHF（CHF）<br>- NWDAF（NWDAF）<br>- CUSTOM_OCS（CUSTOM_OCS）<br>- SCP（SCP）<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NRFIGNDISCPARA]] · NF服务发现忽略参数规则（NRFIGNDISCPARA）

## 使用实例

查询网元类型为NRF的服务发现忽略参数规则。

```
LST NRFIGNDISCPARA:;
%%LST NRFIGNDISCPARA:;%%
RETCODE = 0  操作成功

The result is as follows
------------------------
网元类型          =  NRF
服务发现忽略参数  =  Tai
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-NRFIGNDISCPARA.md`
