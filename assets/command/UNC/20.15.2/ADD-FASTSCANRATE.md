---
id: UNC@20.15.2@MMLCommand@ADD FASTSCANRATE
type: MMLCommand
name: ADD FASTSCANRATE（增加快速扫描任务）
nf: UNC
version: 20.15.2
verb: ADD
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

# ADD FASTSCANRATE（增加快速扫描任务）

## 功能

**适用NF：SMF、SGW-C、PGW-C、GGSN**

该命令用于增加快速扫描任务。

## 注意事项

- 该命令执行后立即生效。

- 当扫描任务类型配置为“UPF去活扫描任务”时，会话去活时长会受整系统去活会话的流控保护（SET DEACTIVERATE）影响。
- 当扫描任务类型配置为“UPF去活扫描任务”时，推荐速率为单DS 1个/秒，若速率过快，超过流控阈值（SET DEACTIVERATE），扫描进度会变缓。

- 最多可输入100条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TASKTYPE | 扫描任务类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定扫描任务的类型。<br>数据来源：本端规划<br>取值范围：<br>- UPF_DEACTIVE（UPF去活扫描任务）<br>- SBC_FAULT（SBC故障扫描任务）<br>默认值：无<br>配置原则：无 |
| RATE | 单DS扫描速率(个/秒) | 可选必选说明：必选参数<br>参数含义：该参数用于设置指定扫描任务的单DS扫描速率。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~300，单位是个每秒。<br>默认值：无<br>配置原则：<br>推荐扫描速率为单DS 1个/秒。可根据实际情况进行修改，若速率过快会导致对端过载。单DS每秒扫描的个数计算公式为：DSP FASTSCANDATA中汇总的扫描任务数据个数结果/全部扫描完成的期望时间（秒）/DSP FASTSCANDATA中汇总的Token编号。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/FASTSCANRATE]] · 快速扫描任务（FASTSCANRATE）

## 使用实例

增加扫描任务类型为UPF_DEACTIVE，扫描速率为200的快速扫描任务：

```
ADD FASTSCANRATE: TASKTYPE=UPF_DEACTIVE, RATE=200;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加快速扫描任务（ADD-FASTSCANRATE）_11762196.md`
