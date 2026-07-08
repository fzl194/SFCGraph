# 删除媒体中继HTTP消息头（RMV RELAYHTTPMHD）

- [命令功能](#ZH-CN_CONCEPT_0000207243992604__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000207243992604__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000207243992604__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000207243992604__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000207243992604__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0000207243992604)

**适用NF：UPF、PGW-U**

该命令用于删除媒体中继HTTP消息头。

#### [注意事项](#ZH-CN_CONCEPT_0000207243992604)

该命令执行后立即生效。

#### [操作用户权限](#ZH-CN_CONCEPT_0000207243992604)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000207243992604)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| HTTPMSGCTRLNAME | HTTP消息控制名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定HTTP消息控制名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~31。不区分大小写。<br>默认值：无<br>配置原则：<br>- 该参数使用ADD RELAYHTTPMCTL命令配置生成。<br>- 该取值必须和ADD RELAYHTTPMCTL中配置的"HTTPMAGCTRLNAME"参数取值相同。 |
| MSGTYPE | 消息类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定消息类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- UEHTTPRSP：UE HTTP响应。<br>- CDNHTTPREQ：CDN HTTP请求。<br>默认值：无<br>配置原则：无 |
| HEADERNAME | 头域名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定头域名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。区分大小写，不允许仅大小写不同的重复记录。<br>默认值：无<br>配置原则：以下字段为通用必选或条件必选字段，不允许配置 Connection、Content-Length、Content-Range、Content-Type、Date、Location。 |

#### [使用实例](#ZH-CN_CONCEPT_0000207243992604)

删除媒体中继HTTP消息头：

```
RMV RELAYHTTPMHD: HTTPMSGCTRLNAME="http01";
```
