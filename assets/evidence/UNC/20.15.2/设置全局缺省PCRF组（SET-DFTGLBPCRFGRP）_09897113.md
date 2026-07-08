# 设置全局缺省PCRF组（SET DFTGLBPCRFGRP）

- [命令功能](#ZH-CN_CONCEPT_0209897113__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0209897113__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0209897113__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0209897113__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0209897113__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0209897113)

**适用NF：PGW-C、GGSN**

此命令用来修改缺省全局PCRF分组。

#### [注意事项](#ZH-CN_CONCEPT_0209897113)

- 该命令执行后立即生效。
- 该命令最大记录数为1。

#### [操作用户权限](#ZH-CN_CONCEPT_0209897113)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0209897113)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PCRFGRPNAME | PCRF组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置绑定的PCRF组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～128。<br>默认值：无<br>配置原则：输入单空格将删除该参数已有配置项。 |

#### [使用实例](#ZH-CN_CONCEPT_0209897113)

修改DFTGLBPCRFGRP：PCRFGRPNAME为pcr：

```
SET DFTGLBPCRFGRP:PCRFGRPNAME="pcr";
```
