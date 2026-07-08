# 删除带宽管理规则（RMV BWMRULE）

- [命令功能](#ZH-CN_CONCEPT_0182837480__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0182837480__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0182837480__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0182837480__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0182837480__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0182837480)

**适用NF：PGW-U、UPF**

![](删除带宽管理规则（RMV BWMRULE）_82837480.assets/notice_3.0-zh-cn.png)

本命令属于高危命令,执行本命令后将删除默认用户组或具体用户组的指定或所有带宽管理规则，可能导致用户无法进行带宽控制，请谨慎使用。

该命令用于删除默认用户组、或具体用户组的带宽管理规则。当运营商希望删除某个或全部带宽控制规则时，则执行该命令。

#### [注意事项](#ZH-CN_CONCEPT_0182837480)

- 该命令执行后立即生效。
- 如果指定用户组类型，而不指定带宽管理规则名称，可以删除用户组下的所有带宽管理规则，包括默认的规则。
- 如果TOS类型的组级BWMRULE已经生效，修改该BWMRULE下的BWMCONTROLLER，只对新用户或重新激活用户生效，所有组级用户生效前可能会导致带宽控制不准。

#### [操作用户权限](#ZH-CN_CONCEPT_0182837480)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0182837480)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| USERGROUPTYPE | 用户组类型 | 可选必选说明：必选参数<br>参数含义：该参数用于配置带宽管理用户组的类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DEFAULT_GROUP：默认用户组。<br>- SPECIFIC_GROUP：特定用户组。<br>默认值：无<br>配置原则：无 |
| USERGROUPNAME | 用户组名称 | 可选必选说明：条件必选参数<br>前提条件：该参数在“USERGROUPTYPE”配置为“SPECIFIC_GROUP”时为必选参数。<br>参数含义：该参数用于配置具体用户组的名称，该参数由增加带宽管理用户组定义。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| BWMRULETYPE | 带宽管理规则类型 | 可选必选说明：条件可选参数<br>前提条件：该参数在“USERGROUPTYPE”配置为“SPECIFIC_GROUP” 或 “DEFAULT_GROUP”时为可选参数。<br>参数含义：该参数用于配置带宽管理规则的类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- GROUP_DEFAULT：用户组级别默认规则。<br>- SUBSCRIBER_DEFAULT：用户级别默认规则。<br>- GROUP_SPECIFIC：用户组级别特定规则。<br>- SUBSCRIBER_SPECIFIC：用户级别特定规则。<br>默认值：无<br>配置原则：无 |
| BWMRULENAME | 带宽管理规则名称 | 可选必选说明：条件必选参数<br>前提条件：该参数在“BWMRULETYPE”配置为“GROUP_SPECIFIC” 或 “SUBSCRIBER_SPECIFIC”时为必选参数。<br>参数含义：该参数用于配置带宽管理规则的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0182837480)

- 假如运营商需要删除默认用户组下用户组级默认带宽管理规则：
  ```
  RMV BWMRULE:USERGROUPTYPE=DEFAULT_GROUP,BWMRULETYPE=SUBSCRIBER_DEFAULT;
  ```
- 假如运营商需要删除具体用户组“testbwmusergroup”下的所有的带宽管理规则：
  ```
  RMV BWMRULE:USERGROUPTYPE=SPECIFIC_GROUP,USERGROUPNAME="testbwmusergroup";
  ```
