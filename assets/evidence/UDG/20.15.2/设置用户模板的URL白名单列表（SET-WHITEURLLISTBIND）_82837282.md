# 设置用户模板的URL白名单列表（SET WHITEURLLISTBIND）

- [命令功能](#ZH-CN_CONCEPT_0182837282__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0182837282__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0182837282__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0182837282__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0182837282__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0182837282)

**适用NF：PGW-U、UPF**

该命令用于设置用户模板的URL白名单列表。配置该URL白名单列表后，用户进行内容计费的在线计费时，如果匹配的费率组的配额不足，用户报文会触发SMF/UPF 向OCS发送配额请求消息，如果OCS返回的是重定向处理，并且业务报文的URL匹配了其中配置的URL，用户业务可以正常访问URL，无需进行重定向处理。

#### [注意事项](#ZH-CN_CONCEPT_0182837282)

- 该命令执行后立即生效。
- 该命令最大记录数为105000。
- 该命令设定后的数据，需要通过LST USERPROFILE命令进行查看。

#### [操作用户权限](#ZH-CN_CONCEPT_0182837282)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0182837282)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| USERPROFILENAME | 用户模板名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定用户模板名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格及“,”、“;”、“"”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD USERPROFILE命令配置生成。 |
| WHITELISTNAME | URL白名单名称 | 可选必选说明：必选参数<br>参数含义：指定URL白名单名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。支持空格，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD WHITEURLLIST命令配置生成。 |

#### [使用实例](#ZH-CN_CONCEPT_0182837282)

假如运营商需要绑定URL白名单列表“testwhiteurllist”到名称为“testuserprofilename”的用户模板：

```
SET WHITEURLLISTBIND:USERPROFILENAME="testuserprofilename",WhiteListName="testwhiteurllist";
```
