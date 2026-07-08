# 查询前缀URL组（LST PREFIXURLGRP）

- [命令功能](#ZH-CN_CONCEPT_0186526656__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0186526656__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0186526656__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0186526656__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0186526656__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0186526656__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0186526656)

**适用NF：PGW-U、UPF**

该命令用于查询所有的前缀URL组，或者查询指定名称的前缀URL组。

#### [注意事项](#ZH-CN_CONCEPT_0186526656)

无。

#### [操作用户权限](#ZH-CN_CONCEPT_0186526656)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0186526656)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PREURLGRPNAME | 前缀URL组名字 | 可选必选说明：可选参数<br>参数含义：该参数用于指定前缀URL组名字。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不区分大小写。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0186526656)

- 查询名为testurlgroup的前缀URL组：
  ```
  LST PREFIXURLGRP: PREURLGRPNAME="testurlgroup ";
  ```
  ```

  RETCODE = 0  操作成功。

  Prefixed URL组信息
  ------------------
  前缀URL组名称    前缀URL        配置域名称

  testurlgroup     www.huawei.com  NULL
  testurlgroup     www.example.com NULL
  (结果个数 = 2)
  ---    END
  ```
- 查询所有的前缀URL组：
  ```
  LST PREFIXURLGRP:;
  ```
  ```

  RETCODE = 0  操作成功。

  Prefixed URL组信息
  ------------------
  前缀URL组名称    前缀URL          配置域名称

  testurlgroup     www.huawei.com    NULL
  testurlgroup     www.example.com   NULL
  testurlgroup2    www.example1.com  NULL
  (结果个数 = 3)
  ---    END
  ```

#### [输出结果说明](#ZH-CN_CONCEPT_0186526656)

参见ADD PREFIXURLGRP的参数说明。
