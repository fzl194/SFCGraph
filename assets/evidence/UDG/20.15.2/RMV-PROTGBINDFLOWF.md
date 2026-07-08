# 删除流过滤器协议组绑定关系（RMV PROTGBINDFLOWF）

- [命令功能](#ZH-CN_CONCEPT_0182837376__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0182837376__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0182837376__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0182837376__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0182837376__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0182837376)

**适用NF：PGW-U、UPF**

![](删除流过滤器协议组绑定关系（RMV PROTGBINDFLOWF）_82837376.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，可能会影响业务。

该命令用于删除协议组与流过滤器绑定关系。

#### [注意事项](#ZH-CN_CONCEPT_0182837376)

- 该命令执行后立即生效。
- 如果不输入ProtGroupName，则代表删除该FlowFilterName对应的流过滤器下所有的协议组与流过滤器绑定关系。
- 该命令会导致用户匹配范围发生变化，可能导致性能下降。执行命令前请评估对性能的影响，如果无法评估请联系华为技术支持。

#### [操作用户权限](#ZH-CN_CONCEPT_0182837376)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0182837376)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| FLOWFILTERNAME | 流过滤器名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定流过滤器名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| PROTGROUPNAME | 协议组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置协议组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0182837376)

删除协议组与流过滤器绑定关系：“FLOWFILTERNAME”为“testflowfiltername”，“PROTGROUPNAME”为“p2p”：

```
RMV PROTGBINDFLOWF:FLOWFILTERNAME="testflowfiltername",PROTGROUPNAME ="p2p";
```
