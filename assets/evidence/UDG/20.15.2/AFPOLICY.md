# 查询防欺诈策略配置（LST AFPOLICY）

- [命令功能](#ZH-CN_CONCEPT_0186527026__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0186527026__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0186527026__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0186527026__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0186527026__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0186527026__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0186527026)

**适用NF：PGW-U、UPF**

该命令用于查询判断出欺诈行为后的处理策略。

#### [注意事项](#ZH-CN_CONCEPT_0186527026)

无。

#### [操作用户权限](#ZH-CN_CONCEPT_0186527026)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0186527026)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| AFPOLICYTYPE | 防欺诈策略类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定防欺诈策略类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DNS：指定DNS防欺诈。<br>- HTTP：指定HTTP防欺诈。<br>- HTTPS：指定HTTPS防欺诈。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0186527026)

- 假如运营商需要查询判断出DNS欺诈行为后的处理策略，则命令如下：
  ```
  LST AFPOLICY:AFPOLICYTYPE=DNS;
  ```
  ```

  RETCODE = 0  操作成功。

  防欺诈策略信息
  --------------
  防欺诈策略类型  =  DNS防欺诈
   PCC策略组名称  =  pccpolicygroup
  防欺诈应用标识  =  NULL
    分类属性名称  =  NULL
  (结果个数 = 1)
  ---    END
  ```
- 假如运营商需要查询判断出欺诈行为后的处理策略，则命令如下：
  ```
  LST AFPOLICY:;
  ```
  ```

  RETCODE = 0  操作成功。

  防欺诈策略信息
  --------------
  防欺诈策略类型    PCC策略组名称     防欺诈应用标识    分类属性名称

  DNS防欺诈         pccpolicygroup    NULL              NULL        
  HTTP防欺诈        pccpolicygroup    NULL              NULL        
  (结果个数 = 2)
  ---    END
  ```

#### [输出结果说明](#ZH-CN_CONCEPT_0186527026)

参见ADD AFPOLICY的参数说明。
