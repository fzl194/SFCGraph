---
id: UDG@20.15.2@MMLCommand@LST EVTPARA
type: MMLCommand
name: LST EVTPARA（查询策略参数值）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: EVTPARA
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 可靠性管理
- 微服务可靠性管理
status: active
---

# LST EVTPARA（查询策略参数值）

## 功能

该命令用于查询策略参数值。

> **说明**
> 无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SERVICE | 服务名称 | 可选必选说明：可选参数<br>参数含义：该参数表示策略模型绑定的服务名称，可以通过<br>[**LST EVTPARA**](查询策略参数值（LST EVTPARA）_36260906.md)<br>命令获取参数。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~16。<br>默认值：无<br>配置原则：无 |
| EVENTID | 事件ID | 可选必选说明：可选参数<br>参数含义：该参数表示服务名称对应的事件ID，可以通过<br>[**LST EVTPARA**](查询策略参数值（LST EVTPARA）_36260906.md)<br>命令获取参数。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~4294967295。<br>默认值：无<br>配置原则：<br>只支持配置LST EVTPARA命令获取到的服务实例。 |
| PARANAME | 策略参数 | 可选必选说明：可选参数<br>参数含义：该参数用于表示策略对应的参数名称。<br>数据来源：本端规划<br>取值范围：<br>- “AssStatic-Suspect（关联诊断嫌疑实例数）”：关联诊断配置的嫌疑实例数量。<br>- “AssStatic-Proportion（关联诊断嫌疑实例比例）”：关联诊断配置的嫌疑实例比例。<br>- “CellReset-Delay（进程复位延迟时间）”：进程复位延迟执行时间。<br>- “CellReset-Retry（进程复位重试次数）”：进程复位重试次数。<br>- “CellReset-Interval（进程复位间隔时间）”：进程复位重试间隔。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@EVTPARA]] · 策略参数值（EVTPARA）

## 使用实例

查询配置表内事件1关联诊断中参数嫌疑实例数量的值

```
%%LST EVTPARA: SERVICE="SDRS", EVENTID=1, PARANAME=AssStatic-Suspect;%%
RETCODE = 0  操作成功

结果如下
-----------
  服务名称 = SDRS
    事件ID = 1
  策略参数 = 关联诊断嫌疑实例数
策略参数值 = 4
  事件名称 = sdrs link down1
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-EVTPARA.md`
