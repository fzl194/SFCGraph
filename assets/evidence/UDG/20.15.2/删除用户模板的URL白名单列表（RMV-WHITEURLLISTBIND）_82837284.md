# 删除用户模板的URL白名单列表（RMV WHITEURLLISTBIND）

- [命令功能](#ZH-CN_CONCEPT_0182837284__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0182837284__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0182837284__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0182837284__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0182837284__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0182837284)

**适用NF：PGW-U、UPF**

![](删除用户模板的URL白名单列表（RMV WHITEURLLISTBIND）_82837284.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，该命令有可能会影响业务计费，导致业务阻塞，请谨慎使用并联系华为技术支持协助操作。

RMV WHITEURLLISTBIND命令用于删除USERPROFILE下白名单绑定关系。

#### [注意事项](#ZH-CN_CONCEPT_0182837284)

该命令执行后立即生效。

#### [操作用户权限](#ZH-CN_CONCEPT_0182837284)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0182837284)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| USERPROFILENAME | 用户模板名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定用户模板名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格及“,”、“;”、“"”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0182837284)

删除用户模板的URL白名单列表: USERPROFILENAME为TestUserProfileName：

```
RMV WHITEURLLISTBIND:USERPROFILENAME="TestUserProfileName";
```
