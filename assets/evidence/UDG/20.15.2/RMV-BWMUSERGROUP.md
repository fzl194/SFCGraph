# 删除带宽管理用户组（RMV BWMUSERGROUP）

- [命令功能](#ZH-CN_CONCEPT_0186526876__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0186526876__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0186526876__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0186526876__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0186526876__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0186526876)

**适用NF：PGW-U、UPF**

![](删除带宽管理用户组（RMV BWMUSERGROUP）_86526876.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，会删除带宽管理用户组下所有绑定关系。

该命令用于删除带宽管理用户组。当运营商希望删除已配置的默认用户组或具体用户组时，则执行该命令。

#### [注意事项](#ZH-CN_CONCEPT_0186526876)

- 删除一个带宽管理用户组，对已在线用户的用户级TOS业务立即生效，而用户更新才会触发删除的配置对其他业务生效。
- 删除一个带宽管理用户组会同时删除该用户组下所有的带宽管理规则和与APN、UserProfile的绑定关系。
- 全局用户组为系统默认配置，不能删除。

#### [操作用户权限](#ZH-CN_CONCEPT_0186526876)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0186526876)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| USERGROUPTYPE | 用户组类型 | 可选必选说明：必选参数<br>参数含义：该参数用于配置带宽管理用户组的类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DEFAULT_GROUP：默认用户组。<br>- SPECIFIC_GROUP：特定用户组。<br>默认值：无<br>配置原则：无 |
| USERGROUPNAME | 用户组名称 | 可选必选说明：条件必选参数<br>前提条件：该参数在“USERGROUPTYPE”配置为“SPECIFIC_GROUP”时为必选参数。<br>参数含义：该参数用于配置带宽管理用户组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0186526876)

假如运营商需要删除名为“testbwmusergroup”的具体带宽管理业务：

```
RMV BWMUSERGROUP: USERGROUPTYPE=SPECIFIC_GROUP,USERGROUPNAME="testbwmusergroup";
```
