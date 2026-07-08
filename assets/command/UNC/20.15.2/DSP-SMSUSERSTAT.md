---
id: UNC@20.15.2@MMLCommand@DSP SMSUSERSTAT
type: MMLCommand
name: DSP SMSUSERSTAT（显示CS粒度或DS粒度的用户数）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: SMSUSERSTAT
command_category: 查询类
applicable_nf:
- SMSF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- SMSF业务管理
- SMS维测管理
status: active
---

# DSP SMSUSERSTAT（显示CS粒度或DS粒度的用户数）

## 功能

**适用NF：SMSF**

该命令用于显示CS粒度或DS粒度的用户数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| STATFUNCTYPE | 统计目标的逻辑功能类型 | 可选必选说明：必选参数<br>参数含义：该参数用于表示统计目标的逻辑功能类型。<br>数据来源：本端规划<br>取值范围：<br>- “SMSF（短消息服务功能）”：短消息服务功能<br>- “VLR（拜访地位置寄存器）”：拜访地位置寄存器<br>默认值：无<br>配置原则：无 |
| STATGRANULARITY | 统计粒度的类型 | 可选必选说明：必选参数<br>参数含义：该参数用于表示统计粒度的类型。<br>数据来源：本端规划<br>取值范围：<br>- “CS（Cell服务）”：Cell服务<br>- “DS（Domain服务）”：Domain服务<br>默认值：无<br>配置原则：无 |
| USERTYPE | 用户类型 | 可选必选说明：该参数在"STATFUNCTYPE"配置为"VLR"时为条件可选参数。<br>参数含义：该参数用于表示查询的用户类型。<br>数据来源：本端规划<br>取值范围：<br>- “MOMT（签约MO或MT业务的用户）”：VLR全量用户表中签约MOMT业务的用户数<br>- “NON-MOMT（未签约MO和MT业务的用户）”：VLR全量用户表既未签约MO也未签约MT业务的用户数<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SMSUSERSTAT]] · CS粒度或DS粒度的用户数（SMSUSERSTAT）

## 使用实例

当运营商希望查询CS粒度的VLR用户数，执行如下命令：

```
DSP SMSUSERSTAT: STATFUNCTYPE=VLR, STATGRANULARITY=CS;
%%DSP SMSUSERSTAT: STATFUNCTYPE=VLR, STATGRANULARITY=CS;%%
RETCODE = 0  操作成功

结果如下：
------------------------
                    统计结果对应的实体  =  CS1
                    统计实体上的用户数(个)  =  50

(结果个数 = 1)
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-SMSUSERSTAT.md`
