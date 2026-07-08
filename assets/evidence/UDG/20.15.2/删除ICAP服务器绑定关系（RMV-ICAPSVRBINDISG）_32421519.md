# 删除ICAP服务器绑定关系（RMV ICAPSVRBINDISG）

- [命令功能](#ZH-CN_CONCEPT_0000203432421519__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000203432421519__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000203432421519__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000203432421519__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000203432421519__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0000203432421519)

**适用NF：PGW-U、UPF**

该命令用于解除指定名称的ICAP Server Group和ICAP Server实例的绑定关系。

#### [注意事项](#ZH-CN_CONCEPT_0000203432421519)

该命令执行后立即生效。

#### [操作用户权限](#ZH-CN_CONCEPT_0000203432421519)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000203432421519)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ICAPSVRGRPNAME | ICAP服务器组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定ICAP Server Group的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格。<br>默认值：无<br>配置原则：无 |
| ICAPSERVERNAME | ICAP服务器名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定ICAP Server的服务器名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0000203432421519)

删除ICAP Server服务器is1与ICAP服务器组isg1的绑定信息：

```
RMV ICAPSVRBINDISG:ICAPSVRGRPNAME="isg1",ICAPSERVERNAME="is1";
```
