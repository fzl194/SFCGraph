---
id: UDG@20.15.2@MMLCommand@SET IOTCAPABILITY
type: MMLCommand
name: SET IOTCAPABILITY（设置物联网能力上报）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: IOTCAPABILITY
command_category: 配置类
applicable_nf:
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 1
category_path:
- 用户面服务管理
- NB-IOT管理
- 物联网能力
status: active
---

# SET IOTCAPABILITY（设置物联网能力上报）

## 功能

**适用NF：UPF**

设置UPF的物联网能力上报功能选择指示。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | NBIOT |
| --- | --- |
| 初始值 | ENABLE |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NBIOT | NB-IoT接入能力上报 | 可选必选说明：可选参数<br>参数含义：该参数用来打开或者关闭UPF的NB-IoT用户接入功能。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [物联网能力上报（IOTCAPABILITY）](configobject/UDG/20.15.2/IOTCAPABILITY.md)

## 关联任务

- [0-00085](task/UDG/20.15.2/0-00085.md)

## 使用实例

配置UPF的NB-IoT用户接入能力上报功能开关为ENABLE：

```
SET IOTCAPABILITY:NBIOT=ENABLE;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置物联网能力上报（SET-IOTCAPABILITY）_70824408.md`
