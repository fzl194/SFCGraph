# 查询URL白名单（LST WHITEURLLIST）

- [命令功能](#ZH-CN_CONCEPT_0182837395__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0182837395__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0182837395__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0182837395__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0182837395__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0182837395__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0182837395)

**适用NF：PGW-U、UPF**

该命令用于查询白名单及白名单下的URL。

#### [注意事项](#ZH-CN_CONCEPT_0182837395)

无。

#### [操作用户权限](#ZH-CN_CONCEPT_0182837395)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0182837395)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| WHITELISTNAME | URL白名单列表名字 | 可选必选说明：可选参数<br>参数含义：该参数用于指定URL白名单列表名字。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不区分大小写。<br>默认值：无<br>配置原则：<br>- 如果没有配置该参数，则显示所有的白名单及白名单下的URL。<br>- 如果配置该参数，则显示指定白名单及白名单下的URL。 |

#### [使用实例](#ZH-CN_CONCEPT_0182837395)

- 查询所有白名单配置，可以执行如下命令：
  ```
  LST WHITEURLLIST:;
  ```
  ```

  RETCODE = 0  操作成功。

  URL白名单信息
  -------------
  URL白名单列表名字    URL           配置域名称

  test                test           NULL
  test2               test2          NULL
  (结果个数 = 2)
  ---    END
  ```
- 查询名称为test的白名单配置，可以执行如下命令：
  ```
  LST WHITEURLLIST: WHITELISTNAME="test";
  ```
  ```

  RETCODE = 0  操作成功。

  URL白名单信息
  -------------
        
  URL白名单列表名字  =  test
               URL  =  test
         配置域名称  =  NULL
  (结果个数 = 1)
  ---    END
  ```

#### [输出结果说明](#ZH-CN_CONCEPT_0182837395)

参见ADD WHITEURLLIST的参数说明。
