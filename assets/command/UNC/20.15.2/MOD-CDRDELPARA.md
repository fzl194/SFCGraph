---
id: UNC@20.15.2@MMLCommand@MOD CDRDELPARA
type: MMLCommand
name: MOD CDRDELPARA（修改话单删除参数）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: CDRDELPARA
command_category: 配置类
applicable_nf:
- NCG
effect_mode: ''
is_dangerous: false
max_records: 10
category_path:
- 业务服务管理
- NCG业务及策略管理
- 计费管理
- 业务配置管理
- 话单删除参数管理
status: active
---

# MOD CDRDELPARA（修改话单删除参数）

## 功能

![](修改话单删除参数（MOD CDRDELPARA）_51174269.assets/notice_3.0-zh-cn_2.png)

如果设置删除时间为业务忙时，可能会对业务产生影响，建议设置删除时间为系统闲时。

**适用NF：NCG**

该命令用于修改话单删除、话单备份和话单分发任务的话单删除开始时间和话单删除时间间隔，它包含修改和查询命令，防止在NCG业务忙碌时进行过期删除任务时可能导致IO较高，对NCG业务产生影响。

执行命令之前，可执行 [**LST CDRDELPARA**](查询话单删除参数（LST CDRDELPARA）_51174270.md) 命令查询当前各任务设置的话单删除参数。

## 注意事项

- 该命令最大记录数为10。
- 如果设置删除时间为业务忙时，可能会对业务产生影响，建议设置删除时间为系统闲时，否则可能会导致IO较高，对NCG业务产生影响。
- 该命令存在系统初始设置记录，参数的初始设置值如下表：

| CDRDELOBJ | CDRDELSTARTTIME | CDRDELINTERVAL |
| --- | --- | --- |
| CDRDELTASK | 04:00 | 20 |
| CDRBACKUP | 04:00 | 1000 |
| CDRDISTR | 04:00 | 1000 |

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CDRDELOBJ | 话单删除对象 | 可选必选说明：必选参数<br>参数含义：用于修改话单删除、话单备份和话单分发三种类型任务的话单删除参数。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- CDRDELTASK：话单删除。<br>- CDRBACKUP：话单备份。<br>- CDRDISTR：话单分发。<br>默认值：无<br>配置原则：<br>- 话单删除：修改话单删除任务的话单删除参数时，选择此选项。<br>- 话单备份：修改话单备份任务的话单删除参数时，选择此选项。<br>- 话单分发：修改话单分发任务的话单删除参数时，选择此选项。 |
| CDRDELSTARTTIME | 话单删除开始时间 | 可选必选说明：条件可选参数<br>前提条件：该参数在“CDRDELOBJ”配置为“CDRDELTASK”、“CDRBACKUP” 或 “CDRDISTR”时为条件可选参数。<br>参数含义：用于设置话单删除、话单备份或分发任务的话单删除开始时间，系统默认04:00开始话单过期删除任务。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～16。<br>默认值：无<br>配置原则：<br>- 如果修改“话单删除开始时间”，请确保时间是业务空闲时，如果是业务忙时，可能对NCG业务产生影响。并且请确保与话单存储的过期删除任务开始时间间隔2个小时。<br>- HH:MM格式时间字符串。<br>- 不能输入的特殊字符请参考“[**特殊字符表**](../话单存储/增加话单存储（ADD CDRSTOR）_51174277.md#ZH-CN_CONCEPT_0251174277__table_0365FEF0)”。 |
| CDRDELINTERVAL | 话单删除时间间隔(毫秒) | 可选必选说明：条件可选参数<br>前提条件：该参数在“CDRDELOBJ”配置为“CDRDELTASK”、“CDRBACKUP” 或 “CDRDISTR”时为条件可选参数。<br>参数含义：用于设置话单删除、话单备份或分发任务的话单删除休眠时间。话单删除任务每删除1个话单文件休眠此参数时间间隔，话单备份分发任务每删除1000个文件休眠此参数时间间隔。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～2000，单位是毫秒。<br>默认值：无<br>配置原则：<br>- 当“话单删除对象”参数的值为“CDRDELTASK(话单删除)”时，此参数默认值为“20”。<br>- 当“话单删除对象”参数的值为“CDRBACKUP(话单备份)” 或“CDRDISTR(话单分发)”时，此参数默认值为“1000”。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@CDRDELPARA]] · 话单删除参数（CDRDELPARA）

## 使用实例

修改话单删除任务，将“话单删除开始时间”修改为“05:00”，“话单删除时间间隔”修改为“30”ms：

```
MOD CDRDELPARA: CDRDELOBJ=CDRDELTASK, CDRDELSTARTTIME="05:00", CDRDELINTERVAL=30;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-CDRDELPARA.md`
