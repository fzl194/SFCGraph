---
id: UDG@20.15.2@MMLCommand@DSP FEIMCFWDTAB
type: MMLCommand
name: DSP FEIMCFWDTAB（显示FEI组播转发表项统计信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: FEIMCFWDTAB
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- 转发引擎实例FEI
- FEI消息统计
status: active
---

# DSP FEIMCFWDTAB（显示FEI组播转发表项统计信息）

## 功能

该命令用于显示FEI组播转发表项统计信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IIFTYPE | 入接口类型 | 可选必选说明：可选参数<br>参数含义：该参数表示入接口类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ifname：接口名称。<br>- register：注册接口。<br>- pae：PAE。<br>默认值：无 |
| OIFTYPE | 出接口类型 | 可选必选说明：可选参数<br>参数含义：该参数表示出接口类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ifname：接口名称。<br>- none：None。<br>- pae：PAE。<br>默认值：无 |
| STATICSTICSFLG | 查询模式 | 可选必选说明：必选参数<br>参数含义：该参数表示查询模式。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- Table：表项查询。<br>- Statistic：统计查询。<br>默认值：无 |
| INSTANCENAME | VPN实例名称 | 可选必选说明：条件必选参数<br>前提条件：该参数在“STATICSTICSFLG”配置为“Table”时为必选参数。<br>可选必选说明：条件可选参数<br>前提条件：该参数在“STATICSTICSFLG”配置为“Statistic”时为可选参数。<br>参数含义：该参数表示VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。区分大小写。<br>默认值：无 |
| SOURCEADDR | 源IP地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“STATICSTICSFLG”配置为“Table”时为必选参数。<br>可选必选说明：条件可选参数<br>前提条件：该参数在“STATICSTICSFLG”配置为“Statistic”时为可选参数。<br>参数含义：该参数表示源IP地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无 |
| GROUPADDR | 组IP地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“STATICSTICSFLG”配置为“Table”时为必选参数。<br>可选必选说明：条件可选参数<br>前提条件：该参数在“STATICSTICSFLG”配置为“Statistic”时为可选参数。<br>参数含义：该参数表示组播组IP地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无 |
| IIFNAME | 入接口名称 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IIFTYPE”配置为“ifname”时为必选参数。<br>参数含义：该参数用于指定表项的入接口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～47。<br>默认值：无<br>配置原则：使用LST INTERFACE命令查看可用接口。 |
| OIFNAME | 出接口名称 | 可选必选说明：条件必选参数<br>前提条件：该参数在“OIFTYPE”配置为“ifname”时为必选参数。<br>参数含义：该参数用于指定表项的出接口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～47。<br>默认值：无<br>配置原则：使用LST INTERFACE命令查看可用接口。 |
| TB | TB | 可选必选说明：条件必选参数<br>前提条件：该参数在“OIFTYPE”配置为“pae”时为必选参数。<br>参数含义：该参数用于指定TB的值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～9223372036854775807。<br>默认值：无 |
| TP | TP | 可选必选说明：条件必选参数<br>前提条件：该参数在“OIFTYPE”配置为“pae”时为必选参数。<br>参数含义：该参数用于指定TP的值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无 |
| RUNAME | RU名称 | 可选必选说明：可选参数<br>参数含义：该参数表示资源单元名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：使用DSP RU查看RU名称。 |
| OIFFILTERMODE | 出接口过滤模式 | 可选必选说明：条件必选参数<br>前提条件：该参数在“OIFTYPE”配置为“ifname” 或 “pae”时为必选参数。<br>参数含义：该参数指定出接口过滤模式。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- include：Include。<br>- exclude：Exclude。<br>- match：Match。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/FEIMCFWDTAB]] · FEI组播转发表项统计信息（FEIMCFWDTAB）

## 使用实例

- 显示FEI组播转发表项统计信息：
  ```
  DSP FEIMCFWDTAB: STATICSTICSFLG=Statistic;
  ```
  ```
  RETCODE = 0  操作成功

  结果如下
  ------------------------
  正在注册入接口的表项个数 = 0
    有注册入接口的表项个数 = 0
      没有出接口的表项个数 = 0
            匹配的表项个数 = 1
                总表项个数 = 1
  (结果个数 = 1)
  ---    END
  ```
- 显示FEI组播转发表项信息：
  ```
  DSP FEIMCFWDTAB: STATICSTICSFLG=Table, INSTANCENAME="_public_", SOURCEADDR="0.0.0.0", GROUPADDR="239.0.0.1";
  ```
  ```
  RETCODE = 0  操作成功

  结果如下
  ------------------------
         表项序号 = 1
      VPN实例名称 = _public_
         源IP地址 = 0.0.0.0
         组IP地址 = 239.0.0.1
           TMG ID = 2
   匹配的报文个数 = 176736
   匹配的字节个数 = 22622208
  WrongIF报文个数 = 0
     转发报文个数 = 176736
   转发的字节个数 = 22622208
      入接口列表  =  LoopBack1,PAE 
      出接口列表  =  PAE 00 0 
  (结果个数 = 1)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示FEI组播转发表项统计信息（DSP-FEIMCFWDTAB）_49801946.md`
