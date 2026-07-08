# 删除Profile Space（RMV PROFILESPACE）

- [命令功能](#ZH-CN_CONCEPT_0209897049__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0209897049__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0209897049__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0209897049__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0209897049__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0209897049)

**适用NF：PGW-C、SMF**

本命令用于删除Profile Space实例。

#### [注意事项](#ZH-CN_CONCEPT_0209897049)

- 该命令执行后立即生效。
- 删除ProfileSpace实例前，请确认是否有用户在使用此ProfileSpace实例。如果有用户使用，不要删除此配置。
- 如果待删除的ProfileSpace实例和APN绑定（通过ADD APNPROFSPACE命令），会自动解除绑定关系。

#### [操作用户权限](#ZH-CN_CONCEPT_0209897049)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0209897049)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROFSPACENAME | Profile Space名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定ProfileSpace名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0209897049)

删除ProfileSpace名称为“profilespace1”的ProfileSpace配置：

```
RMV PROFILESPACE:PROFSPACENAME="profilespace1";
```
