# 查询扩展过滤器（LST EXTENDEDFILTER）

- [命令功能](#ZH-CN_CONCEPT_0182837382__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0182837382__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0182837382__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0182837382__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0182837382__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0182837382__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0182837382)

**适用NF：PGW-U、UPF**

该命令用于查询指定的ExtendedFilter的配置。如果不指定可选参数，该命令将显示所有ExtendedFilter配置信息；如果指定EXTFLTNAME，则显示该扩展过滤器的配置信息。

#### [注意事项](#ZH-CN_CONCEPT_0182837382)

无。

#### [操作用户权限](#ZH-CN_CONCEPT_0182837382)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0182837382)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| EXTFLTNAME | 扩展过滤器名字 | 可选必选说明：可选参数<br>参数含义：该参数用于设置扩展过滤器名字。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。字符串形式，不支持空格。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0182837382)

- 查询所有扩展过滤器的配置：
  ```
  LST EXTENDEDFILTER:;
  ```
  ```

  RETCODE = 0  操作成功。

  扩展过滤器信息
  --------------
  扩展过滤器名字    扩展过滤器记录类型    URL               ContentType    客户端类型    Url后缀    后缀名匹配标识    分组匹配标识    配置域名称

  eftest            URL                   www.example.com      NULL           NULL          NULL       不使能            不使能      NULL
  testextflt        URL                   www.huawei.com    NULL           NULL          NULL       不使能            不使能         NULL
  (结果个数 = 2)
  ---    END
  ```
- 查询一个名字为eftest的扩展过滤器的配置：
  ```
  LST EXTENDEDFILTER:EXTFLTNAME="eftest";
  ```
  ```

  RETCODE = 0  操作成功。

  扩展过滤器信息
  --------------
      扩展过滤器名字  =  eftest
  扩展过滤器记录类型  =  URL
                 URL  =  www.example.com
         ContentType  =  NULL
          客户端类型  =  NULL
             Url后缀  =  NULL
      后缀名匹配标识  =  不使能
        分组匹配标识  =  不使能
          配置域名称  =  NULL
  (结果个数 = 1)
  ---    END
  ```

#### [输出结果说明](#ZH-CN_CONCEPT_0182837382)

| 输出项名称 | 输出项解释 |
| --- | --- |
| 扩展过滤器记录类型 | 用于设置扩展过滤器记录类型。 |

其余输出项请参见ADD EXTENDEDFILTER的参数说明。
