# 查询ScaleGroup信息(DSP SCALEGROUP)

- [命令功能](#ZH-CN_CONCEPT_0129626972__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0129626972__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0129626972__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0129626972__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0129626972__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0129626972__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0129626972)

该命令用来查看VNFC下所有ScaleGroup的信息。

#### [注意事项](#ZH-CN_CONCEPT_0129626972)

无。

#### [操作用户权限](#ZH-CN_CONCEPT_0129626972)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0129626972)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。数据来源：本端规划<br>取值范围：字符串类型，通过<br>**[LST VNFC](../../../../单体服务平台功能管理/操作维护/配置管理/VNFC信息/查询VNFC（LST VNFC）_59036046.md)**<br>命令获取。<br>默认值：无<br>配置原则：只能填写通过<br>**[LST VNFC](../../../../单体服务平台功能管理/操作维护/配置管理/VNFC信息/查询VNFC（LST VNFC）_59036046.md)**<br>命令查询到的管理代理标识，不支持对"VNFC类型名称"为VNFP、VNRS_VNFC、ACS、IPSEC_VNFC的RU状态查询。 |

#### [使用实例](#ZH-CN_CONCEPT_0129626972)

查看ScaleGroup的信息。

DSP SCALEGROUP :SERVICEINSTANCE="CSLB_VNFC_999" ;

```
%%/*4166*/DSP SCALEGROUP:
SERVICEINSTANCE="CSLB_VNFC_999"
;%%
RETCODE = 0  操作成功。

结果如下
--------
          组索引  =  1
  ScaleGroup名字  =  SG0_CSLB_IPFWD
(结果个数 = 1)
---    END 
```

#### [输出结果说明](#ZH-CN_CONCEPT_0129626972)

| 输出项名称 | 输出项解释 |
| --- | --- |
| 组索引 | 同一VNFC下的每一个ScaleGroup对应一个索引。<br>取值范围：整数类型，取值范围为0～4294967294 |
| ScaleGroup名字 | VNFC下的ScaleGroup名字。<br>字符串类型，长度为：1～63 |
