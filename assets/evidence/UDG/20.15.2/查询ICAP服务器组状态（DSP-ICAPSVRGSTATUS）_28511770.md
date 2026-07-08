# 查询ICAP服务器组状态（DSP ICAPSVRGSTATUS）

- [命令功能](#ZH-CN_CONCEPT_0000203228511770__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000203228511770__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000203228511770__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000203228511770__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000203228511770__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0000203228511770__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0000203228511770)

**适用NF：PGW-U、UPF**

该命令用来显示所有已经配置的ICAP Server Group或者指定名字的ICAP Server Group的工作状态信息。

#### [注意事项](#ZH-CN_CONCEPT_0000203228511770)

无。

#### [操作用户权限](#ZH-CN_CONCEPT_0000203228511770)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000203228511770)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ICAPSVRGRPNAME | ICAP服务器组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定ICAP Server Group的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格。不区分大小写。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0000203228511770)

- 查询所有已经配置的ICAP Server Group的工作状态信息：
  ```
  DSP ICAPSVRGSTATUS:;
  ```
  ```

  RETCODE = 0 操作成功

  ICAP服务器组状态
  ------------------------
  ICAP服务器组名称  Pod名称      ICAP服务器组状态  

  isg1              icapc-pod-0  Abnormal          
  isg2              icapc-pod-0  Abnormal          
  (结果个数 = 2)

  ---    END
  ```
- 查询指定名字的ICAP Server Group的状态信息：
  ```
  DSP ICAPSVRGSTATUS: ICAPSVRGRPNAME="isg1";
  ```
  ```

  RETCODE = 0 操作成功

  ICAP服务器组状态
  ------------------------
  ICAP服务器组名称  =  isg1
           Pod名称  =  icapc-pod-0
  ICAP服务器组状态  =  Abnormal
  (结果个数 = 1)

  ---    END
  ```

#### [输出结果说明](#ZH-CN_CONCEPT_0000203228511770)

| 输出项名称 | 输出项解释 |
| --- | --- |
| Pod名称 | 用于指定资源单元名称。 |
| ICAP服务器组状态 | ICAP Server Group的通信状态。 |

其余输出项请参见ADD ICAPSVRGRP的参数说明。
