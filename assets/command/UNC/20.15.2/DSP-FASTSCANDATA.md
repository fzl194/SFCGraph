---
id: UNC@20.15.2@MMLCommand@DSP FASTSCANDATA
type: MMLCommand
name: DSP FASTSCANDATA（显示快速扫描任务信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: FASTSCANDATA
command_category: 查询类
applicable_nf:
- SGW-C
- PGW-C
- SMF
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

# DSP FASTSCANDATA（显示快速扫描任务信息）

## 功能

**适用NF：SGW-C、PGW-C、SMF、GGSN**

该命令用于显示快速扫描任务信息。

## 注意事项

最多输出100个DS的快速扫描任务详细信息，最后一行输出所有DS的汇总记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TASKTYPE | 扫描任务类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定扫描任务类型。<br>数据来源：本端规划<br>取值范围：<br>- UPF_DEACTIVE（UPF去活扫描任务）<br>- SBC_FAULT（SBC故障扫描任务）<br>默认值：无<br>配置原则：无 |
| CONDITION | 查询条件 | 可选必选说明：可选参数<br>参数含义：该参数用于表示扫描任务数据查询条件。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~1024。<br>默认值：无<br>配置原则：<br>不输入CONDITION时，查询指定TASKTYPE的所有任务信息。TASKTYPE为UPF_DEACTIVE时，需要查询特定UPF实例的任务信息时，CONDITION填写UPF实例ID，UPF实例ID不区分大小写。TASKTYPE为SBC_FAULT时，需要查询特定UPF实例关联特定PCSCF地址的任务信息时，CONDITION填写UPF实例ID+PCSCFIP，UPF实例ID不区分大小写。 |

## 操作的配置对象

- [快速扫描任务信息（FASTSCANDATA）](configobject/UNC/20.15.2/FASTSCANDATA.md)

## 使用实例

- 查询系统中TASKTYPE=UPF_DEACTIVE的快速扫描任务信息：
  ```
  %%DSP FASTSCANDATA: TASKTYPE=UPF_DEACTIVE;%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
  扫描任务类型      查询条件     Token编号   扫描任务数据个数

  UPF去活扫描任务   NULL         9           10
  UPF去活扫描任务   NULL         5           10
  UPF去活扫描任务   NULL         2           20
  (结果个数 = 3)

  ---    END
  ```
- 查询系统中TASKTYPE=UPF_DEACTIVE，CONDITION=“upf_instance_1”（对应UPF实例ID为“upf_instance_1”）的快速扫描任务信息：
  ```
  %%DSP FASTSCANDATA: TASKTYPE=UPF_DEACTIVE, CONDITION="upf_instance_1";%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
  扫描任务类型      查询条件         Token编号   扫描任务数据个数

  UPF去活扫描任务   upf_instance_1   9           10
  UPF去活扫描任务   upf_instance_1   5           10
  UPF去活扫描任务   upf_instance_1   2           20
  (结果个数 = 3)

  ---    END
  ```
- 查询系统中TASKTYPE为SBC_FAULT的快速扫描任务信息：
  ```
  %%DSP FASTSCANDATA: TASKTYPE=SBC_FAULT;%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
  扫描任务类型      查询条件     Token编号   扫描任务数据个数

  SBC故障扫描任务   NULL         9           10
  SBC故障扫描任务   NULL         5           10
  SBC故障扫描任务   NULL         2           20
  (结果个数 = 3)

  ---    END
  ```
- 查询系统中TASKTYPE为SBC_FAULT，CONDITION为"upf_instance_1+1.2.3.4"（对应UPF实例ID为"upf_instance_1"，PCSCFID为"1.2.3.4"）的快速扫描任务信息：
  ```
  %%DSP FASTSCANDATA: TASKTYPE=SBC_FAULT, CONDITION="upf_instance_1+1.2.3.4";%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
  扫描任务类型      查询条件                 Token编号   扫描任务数据个数

  SBC故障扫描任务   upf_instance_1+1.2.3.4   9           10
  SBC故障扫描任务   upf_instance_1+1.2.3.4   5           10
  SBC故障扫描任务   upf_instance_1+1.2.3.4   2           20
  (结果个数 = 3)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示快速扫描任务信息（DSP-FASTSCANDATA）_47441357.md`
