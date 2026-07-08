---
id: UDG@20.15.2@MMLCommand@CLR CHGDATASTAT
type: MMLCommand
name: CLR CHGDATASTAT（清除计费数据统计信息）
nf: UDG
version: 20.15.2
verb: CLR
object_keyword: CHGDATASTAT
command_category: 动作类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 业务监控
- 业务统计管理
- 计费数据统计信息
status: active
---

# CLR CHGDATASTAT（清除计费数据统计信息）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用于清除计费数据统计信息，比如预定义URR流量上报信息、UserProfile安装次数、整体转发和计费流量差异比例信息、缺省费率流量增量信息、子协议Top30的流量增量信息、预定义规则Top20的匹配次数增量信息、URR Top20的流量增量信息。

## 注意事项

- 该命令执行后立即生效。
- 执行该命令后会清空已保存的统计数据，导致历史数据无法查询。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| STATTYPE | 统计类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定要显示计费数据的统计类型。<br>数据来源：本端规划<br>取值范围：ENUM。<br>- UPINSTALL：查询UserProfile安装次数。<br>- URRVOLUME：查询URR流量统计信息。<br>- WHOLE_VOLUME_CONDITION：整体转发和计费流量差异比例信息。<br>- TOPN_URR_VOLUME：URR流量增量Top20信息。<br>- RULE_MATCH_NUM：预定义规则Top20的匹配次数增量信息。<br>- PROTOCOL_VOLUME：协议Top30的流量增量信息。<br>- DEFAULT_URR_VOLUME：缺省费率流量增量信息。<br>默认值：无<br>配置原则：无 |
| URRID | URRID(Predef) | 可选必选说明：条件可选参数<br>前提条件：该参数在“STATTYPE”配置为“URRVOLUME”时为可选参数。<br>参数含义：用于指示URR标识（预定义）。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～2147483646。<br>默认值：无<br>配置原则：无 |
| USERPROFILENAME | UserProfileName | 可选必选说明：条件可选参数<br>前提条件：该参数在“STATTYPE”配置为“UPINSTALL”时为可选参数。<br>参数含义：该参数用于指定用户模板名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1~63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/CHGDATASTAT]] · 计费数据统计信息（CHGDATASTAT）

## 使用实例

清除URR流量统计数据：

```
%%CLR CHGDATASTAT: STATTYPE=URRVOLUME;%%
RETCODE = 0  Operation succeeded

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/清除计费数据统计信息（CLR-CHGDATASTAT）_75626870.md`
