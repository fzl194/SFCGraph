# 查询CDF的功能参数（LST CDFFUNCPARA）

- [命令功能](#ZH-CN_MMLREF_0000001823782750__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001823782750__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001823782750__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001823782750__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0000001823782750__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0000001823782750)

**适用NF：NCG**

该命令用于查询CDF的功能参数。

## [注意事项](#ZH-CN_MMLREF_0000001823782750)

无

#### [操作用户权限](#ZH-CN_MMLREF_0000001823782750)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001823782750)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CDR5GFILTER | 是否开启格式引擎包话单分拣功能 | 可选必选说明：可选参数<br>参数含义：是否开启格式引擎包话单分拣功能。<br>数据来源：本端规划<br>取值范围：<br>- TRUE(TRUE)<br>- FALSE(FALSE)<br>默认值：无<br>配置原则：无 |
| QBCINDEPENDDIR | QBC话单独立目录 | 可选必选说明：可选参数<br>参数含义：是否将QBC话单存放到独立目录。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE（不使能）<br>- ENABLE（使能）<br>默认值：无<br>配置原则：<br>当格式引擎包为PS_R15_VF80_xxx_CMCC.tar.gz、PS_R15_VF80_Unicom.tar.gz时，该参数才能被设置为“使能”，否则可能导致话单分拣异常。 |
| QFIRATINGINDI | QFI容器中的ratingIndicator字段 | 可选必选说明：可选参数<br>参数含义：该参数用于控制话单是否携带QFI容器中的ratingIndicator字段。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE（不使能）<br>- ENABLE（使能）<br>默认值：无<br>配置原则：无 |
| QFIAREAINFO | QFI容器中的presenceReportingAreaInfo字段 | 可选必选说明：可选参数<br>参数含义：该参数用于控制话单是否携带QFI容器中的presenceReportingAreaInfo字段。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE（不使能）<br>- ENABLE（使能）<br>默认值：无<br>配置原则：无 |
| SEGREGATESWITCH | CDF快速隔离开关 | 可选必选说明：可选参数<br>参数含义：该参数用于控制当5G业务模块故障时是否隔离CDF。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE（不使能）<br>- ENABLE（使能）<br>默认值：无<br>配置原则：无 |
| DETECTDURATION | 隔离检测时长 | 可选必选说明：可选参数<br>参数含义：该参数用于控制5G业务模块故障到CDF隔离的时长。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~60，单位是分钟。<br>默认值：无<br>配置原则：<br>需要大于CG_VNFC从复位到业务恢复的时长。 |

## [使用实例](#ZH-CN_MMLREF_0000001823782750)

查询CDF的功能参数：

```
LST CDFFUNCPARA:;
```

## [输出结果说明](#ZH-CN_MMLREF_0000001823782750)

| 输出项名称 | 输出项解释 |
| --- | --- |
| 是否开启格式引擎包话单分拣功能 | 是否开启格式引擎包话单分拣功能。 |
| QBC话单独立目录 | 是否将QBC话单存放到独立目录。 |
| QFI容器中的ratingIndicator字段 | 该参数用于控制话单是否携带QFI容器中的ratingIndicator字段。 |
| QFI容器中的presenceReportingAreaInfo字段 | 该参数用于控制话单是否携带QFI容器中的presenceReportingAreaInfo字段。 |
| CDF快速隔离开关 | 该参数用于控制当5G业务模块故障时是否隔离CDF。 |
| 隔离检测时长 | 该参数用于控制5G业务模块故障到CDF隔离的时长。 |
