---
id: UNC@20.15.2@MMLCommand@LST PCCPOLICYGRP
type: MMLCommand
name: LST PCCPOLICYGRP（查询PCC策略组）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: PCCPOLICYGRP
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费和策略的业务管理
- 业务策略
- PCC策略组
status: active
---

# LST PCCPOLICYGRP（查询PCC策略组）

## 功能

**适用NF：PGW-C、SMF**

此命令用于查询PCC策略组。

支持批量查询，不输入查询条件，表示查询已经配置的所有PCC策略组。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PCCPOLICYGRPNM | PCC策略组名称 | 可选必选说明：可选参数<br>参数含义：设置PCC策略组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@PCCPOLICYGRP]] · PCC策略组（PCCPOLICYGRP）

## 使用实例

- 查询名称为test_pccgrp_1的PCC策略组：
  ```
  LST PCCPOLICYGRP: PCCPOLICYGRPNM="test_pccgrp_1";
  ```
  ```

  RETCODE = 0  操作成功。

  PCC策略组信息
  -------------
         PCC策略组名称  =  test_pccgrp_1
  使用量上报规则组名称  =  NULL
  Session级FUP累计标识  =  不使能
           Qos属性名称  =  NULL
  (结果个数 = 1)
  ---    END
  ```
- 查询所有的PCC策略组：
  ```
  LST PccPolicyGrp:;
  ```
  ```

  RETCODE = 0  操作成功。

  结果如下
  --------
  PCC策略组名称  使用量上报规则组名称    Session级FUP累计标识   Qos属性名称

  test_pccgrp_1       NULL                不使能                      NULL
  test_pccgrp_2       NULL                不使能                      NULL
  (结果个数 = 2)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-PCCPOLICYGRP.md`
