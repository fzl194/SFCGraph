---
id: UNC@20.15.2@MMLCommand@SET NRFDISCPARARULE
type: MMLCommand
name: SET NRFDISCPARARULE（设置NF服务发现参数处理规则）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: NRFDISCPARARULE
command_category: 配置类
applicable_nf:
- NRF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- NRF业务参数
- NF服务发现参数处理规则
status: active
---

# SET NRFDISCPARARULE（设置NF服务发现参数处理规则）

## 功能

**适用NF：NRF**

该命令用于增加NRF发现参数处理规则。

## 注意事项

- 该命令执行后立即生效。

- 主备或双活组网的场景下，如果需要配置此命令，则两个NRF上均需执行此命令，且配置参数一致。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

> **说明**
> 此处仅展示前20条初始记录值，您可以通过相关查询命令查看全部记录值。

| NFTYPE | DISCPARA |
| --- | --- |
| DEFAULT | - |
| NRF | - |
| UDM | TARGETNFTYPE-1 |
| AMF | TARGETNFTYPE-1 |
| SMF | TARGETNFTYPE-1 |
| AUSF | TARGETNFTYPE-1 |
| NEF | - |
| PCF | TARGETNFTYPE-1 |
| SMSF | - |
| NSSF | - |
| UDR | - |
| LMF | - |
| GMLC | - |
| EIR_5G | - |
| SEPP | - |
| UPF | - |
| N3IWF | - |
| AF | - |
| UDSF | - |
| BSF | TARGETNFTYPE-1 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFTYPE | 网元类型 | 可选必选说明：必选参数<br>参数含义：该参数用于表示发现参数处理规则对应的目标NF类型。其中，DEFAULT范围为下面列举的具体NF外的其他NF类型。<br>数据来源：本端规划<br>取值范围：<br>- DEFAULT（DEFAULT）<br>- NRF（NRF）<br>- UDM（UDM）<br>- AMF（AMF）<br>- SMF（SMF）<br>- AUSF（AUSF）<br>- NEF（NEF）<br>- PCF（PCF）<br>- SMSF（SMSF）<br>- NSSF（NSSF）<br>- UDR（UDR）<br>- LMF（LMF）<br>- GMLC（GMLC）<br>- EIR_5G（EIR5G）<br>- SEPP（SEPP）<br>- UPF（UPF）<br>- N3IWF（N3IWF）<br>- AF（AF）<br>- UDSF（UDSF）<br>- BSF（BSF）<br>- CHF（CHF）<br>- NWDAF（NWDAF）<br>- CUSTOM_OCS（CUSTOM_OCS）<br>- SCP（SCP）<br>默认值：无。<br>配置原则：无 |
| DISCPARA | 发现参数防呆规则 | 可选必选说明：可选参数<br>参数含义：该参数用于表示服务发现参数防呆规则。如果服务发现参数中目标NF相关参数包含勾选项以外的参数，则NRF正常处理服务发现请求，否则，服务发现结果返回403(Forbidden)。如果没有勾选任何选项，NRF不进行上述判断，正常处理服务发现请求。例如，如果此参数只设置了“TARGETNFTYPE”，表示如果服务发现目标NF只携带了“TARGETNFTYPE”，则服务发现结果返回403(Forbidden)，NRF不进行处理。<br>数据来源：本端规划<br>取值范围：<br>- TARGETNFTYPE（服务发现参数中的目标NF类型）<br>- SERVICENAMES（服务发现参数中的服务名称）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NRFDISCPARARULE查询当前参数配置值。<br>配置原则：<br>由于TARGETNFTYPE是服务发现必选参数，勾选其他选项时必须要勾选TARGETNFTYPE。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NRFDISCPARARULE]] · NF发现参数防呆规则（NRFDISCPARARULE）

## 使用实例

配置AMF网元的服务发现参数规则为“TARGETNFTYPE”，执行如下命令。

```
SET NRFDISCPARARULE: NFTYPE=AMF, DISCPARA=TARGETNFTYPE-1&SERVICENAMES-0;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置NF服务发现参数处理规则（SET-NRFDISCPARARULE）_35273633.md`
