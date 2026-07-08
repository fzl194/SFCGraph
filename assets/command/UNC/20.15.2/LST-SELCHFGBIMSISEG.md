---
id: UNC@20.15.2@MMLCommand@LST SELCHFGBIMSISEG
type: MMLCommand
name: LST SELCHFGBIMSISEG（查询IMSI号段和该号段绑定的主备CHF组）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SELCHFGBIMSISEG
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 融合计费
- CHF选择
status: active
---

# LST SELCHFGBIMSISEG（查询IMSI号段和该号段绑定的主备CHF组）

## 功能

**适用NF：PGW-C、SMF、GGSN**

该命令用于查询IMSI号段和该号段绑定的主备CHF组。

## 注意事项

不输入任何参数默认查询所有配置。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MODE | 查询模式 | 可选必选说明：可选参数<br>参数含义：该参数用于设置查询模式。<br>数据来源：本端规划<br>取值范围：<br>- IMSI（使用IMSI查询IMSI号段和该号段绑定的主备CHF组）<br>- IMSISEG（使用IMSI号段查询该号段绑定的主备CHF组）<br>默认值：无<br>配置原则：无 |
| IMSI | 用户的IMSI | 可选必选说明：该参数在"MODE"配置为"IMSI"时为条件必选参数。<br>参数含义：该参数用于设置用户的IMSI。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是5~15。用户的IMSI长度为15位，不足15位时系统自动在末尾补0。十进制数字，IMSI不能以0开始，全0除外。<br>默认值：无<br>配置原则：无 |
| SEGSTART | 号段起始字符串 | 可选必选说明：该参数在"MODE"配置为"IMSISEG"时为条件必选参数。<br>参数含义：该参数用于设置绑定的IMSI号段的起始字符串。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是5~15。号段起始字符串长度为15位，不足15位时系统自动在末尾补0。十进制数字，号段的起始号码数值必须小于或等于号段结束号码的数值，且号段的起始号码不能以0开始，全0除外。<br>默认值：无<br>配置原则：无 |
| SEGEND | 号段结束字符串 | 可选必选说明：该参数在"MODE"配置为"IMSISEG"时为条件必选参数。<br>参数含义：该参数用于设置绑定的IMSI号段的结束字符串。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是5~15。号段结束字符串长度为15位，不足15位时系统自动在末尾补9。十进制数字，号段的结束号码数值必须大于或等于起始号码的数值，且号段的结束号码不能以0开始。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SELCHFGBIMSISEG]] · IMSI号段与CHF组的绑定关系（SELCHFGBIMSISEG）

## 使用实例

- 查询所有配置：
  ```
  %%LST SELCHFGBIMSISEG:;%%
  RETCODE = 0  操作成功。

  结果如下
  ------------------------
  号段起始字符串   号段结束字符串   主CHF组  备CHF组   
  
  123456789010000  123456789059999  CHF1       CHF2  
  460010000000000  460019999999999  CHF1       CHF2  
  (结果个数 = 2)

  ---    END
  ```
- 基于IMSI查询选择CHF处理：
  ```
  %%LST SELCHFGBIMSISEG: MODE=IMSI, IMSI="12345678903";%%
  RETCODE = 0  操作成功。

  结果如下
  ------------------------
  号段起始字符串  =  123456789010000
  号段结束字符串  =  123456789059999
  主CHF组  =  CHF1
  备CHF组  =  CHF2
  (结果个数 = 1)

  ---    END
  ```
- 基于IMSI号段查询选择CHF处理：
  ```
  %%LST SELCHFGBIMSISEG: MODE=IMSISEG, SEGSTART="12345678901", SEGEND="12345678905";%%
  RETCODE = 0  操作成功。

  结果如下
  ------------------------
  号段起始字符串  =  123456789010000
  号段结束字符串  =  123456789059999
  主CHF组  =  CHF1
  备CHF组  =  CHF2
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-SELCHFGBIMSISEG.md`
