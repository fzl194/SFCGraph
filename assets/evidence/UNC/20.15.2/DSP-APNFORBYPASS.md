# 显示APN锁定状态（DSP APNFORBYPASS）

- [命令功能](#ZH-CN_MMLREF_0000001229208339__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001229208339__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001229208339__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001229208339__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0000001229208339__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0000001229208339)

**适用NF：SGW-C、PGW-C、SMF、GGSN**

该命令用来查看存储Bypass场景下所有被锁定的APN实例名。

## [注意事项](#ZH-CN_MMLREF_0000001229208339)

无

#### [操作用户权限](#ZH-CN_MMLREF_0000001229208339)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001229208339)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN | 可选必选说明：可选参数<br>参数含义：该参数用于指定APN实例名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：<br>输入的APN名称需要符合APN命名规则。 |
| POD_ID | POD名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定POD名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~255。<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0000001229208339)

- 显示整机APN实例信息
  ```
  %%DSP APNFORBYPASS:;%%
  RETCODE = 0  操作成功。

  结果如下
  ------------------------
  APN          Pod Name  APN Lock Status  

  huawei.com   uncpod-1  locked           
  huawei2.com  uncpod-1  locked       
  huawei2.com  uncpod-0  locked
  huawei.com   uncpod-0  locked    
  (Number of results = 4)

  ---    END
  ```
- 显示指定APN实例信息
  ```
  %%DSP APNFORBYPASS: APN="huawei.com";%%
  RETCODE = 0  操作成功。

  结果如下
  ------------------------
  APN          Pod Name  APN Lock Status  

  huawei.com  uncpod-0  locked           
  huawei.com  uncpod-1  locked           
  (Number of results = 2)

  ---    END
  ```
- 显示指定POD中的APN实例信息
  ```
  %%DSP APNFORBYPASS: POD_ID="uncpod-0";%%
  RETCODE = 0  操作成功。

  结果如下
  ------------------------
  APN          Pod Name  APN Lock Status  

  huawei2.com  uncpod-0  locked           
  huawei.com   uncpod-0  locked           
  (Number of results = 2)

  ---    END
  ```

## [输出结果说明](#ZH-CN_MMLREF_0000001229208339)

| 输出项名称 | 输出项解释 |
| --- | --- |
| APN | 该参数用于指定APN实例名。 |
| POD名称 | 该参数用于指定POD名称。 |
| APN的锁定状态 | 此参数描述存储Bypass状态下APN的锁定状态。<br>取值说明：<br>- INVALID（无效）<br>- LOCKED（锁定） |
