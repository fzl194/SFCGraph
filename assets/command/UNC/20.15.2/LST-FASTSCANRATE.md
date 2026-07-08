---
id: UNC@20.15.2@MMLCommand@LST FASTSCANRATE
type: MMLCommand
name: LST FASTSCANRATE（查询快速扫描任务）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: FASTSCANRATE
command_category: 查询类
applicable_nf:
- SMF
- SGW-C
- PGW-C
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 操作维护
- 设备管理
- 快速扫描任务管理
status: active
---

# LST FASTSCANRATE（查询快速扫描任务）

## 功能

**适用NF：SMF、SGW-C、PGW-C、GGSN**

该命令用于查询快速扫描任务。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TASKTYPE | 扫描任务类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定扫描任务的类型。<br>数据来源：本端规划<br>取值范围：<br>- UPF_DEACTIVE（UPF去活扫描任务）<br>- SBC_FAULT（SBC故障扫描任务）<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/FASTSCANRATE]] · 快速扫描任务（FASTSCANRATE）

## 使用实例

查询当前系统中TASKTYPE=UPF_DEACTIVE的快速扫描任务：

```
%%LST FASTSCANRATE: TASKTYPE=UPF_DEACTIVE;%%
RETCODE = 0  操作成功

结果如下
--------
扫描任务类型  =  UPF_DEACTIVE
扫描速率      =  200
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询快速扫描任务（LST-FASTSCANRATE）_11602432.md`
