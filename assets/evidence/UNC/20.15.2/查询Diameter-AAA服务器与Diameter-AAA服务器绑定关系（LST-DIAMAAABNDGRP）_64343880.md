# 查询Diameter AAA服务器与Diameter AAA服务器绑定关系（LST DIAMAAABNDGRP）

- [命令功能](#ZH-CN_MMLREF_0264343880__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0264343880__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0264343880__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0264343880__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0264343880__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0264343880)

**适用NF：PGW-C**

此命令用于查询指定Diameter AAA组下的Diameter AAA绑定配置信息或者查询所有Diameter AAA组下的Diameter AAA绑定配置信息。

## [注意事项](#ZH-CN_MMLREF_0264343880)

无

#### [操作用户权限](#ZH-CN_MMLREF_0264343880)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0264343880)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GROUPNAME | Diameter AAA组名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定Diameter AAA组名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~31。不区分大小写，不支持空格。<br>默认值：无<br>配置原则：<br>该参数使用<br>[**ADD DIAMAAAGRP**](../Diameter AAA组/增加Diameter AAA服务器组（ADD DIAMAAAGRP）_64343820.md)<br>命令配置生成。 |

## [使用实例](#ZH-CN_MMLREF_0264343880)

- 查询名称为“diametergroup”的Diameter AAA组下的Diameter AAA绑定配置信息：
  ```
  %%LST DIAMAAABNDGRP:GROUPNAME="diametergroup";%%
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
  %%LST DIAMAAABNDGRP:;%%
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

## [输出结果说明](#ZH-CN_MMLREF_0264343880)

| 输出项名称 | 输出项解释 |
| --- | --- |
| Diameter AAA组名 | 该参数用于指定Diameter AAA组名。 |
| 服务器类型 | 该参数用于指定服务器类型。 |
| 主机名 | 该参数用于指定Diameter AAA。 |
| 主备用标记 | 该参数用于指定服务器主备标记。 |
