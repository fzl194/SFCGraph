---
id: UNC@20.15.2@MMLCommand@LST DNAIUPFINFO
type: MMLCommand
name: LST DNAIUPFINFO（查询指定DNAI的UPF节点信息）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: DNAIUPFINFO
command_category: 查询类
applicable_nf:
- SMF
- PGW-C
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- PFCP接口管理
- UP管理
- DNAI UPF信息管理
status: active
---

# LST DNAIUPFINFO（查询指定DNAI的UPF节点信息）

## 功能

**适用NF：SMF、PGW-C**

该命令用于查询指定DNAI的UPF节点信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DNAI | 数据网络访问标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定数据网络访问标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| UPFINSTANCEID | UPF实例标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定UPF实例名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。该参数必须满足以下约束规则：1.如果输入为uuid格式（格式例如：a6a61c6f-0d3a-4221-b1da-424eda3ccf67）只能为A-F、a-f、0-9的字符。2.如果输入不为uuid格式，长度不能超过18且不允许输入只包含0-9和“.”的字符串，例如：1.2.3.4、不允许输入只包含十六进制数（A-F、a-f、0-9）和“:”的字符串，例如：1::2、FBFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF。不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@DNAIUPFINFO]] · 指定DNAI的UPF节点信息（DNAIUPFINFO）

## 使用实例

- 查询DNAI为huawei.com，UPF实例为upf1的节点信息：
  ```
  %%LST DNAIUPFINFO: DNAI="huawei.com",UPFINSTANCEID="upf1";%%
  RETCODE = 0  操作成功

  结果如下
  --------
  数据网络访问标识  =  huawei.com
       UPF实例标识  =  upf1
       UPF共享开关  =  继承
  (结果个数 = 1)

  ---    END
  ```
- 查询所有DNAI粒度的UPF节点信息：
  ```
  %%LST DNAIUPFINFO:;%%
  RETCODE = 0  操作成功

  结果如下
  --------
  数据网络访问标识  UPF实例标识  UPF共享开关

  huawei.com        upf1         继承
  huawei2.com       upf2         继承
  (结果个数 = 2)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-DNAIUPFINFO.md`
