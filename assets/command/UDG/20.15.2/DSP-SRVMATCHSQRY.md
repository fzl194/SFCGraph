---
id: UDG@20.15.2@MMLCommand@DSP SRVMATCHSQRY
type: MMLCommand
name: DSP SRVMATCHSQRY（查询业务匹配统计结果）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: SRVMATCHSQRY
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务运维
- 业务性能统计管理
- 业务匹配统计配置
status: active
---

# DSP SRVMATCHSQRY（查询业务匹配统计结果）

## 功能

**适用NF：PGW-U、UPF**

该命令用于查询匹配到对应业务的计数。

## 注意事项

使用该命令可以监控规则的业务匹配次数。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SRVMATCHQRYT | 业务匹配统计查询类型 | 可选必选说明：必选参数<br>参数含义：该参数用于设置业务匹配统计查询类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- RULE：监控规则匹配。<br>默认值：无<br>配置原则：RULE：需要监控规则匹配次数时，配置该参数。 |
| RULENAME | 规则名称 | 可选必选说明：条件可选参数<br>前提条件：该参数在“SRVMATCHQRYT”配置为“RULE”时为可选参数。<br>参数含义：该参数用于设置规则名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该参数使用 ADD RULE 或 ADD BLACKLISTRULE 命令配置生成。 |
| DSPMODE | 显示模式 | 可选必选说明：可选参数<br>参数含义：用于显示匹配统计结果的显示模式。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- FULL：全量显示模式。<br>- DAYS：增量显示模式。<br>默认值：FULL<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/SRVMATCHSQRY]] · 业务匹配统计结果（SRVMATCHSQRY）

## 使用实例

查询Rule的匹配次数：

```
DSP SRVMATCHSQRY:SRVMATCHQRYT=RULE;
```

```

Service Match Statistic Query Information
-----------------------------------------
Statistic Result
Match times on Pod ssgpod-0103-30-0-235:
Rule Info:
                    Rule Name  =  ruletest(PCC)
                     MatchCnt  =  5

                    Rule Name  =  ruletest2(REMARK_FPI)
                     MatchCnt  =  2

Match times on Pod ssgpod-0103-30-0-236:
Rule Info:
                    Rule Name  =  ruletest3(PCC)
                     MatchCnt  =  2

                    Rule Name  =  ruletest4(REMARK_FPI)
                     MatchCnt  =  3

(Number of results = 2)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-SRVMATCHSQRY.md`
