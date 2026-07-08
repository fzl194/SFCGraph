---
id: UDG@20.15.2@MMLCommand@SET RPTPERIOD
type: MMLCommand
name: SET RPTPERIOD（设置APN N6故障状态上报周期）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: RPTPERIOD
command_category: 配置类
applicable_nf:
- SGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 1
category_path:
- 用户面服务管理
- 路径管理
- N6路径管理
- APN周期上报参数
status: active
---

# SET RPTPERIOD（设置APN N6故障状态上报周期）

## 功能

**适用NF：SGW-U、UPF**

该命令用于设置APN N6故障状态上报周期。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 周期上报时间参数配置需要小于SMF故障apn的老化时长（通过LST PFCPPARA命令查询）。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | RPTPERIOD |
| --- | --- |
| 初始值 | 4 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RPTPERIOD | APN N6故障状态周期上报时长 | 可选必选说明：必选参数<br>参数含义：设置APN状态周期上报时长。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围0~72，单位是小时。需要关闭周期上报功能时，设置为0。<br>默认值：无<br>配置原则：必须小于SMF上配置的老化时间。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/RPTPERIOD]] · APN N6故障状态上报周期（RPTPERIOD）

## 使用实例

设置APN N6故障状态上报周期为4小时,做如下配置：

```
SET RPTPERIOD: RPTPERIOD=4;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-RPTPERIOD.md`
