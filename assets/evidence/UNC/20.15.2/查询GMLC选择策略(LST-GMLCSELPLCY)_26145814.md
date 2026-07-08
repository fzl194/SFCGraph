# 查询GMLC选择策略(LST GMLCSELPLCY)

- [命令功能](#ZH-CN_MMLREF_0000001126145814__1.3.1.1)
- [注意事项](#ZH-CN_MMLREF_0000001126145814__1.3.2.1)
- [本地用户权限](#ZH-CN_MMLREF_0000001126145814__1.3.3.1)
- [网管用户权限](#ZH-CN_MMLREF_0000001126145814__1.3.4.1)
- [参数说明](#ZH-CN_MMLREF_0000001126145814__1.3.5.1)
- [使用实例](#ZH-CN_MMLREF_0000001126145814__1.3.6.1)
- [输出结果说明](#ZH-CN_MMLREF_0000001126145814__1.3.7.1)

#### [命令功能](#ZH-CN_MMLREF_0000001126145814)

**适用网元：MME**

该命令用于查询GMLC选择策略。

#### [注意事项](#ZH-CN_MMLREF_0000001126145814)

- 无。

#### [本地用户权限](#ZH-CN_MMLREF_0000001126145814)

manage-ug；system-ug；monitor-ug

#### [网管用户权限](#ZH-CN_MMLREF_0000001126145814)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_MMLREF_0000001126145814)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GMLCGRPID | GMLC选择策略组索引 | 可选必选说明：可选参数<br>参数含义：该参数在系统内唯一标识一个GMLC组。<br>数据来源：本端规划<br>取值范围：0~191<br>默认值：无<br>配置原则：该参数需要在<br>[**ADD GMLCSELGRP**](../GMLC选择策略组/增加GMLC选择策略组(ADD GMLCSELGRP)_26145810.md)<br>中事先配置，可执行<br>[**LST GMLCSELGRP**](../GMLC选择策略组/查询GMLC选择策略组(LST GMLCSELGRP)_72345411.md)<br>进行查看。 |
| LCSCLIENTTYPE | LCS客户端类型 | 可选必选说明：可选参数<br>参数含义：该参数用于标识LCS客户端类型。<br>数据来源：整网规划<br>取值范围：枚举类型。目前就紧急呼叫类型触发的NI-LR流程会选择GMLC，其他参数预留使用。<br>取值范围：<br>- “EMERGENCY_SERVICES(紧急业务)”<br>- “VALUE_ADDED_SERVICES(增值业务)”<br>- “PLMN_OPERATOR_SERVICES(运营商业务)”<br>- “LAWFUL_INTERCEPT_SERVICES(合法定位)”<br>默认值：无<br>配置原则：目前就紧急呼叫类型触发的NI-LR流程会选择GMLC，其他参数取值预留使用。 |
| LOCATIONTYPE | 位置区标识类型 | 可选必选说明：可选参数<br>参数含义：该参数标识位置标识类型。<br>数据来源：整网规划<br>取值范围：<br>- “ECI(小区标识)”<br>- “TAC(跟踪区编码)”<br>默认值：无 |
| TACBEGIN | 跟踪区起始编码 | 可选必选说明：条件可选参数<br>参数含义：该参数表示跟踪区起始编码<br>前提条件：该参数在"位置区标识类型"参数配置为"跟踪区编码"后生效。<br>数据来源：整网规划<br>取值范围：0x0000~0xFFFF<br>默认值：无 |
| ECIBEGIN | 小区起始标识 | 可选必选说明：条件可选参数<br>参数含义：该参数表示E-UTRAN小区起始标识。<br>前提条件：该参数在"位置区标识类型"参数配置为"小区标识"后生效。<br>数据来源：整网规划<br>取值范围：0~268435455<br>默认值：无 |

#### [使用实例](#ZH-CN_MMLREF_0000001126145814)

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

#### [输出结果说明](#ZH-CN_MMLREF_0000001126145814)

请参考 [**ADD GMLCSELPLCY**](增加GMLC选择策略(ADD GMLCSELPLCY)_72225491.md) 命令的参数标识。
