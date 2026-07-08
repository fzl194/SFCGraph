# 删除GMLC权限配置(RMV GMLCAU)

- [命令功能](#ZH-CN_MMLREF_0000001172225473__1.3.1.1)
- [注意事项](#ZH-CN_MMLREF_0000001172225473__1.3.2.1)
- [本地用户权限](#ZH-CN_MMLREF_0000001172225473__1.3.3.1)
- [网管用户权限](#ZH-CN_MMLREF_0000001172225473__1.3.4.1)
- [参数说明](#ZH-CN_MMLREF_0000001172225473__1.3.5.1)
- [使用实例](#ZH-CN_MMLREF_0000001172225473__1.3.6.1)

#### [命令功能](#ZH-CN_MMLREF_0000001172225473)

**适用网元：MME**

此命令用于删除GMLC权限配置。

#### [注意事项](#ZH-CN_MMLREF_0000001172225473)

- 此命令执行后立即生效。
- 如果只输入GMLCID，则删除指定GMLC标识的所有记录。
- 如果只输入GMLCID与CLTTYPE，则删除指定GMLC标识与客户端类型的所有记录。
- 如果输入GMLCID、CLTTYPE、SERTYPE，则删除指定的GMLCID、客户端类型与LCS业务类型的记录。

#### [本地用户权限](#ZH-CN_MMLREF_0000001172225473)

manage-ug；system-ug

#### [网管用户权限](#ZH-CN_MMLREF_0000001172225473)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_MMLREF_0000001172225473)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GMLCID | GMLC 标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定GMLC标识。<br>取值范围：0～639<br>默认值 ：无 |
| CLTTYPE | 支持的客户端类型 | 可选必选说明：可选参数<br>参数含义：该参数用于标识客户端（LCS Client）类型。<br>取值范围：<br>- “EMERGENCY_SERVICES（紧急业务）”<br>- “VALUE_ADDED_SERVICES（增值业务）”<br>- “PLMN_OPERATOR_SERVICES（运营商业务）”<br>- “LAWFUL_INTERCEPT_SERVICES（合法定位）”<br>默认值 ：无 |
| SERTYPE | 支持的LCS业务类型 | 可选必选说明：条件可选参数<br>参数含义：该参数用于标识LCS Client的指定定位业务。<br>前提条件：该参数在<br>“支持的客户端类型”<br>输入时本参数有效。<br>取值范围： 0～127<br>默认值 ：无 |

#### [使用实例](#ZH-CN_MMLREF_0000001172225473)

删除一条 “GMLC 标识” 为 “1” ， “支持的客户端类型” 为 “VALUE_ADDED_SERVICES（增值业务）” ， “支持的LCS业务类型” 为 “3” 的GMLC权限配置记录：

RMV GMLCAU: GMLCID=1, CLTTYPE=VALUE_ADDED_SERVICES,SERTYPE=3;
