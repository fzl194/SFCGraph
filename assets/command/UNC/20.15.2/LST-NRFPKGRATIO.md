---
id: UNC@20.15.2@MMLCommand@LST NRFPKGRATIO
type: MMLCommand
name: LST NRFPKGRATIO（查询NRF内外包长比例）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NRFPKGRATIO
command_category: 查询类
applicable_nf:
- NRF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- NRF业务参数
- NRF包长比例
status: active
---

# LST NRFPKGRATIO（查询NRF内外包长比例）

## 功能

**适用NF：NRF**

该命令用于查询NRF内部报文长度和http接口json报文长度的比例系数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFTYPE | NF类型 | 可选必选说明：可选参数<br>参数含义：该参数用于表示NRF处理注册/更新的NF类型或服务发现的目标NF类型。<br>数据来源：全网规划<br>取值范围：<br>- DEFAULT（DEFAULT）<br>- NRF（NRF）<br>- UDM（UDM）<br>- AMF（AMF）<br>- SMF（SMF）<br>- AUSF（AUSF）<br>- NEF（NEF）<br>- PCF（PCF）<br>- SMSF（SMSF）<br>- NSSF（NSSF）<br>- UDR（UDR）<br>- LMF（LMF）<br>- GMLC（GMLC）<br>- EIR_5G（EIR5G）<br>- SEPP（SEPP）<br>- UPF（UPF）<br>- N3IWF（N3IWF）<br>- AF（AF）<br>- UDSF（UDSF）<br>- BSF（BSF）<br>- CHF（CHF）<br>- NWDAF（NWDAF）<br>- CUSTOM_OCS（CUSTOM_OCS）<br>- SCP（SCP）<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NRFPKGRATIO]] · NRF内外包长比例（NRFPKGRATIO）

## 使用实例

查询NRF包长比例：

```
LST NRFPKGRATIO:;
%%LST NRFPKGRATIO:;%%
RETCODE = 0  操作成功

结果如下
--------
      NF类型  =  AMF
 比例系数(%)  =  30
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-NRFPKGRATIO.md`
