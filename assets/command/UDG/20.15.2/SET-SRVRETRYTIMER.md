---
id: UDG@20.15.2@MMLCommand@SET SRVRETRYTIMER
type: MMLCommand
name: SET SRVRETRYTIMER（设置服务重试等待时间）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: SRVRETRYTIMER
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 1
category_path:
- 用户面服务管理
- 业务控制策略
- 业务控制公共配置
- 服务重试定时器
status: active
---

# SET SRVRETRYTIMER（设置服务重试等待时间）

## 功能

**适用NF：PGW-U、UPF**

此命令用于设置服务上报出现上报失败/上报响应超时/响应失败的异常场景后重新发起上报需要等待的时间。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | ADCRPTRETRYTIME | QOSRPTRETRYTIME | TETHERRPTRETIME |
| --- | --- | --- | --- |
| 初始值 | 30 | 30 | 30 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ADCRPTRETRYTIME | ADC重新上报等待时间（秒） | 可选必选说明：可选参数<br>参数含义：该参数用于设置ADC重新上报的等待时间。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0-1800，单位是秒。<br>默认值：无<br>配置原则：无 |
| QOSRPTRETRYTIME | QoS重新上报等待时间（秒） | 可选必选说明：可选参数<br>参数含义：该参数用于设置Qos重新上报的等待时间。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0-1800，单位是秒。<br>默认值：无<br>配置原则：无 |
| TETHERRPTRETIME | Tethering重新上报等待时间（秒） | 可选必选说明：可选参数<br>参数含义：该参数用于设置Tethering重新上报的等待时间。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0-1800，单位是秒。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/SRVRETRYTIMER]] · 服务重试等待时间（SRVRETRYTIMER）

## 使用实例

设置ADC重新上报等待时间为40，QOS重新上报等待时间为50，Tethering重新上报等待时间为60，命令为：

```
SET SRVRETRYTIMER: ADCRPTRETRYTIME=40, QOSRPTRETRYTIME=50, TETHERRPTRETIME=60;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-SRVRETRYTIMER.md`
