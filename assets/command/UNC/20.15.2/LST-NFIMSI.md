---
id: UNC@20.15.2@MMLCommand@LST NFIMSI
type: MMLCommand
name: LST NFIMSI（查询IMSI号段）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NFIMSI
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
- IMSI号段管理
status: active
---

# LST NFIMSI（查询IMSI号段）

## 功能

![](查询IMSI号段（LST NFIMSI）_09651705.assets/notice_3.0-zh-cn_2.png)

该命令可能返回报文数据量较大，执行会影响系统性能，可通过增加查询参数减少返回结果报文。

**适用NF：NRF**

该命令用于在NRF上查询NF组支持的IMSI号段信息。

若要查询全部NF组支持的IMSI号段信息，请不要输入任何参数。

若要查询某个“NF组标识”的IMSI号段信息，请输入“NF组标识”或其他参数的组合。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFGROUPID | NF组标识 | 可选必选说明：可选参数<br>参数含义：该参数用于表示支持IMSI号段的NF组标识，可以通过LST NFGROUP进行查询，支持IMSI号段配置的NF类型仅包含AUSF、PCF、UDM、 UDR、CHF、CUSTOM_OCS。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~128。<br>默认值：无<br>配置原则：无 |
| SEGSTART | 号段起始字符串 | 可选必选说明：可选参数<br>参数含义：该参数用于表示IMSI号段配置的号段起始字符串。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是5~15。号段起始字符串长度为15位，不足15位时系统自动在末尾补0。十进制数字，号段的起始号码数值必须小于或等于号段结束号码的数值，且号段的起始号码不能以0开始，全0除外。<br>默认值：无<br>配置原则：无 |
| SEGEND | 号段结束字符串 | 可选必选说明：可选参数<br>参数含义：该参数用于表示IMSI号段配置的号段结束字符串。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是5~15。号段结束字符串长度为15位，不足15位时系统自动在末尾补9。十进制数字，号段的结束号码数值必须大于或等于起始号码的数值，且号段的结束号码不能为以0开始。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NFIMSI]] · IMSI号段（NFIMSI）

## 使用实例

- 查询NF组标识为nfgroup01，号段起始字符串为12345678904的IMSI号段信息：
  ```
  LST NFIMSI: NFGROUPID="nfgroup01", SEGSTART="12345678904";
  %%LST NFIMSI: NFGROUPID=" nfgroup01", SEGSTART="12345678904";%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
        NF组标识  =  nfgroup01
  号段起始字符串  =  123456789040000
  号段结束字符串  =  123456789059999

  (结果个数 = 1)
  ```
- 查询NFGROUPID为nfgroup01的全部IMSI号段信息：
  ```
  LST NFIMSI:NFGROUPID="nfgroup01";
  %%LST NFIMSI:NFGROUPID  =  "nfgroup01";%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------

  NF组标识   号段起始字符串   号段结束字符串
  nfgroup01  123456789040000  123456789059999
  nfgroup01  123456789140000  123456789169999

  (结果个数 = 2)
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-NFIMSI.md`
