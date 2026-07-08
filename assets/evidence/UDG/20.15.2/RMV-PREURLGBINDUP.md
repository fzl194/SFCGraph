# 删除用户模板的前缀URL组绑定关系（RMV PREURLGBINDUP）

- [命令功能](#ZH-CN_CONCEPT_0182837412__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0182837412__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0182837412__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0182837412__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0182837412__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0182837412)

**适用NF：PGW-U、UPF**

![](删除用户模板的前缀URL组绑定关系（RMV PREURLGBINDUP）_82837412.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，可能会影响业务。

该命令用于删除用户模板与前缀URL组的绑定关系。

#### [注意事项](#ZH-CN_CONCEPT_0182837412)

- 本命令修改后对所有用户生效，大概五分钟之后生效。
- 如果不输入前缀URL组，则代表删除该UserProfile对应的所有前缀URL组。

#### [操作用户权限](#ZH-CN_CONCEPT_0182837412)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0182837412)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| USERPROFILENAME | 用户模板名称 | 可选必选说明：必选参数<br>参数含义：该参数用于设置用户模板名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| PREURLGRPNAME | 前缀URL组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定前缀URL组名字。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不区分大小写。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0182837412)

删除前缀URL组与UserProfile的绑定关系，USERPROFILENAME为“testprofile1”，PREURLGRPNAME为“testurlgroup”：

```
RMV PREURLGBINDUP:USERPROFILENAME="testprofile",PREURLGRPNAME="testurlgroup";
```
