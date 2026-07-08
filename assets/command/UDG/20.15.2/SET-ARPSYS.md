---
id: UDG@20.15.2@MMLCommand@SET ARPSYS
type: MMLCommand
name: SET ARPSYS（配置ARP系统信息）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: ARPSYS
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- ARP管理
- ARP系统配置
status: active
---

# SET ARPSYS（配置ARP系统信息）

## 功能

该命令用于配置系统老化时间、全局ARP严格学习使能、ARP日志告警上报时间间隔和免费ARP发送类型。

## 注意事项

- 该命令执行后立即生效。
- 全局配置ARP表项老化时间，接口下ARP表项老化时间配置为默认值时，全局配置生效。全局和接口下同时配置ARP表项老化时间，接口下配置生效。
- 至少要配置一个参数。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| EXPIRETIME | LEARNSTRICTENABLE | LOGTRAPINTERVAL | GRATTYPE |
| --- | --- | --- | --- |
| 1200 | FALSE | 0 | Request |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| EXPIRETIME | 表项老化时间（s） | 可选必选说明：可选参数<br>参数含义：该参数用于指定动态ARP表项生存时间。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为60～86400，单位是秒。<br>默认值：无 |
| LEARNSTRICTENABLE | 全局ARP严格学习使能 | 可选必选说明：可选参数<br>参数含义：该参数用于指定全局ARP严格学习是否使能。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：无 |
| LOGTRAPINTERVAL | ARP日志告警上报时间间隔（s） | 可选必选说明：可选参数<br>参数含义：该参数用于指定ARP写日志和发送告警的时间间隔。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～1200，单位是秒。<br>默认值：无<br>配置原则：<br>- 当该参数初始值为0时，将抑制告警。<br>- 如果需要上报告警，建议配置ARP日志告警上报时间间隔为300s。 |
| GRATTYPE | 免费ARP发送类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定发送免费ARP报文的类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- Request：请求。<br>- Reply：应答。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/ARPSYS]] · ARP系统信息（ARPSYS）

## 使用实例

配置ARP全局老化时间为80秒，免费ARP发送类型为应答：

```
SET ARPSYS:EXPIRETIME=80,GRATTYPE=Reply;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-ARPSYS.md`
