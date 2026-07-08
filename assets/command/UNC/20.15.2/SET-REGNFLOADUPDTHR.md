---
id: UNC@20.15.2@MMLCommand@SET REGNFLOADUPDTHR
type: MMLCommand
name: SET REGNFLOADUPDTHR（设置NF负载更新阈值）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: REGNFLOADUPDTHR
command_category: 配置类
applicable_nf:
- NRF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- 对端NF管理
- NF信息管理
- NF负载管理
status: active
---

# SET REGNFLOADUPDTHR（设置NF负载更新阈值）

## 功能

**适用NF：NRF**

当运营商希望设置不同于初始设置的NF负载更新阈值时，可使用此命令。

当NF相邻两次上报的负载差值超过负载更新阈值时，NRF会对NF的负载更新成最新上报的负载，并通知订阅该负载信息的NF实例。

## 注意事项

- 该命令执行后立即生效。

- NF类型字段为DEFAULT时，该条记录属于整系统默认值，系统默认值的生效优先级低于其他NF类型，当NF类型匹配不上时，NRF才使用该系统默认值。
- 主备或双活组网的场景下，如果需要配置此命令，则两个NRF上均需执行此命令，且配置参数一致。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

> **说明**
> 此处仅展示前20条初始记录值，您可以通过相关查询命令查看全部记录值。

| NFTYPE | LLOADTHR | SLOADTHR | HLOADTHR |
| --- | --- | --- | --- |
| DEFAULT | 5 | 3 | 1 |
| NRF | 5 | 3 | 1 |
| UDM | 5 | 3 | 1 |
| AMF | 5 | 3 | 1 |
| SMF | 5 | 3 | 1 |
| AUSF | 5 | 3 | 1 |
| NEF | 5 | 3 | 1 |
| PCF | 5 | 3 | 1 |
| SMSF | 5 | 3 | 1 |
| NSSF | 5 | 3 | 1 |
| UDR | 5 | 3 | 1 |
| LMF | 5 | 3 | 1 |
| GMLC | 5 | 3 | 1 |
| EIR_5G | 5 | 3 | 1 |
| SEPP | 5 | 3 | 1 |
| UPF | 5 | 3 | 1 |
| N3IWF | 5 | 3 | 1 |
| AF | 5 | 3 | 1 |
| UDSF | 5 | 3 | 1 |
| BSF | 5 | 3 | 1 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFTYPE | NF类型 | 可选必选说明：必选参数<br>参数含义：该参数用于表示要配置的负载更新阈值的NF类型。<br>数据来源：全网规划<br>取值范围：<br>- DEFAULT（系统默认值）<br>- NRF（NRF）<br>- UDM（UDM）<br>- AMF（AMF）<br>- SMF（SMF）<br>- AUSF（AUSF）<br>- NEF（NEF）<br>- PCF（PCF）<br>- SMSF（SMSF）<br>- NSSF（NSSF）<br>- UDR（UDR）<br>- LMF（LMF）<br>- GMLC（GMLC）<br>- EIR_5G（EIR_5G）<br>- SEPP（SEPP）<br>- UPF（UPF）<br>- N3IWF（N3IWF）<br>- AF（AF）<br>- UDSF（UDSF）<br>- BSF（BSF）<br>- CHF（CHF）<br>- NWDAF（NWDAF）<br>- CUSTOM_OCS（CUSTOM_OCS）<br>- SCP（SCP）<br>默认值：无。<br>配置原则：无 |
| LLOADTHR | 低负载更新阈值 | 可选必选说明：可选参数<br>参数含义：该参数用于表示NF低负载（负载值为0-50之间，这里的负载指的是NF上报的load信元）的更新阈值。NF的负载值范围在匹配时以NRF系统中当前的负载值为准。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~20。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST REGNFLOADUPDTHR查询当前参数配置值。<br>配置原则：无 |
| SLOADTHR | 中负载更新阈值 | 可选必选说明：可选参数<br>参数含义：该参数用于表示NF中负载（负载值为51-70之间，这里的负载指的是NF上报的load信元）的更新阈值。NF的负载值范围在匹配时以NRF系统中当前的负载值为准。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~20。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST REGNFLOADUPDTHR查询当前参数配置值。<br>配置原则：无 |
| HLOADTHR | 高负载更新阈值 | 可选必选说明：可选参数<br>参数含义：该参数用于表示NF高负载（负载值为71-100之间，这里的负载指的是NF上报的load信元）的更新阈值。NF的负载值范围在匹配时以NRF系统中当前的负载值为准。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~20。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST REGNFLOADUPDTHR查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [NF负载更新阈值（REGNFLOADUPDTHR）](configobject/UNC/20.15.2/REGNFLOADUPDTHR.md)

## 使用实例

当运营商希望将低负载场景下的NRF更新阈值修改为10时，配置此命令。

```
SET REGNFLOADUPDTHR: NFTYPE=NRF, LLOADTHR=10;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置NF负载更新阈值（SET-REGNFLOADUPDTHR）_09652688.md`
