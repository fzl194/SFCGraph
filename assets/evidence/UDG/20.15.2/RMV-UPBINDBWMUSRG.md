# 删除带宽管理用户组User Profile绑定（RMV UPBINDBWMUSRG）

- [命令功能](#ZH-CN_CONCEPT_0182837492__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0182837492__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0182837492__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0182837492__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0182837492__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0182837492)

**适用NF：PGW-U、UPF**

![](删除带宽管理用户组User Profile绑定（RMV UPBINDBWMUSRG）_82837492.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，删除不当可能影响UP下用户的带宽策略选取，请谨慎使用并联系华为技术支持协助操作。

该命令用于将某个UserProfile下的用户从一个带宽管理用户组中删除。当运营商不希望对某UserProfile下的用户进行带宽控制时，则需要解除该UserProfile与用户组的绑定关系，该命令就是完成删除绑定的功能。

#### [注意事项](#ZH-CN_CONCEPT_0182837492)

删除一个UserProfile和某带宽管理用户组的绑定，用户更新可以触发该删除的配置对该用户组已在线的用户生效，否则对该用户组已在线用户不生效。

#### [操作用户权限](#ZH-CN_CONCEPT_0182837492)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0182837492)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| USERGROUPNAME | 用户组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定要被用户模板绑定的带宽管理用户组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| USERPROFILENAME | 用户模板名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定要绑定的用户模板名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0182837492)

假如运营商希望解除名为“testbwmusergroup”的用户组和“testuserprofile”的绑定：

```
RMV UPBINDBWMUSRG:USERGROUPNAME="testbwmusergroup",USERPROFILENAME="testuserprofile";
```
