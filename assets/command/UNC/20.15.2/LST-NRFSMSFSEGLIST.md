---
id: UNC@20.15.2@MMLCommand@LST NRFSMSFSEGLIST
type: MMLCommand
name: LST NRFSMSFSEGLIST（查询SMSF号段白名单）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NRFSMSFSEGLIST
command_category: 查询类
applicable_nf:
- NRF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- NRF业务参数
- SMSF割接场景NRF处理策略
status: active
---

# LST NRFSMSFSEGLIST（查询SMSF号段白名单）

## 功能

**适用NF：NRF**

该命令用于查询SMSF号段白名单。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SEGTYPE | 号段类型 | 可选必选说明：可选参数<br>参数含义：该参数用于表示配置SMSF号段白名单的号段类型。<br>数据来源：本端规划<br>取值范围：<br>- IMSI（IMSI）<br>- MSISDN（MSISDN）<br>默认值：无<br>配置原则：无 |
| IMSISTART | IMSI起始号段 | 可选必选说明：该参数在"SEGTYPE"配置为"IMSI"时为条件可选参数。<br>参数含义：该参数用于表示配置SMSF号段白名单中IMSI号段的起始号码。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是5~15。<br>默认值：无<br>配置原则：<br>号段起始字符串长度为15位，不足15位时系统自动在末尾补0。十进制数字，号段的起始号码数值必须小于或等于号段结束号码的数值，且号段的起始号码不能以0开始，全0除外。 |
| IMSIEND | IMSI结束号段 | 可选必选说明：该参数在"SEGTYPE"配置为"IMSI"时为条件可选参数。<br>参数含义：该参数用于表示配置SMSF号段白名单中IMSI号段的结束号码。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是5~15。<br>默认值：无<br>配置原则：<br>号段结束字符串长度为15位，不足15位时系统自动在末尾补9。十进制数字，号段的结束号码数值必须大于或等于起始号码的数值，且号段的结束号码不能为以0开始。 |
| MSISDNSTART | MSISDN开始号段 | 可选必选说明：该参数在"SEGTYPE"配置为"MSISDN"时为条件可选参数。<br>参数含义：该参数用于表示配置SMSF号段白名单中MSISDN号段的起始号码。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是5~15。<br>默认值：无<br>配置原则：<br>十进制数字，号段的起始号码必须与结束号码长度保持一致，数值必须小于或等于结束号码的数值，且号段的起始号码不能以0开始，全0除外。 |
| MSISDNEND | MSISDN结束号段 | 可选必选说明：该参数在"SEGTYPE"配置为"MSISDN"时为条件可选参数。<br>参数含义：该参数用于表示配置SMSF号段白名单中MSISDN号段的结束号码。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是5~15。<br>默认值：无<br>配置原则：<br>十进制数字，号段的结束号码必须与起始号码长度保持一致，数值大于或等于起始号码的数值，且号段的结束号码不能以0开始。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NRFSMSFSEGLIST]] · SMSF号段白名单（NRFSMSFSEGLIST）

## 使用实例

查询SMSF号段白名单的记录，执行如下命令：

```
LST NRFSMSFSEGLIST:;
%%LST NRFSMSFSEGLIST:;%%
RETCODE = 0  操作成功

结果如下
---------
     号段类型   =  IMSI        
  IMSI起始号码  =  123467040000000    
  IMSI结束号码  =  123467059999999        
MSISDN起始号码  =  NULL  
MSISDN结束号码  =  NULL 
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-NRFSMSFSEGLIST.md`
