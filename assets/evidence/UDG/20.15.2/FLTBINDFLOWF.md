# 查询流过滤器的过滤器绑定关系（LST FLTBINDFLOWF）

- [命令功能](#ZH-CN_CONCEPT_0182837368__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0182837368__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0182837368__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0182837368__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0182837368__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0182837368__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0182837368)

**适用NF：PGW-U、UPF**

该命令用于查询过滤器与流过滤器绑定关系。

#### [注意事项](#ZH-CN_CONCEPT_0182837368)

无。

#### [操作用户权限](#ZH-CN_CONCEPT_0182837368)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0182837368)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| FLOWFILTERNAME | 流过滤器名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置流过滤器名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0182837368)

- 查询过滤器与名为testflowfiltername的流过滤器绑定关系：
  ```
  LST FLTBINDFLOWF:FLOWFILTERNAME="testflowfiltername";
  ```
  ```

  RETCODE = 0  操作成功。

  流过滤器的过滤器绑定信息
  ------------------------
  流过滤器名称  =  testflowfiltername
    过滤器名称  =  filter1
  (结果个数 = 1)
  ---    END
  ```
- 查询过滤器与流过滤器所有的绑定关系：
  ```
  LST FLTBINDFLOWF:;
  ```
  ```

  RETCODE = 0  操作成功。

  流过滤器的过滤器绑定信息
  ------------------------
  流过滤器名称           过滤器名称

  testflowfiltername     filter1   
  testflowfiltername2    filter    
  (结果个数 = 2)
  ---    END
  ```

#### [输出结果说明](#ZH-CN_CONCEPT_0182837368)

参见ADD FLTBINDFLOWF的参数说明。
