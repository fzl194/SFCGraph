---
id: UNC@20.15.2@MMLCommand@LST NRFPLMNNF
type: MMLCommand
name: LST NRFPLMNNF（查询关口局NF信息）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NRFPLMNNF
command_category: 查询类
applicable_nf:
- NRF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- NRF业务参数
- NRF国际漫游参数管理
status: active
---

# LST NRFPLMNNF（查询关口局NF信息）

## 功能

**适用NF：NRF**

该命令用于查询本NRF管理的关口局NF。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFTYPE | NF类型 | 可选必选说明：可选参数<br>参数含义：该参数用于表示目的NF类型。<br>数据来源：全网规划<br>取值范围：<br>- NRF（NRF）<br>- UDM（UDM）<br>- AMF（AMF）<br>- SMF（SMF）<br>- AUSF（AUSF）<br>- NEF（NEF）<br>- PCF（PCF）<br>- SMSF（SMSF）<br>- NSSF（NSSF）<br>- UDR（UDR）<br>- LMF（LMF）<br>- GMLC（GMLC）<br>- EIR_5G（EIR_5G）<br>- SEPP（SEPP）<br>- UPF（UPF）<br>- N3IWF（N3IWF）<br>- AF（AF）<br>- UDSF（UDSF）<br>- BSF（BSF）<br>- CHF（CHF）<br>- NWDAF（NWDAF）<br>- CUSTOM_OCS（CUSTOM_OCS）<br>- SCP（SCP）<br>默认值：无<br>配置原则：无 |
| NFINSTANCEID | NF实例标识 | 可选必选说明：可选参数<br>参数含义：该参数用于表示本NRF管理的关口局NF实例标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~36。该参数只能由字母（A-Z或者a-z）、数字（0-9）、中划线（-）、星号（*）组成，不区分大小写。<br>默认值：无<br>配置原则：<br>支持统配ID，通配ID为“*”，表示该NRF下所有的NF均为关口局NF。 |
| NFNAME | NF名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示本NRF管理的关口局NF名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~64。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NRFPLMNNF]] · 关口局NF信息（NRFPLMNNF）

## 使用实例

使用以下命令查询关口局NF信息：

```
%%LST NRFPLMNNF:;%%
RETCODE = 0  操作成功

结果如下
--------
    NF类型  =  SMF
NF实例标识  =  123e4567-e89b-12d3-a456-426655440000
    NF名称  =  superom11-v6
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-NRFPLMNNF.md`
