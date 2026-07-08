---
id: UDG@20.15.2@MMLCommand@ACT MIGRATE
type: MMLCommand
name: ACT MIGRATE（异构迁移）
nf: UDG
version: 20.15.2
verb: ACT
object_keyword: MIGRATE
command_category: 动作类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 系统管理
- 架构管理
status: active
---

# ACT MIGRATE（异构迁移）

## 功能

![](异构迁移（ACT MIGRATE）_35833852.assets/notice_3.0-zh-cn.png)

该命令禁止手工执行，会导致系统异常，请确保已明确风险。

该命令用于网元由X86单板架构切换至ARM单板架构执行具体迁移子任务。

> **说明**
> 该命令仅在Full-stack虚机场景下支持。

## 注意事项

异构迁移是系统性工程，需要各个部件按固定顺序执行，本命令只是其中一个步骤，单独执行会严重影响系统稳定运行，因此禁止在前台执行。

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| OPRTYPE | 操作类型 | 可选必选说明：必选参数。<br>参数含义：操作类型。<br>取值范围：<br>- BACKUP（数据导出）<br>- SYNCFILE（文件同步）<br>- RESTORE（数据恢复）<br>- MSWITCH（主备倒换）<br>- SWFORBID（主备服务禁止倒换）<br>- SWFCANCEL（取消主备服务禁止倒换）<br>- DBDATACLR（GAUSSDB数据清除）<br>- OMADAPTERDLD（适配包下载）<br>- OSPKGDLD（OS包下载）<br>默认值：无。<br>配置原则：无。 |
| PARAM1 | 参数1 | 可选必选说明：必选参数。<br>参数含义：包含网元pod名称、请求body参数，omutype参数。请求body参数表示配置各服务对应数据库无需导出的表名称。<br>取值范围：字符或字母（a～z或A～Z），不超过2048个字符长度，omutype是枚举类型，枚举值是omu和omu-ex。<br>默认值：无。<br>配置原则：<br>- “OPRTYPE”参数为“SYNCFILE(文件同步)”，请求body参数中body内容必须为空 。 |

## 操作的配置对象

- [异构迁移查询（MIGRATE）](configobject/UDG/20.15.2/MIGRATE.md)

## 使用实例

ACT MIGRATE该命令用于OMU异构迁移，异构迁移是系统性工程，需要各个部件按固定顺序执行，本命令只是其中一个步骤，单独执行会严重影响系统稳定运行，因此禁止在前台执行。

## 证据

- 原始手册：`evidence/UDG/20.15.2/异构迁移（ACT-MIGRATE）_35833852.md`
