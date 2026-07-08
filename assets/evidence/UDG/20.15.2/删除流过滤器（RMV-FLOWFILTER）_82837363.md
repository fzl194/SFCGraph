# 删除流过滤器（RMV FLOWFILTER）

- [命令功能](#ZH-CN_CONCEPT_0182837363__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0182837363__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0182837363__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0182837363__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0182837363__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0182837363)

**适用NF：PGW-U、UPF**

![](删除流过滤器（RMV FLOWFILTER）_82837363.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，会删除流过滤器下所有绑定关系以及流过滤器与流过滤器组之间的绑定关系。

该命令删除所有的流过滤器，或者删除指定名称的流过滤器。

#### [注意事项](#ZH-CN_CONCEPT_0182837363)

- 该命令执行后立即生效。
- 可以通过LST RULE查看该FlowFilter是否被Rule绑定，如果是，则必须先解除绑定关系，才能删除FlowFilter记录。
- 如果不输入FlowFilter名称， 需要执行多次。

#### [操作用户权限](#ZH-CN_CONCEPT_0182837363)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0182837363)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| FLOWFILTERNAME | 流过滤器名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置流过滤器名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0182837363)

删除流过滤器：“FlowFilterName”为“testflowfiltername”：

```
RMV FLOWFILTER:FLOWFILTERNAME="testflowfiltername";
```
