# 查询Diameter路由域名信息（LST UPDIAMRTREALM）

- [命令功能](#ZH-CN_CONCEPT_0000206145195196__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000206145195196__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000206145195196__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000206145195196__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000206145195196__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0000206145195196__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0000206145195196)

**适用NF：UPF**

该命令用于查看已配置的Diameter路由相关参数。

#### [注意事项](#ZH-CN_CONCEPT_0000206145195196)

无。

#### [操作用户权限](#ZH-CN_CONCEPT_0000206145195196)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000206145195196)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| REALMNAME | Diameter域名名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定Diameter路由的realm名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～127。不支持空格，必须是可见ASCII码，由软参BIT 2670控制是否区分大小写。<br>默认值：无<br>配置原则：无 |
| APPLICATION | Diameter应用 | 可选必选说明：可选参数<br>参数含义：该参数用于指定Diameter路由的Diameter应用。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- SWM：SWM接口应用。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0000206145195196)

- 显示指定realm名的Diameter路由参数，realm名为“example.com”：
  ```
  LST UPDIAMRTREALM:REALMNAME="example.com";
  ```
  ```

  RETCODE = 0  操作成功
  Diameter路由信息
  ----------------
  Diameter域名名称  =  example.com
      Diameter应用  =  SWM
      路由选择模式  =  主备
      Failover开关  =  允许
      自动倒回开关  =  允许
  (结果个数 = 1)
  ---    END
  ```
- 显示所有Diameter路由信息：
  ```
  LST UPDIAMRTREALM:;
  ```
  ```

  RETCODE = 0  操作成功
  Diameter路由信息
  ----------------
  Diameter域名名称  Diameter应用  路由选择模式  Failover开关  自动倒回开关  
  default           SWM           基于会话轮循  禁止          禁止          
  example.com       SWM           主备          允许          允许          
  (结果个数 = 2)
  ---    END
  ```

#### [输出结果说明](#ZH-CN_CONCEPT_0000206145195196)

参见ADD UPDIAMRTREALM的参数说明。
