---
id: UNC@20.15.2@MMLCommand@DSP MIGRATE
type: MMLCommand
name: DSP MIGRATE（异构迁移查询）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: MIGRATE
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 系统管理
- 架构管理
status: active
---

# DSP MIGRATE（异构迁移查询）

## 功能

该命令用于网元由X86单板架构切换至ARM单板架构时查询迁移子任务执行状态。

> **说明**
> 该命令仅在Full-stack虚机场景下支持。

## 注意事项

无。

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| EVENT | 事件类型 | 可选必选说明：必选参数。<br>参数含义：事件类型。<br>取值范围：<br>- GAUSSDB_TASK_QUERY（GAUSSDB任务查询）<br>- VA_TASK_QUERY（VA任务查询）<br>默认值：无。<br>配置原则：无。 |
| SUBEVENT | 子事件类型 | 可选必选说明：必选参数。<br>参数含义：子事件类型。<br>取值范围：<br>- BACKUP（数据导出查询）<br>- SYNCFILE（数据迁移查询）<br>- RESTORE（数据导入查询）<br>- OMADAPTERDLD（适配包下载状态查询）<br>- OSPKGDLD（OS包下载状态查询）<br>默认值：无。<br>配置原则：无。 |
| PARAM1 | 参数1 | 可选必选说明：必选参数。<br>参数含义：包含网元pod名称，omutype参数。<br>取值范围：字符或字母（a～z或A～Z），不超过512个字符长度，omutype是枚举类型，枚举值是omu和omu-ex。<br>默认值：无。<br>配置原则：无。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/MIGRATE]] · 异构迁移查询（MIGRATE）

## 使用实例

查询GAUSSDB数据库数据导出任务状态。

```
%%DSP MIGRATE: EVENT=GAUSSDB_TASK_QUERY, SUBEVENT=BACKUP, PARAM1="{#podname#:#gaussdb-9cbed835-1#&#omutype#:#omu#}";%%
RETCODE = 0  操作成功
DSP MIGRATE
-----------
  事件类型  =  GAUSSDB_TASK_QUERY
子事件类型  =  BACKUP
     参数1  =  {#podname#:#gaussdb-9cbed835-1#& #omutype#:#omu#}
      状态  =  success
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-MIGRATE.md`
