# 查询Diameter AAA服务器与Diameter AAA服务器绑定关系（LST UPDIAMAAABNDG）

- [命令功能](#ZH-CN_CONCEPT_0000206297314583__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000206297314583__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000206297314583__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000206297314583__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000206297314583__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0000206297314583__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0000206297314583)

**适用NF：UPF**

此命令用于查询指定Diameter AAA组下的Diameter AAA绑定配置信息或者查询所有Diameter AAA组下的Diameter AAA绑定配置信息。

#### [注意事项](#ZH-CN_CONCEPT_0000206297314583)

无。

#### [操作用户权限](#ZH-CN_CONCEPT_0000206297314583)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000206297314583)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GROUPNAME | Diameter AAA组名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定Diameter AAA组名。<br>数据来源：本端规划<br>取值范围：不区分大小写，不支持空格。<br>默认值：无<br>配置原则：该参数使用ADD UPDIAMAAAGRP命令配置生成。 |

#### [使用实例](#ZH-CN_CONCEPT_0000206297314583)

- 查询名称为“diametergroup”的Diameter AAA组下的Diameter AAA绑定配置信息：
  ```
  %%LST UPDIAMAAABNDG:GROUPNAME="diametergroup";
  ```
  ```
  %%
  RETCODE = 0  操作成功
  Diameter AAA服务器与Diameter AAA服务器绑定关系
  ----------------------------------------------
  Diameter AAA组名  =  diametergroup
        服务器类型  =  3GPP AAA服务器
            主机名  =  diameteraaa1
        主备用标记  =  主用
  (结果个数 = 1)
  ---    END
  ```
- 查询所有Diameter AAA组下的Diameter AAA绑定配置信息：
  ```
  %%LST UPDIAMAAABNDG:;
  ```
  ```
  %%
  RETCODE = 0  操作成功
  Diameter AAA服务器与Diameter AAA服务器绑定关系
  ----------------------------------------------
  Diameter AAA组名  服务器类型      主机名        主备用标记  
  diametergroup     3GPP AAA服务器  diameteraaa1  主用        
  diametergroup1    3GPP AAA服务器  diameteraaa1  主用        
  diametergroup1    3GPP AAA服务器  diameteraaa2  备用        
  (结果个数 = 3)
  ---    END
  ```

#### [输出结果说明](#ZH-CN_CONCEPT_0000206297314583)

| 输出项名称 | 输出项解释 |
| --- | --- |
| Diameter AAA组名 | 用于指定Diameter AAA组名。 |
| 服务器类型 | 用于指定服务器类型。 |
| 主机名 | 用于指定Diameter AAA。 |
| 主备用标记 | 用于指定服务器主备标记。 |
