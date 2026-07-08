# 查询RU CPU占用率、告警上报门限和告警恢复门限(DSP RUCPUUSGTHRESH)

- [命令功能](#ZH-CN_CONCEPT_0129626966__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0129626966__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0129626966__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0129626966__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0129626966__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0129626966__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0129626966)

该命令用于查询某个RU的CPU占用率、告警上报门限和告警恢复门限。

#### [注意事项](#ZH-CN_CONCEPT_0129626966)

该命令只适用于查询非主控的RU的CPU信息。

#### [操作用户权限](#ZH-CN_CONCEPT_0129626966)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0129626966)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUID | RU的ID | 可选必选说明：必选参数。<br>参数含义：表示资源单元的ID号。通过<br>**[LST SERVICERUSTATE](查询RU的信息(LST SERVICERUSTATE)_29626965.md)**<br>命令可以查询RU的ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为64～4294967294。 |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过<br>**[LST VNFC](../../../../单体服务平台功能管理/操作维护/配置管理/VNFC信息/查询VNFC（LST VNFC）_59036046.md)**<br>命令获取。<br>默认值：无<br>配置原则：只能填写通过<br>**[LST VNFC](../../../../单体服务平台功能管理/操作维护/配置管理/VNFC信息/查询VNFC（LST VNFC）_59036046.md)**<br>命令查询到的管理代理标识，不支持对"VNFC类型名称"为VNFP、VNRS_VNFC、ACS、IPSEC_VNFC的RU状态查询。 |

#### [使用实例](#ZH-CN_CONCEPT_0129626966)

查询 “RU的ID” 为64的CPU占用率及过载告警上报门限和告警恢复门限:

DSP RUCPUUSGTHRESH:RUID=64 , SERVICEINSTANCE="CSLB_VNFC_999" ;

```
%%/*4191*/DSP RUCPUUSGTHRESH:RUID=64
, SERVICEINSTANCE="CSLB_VNFC_999"
;%%
RETCODE = 0   操作成功。

结果如下
--------
告警上报门限  =  80
告警恢复门限  =  70
   CPU占用率  =  35
(结果个数 = 1)
---    END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0129626966)

| 输出项名称 | 输出项解释 |
| --- | --- |
| 告警上报门限 | RU的CPU过载告警上报门限。 |
| 告警恢复门限 | RU的CPU过载告警恢复门限。 |
| CPU占用率 | 查询RU的当前CPU占用率。 |
