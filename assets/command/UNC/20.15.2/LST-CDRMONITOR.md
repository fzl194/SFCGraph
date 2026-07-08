---
id: UNC@20.15.2@MMLCommand@LST CDRMONITOR
type: MMLCommand
name: LST CDRMONITOR（查询话单监控）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: CDRMONITOR
command_category: 查询类
applicable_nf:
- NCG
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NCG业务及策略管理
- 计费管理
- 业务配置管理
- 话单监控
status: active
---

# LST CDRMONITOR（查询话单监控）

## 功能

**适用NF：NCG**

该命令用于查询长时间未取话单监控任务。

## 注意事项

当前版本不支持Bi口SingleIP功能，请勿开启。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MONITORID | 话单监控标识 | 可选必选说明：可选参数<br>参数含义：监控任务标识，全局唯一。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32。<br>默认值：无<br>配置原则：无 |
| ISSINGLEBI | 是否开启Bi口SingleIP功能 | 可选必选说明：可选参数<br>参数含义：是否开启BI口的SingleIP功能，用于话单监控。暂不支持“ISSINGLEBI”配置为“YES”。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- NO：否。<br>- YES：是。<br>默认值：无<br>配置原则：无 |
| CDRDISTRID | 分发任务标识 | 可选必选说明：条件可选参数<br>前提条件：该参数在“ISSINGLEBI”配置为“YES” 或 “NO”时为条件可选参数。暂不支持“ISSINGLEBI”配置为“YES”。<br>参数含义：该参数用于表示当前监控任务所监控的PULL分发任务。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32。<br>默认值：无<br>配置原则：无 |
| ISCUSTOMDIR | 是否自定义目录 | 可选必选说明：条件可选参数<br>前提条件：该参数在“ISSINGLEBI”配置为“NO”时为条件可选参数。<br>参数含义：该参数用于表示监控的PULL任务开放给计费中心的目录是否是自定义目录。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- NO：否。<br>- YES：是。<br>默认值：无<br>配置原则：无 |
| MONSUBDIR | 监控子目录 | 可选必选说明：条件可选参数<br>前提条件：该参数在“ISCUSTOMDIR”配置为“YES”时为条件可选参数。<br>参数含义：该参数用来表示PULL任务“开放给BS的目录”下面的子目录。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～128。<br>默认值：无<br>配置原则：无 |
| AGID | 接入网元分组标识 | 可选必选说明：条件可选参数<br>前提条件：该参数在“ISCUSTOMDIR”配置为“NO”时为条件可选参数。<br>参数含义：用于区分不同域的接入网元。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32。<br>默认值：无<br>配置原则：无 |
| MNAME | 模块名 | 可选必选说明：条件可选参数<br>前提条件：该参数在“ISCUSTOMDIR”配置为“NO”时为条件可选参数。<br>参数含义：用于标识一个业务模块对象，全局唯一。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～15。<br>默认值：无<br>配置原则：无 |
| CHLNAME | 通道名称 | 可选必选说明：条件可选参数<br>前提条件：该参数在“ISCUSTOMDIR”配置为“NO”时为条件可选参数。<br>参数含义：该参数表示长时间未取话单监控的通道名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32。<br>默认值：无<br>配置原则：无 |
| TIMEOUT | 长时间未取话单告警的监控时长（分） | 可选必选说明：条件可选参数<br>前提条件：该参数在“ISSINGLEBI”配置为“YES” 或 “NO”时为条件可选参数。暂不支持“ISSINGLEBI”配置为“YES”。<br>参数含义：该参数表示NCG检测计费中心未取话单的时间阈值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～259200，单位是分钟。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/CDRMONITOR]] · 话单监控（CDRMONITOR）

## 使用实例

查询一个非自定义目录的话单监控任务示例：

```
LST CDRMONITOR:;
```

```
RETCODE = 0  操作成功

结果如下:
---------
                      话单监控标识  =  MON_1
          是否开启Bi口SingleIP功能  =  否
                      分发任务标识  =  pull_1
                    是否自定义目录  =  否
                        监控子目录  =  NULL
                  接入网元分组标识  =  PS_GROUP_1
                            模块名  =  AP66_1
                          通道名称  =  scdr
长时间未取话单告警的监控时长（分）  =  30
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-CDRMONITOR.md`
