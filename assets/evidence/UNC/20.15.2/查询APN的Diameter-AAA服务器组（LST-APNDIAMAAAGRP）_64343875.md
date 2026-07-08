# 查询APN的Diameter AAA服务器组（LST APNDIAMAAAGRP）

- [命令功能](#ZH-CN_MMLREF_0264343875__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0264343875__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0264343875__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0264343875__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0264343875__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0264343875)

**适用NF：PGW-C**

此命令用于查询指定APN下的Diameter AAA组绑定关系或者所有APN下的Diameter AAA组绑定关系。

## [注意事项](#ZH-CN_MMLREF_0264343875)

无

#### [操作用户权限](#ZH-CN_MMLREF_0264343875)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0264343875)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定APN实例名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“ ” ”、“ ' ”特殊字符，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数使用<br>[**ADD APN**](../../../接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)<br>命令配置生成。 |

## [使用实例](#ZH-CN_MMLREF_0264343875)

- 查询名称为“apn”的APN下的Diameter AAA组绑定关系：
  ```
  %%LST APNDIAMAAAGRP: APN="apn";%%
  RETCODE = 0  操作成功

  APN的Diameter AAA服务器组
  -------------------------
           APN名称  =  apn
  Diameter AAA组名  =  diametergroup
  (结果个数 = 1)

  ---    END
  ```
- 查询所有APN下的Diameter AAA组绑定关系：
  ```
  %%LST APNDIAMAAAGRP:;%%
  RETCODE = 0  操作成功

  APN的Diameter AAA服务器组
  -------------------------
  APN名称  Diameter AAA组名  

  apn      diametergroup     
  apn2     diametergroup1    
  (结果个数 = 2)

  ---    END
  ```

## [输出结果说明](#ZH-CN_MMLREF_0264343875)

| 输出项名称 | 输出项解释 |
| --- | --- |
| APN名称 | 该参数用于指定APN实例名。 |
| Diameter AAA组名 | 该参数用于指定Diameter AAA组名。 |
