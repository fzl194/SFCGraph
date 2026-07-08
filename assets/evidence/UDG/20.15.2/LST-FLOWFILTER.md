# 查询流过滤器（LST FLOWFILTER）

- [命令功能](#ZH-CN_CONCEPT_0182837364__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0182837364__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0182837364__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0182837364__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0182837364__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0182837364__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0182837364)

**适用NF：PGW-U、UPF**

该命令用于查询所有的流过滤器实例，或者查询指定名称的流过滤器。

#### [注意事项](#ZH-CN_CONCEPT_0182837364)

无。

#### [操作用户权限](#ZH-CN_CONCEPT_0182837364)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0182837364)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| FLOWFILTERNAME | 流过滤器名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置流过滤器名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0182837364)

- 查询名为testflowfiltername的流过滤器：
  ```
  LST FLOWFILTER:FLOWFILTERNAME="testflowfiltername";
  ```
  ```
  %
  RETCODE = 0  操作成功

  流过滤器信息
  ------------
       流过滤器名称  =  testflowfiltername
  Tethering检测标识  =  过滤器
       过滤器组名称  =  NULL
     FlowFilter类型  =  用户配置
         配置域名称  =  NULL
  (结果个数 = 1)
  ---    END
  ```
- 查询所有的流过滤器：
  ```
  LST FLOWFILTER:;
  ```
  ```

  RETCODE = 0  操作成功

  流过滤器信息
  ------------
  流过滤器名称                 Tethering检测标识  过滤器组名称  FlowFilter类型  配置域名称

  testflowfiltername           过滤器             NULL          用户配置      NULL           
  flowfilter_dyh_053_125_001   无效               NULL          用户配置      NULL 
  (结果个数 = 2)
  ---    END
  ```

#### [输出结果说明](#ZH-CN_CONCEPT_0182837364)

参见ADD FLOWFILTER的参数说明。
