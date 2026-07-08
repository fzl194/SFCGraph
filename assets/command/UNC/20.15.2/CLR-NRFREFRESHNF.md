---
id: UNC@20.15.2@MMLCommand@CLR NRFREFRESHNF
type: MMLCommand
name: CLR NRFREFRESHNF（清除网元信息刷新记录）
nf: UNC
version: 20.15.2
verb: CLR
object_keyword: NRFREFRESHNF
command_category: 动作类
applicable_nf:
- NRF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- 对端NF管理
- NF信息刷新
status: active
---

# CLR NRFREFRESHNF（清除网元信息刷新记录）

## 功能

**适用NF：NRF**

此命令用于撤销已经下发但还未生效的OPR NRFREFRESHNF命令和清除OPR NRFREFRESHNF的执行结果记录。

## 注意事项

- 该命令执行后立即生效。

- 在OPR NRFREFRESHNF命令还未生效期间执行CLR NRFREFRESHEDNF命令，OPR NRFREFRESHNF命令将被撤销，其执行记录也会被清除；如果OPR NRFREFRESHNF命令已经生效，或者过期则无法撤销，只清除其执行记录。
- 此命令需要与DSP NRFREFRESHEDNF配合使用，命令执行前，先通过DSP NRFREFRESHEDNF查询是否有可以撤销的命令，命令执行后，通过DSP NRFREFRESHEDNF查询执行结果。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFINSTANCEID | NF实例标识 | 可选必选说明：可选参数<br>参数含义：该参数表示待指示刷新的NF实例标识。如果输入具体的NF实例标识，表示撤销该NF的OPR NRFREFRESHNF操作并清除其操作记录。如果不输入具体的NF实例标识，表示撤销所有已执行的OPR NRFREFRESHNF操作并清除其操作记录。如果OPR NRFREFRESHNF命令还未生效则撤销该命令并清除其操作记录，如果命令已经生效或过期，则只清除其操作记录。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~36。该参数只能由字母（A-Z或者a-z）、数字（0-9）、中划线（-）组成。不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [操作执行网元信息刷新（NRFREFRESHNF）](configobject/UNC/20.15.2/NRFREFRESHNF.md)

## 使用实例

清除NF实例标识为123e4567-e89b-12d3-a456-426655440000的网元信息刷新记录。

```
CLR NRFNFATTRVRY: NFINSTANCEID="123e4567-e89b-12d3-a456-426655440000";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/清除网元信息刷新记录（CLR-NRFREFRESHNF）_35374735.md`
