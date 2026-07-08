# 创建DN比特位配置（ADD OSPFDNBITSET）

- [命令功能](#ZH-CN_CONCEPT_0000001600865801__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000001600865801__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000001600865801__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000001600865801__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000001600865801__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0000001600865801)

该命令用于设置OSPF LSA的DN位。

#### [注意事项](#ZH-CN_CONCEPT_0000001600865801)

- 该命令执行后立即生效。
- 该命令最大记录数为8000。
- 只有在执行ADD OSPF配置了OSPF进程后才能使用此命令。
- 仅支持在OSPF私网进程下配置，并且只在PE上生效。
- 可选参数至少选一项，并且至少禁止设置一种OSPF LSA的DN位。

#### [操作用户权限](#ZH-CN_CONCEPT_0000001600865801)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000001600865801)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCID | 进程号 | 可选必选说明：必选参数<br>参数含义：OSPF进程号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无<br>配置原则：OSPF进程必须已经存在。请使用LST OSPF命令查看可用的OSPF进程。 |
| DNBITSETASEFLAG | 禁止配置ASE LSA的DN位 | 可选必选说明：可选参数<br>参数含义：禁止配置ASE LSA的DN位。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：FALSE |
| DNBITSETNSSAFLAG | 禁止配置NSSA LSA的DN位 | 可选必选说明：可选参数<br>参数含义：禁止配置NSSA LSA的DN位。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：FALSE |
| DNBITSETSUMMARYFLAG | 禁止配置Summary LSA的DN位 | 可选必选说明：可选参数<br>参数含义：禁止配置Summary LSA的DN位。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：FALSE |
| DNBITCHKASEFLAG | 禁止检查ASE LSA的DN位 | 可选必选说明：可选参数<br>参数含义：禁止检查ASE LSA的DN位。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：FALSE |
| DNBITCHKNSSAFLAG | 禁止检查NSSA LSA的DN位 | 可选必选说明：可选参数<br>参数含义：禁止检查NSSA LSA的DN位。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：FALSE |
| DNBITCHKSUMMARYFLAG | 禁止检查Summary LSA的DN位 | 可选必选说明：可选参数<br>参数含义：禁止检查Summary LSA的DN位。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：FALSE |

#### [使用实例](#ZH-CN_CONCEPT_0000001600865801)

禁止OSPF进程1下设置AS-external-LSA的DN位：

```
ADD OSPFDNBITSET:PROCID=1,DNBITSETASEFLAG=FALSE;
```
