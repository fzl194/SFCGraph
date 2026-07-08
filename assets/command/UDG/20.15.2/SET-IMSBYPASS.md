---
id: UDG@20.15.2@MMLCommand@SET IMSBYPASS
type: MMLCommand
name: SET IMSBYPASS（设置IMS Bypass功能相关参数）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: IMSBYPASS
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 对新流生效
is_dangerous: false
max_records: 1
category_path:
- 用户面服务管理
- VOLTE管理
- IMS Bypass
status: active
---

# SET IMSBYPASS（设置IMS Bypass功能相关参数）

## 功能

**适用NF：PGW-U、UPF**

该命令用于设置PCF双故障场景下，IMS语音业务保障功能的开关及相关参数。

## 注意事项

- 该命令执行后对新数据流生效。
- 该命令最大记录数为1。
- IMS Bypass功能在当前版本为测试特性，仅用于测试场景，不能用于现网业务部署。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | IMSBYPASSSW | QOSURRFLOWRPT | QOSURRHYSTIMER |
| --- | --- | --- | --- |
| 初始值 | DISABLE | FLOW | 0 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IMSBYPASSSW | IMS Bypass 开关 | 可选必选说明：必选参数<br>参数含义：该参数用于设置IMS Bypass开关。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |
| QOSURRFLOWRPT | QoSURR上报流信息方式 | 可选必选说明：条件可选参数<br>前提条件：该参数在“IMSBYPASSSW”配置为“ENABLE”时为可选参数。<br>参数含义：该参数用于设置IMS业务触发QoSURR时流信息的填充方式。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- FLOW：基于数据报文五元组上报。<br>- FILTER：基于命中的FILTER上报。<br>默认值：无<br>配置原则：无 |
| QOSURRHYSTIMER | QoSURR的迟滞时间（秒） | 可选必选说明：条件可选参数<br>前提条件：该参数在“IMSBYPASSSW”配置为“ENABLE”时为可选参数。<br>参数含义：该参数用于配置QoS类型URR Stop上报迟滞时间。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～3600，单位是秒。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/IMSBYPASS]] · IMS Bypass功能的相关参数（IMSBYPASS）

## 关联任务

- [[UDG@20.15.2@Task@0-00282]]

## 使用实例

在需要开启IMS Bypass功能时，通过此命令设置流上报模式和迟滞时间：

```
SET IMSBYPASS: IMSBYPASSSW=ENABLE,QOSURRFLOWRPT=FLOW,QOSURRHYSTIMER=0;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置IMS-Bypass功能相关参数（SET-IMSBYPASS）_08965289.md`
