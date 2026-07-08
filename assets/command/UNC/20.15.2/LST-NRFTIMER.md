---
id: UNC@20.15.2@MMLCommand@LST NRFTIMER
type: MMLCommand
name: LST NRFTIMER（查询NRF时长信息）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NRFTIMER
command_category: 查询类
applicable_nf:
- NRF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- NRF业务参数
- 定时器参数
status: active
---

# LST NRFTIMER（查询NRF时长信息）

## 功能

**适用NF：NRF**

该命令用于查询NRF各类时长信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFTYPE | NF类型 | 可选必选说明：可选参数<br>参数含义：该参数用于表示各定时器时长针对的NF类型。其中，DEFALUT范围为下面列举的具体NF外的其他NF类型。<br>数据来源：全网规划<br>取值范围：<br>- DEFAULT（DEFAULT）<br>- NRF（NRF）<br>- UDM（UDM）<br>- AMF（AMF）<br>- SMF（SMF）<br>- AUSF（AUSF）<br>- NEF（NEF）<br>- PCF（PCF）<br>- SMSF（SMSF）<br>- NSSF（NSSF）<br>- UDR（UDR）<br>- LMF（LMF）<br>- GMLC（GMLC）<br>- EIR_5G（EIR5G）<br>- SEPP（SEPP）<br>- UPF（UPF）<br>- N3IWF（N3IWF）<br>- AF（AF）<br>- UDSF（UDSF）<br>- BSF（BSF）<br>- CHF（CHF）<br>- NWDAF（NWDAF）<br>- CUSTOM_OCS（CUSTOM_OCS）<br>- SCP（SCP）<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NRFTIMER]] · NRF时长信息（NRFTIMER）

## 使用实例

查询NF类型为NRF的各类时长信息：

```
LST NRFTIMER: NFTYPE=NRF;
%%LST NRFTIMER:NFTYPE=NRF;%%
RETCODE = 0  执行成功

操作结果如下:
-------------------------
                                       NF类型  =  NRF
                              心跳超时次数  =  3
                        心跳周期时长(秒)  =  5
          服务发现缓存有效时长(秒)  =  86400
   服务发现缓存有效宽限时长(秒)  =  0
                        订阅有效时长(秒)  =  86400
订阅更新有效期误差宽限时长(秒)  =  300 
(结果个数 = 1)
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-NRFTIMER.md`
