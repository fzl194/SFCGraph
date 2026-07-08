---
id: UNC@20.15.2@MMLCommand@DSP REGNFINSTANCE
type: MMLCommand
name: DSP REGNFINSTANCE（显示NF实例）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: REGNFINSTANCE
command_category: 查询类
applicable_nf:
- NRF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- 对端NF管理
- NF信息管理
- NF实例管理
status: active
---

# DSP REGNFINSTANCE（显示NF实例）

## 功能

**适用NF：NRF**

该命令用于查询NRF上已注册的NF实例。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFTYPE | NF类型 | 可选必选说明：可选参数<br>参数含义：该参数表示NF实例的类型。<br>数据来源：全网规划<br>取值范围：<br>- NRF（NRF）<br>- UDM（UDM）<br>- AMF（AMF）<br>- SMF（SMF）<br>- AUSF（AUSF）<br>- NEF（NEF）<br>- PCF（PCF）<br>- SMSF（SMSF）<br>- NSSF（NSSF）<br>- UDR（UDR）<br>- LMF（LMF）<br>- GMLC（GMLC）<br>- EIR_5G（EIR_5G）<br>- SEPP（SEPP）<br>- UPF（UPF）<br>- N3IWF（N3IWF）<br>- AF（AF）<br>- UDSF（UDSF）<br>- BSF（BSF）<br>- CHF（CHF）<br>- NWDAF（NWDAF）<br>- CUSTOM_OCS（CUSTOM_OCS）<br>- DRA（DRA）<br>- SCP（SCP）<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [NF实例（REGNFINSTANCE）](configobject/UNC/20.15.2/REGNFINSTANCE.md)

## 使用实例

查询NRF上已注册的NF实例：

```
DSP REGNFINSTANCE:;
%%DSP REGNFINSTANCE:;%%
RETCODE = 0  操作成功

操作结果如下：
------------------------
      NF实例标识  =  123e4567-e89b-12d3-a456-426655440000
       IPV4地址  =  IP1:10.29.7.108
       IPV6地址  =  IP1:2001:db8:0:1:1:1:1:1
         NF状态  =  暂停状态
          FQDN  =  tac-123.epc.mnc003.mcc123.3gppnetwork.org
         NF类型  =  AMF
        NF组标识 =  NULL
      NF更新时间  =  2020-08-20 19:59:50
    NF客户端地址  =  10.29.7.102
  从本NRF接入标识 =  YES
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示NF实例（DSP-REGNFINSTANCE）_09653688.md`
