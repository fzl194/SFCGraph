# 查询Diameter AAA服务器组（LST DIAMAAAGRP）

- [命令功能](#ZH-CN_MMLREF_0264343881__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0264343881__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0264343881__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0264343881__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0264343881__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0264343881)

**适用NF：PGW-C**

该命令用于查询Diameter AAA组配置信息。

## [注意事项](#ZH-CN_MMLREF_0264343881)

无

#### [操作用户权限](#ZH-CN_MMLREF_0264343881)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0264343881)

无

## [使用实例](#ZH-CN_MMLREF_0264343881)

- 当存在一条Diameter AAA组配置时，查询Diameter AAA组配置信息：
  ```
  %%LST DIAMAAAGRP:;%%
  RETCODE = 0  操作成功

  Diameter AAA组
  --------------
         Diameter AAA组名  =  diametergroup
  PDN GW Identity携带方式  =  P-GW主机名
  (结果个数 = 1)

  ---    END
  ```
- 当存在多条Diameter AAA组配置时，查询Diameter AAA组配置信息：
  ```
  %%LST DIAMAAAGRP:;%%
  RETCODE = 0  操作成功

  Diameter AAA组
  --------------
  Diameter AAA组名  PDN GW Identity携带方式  

  diametergroup     P-GW主机名               
  diametergroup1    P-GW IP地址              
  (结果个数 = 2)

  ---    END
  ```

## [输出结果说明](#ZH-CN_MMLREF_0264343881)

| 输出项名称 | 输出项解释 |
| --- | --- |
| Diameter AAA组名 | 该参数用于指定Diameter AAA组名。 |
| PDN GW Identity携带方式 | 该参数用于指定PDN GW Identity携带方式。 |
