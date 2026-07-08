---
id: UNC@20.15.2@MMLCommand@LST NFMSISDN
type: MMLCommand
name: LST NFMSISDN（查询MSISDN号段）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NFMSISDN
command_category: 查询类
applicable_nf:
- NRF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- 对端NF管理
- 号段配置管理
- MSISDN号段管理
status: active
---

# LST NFMSISDN（查询MSISDN号段）

## 功能

![](查询MSISDN号段（LST NFMSISDN）_09653764.assets/notice_3.0-zh-cn_2.png)

该命令可能返回报文数据量较大，执行会影响系统性能，可通过增加查询参数减少返回结果报文。

**适用NF：NRF**

该命令用于在NRF上查询NF组支持的MSISDN号段信息。

若要查询全部NF组支持的MSISDN号段信息，请不要输入任何参数。

若要查询某个“NF组标识”的MSISDN号段信息，请输入“NF组标识”或其他参数的组合。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFGROUPID | NF组标识 | 可选必选说明：可选参数<br>参数含义：该参数用于表示MSISDN号段配置的NF组标识，可以通过LST NFGROUP进行查询，支持MSISDN号段配置的NF类型仅包含UDM、UDR、CHF、PCF、CUSTOM_OCS。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~128。<br>默认值：无<br>配置原则：无 |
| SEGSTART | 号段起始字符串 | 可选必选说明：可选参数<br>参数含义：该参数用于表示MSISDN号段的起始号码。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是5~15。十进制数字，号段的起始号码必须与结束号码长度保持一致，数值必须小于或等于结束号码的数值，且号段的起始号码不能以0开始，全0除外。<br>默认值：无<br>配置原则：无 |
| SEGEND | 号段结束字符串 | 可选必选说明：可选参数<br>参数含义：该参数用于表示MSISDN号段的结束号码。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是5~15。十进制数字，号段的结束号码必须与起始号码长度保持一致，数值大于或等于起始号码的数值，且号段的结束号码不能以0开始。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NFMSISDN]] · MSISDN号段（NFMSISDN）

## 使用实例

查询NF组标识为nfgroupid-city1的MSISDN号段：

```
LST NFMSISDN: NFGROUPID="nfgroupid-city1":;
%%LST NFMSISDN: NFGROUPID="nfgroupid-city1";%%
RETCODE = 0  执行成功

操作结果如下:
-------------------------
       NF组标识  =  nfgroupid-city1
 号段起始字符串  =  11111
 号段结束字符串  =  99999
(结果个数 = 1)
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-NFMSISDN.md`
