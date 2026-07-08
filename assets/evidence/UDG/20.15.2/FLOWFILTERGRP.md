# 查询流过滤器组（LST FLOWFILTERGRP）

- [命令功能](#ZH-CN_CONCEPT_0186528844__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0186528844__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0186528844__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0186528844__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0186528844__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0186528844__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0186528844)

**适用NF：PGW-U、UPF**

该命令用于查询所有的流过滤器组信息，或者查询指定名称的流过滤器组信息。

#### [注意事项](#ZH-CN_CONCEPT_0186528844)

无。

#### [操作用户权限](#ZH-CN_CONCEPT_0186528844)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0186528844)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| FLWFLTRGRPNAME | 流过滤器组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定流过滤器组名字。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不区分大小写。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0186528844)

- 查询名为testflowfiltergrp的流过滤器组：
  ```
  LST FLOWFILTERGRP:FLWFLTRGRPNAME="testflowfiltergrp";
  ```
  ```

  RETCODE = 0  操作成功

    流过滤器组名称  =  testflowfiltergrp
      流过滤器名称  =  testflowfilter
  流过滤器逻辑分组  =  或
        配置域名称  =  NULL
  (结果个数 = 1)
  ---    END
  ```
- 查询所有的流过滤器组：
  ```
  LST FLOWFILTERGRP:;
  ```
  ```

  RETCODE = 0  操作成功

  流过滤器组名称     流过滤器名称     流过滤器逻辑分组        配置域名称

  testflowfiltergrp   testflowfilter   或                       NULL
  testflowfiltergrp2  testflowfilter2  或                       NULL
  (结果个数 = 2)
  ---    END
  ```

#### [输出结果说明](#ZH-CN_CONCEPT_0186528844)

参见ADD FLOWFILTERGRP的参数说明。
