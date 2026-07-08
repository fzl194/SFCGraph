---
id: UDG@20.15.2@MMLCommand@RMV HPATCH
type: MMLCommand
name: RMV HPATCH（删除热补丁）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: HPATCH
command_category: 配置类
effect_mode: ''
is_dangerous: true
category_path:
- 平台服务管理
- 操作维护
- 升级补丁管理
- 热补丁管理
status: active
---

# RMV HPATCH（删除热补丁）

## 功能

该命令用于删除指定网元微服务进程的热补丁。

> **注意**
> 本命令属于高危命令，执行此命令会删除当前网元微服务的所有热补丁，请谨慎使用。如需使用请联系华为支持协助操作。

> **说明**
> - 该命令在执行后立即生效。
> - 网元ID必须在系统中存在。

## 参数

| **参数标识** | **参数名称** | **参数说明** |
| --- | --- | --- |
| MEID | 网元ID | 可选必选说明：必选参数。<br>参数含义：用于指示系统需要删除哪个网元Id对应的热补丁。<br>取值范围：0~65535。<br>默认值：无。<br>配置原则：无。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/HPATCH]] · 热补丁（HPATCH）

## 使用实例

删除热补丁：

```
%%RMV HPATCH: MEID=0;%% 
RETCODE = 0  操作成功  

进度报告 
-------- 
已完成 = 40% 
(结果个数 = 1) 

---    END  

%%RMV HPATCH: MEID=0;%% 
RETCODE = 0  操作成功  

共有2个报告 
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除热补丁(RMV-HPATCH)_25343986.md`
