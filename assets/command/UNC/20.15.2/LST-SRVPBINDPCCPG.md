---
id: UNC@20.15.2@MMLCommand@LST SRVPBINDPCCPG
type: MMLCommand
name: LST SRVPBINDPCCPG（查询PCC组业务属性绑定）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SRVPBINDPCCPG
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
- PCC策略组业务属性绑定
status: active
---

# LST SRVPBINDPCCPG（查询PCC组业务属性绑定）

## 功能

**适用NF：PGW-C、SMF**

此命令用于查询PCC策略组业务属性绑定组合。

## 注意事项

- 不输入查询条件，表示查询已经配置的所有PCC策略组业务属性绑定组合。
- 只输入PCCPOLICYGRPNM，表示查询指定名称的PCC策略组业务属性绑定组合。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PCCPOLICYGRPNM | PCC策略组名称 | 可选必选说明：必选参数<br>参数含义：PCC策略组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| SRVPROPNAME | 业务属性名称 | 可选必选说明：可选参数<br>参数含义：业务属性名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SRVPBINDPCCPG]] · PCC组业务属性绑定（SRVPBINDPCCPG）

## 使用实例

- 查询PCC策略组名称为test_pccgrp_1，业务属性名称为test_srvp_1的PCC策略组业务属性绑定组合：
  ```
  LST SRVPBINDPCCPG: PCCPOLICYGRPNM="test_pccgrp_1",SRVPROPNAME="test_srvp_1";
  ```
  ```

  RETCODE = 0  操作成功。

  业务属性绑定PCC策略组信息
  -------------------------
         PCC策略组名称  =  test_pccgrp_1
          业务属性名称  =  test_srvp_1
          计费属性名称  =  NULL
       PCC动作属性名称  =  NULL
          扩展属性名称  =  NULL
            监控属性值  =  NULL
  Session级FUP累计标识  =  不使能
  (结果个数 = 1)
  ---    END
  ```
- 查询PCC策略组名称为test_pccgrp_1的PCC策略组业务属性绑定组合：
  ```
  LST SRVPBINDPCCPG: PCCPOLICYGRPNM="test_pccgrp_1";
  ```
  ```

  RETCODE = 0  操作成功。

  业务属性绑定PCC策略组信息
  -------------------------
  PCC策略组名称    业务属性名称    计费属性名称    PCC动作属性名称    扩展属性名称    监控属性值    Session级FUP累计标识

  test_pccgrp_1    test_srvp_1     NULL            NULL               NULL            NULL          不使能              
  test_pccgrp_1    test_srvp_2     NULL            NULL               NULL            NULL          不使能              
  (结果个数 = 2)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-SRVPBINDPCCPG.md`
