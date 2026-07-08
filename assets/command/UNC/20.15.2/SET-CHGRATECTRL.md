---
id: UNC@20.15.2@MMLCommand@SET CHGRATECTRL
type: MMLCommand
name: SET CHGRATECTRL（计费速率控制）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: CHGRATECTRL
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: true
max_records: 1
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 计费控制
- 计费相关速率控制
status: active
---

# SET CHGRATECTRL（计费速率控制）

## 功能

**适用NF：PGW-C、SMF**

![](计费速率控制（SET CHGRATECTRL）_09896823.assets/notice_3.0-zh-cn_2.png)

本命令属于高危命令，ONLINEREC --- POD粒度生效，如果现网smpod个数多，可能导致对UPF，OCS造成信令冲击； CONVERGEDREC --- 整机粒度生效，配置上限1000条/s，对周边无影响;

该命令用于设置每个POD上，当在线计费用户转离线后，每秒最大离线转在线的用户数。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | ONLINEREC | CONVERGEDREC |
| --- | --- | --- |
| 初始值 | 300 | 500 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ONLINEREC | 在线计费恢复速率 | 可选必选说明：可选参数<br>参数含义：该参数表示每个SM-POD每秒最大恢复的在线计费上下文数。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为10～1000。10到1000的整数。<br>默认值：无<br>配置原则：无 |
| CONVERGEDREC | 融合计费恢复速率 | 可选必选说明：可选参数<br>参数含义：该参数表示整机每秒最大恢复的融合计费会话数。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为10～1000。10到1000的整数。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@CHGRATECTRL]] · 计费速率控制（CHGRATECTRL）

## 使用实例

设置OnlineRec为500：

```
SET CHGRATECTRL: ONLINEREC=500;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-CHGRATECTRL.md`
