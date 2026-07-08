---
id: UNC@20.15.2@MMLCommand@LST HSSBPAPNGRP
type: MMLCommand
name: LST HSSBPAPNGRP（查询HSS BYPASS最小APN签约数据群组）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: HSSBPAPNGRP
command_category: 查询类
applicable_nf:
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- 可靠性管理
- HSS BYPASS最小签约数据配置管理
status: active
---

# LST HSSBPAPNGRP（查询HSS BYPASS最小APN签约数据群组）

## 功能

**适用网元：MME**

此命令用于查询HSS BYPASS最小APN签约数据群组配置。

## 注意事项

无

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APNGRPID | APN群组ID | 可选必选说明：可选参数<br>参数含义：该参数用于指定APN本地配置签约群组ID。<br>数据来源：本端规划<br>取值范围：0~511<br>默认值：无<br>配置原则：无 |
| APNSUBIDX | APN本地签约索引 | 可选必选说明：可选参数<br>参数含义：该参数用于指定APN群组包含的APN本地签约数据索引。<br>数据来源：本端规划<br>取值范围：0~255<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/HSSBPAPNGRP]] · HSS BYPASS最小APN签约数据群组（HSSBPAPNGRP）

## 使用实例

查询HSS BYPASS最小APN签约数据群组配置，可以用如下命令：

LST HSSBPAPNGRP:;

```
%%LST HSSBPAPNGRP:;%%
RETCODE = 0  操作成功。

操作结果如下
------------
      APN群组ID  =  0
APN本地签约索引  =  12
    是否默认APN  =  否
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-HSSBPAPNGRP.md`
