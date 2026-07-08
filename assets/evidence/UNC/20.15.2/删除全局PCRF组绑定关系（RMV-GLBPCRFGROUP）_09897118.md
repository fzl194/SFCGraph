# 删除全局PCRF组绑定关系（RMV GLBPCRFGROUP）

- [命令功能](#ZH-CN_CONCEPT_0209897118__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0209897118__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0209897118__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0209897118__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0209897118__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0209897118)

**适用NF：PGW-C、GGSN**

此命令用来删除PCRF分组和指定的号段绑定，以及绑定优先级。

#### [注意事项](#ZH-CN_CONCEPT_0209897118)

- 该命令执行后只对新激活用户生效。
- 该命令支持批量删除。

#### [操作用户权限](#ZH-CN_CONCEPT_0209897118)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0209897118)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IMSIMSISDNSEG | IMSI/MSISDN号段名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置绑定的IMSIMSISDN号段名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0209897118)

删除GLBPCRFGROUP：IMSIMSISDNSEG为“ims”：

```
RMV GLBPCRFGROUP:IMSIMSISDNSEG="ims";
```
