# 设置Fabric-In功能开关（SET FABRICINSWITCH）

- [命令功能](#ZH-CN_CONCEPT_0000001103218174__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000001103218174__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000001103218174__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000001103218174__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000001103218174__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0000001103218174)

该命令用于设置Fabric-In功能开关。Fabric-In对应是内置FullMesh卡，内置FullMesh卡负责框内流量交换。

#### [注意事项](#ZH-CN_CONCEPT_0000001103218174)

该命令本版本不再支持生效。

#### [操作用户权限](#ZH-CN_CONCEPT_0000001103218174)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000001103218174)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ENABLE | 功能是否开启 | 可选必选说明：必选参数<br>参数含义：该参数表示是否开启和关闭Fabric-In功能。数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”<br>默认值：TRUE |

#### [使用实例](#ZH-CN_CONCEPT_0000001103218174)

- 设置Fabric-In功能开启：
  ```
  %%SET FABRICINSWITCH: ENABLE=TRUE;%%
  RETCODE = 0  操作成功

  ---    END
  ```
