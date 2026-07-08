# 增加用户模板的前缀URL组绑定关系（ADD PREURLGBINDUP）

- [命令功能](#ZH-CN_CONCEPT_0182837411__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0182837411__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0182837411__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0182837411__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0182837411__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0182837411)

**适用NF：PGW-U、UPF**

该命令用于新增用户模板与前缀URL组的绑定关系，若用户使用的用户模板中绑定了一个或多个前缀URL组，且当前用户访问的业务为前缀URL业务，则会启动前缀URL的过滤。若访问的业务命中前缀URL，则会进行URL的截断，使用前缀URL之后的内容作为URL，进行计费和业务控制处理。

#### [注意事项](#ZH-CN_CONCEPT_0182837411)

- 该命令执行后立即生效。
- 该命令最大记录数为100000。
- 单个UserProfile可以配置100个前缀URL组。

#### [操作用户权限](#ZH-CN_CONCEPT_0182837411)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0182837411)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| USERPROFILENAME | 用户模板名称 | 可选必选说明：必选参数<br>参数含义：该参数用于设置用户模板名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD USERPROFILE命令配置生成。 |
| PREURLGRPNAME | 前缀URL组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定前缀URL组名字。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD PREFIXURLGRP命令配置生成。 |

#### [使用实例](#ZH-CN_CONCEPT_0182837411)

增加前缀URL组到UserProfile，USERPROFILENAME为“testprofile1”，PREURLGRPNAME为“testurlgroup”：

```
ADD PREURLGBINDUP:USERPROFILENAME="testprofile",PREURLGRPNAME="testurlgroup";
```
