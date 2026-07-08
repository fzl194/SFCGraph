---
id: UNC@20.15.2@MMLCommand@LST GMLCSELPLCY
type: MMLCommand
name: LST GMLCSELPLCY（查询GMLC选择策略）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: GMLCSELPLCY
command_category: 查询类
applicable_nf:
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- LCS
- GMLC选择策略
status: active
---

# LST GMLCSELPLCY（查询GMLC选择策略）

## 功能

**适用网元：MME**

该命令用于查询GMLC选择策略。

## 注意事项

- 无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GMLCGRPID | GMLC选择策略组索引 | 可选必选说明：可选参数<br>参数含义：该参数在系统内唯一标识一个GMLC组。<br>数据来源：本端规划<br>取值范围：0~191<br>默认值：无<br>配置原则：该参数需要在<br>[**ADD GMLCSELGRP**](../GMLC选择策略组/增加GMLC选择策略组(ADD GMLCSELGRP)_26145810.md)<br>中事先配置，可执行<br>[**LST GMLCSELGRP**](../GMLC选择策略组/查询GMLC选择策略组(LST GMLCSELGRP)_72345411.md)<br>进行查看。 |
| LCSCLIENTTYPE | LCS客户端类型 | 可选必选说明：可选参数<br>参数含义：该参数用于标识LCS客户端类型。<br>数据来源：整网规划<br>取值范围：枚举类型。目前就紧急呼叫类型触发的NI-LR流程会选择GMLC，其他参数预留使用。<br>取值范围：<br>- “EMERGENCY_SERVICES(紧急业务)”<br>- “VALUE_ADDED_SERVICES(增值业务)”<br>- “PLMN_OPERATOR_SERVICES(运营商业务)”<br>- “LAWFUL_INTERCEPT_SERVICES(合法定位)”<br>默认值：无<br>配置原则：目前就紧急呼叫类型触发的NI-LR流程会选择GMLC，其他参数取值预留使用。 |
| LOCATIONTYPE | 位置区标识类型 | 可选必选说明：可选参数<br>参数含义：该参数标识位置标识类型。<br>数据来源：整网规划<br>取值范围：<br>- “ECI(小区标识)”<br>- “TAC(跟踪区编码)”<br>默认值：无 |
| TACBEGIN | 跟踪区起始编码 | 可选必选说明：条件可选参数<br>参数含义：该参数表示跟踪区起始编码<br>前提条件：该参数在"位置区标识类型"参数配置为"跟踪区编码"后生效。<br>数据来源：整网规划<br>取值范围：0x0000~0xFFFF<br>默认值：无 |
| ECIBEGIN | 小区起始标识 | 可选必选说明：条件可选参数<br>参数含义：该参数表示E-UTRAN小区起始标识。<br>前提条件：该参数在"位置区标识类型"参数配置为"小区标识"后生效。<br>数据来源：整网规划<br>取值范围：0~268435455<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/GMLCSELPLCY]] · GMLC选择策略（GMLCSELPLCY）

## 使用实例

1. 查询索引为0的GMLC选择策略组内的所有选择策略。
  LST GMLCSELPLCY: GMLCGRPID=0;
  ```
  %%LST GMLCSELPLCY:;%%
  RETCODE = 0  操作成功。

  输出结果如下
  --------------
   GMLC选择策略组索引  LCS客户端类型  位置区标识类型  跟踪区起始编码  跟踪区结束编码  小区起始标识  小区结束标识  GMLC域名    Diameter路由组索引  描述  

   0                   紧急业务       跟踪区编码      0x0A            0x0A            NULL          NULL          huawei.com  0                   noname
   0                   紧急业务       小区标识        NULL            NULL            0             0             huawei.com  0                   noname
  (结果个数 = 2)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询GMLC选择策略(LST-GMLCSELPLCY)_26145814.md`
