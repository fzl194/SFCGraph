# 查询RU CPU信息(LST RUCPUINFO)

- [命令功能](#ZH-CN_CONCEPT_0204847994__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0204847994__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0204847994__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0204847994__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0204847994__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0204847994__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0204847994)

该命令用于查询指定RU的CPU信息，CPU信息包含CPU代数、CPU主频以及CPU类型。

#### [注意事项](#ZH-CN_CONCEPT_0204847994)

无。

#### [操作用户权限](#ZH-CN_CONCEPT_0204847994)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0204847994)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：可选参数<br>参数含义：被查询的资源单元名称。通过<br>**DSP RU**<br>命令可以查询资源单元名称。<br>数据来源：本端规划<br>取值范围：1～64位字符串<br>默认值：无<br>说明：- 若不输入，则表示查询系统内所有RU的CPU信息。 |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。该参数不能取值为VNFP、ACS、VNRS_VNFC的服务实例名称。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。 |

#### [使用实例](#ZH-CN_CONCEPT_0204847994)

查询RU名称为USN_OM_RU_0001的CPU信息，执行以下命令：

LST RUCPUINFO: RUNAME="USN_OM_RU_0001" ,SERVICEINSTANCE=" vnfc " ;

```
RETCODE = 0  操作成功。

结果如下
--------
   RuId  =  1
 RU名称  =  USN_OM_RU_0001
CPU代数  =  Gold 6161 CPU
CPU类型  =  x86_64
CPU主频  =  2100
(结果个数 = 1)
---    END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0204847994)

| 输出项名称 | 输出项解释 |
| --- | --- |
| RuId | 该RU对应的ID。 |
| Ru名称 | 该RU对应的名称。 |
| CPU代数 | 该RU使用的CPU代数。 |
| CPU类型 | 该RU使用的CPU类型。 |
| CPU主频 | 该RU使用的CPU主频，单位为MHz。 |
