# 查询PCC策略组（LST PCCPOLICYGRP）

- [命令功能](#ZH-CN_CONCEPT_0209897176__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0209897176__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0209897176__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0209897176__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0209897176__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0209897176__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0209897176)

**适用NF：PGW-C、SMF**

此命令用于查询PCC策略组。

支持批量查询，不输入查询条件，表示查询已经配置的所有PCC策略组。

#### [注意事项](#ZH-CN_CONCEPT_0209897176)

无。

#### [操作用户权限](#ZH-CN_CONCEPT_0209897176)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0209897176)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PCCPOLICYGRPNM | PCC策略组名称 | 可选必选说明：可选参数<br>参数含义：设置PCC策略组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0209897176)

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

#### [输出结果说明](#ZH-CN_CONCEPT_0209897176)

参见ADD PCCPOLICYGRP的参数说明。
