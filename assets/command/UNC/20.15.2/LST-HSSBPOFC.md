---
id: UNC@20.15.2@MMLCommand@LST HSSBPOFC
type: MMLCommand
name: LST HSSBPOFC（查询故障状态HSS）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: HSSBPOFC
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
- HSS故障BYPASS功能
status: active
---

# LST HSSBPOFC（查询故障状态HSS）

## 功能

**适用网元：MME**

该命令用于查询配置的故障状态HSS配置。

## 注意事项

无。

## 权限

manage-ug;system-ug;monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/HSSBPOFC]] · 故障状态HSS（HSSBPOFC）

## 使用实例

查询已经配置的所有故障状态HSS数据。

```
%%LST HSSBPOFC:;%% 
RETCODE = 0  操作成功 
The result is as follows 
------------------------ 
HOSTNAME  =  huawei 
(结果个数 = 1)  
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询故障状态HSS(LST-HSSBPOFC)_20653489.md`
