---
id: UNC@20.15.2@MMLCommand@RMV FASTSCANRATE
type: MMLCommand
name: RMV FASTSCANRATE（删除快速扫描任务）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: FASTSCANRATE
command_category: 配置类
applicable_nf:
- SMF
- SGW-C
- PGW-C
- GGSN
effect_mode: 立即生效
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

# RMV FASTSCANRATE（删除快速扫描任务）

## 功能

**适用NF：SMF、SGW-C、PGW-C、GGSN**

该命令用于删除快速扫描任务。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TASKTYPE | 扫描任务类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定扫描任务的类型。<br>数据来源：本端规划<br>取值范围：<br>- UPF_DEACTIVE（UPF去活扫描任务）<br>- SBC_FAULT（SBC故障扫描任务）<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [快速扫描任务（FASTSCANRATE）](configobject/UNC/20.15.2/FASTSCANRATE.md)

## 使用实例

删除扫描任务类型为UPF_DEACTIVE的快速扫描任务：

```
RMV FASTSCANRATE: TASKTYPE=UPF_DEACTIVE;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除快速扫描任务（RMV-FASTSCANRATE）_47441361.md`
