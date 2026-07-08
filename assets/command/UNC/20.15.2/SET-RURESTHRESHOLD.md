---
id: UNC@20.15.2@MMLCommand@SET RURESTHRESHOLD
type: MMLCommand
name: SET RURESTHRESHOLD（设置RU资源过载和去过载阈值）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: RURESTHRESHOLD
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务公共功能管理
- 系统管理
- 资源管理
- RU管理
status: active
---

# SET RURESTHRESHOLD（设置RU资源过载和去过载阈值）

## 功能

该命令用来设置不同RU类型的资源过载和去过载阈值。

配置资源过载阈值是非常重要的操作，可以控制CPU使用率过载告警和内存使用率过载告警在什么情况下上报网管。

用户可以根据业务的需要，执行该命令修改阈值，从而监控网元的资源使用率和网元运行的健康状态。

## 注意事项

- 该命令执行后立即生效。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| CPUUNOVLIMITMIN | CPUOVLIMITMIN | CPUUNOVLIMIT | CPUOVLIMIT | CPUUNOVLIMITCRI | CPUOVLIMITCRI | MEMUNOVLIMITMIN | MEMOVLIMITMIN | MEMUNOVLIMIT | MEMOVLIMIT | MEMUNOVLIMITCRI | MEMOVLIMITCRI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 0 | 75 | 95 | 0 | 0 | 0 | 0 | 75 | 95 | 0 | 0 |

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUTYPE | RU类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定RU类型。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，区分大小写。<br>默认值：无<br>配置原则：请使用<br>[**LST RESINSTANCETYPE**](查询资源实例类型（LST RESINSTANCETYPE）_59103378.md)<br>命令查询存在的资源单元类型。 |
| CPUUNOVLIMITMIN | CPU使用率过载次要级别告警的恢复阈值（%） | 可选必选说明：可选参数<br>参数含义：该参数用于设置CPU使用率过载次要级别告警的恢复阈值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～100。<br>默认值：无<br>配置原则：<br>- 当不输入时以命令[**LST RURESTHRESHOLD**](查询RU资源过载和去过载阈值（LST RURESTHRESHOLD）_56175397.md)查询到的值为准。<br>- 参数配置为0时，表示不支持该级别的告警，同一级别的过载恢复阈值和过载上报阈值需要同时配置为0。<br>- 参数配置为非0时，表示支持该级别的告警，同一级别的过载恢复阈值和过载上报阈值需要同时配置为非0。<br>- 参数非0时，要满足CPUUNOVLIMITLMIN < CPUOVLIMITMIN < CPUUNOVLIMIT< CPUOVLIMIT < CPUUNOVLIMITCRI < CPUOVLIMITCRI，当字段的阈值为零时，则该字段将不参与比较。 |
| CPUOVLIMITMIN | CPU使用率过载次要级别告警的上报阈值（%） | 可选必选说明：可选参数<br>参数含义：该参数用于设置CPU使用率过载次要级别告警的上报阈值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～100。<br>默认值：无<br>配置原则：<br>- 当不输入时以命令[**LST RURESTHRESHOLD**](查询RU资源过载和去过载阈值（LST RURESTHRESHOLD）_56175397.md)查询到的值为准。<br>- 参数配置为0时，表示不支持该级别的告警，同一级别的过载恢复阈值和过载上报阈值需要同时配置为0。<br>- 参数配置为非0时，表示支持该级别的告警，同一级别的过载恢复阈值和过载上报阈值需要同时配置为非0。<br>- 参数非0时，要满足CPUUNOVLIMITLMIN < CPUOVLIMITMIN < CPUUNOVLIMIT< CPUOVLIMIT < CPUUNOVLIMITCRI < CPUOVLIMITCRI，当字段的阈值为零时，则该字段将不参与比较。 |
| CPUUNOVLIMIT | CPU使用率过载重要级别告警的恢复阈值（%） | 可选必选说明：可选参数<br>参数含义：该参数用于设置CPU使用率过载重要级别告警的恢复阈值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～100。<br>默认值：75<br>配置原则：<br>- 当不输入时以命令[**LST RURESTHRESHOLD**](查询RU资源过载和去过载阈值（LST RURESTHRESHOLD）_56175397.md)查询到的值为准。<br>- 参数配置为0时，表示不支持该级别的告警，同一级别的过载恢复阈值和过载上报阈值需要同时配置为0。<br>- 参数配置为非0时，表示支持该级别的告警，同一级别的过载恢复阈值和过载上报阈值需要同时配置为非0。<br>- 参数非0时，要满足CPUUNOVLIMITLMIN < CPUOVLIMITMIN < CPUUNOVLIMIT< CPUOVLIMIT < CPUUNOVLIMITCRI < CPUOVLIMITCRI，当字段的阈值为零时，则该字段将不参与比较。 |
| CPUOVLIMIT | CPU使用率过载重要级别告警的上报阈值（%） | 可选必选说明：可选参数<br>参数含义：该参数用于设置CPU使用率过载重要级别告警的上报阈值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～100。<br>默认值：95<br>配置原则：<br>- 当不输入时以命令[**LST RURESTHRESHOLD**](查询RU资源过载和去过载阈值（LST RURESTHRESHOLD）_56175397.md)查询到的值为准。<br>- 参数配置为0时，表示不支持该级别的告警，同一级别的过载恢复阈值和过载上报阈值需要同时配置为0。<br>- 参数配置为非0时，表示支持该级别的告警，同一级别的过载恢复阈值和过载上报阈值需要同时配置为非0。<br>- 参数非0时，要满足CPUUNOVLIMITLMIN < CPUOVLIMITMIN < CPUUNOVLIMIT< CPUOVLIMIT < CPUUNOVLIMITCRI < CPUOVLIMITCRI，当字段的阈值为零时，则该字段将不参与比较。 |
| CPUUNOVLIMITCRI | CPU使用率过载紧急级别告警的恢复阈值（%） | 可选必选说明：可选参数<br>参数含义：该参数用于设置CPU使用率过载紧急级别告警的恢复阈值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～100。<br>默认值：无<br>配置原则：<br>- 当不输入时以命令[**LST RURESTHRESHOLD**](查询RU资源过载和去过载阈值（LST RURESTHRESHOLD）_56175397.md)查询到的值为准。<br>- 参数配置为0时，表示不支持该级别的告警，同一级别的过载恢复阈值和过载上报阈值需要同时配置为0。<br>- 参数配置为非0时，表示支持该级别的告警，同一级别的过载恢复阈值和过载上报阈值需要同时配置为非0。<br>- 参数非0时，要满足CPUUNOVLIMITLMIN < CPUOVLIMITMIN < CPUUNOVLIMIT< CPUOVLIMIT < CPUUNOVLIMITCRI < CPUOVLIMITCRI，当字段的阈值为零时，则该字段将不参与比较。 |
| CPUOVLIMITCRI | CPU使用率过载紧急级别告警的上报阈值（%） | 可选必选说明：可选参数<br>参数含义：该参数用于设置CPU使用率过载紧急级别告警的上报阈值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～100。<br>默认值：无<br>配置原则：<br>- 当不输入时以命令[**LST RURESTHRESHOLD**](查询RU资源过载和去过载阈值（LST RURESTHRESHOLD）_56175397.md)查询到的值为准。<br>- 参数配置为0时，表示不支持该级别的告警，同一级别的过载恢复阈值和过载上报阈值需要同时配置为0。<br>- 参数配置为非0时，表示支持该级别的告警，同一级别的过载恢复阈值和过载上报阈值需要同时配置为非0。<br>- 参数非0时，要满足CPUUNOVLIMITLMIN < CPUOVLIMITMIN < CPUUNOVLIMIT< CPUOVLIMIT < CPUUNOVLIMITCRI < CPUOVLIMITCRI，当字段的阈值为零时，则该字段将不参与比较。 |
| MEMUNOVLIMITMIN | 内存使用率过载次要级别告警的恢复阈值（%） | 可选必选说明：可选参数<br>参数含义：该参数用于设置内存使用率过载次要级别告警的恢复阈值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～100。<br>默认值：无<br>配置原则：<br>- 当不输入时以命令[**LST RURESTHRESHOLD**](查询RU资源过载和去过载阈值（LST RURESTHRESHOLD）_56175397.md)查询到的值为准。<br>- 参数配置为0时，表示不支持该级别的告警，同一级别的过载恢复阈值和过载上报阈值需要同时配置为0。<br>- 参数配置为非0时，表示支持该级别的告警，同一级别的过载恢复阈值和过载上报阈值需要同时配置为非0。<br>- 参数非0时，要满足MEMUNOVLIMITLMIN < MEMOVLIMITMIN < MEMUNOVLIMIT< MEMOVLIMIT < MEMUNOVLIMITCRI < MEMOVLIMITCRI，当字段的阈值为零时，则该字段将不参与比较。 |
| MEMOVLIMITMIN | 内存使用率过载次要级别告警的上报阈值（%） | 可选必选说明：可选参数<br>参数含义：该参数用于设置内存使用率过载次要级别告警的上报阈值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～100。<br>默认值：无<br>配置原则：<br>- 当不输入时以命令[**LST RURESTHRESHOLD**](查询RU资源过载和去过载阈值（LST RURESTHRESHOLD）_56175397.md)查询到的值为准。<br>- 参数配置为0时，表示不支持该级别的告警，同一级别的过载恢复阈值和过载上报阈值需要同时配置为0。<br>- 参数配置为非0时，表示支持该级别的告警，同一级别的过载恢复阈值和过载上报阈值需要同时配置为非0。<br>- 参数非0时，要满足MEMUNOVLIMITLMIN < MEMOVLIMITMIN < MEMUNOVLIMIT< MEMOVLIMIT < MEMUNOVLIMITCRI < MEMOVLIMITCRI，当字段的阈值为零时，则该字段将不参与比较。 |
| MEMUNOVLIMIT | 内存使用率过载重要级别告警的恢复阈值（%） | 可选必选说明：可选参数<br>参数含义：该参数用于设置内存使用率过载重要级别告警的恢复阈值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～100。<br>默认值：75<br>配置原则：<br>- 当不输入时以命令[**LST RURESTHRESHOLD**](查询RU资源过载和去过载阈值（LST RURESTHRESHOLD）_56175397.md)查询到的值为准。<br>- 参数配置为0时，表示不支持该级别的告警，同一级别的过载恢复阈值和过载上报阈值需要同时配置为0。<br>- 参数配置为非0时，表示支持该级别的告警，同一级别的过载恢复阈值和过载上报阈值需要同时配置为非0。<br>- 参数非0时，要满足MEMUNOVLIMITLMIN < MEMOVLIMITMIN < MEMUNOVLIMIT< MEMOVLIMIT < MEMUNOVLIMITCRI < MEMOVLIMITCRI，当字段的阈值为零时，则该字段将不参与比较。 |
| MEMOVLIMIT | 内存使用率过载重要级别告警的上报阈值（%） | 可选必选说明：可选参数<br>参数含义：该参数用于设置内存使用率过载重要级别告警的上报阈值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～100。<br>默认值：95<br>配置原则：<br>- 当不输入时以命令[**LST RURESTHRESHOLD**](查询RU资源过载和去过载阈值（LST RURESTHRESHOLD）_56175397.md)查询到的值为准。<br>- 参数配置为0时，表示不支持该级别的告警，同一级别的过载恢复阈值和过载上报阈值需要同时配置为0。<br>- 参数配置为非0时，表示支持该级别的告警，同一级别的过载恢复阈值和过载上报阈值需要同时配置为非0。<br>- 参数非0时，要满足MEMUNOVLIMITLMIN < MEMOVLIMITMIN < MEMUNOVLIMIT< MEMOVLIMIT < MEMUNOVLIMITCRI < MEMOVLIMITCRI，当字段的阈值为零时，则该字段将不参与比较。 |
| MEMUNOVLIMITCRI | 内存使用率过载紧急级别告警的恢复阈值（%） | 可选必选说明：可选参数<br>参数含义：该参数用于设置内存使用率过载紧急级别告警的恢复阈值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～100。<br>默认值：无<br>配置原则：<br>- 当不输入时以命令[**LST RURESTHRESHOLD**](查询RU资源过载和去过载阈值（LST RURESTHRESHOLD）_56175397.md)查询到的值为准。<br>- 参数配置为0时，表示不支持该级别的告警，同一级别的过载恢复阈值和过载上报阈值需要同时配置为0。<br>- 参数配置为非0时，表示支持该级别的告警，同一级别的过载恢复阈值和过载上报阈值需要同时配置为非0。<br>- 参数非0时，要满足MEMUNOVLIMITLMIN < MEMOVLIMITMIN < MEMUNOVLIMIT< MEMOVLIMIT < MEMUNOVLIMITCRI < MEMOVLIMITCRI，当字段的阈值为零时，则该字段将不参与比较。 |
| MEMOVLIMITCRI | 内存使用率过载紧急级别告警的上报阈值（%） | 可选必选说明：可选参数<br>参数含义：该参数用于设置内存使用率过载紧急级别告警的上报阈值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～100。<br>默认值：无<br>配置原则：<br>- 当不输入时以命令[**LST RURESTHRESHOLD**](查询RU资源过载和去过载阈值（LST RURESTHRESHOLD）_56175397.md)查询到的值为准。<br>- 参数配置为0时，表示不支持该级别的告警，同一级别的过载恢复阈值和过载上报阈值需要同时配置为0。<br>- 参数配置为非0时，表示支持该级别的告警，同一级别的过载恢复阈值和过载上报阈值需要同时配置为非0。<br>- 参数非0时，要满足MEMUNOVLIMITLMIN < MEMOVLIMITMIN < MEMUNOVLIMIT< MEMOVLIMIT < MEMUNOVLIMITCRI < MEMOVLIMITCRI，当字段的阈值为零时，则该字段将不参与比较。 |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过<br>**LST VNFC**<br>命令获取。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。 |

## 操作的配置对象

- [RU资源过载和去过载阈值（RURESTHRESHOLD）](configobject/UNC/20.15.2/RURESTHRESHOLD.md)

## 使用实例

将VNODE_CSLB_VNFC_OMU类型的CPU使用率过载重要级别告警的恢复阈值设置为80，上报阈值设置为90：

```
SET RURESTHRESHOLD
:RUTYPE="VNODE_CSLB_VNFC_OMU",CPUUNOVLIMIT=80,CPUOVLIMIT=90
,SERVICEINSTANCE="vnfc"
;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置RU资源过载和去过载阈值（SET-RURESTHRESHOLD）_10095498.md`
