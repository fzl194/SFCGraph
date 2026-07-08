---
id: UDG@20.15.2@MMLCommand@RMV QOSCARBURST
type: MMLCommand
name: RMV QOSCARBURST（删除用户做car的参数）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: QOSCARBURST
command_category: 配置类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 用户QOS控制
- 流量管理
- 配置Qos Car桶深信息
status: active
---

# RMV QOSCARBURST（删除用户做car的参数）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用于清除用户流量管理时的突发尺寸（即令牌桶的深度）做CAR时的突发尺寸。

## 注意事项

- 该命令执行后立即生效。
- RMV QoSCARBURST命令只能用于清除已配置的Rate对应的突发尺寸。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RATE | Qos-Car速率（千比特/秒） | 可选必选说明：必选参数<br>参数含义：该参数用于指定速率，该参数一般由运营商规划给出。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295，单位是千比特每秒。<br>默认值：无<br>配置原则：当指定速率rate为0时，配置的突发尺寸是系统的缺省值。若配置的缺省值为0，或未配置缺省值，则缺省的突发尺寸和速率rate有关：若rate为0，则突发尺寸的值为0。若rate（kbit/s）<=53kbit/s，则突发尺寸的值为10000 Byte。若rate（kbit/s）>53kbit/s，突发尺寸的值等于rate（kbit/s）*1000/8*1.5s，单位是Byte。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/QOSCARBURST]] · 用户做car的参数（QOSCARBURST）

## 使用实例

删除128kbps速率的突发尺寸的配置：

```
RMV QOSCARBURST:RATE=128;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除用户做car的参数（RMV-QOSCARBURST）_86528829.md`
