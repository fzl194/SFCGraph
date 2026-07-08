---
id: UNC@20.15.2@MMLCommand@LST VUPFIDBINDFUNC
type: MMLCommand
name: LST VUPFIDBINDFUNC（查询虚拟UPF实例标识绑定的功能）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: VUPFIDBINDFUNC
command_category: 查询类
applicable_nf:
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- PFCP接口管理
- UP管理
- 虚拟UPF管理
- 功能绑定管理
status: active
---

# LST VUPFIDBINDFUNC（查询虚拟UPF实例标识绑定的功能）

## 功能

**适用NF：SMF**

该命令用于查询虚拟UPF实例标识绑定的功能。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VUPFINSTANCEID | 虚拟UPF实例标识 | 可选必选说明：可选参数<br>参数含义：该参数用于虚拟UPF实例标识。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~36。该参数必须满足以下约束规则：1.如果输入为uuid格式（格式例如：a6a61c6f-0d3a-4221-b1da-424eda3ccf67）只能为A-F、a-f、0-9的字符。2.如果输入不为uuid格式，长度不能超过18且不允许输入只包含0-9和“.”的字符串，例如：1.2.3.4、不允许输入只包含十六进制数（A-F、a-f、0-9）和“:”的字符串，例如：1::2、FBFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF。不区分大小写。<br>默认值：无<br>配置原则：<br>该参数取值应与ADD VIRTUALUPFID中参数“VUPFINSTANCEID”保持一致，使用该前需通过ADD VIRTUALUPFID添加一组记录。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/VUPFIDBINDFUNC]] · 虚拟UPF实例标识的绑定功能（VUPFIDBINDFUNC）

## 使用实例

- 查看虚拟UPF实例标识为v_upf1绑定的功能：
  ```
  %%LST VUPFIDBINDFUNC:VUPFINSTANCEID="v_upf1";%%
  RETCODE = 0  操作成功。

  结果如下
  ------------------------
  虚拟UPF实例标识  =  v_upf1
         功能名称  =  2B2C漫游双DNN与共享UPF
  (结果个数 = 1)

  ---    END
  ```
- 查看所有虚拟UPF实例标识绑定的功能：
  ```
  %%LST VUPFIDBINDFUNC:;%%
  RETCODE = 0  操作成功

  结果如下
  --------
  虚拟UPF实例标识         功能名称
  v_upf1          2B2C漫游双DNN与共享UPF
  v_upf2          2B2C漫游双DNN与共享UPF
  (结果个数 = 2)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询虚拟UPF实例标识绑定的功能（LST-VUPFIDBINDFUNC）_61159693.md`
