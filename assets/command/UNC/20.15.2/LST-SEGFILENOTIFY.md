---
id: UNC@20.15.2@MMLCommand@LST SEGFILENOTIFY
type: MMLCommand
name: LST SEGFILENOTIFY（查询号段文件通知记录）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SEGFILENOTIFY
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
- 号段导入通知管理
status: active
---

# LST SEGFILENOTIFY（查询号段文件通知记录）

## 功能

**适用NF：NRF**

该命令用于查询触发订阅通知的导入IMSI/MSISDN号段信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFTYPE | NF类型 | 可选必选说明：可选参数<br>参数含义：该参数用于表示支持IMSI/MSISDN号段支持的NF类型。<br>数据来源：本端规划<br>取值范围：<br>- AUSF（AUSF）<br>- PCF（PCF）<br>- UDM（UDM）<br>- UDR（UDR）<br>- CHF（CHF）<br>- CUSTOM_OCS（CUSTOM_OCS）<br>默认值：无<br>配置原则：<br>支持IMSI号段配置的NF类型仅包含AUSF、PCF、UDM、 UDR、CHF、CUSTOM_OCS。支持MSISDN号段配置的NF类型仅包含PCF、UDM、 UDR、CHF、CUSTOM_OCS。 |
| SEGTYPE | 号段类型 | 可选必选说明：可选参数<br>参数含义：该参数用于表示号段类型。<br>数据来源：本端规划<br>取值范围：<br>- IMSI（IMSI）<br>- MSISDN（MSISDN）<br>默认值：无<br>配置原则：无 |
| NFGROUPID | NF组标识 | 可选必选说明：可选参数<br>参数含义：该参数用于表示待配置IMSI/MSISDN号段的NF组标识。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~128。<br>默认值：无<br>配置原则：无 |
| SEGSTART | 号段起始字符串 | 可选必选说明：可选参数<br>参数含义：该参数用于表示号段的起始号码。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是5~15。当号段类型为IMSI时，号段起始字符串长度为15位，不足15位时系统自动在末尾补0。十进制数字，号段的起始号码数值必须小于或等于号段结束号码的数值，且号段的起始号码不能以0开始，全0除外。号段类型为MSISDN时，号段的起始号码必须与结束号码长度保持一致，数值必须小于或等于结束号码的数值，且号段的起始号码不能以0开始，全0除外。<br>默认值：无<br>配置原则：无 |
| SEGEND | 号段结束字符串 | 可选必选说明：可选参数<br>参数含义：该参数用于表示号段的结束号码。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是5~15。当号段类型为IMSI时，号段结束字符串长度为15位，不足15位时系统自动在末尾补9。十进制数字，号段的结束号码数值必须大于或等于起始号码的数值，且号段的结束号码不能为以0开始。号段类型为MSISDN时，号段的结束号码必须与起始号码长度保持一致，数值大于或等于起始号码的数值，且号段的结束号码不能以0开始。<br>默认值：无<br>配置原则：无 |
| ISFROMAUSFUDM | 是否来源于AUSFUDM表 | 可选必选说明：该参数在"NFTYPE"配置为"AUSF"、"UDM"时为条件可选参数。<br>参数含义：该参数表示数据是否来源于AUSFUDM表。<br>数据来源：本端规划<br>取值范围：<br>- TRUE(TRUE)<br>- FALSE(FALSE)<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SEGFILENOTIFY]] · 号段文件通知记录（SEGFILENOTIFY）

## 使用实例

- 查询当前缓存的百万号段订阅通知数据：
  ```
  LST SEGFILENOTIFY:;
  %%LST SEGFILENOTIFY:;%%
  RETCODE = 0  执行成功

  结果如下
  ------------------------
  号段类型  NF Type  NF组标识  号段起始字符串    号段结束字符串    是否来源于AUSFUDM表
  IMSI      PCF      pcf       111110000000000   111119999999999   FALSE
  MSISDN    PCF      pcf       111111            111119            FALSE
  (结果个数 = 2)
  ```
- 查询IMSI类型的订阅通知数据：
  ```
  LST SEGFILENOTIFY: SEGTYPE=IMSI;
  %%LST SEGFILENOTIFY: SEGTYPE=IMSI;%%
  RETCODE = 0  执行成功

  结果如下
  -------------------------
             号段类型  =  IMSI
               NF类型  =  PCF
             NF组标识  =  pcf
       号段起始字符串  =  111110000000000
       号段结束字符串  =  111119999999999
  是否来源于AUSFUDM表  =  FALSE

  (结果个数 = 1)
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-SEGFILENOTIFY.md`
