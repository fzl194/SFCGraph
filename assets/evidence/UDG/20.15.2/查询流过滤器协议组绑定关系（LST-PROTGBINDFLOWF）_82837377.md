# 查询流过滤器协议组绑定关系（LST PROTGBINDFLOWF）

- [命令功能](#ZH-CN_CONCEPT_0182837377__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0182837377__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0182837377__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0182837377__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0182837377__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0182837377__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0182837377)

**适用NF：PGW-U、UPF**

该命令用于查询协议组与流过滤器绑定关系。

#### [注意事项](#ZH-CN_CONCEPT_0182837377)

无。

#### [操作用户权限](#ZH-CN_CONCEPT_0182837377)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0182837377)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| FLOWFILTERNAME | 流过滤器名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定流过滤器名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0182837377)

- 查询协议组与名为testflowfiltername的流过滤器绑定关系：
  ```
  LST PROTGBINDFLOWF:FLOWFILTERNAME="testflowfiltername";
  ```
  ```

  RETCODE = 0  操作成功。

  流过滤器协议组绑定信息
  ----------------------
  流过滤器名称  =  testflowfiltername
    协议组名称  =  group1
  (结果个数 = 1)
  ---    END
  ```
- 查询协议组与流过滤器的所有绑定关系：
  ```
  LST PROTGBINDFLOWF:;
  ```
  ```

  RETCODE = 0  操作成功。

  流过滤器协议组绑定信息
  ----------------------
  流过滤器名称           协议组名称  

  testflowfiltername     group1      
  testflowfiltername2    web_browsing
  (结果个数 = 2)
  ---    END
  ```

#### [输出结果说明](#ZH-CN_CONCEPT_0182837377)

参见ADD PROTGBINDFLOWF的参数说明。
