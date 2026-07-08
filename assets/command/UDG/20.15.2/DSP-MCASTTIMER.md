---
id: UDG@20.15.2@MMLCommand@DSP MCASTTIMER
type: MMLCommand
name: DSP MCASTTIMER（查询组播定时器信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: MCASTTIMER
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP组播
- MRM
- 组播定时器信息
status: active
---

# DSP MCASTTIMER（查询组播定时器信息）

## 功能

该命令用于显示组播定时器信息。

## 注意事项

该命令仅适用于非NP卡场景和NP卡非加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| COMPONENTYPE | 组件类型 | 可选必选说明：可选参数<br>参数含义：该参数用于表示组件类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- PIMCORE：PIMCORE组件。<br>- DGMP：DGMP组件。<br>- PIMBSR：PIMBSR组件。<br>- PIMAGENT：PIMAGENT组件。<br>- MGM：MGM组件。<br>默认值：无 |
| PID | 组件PID | 可选必选说明：可选参数<br>参数含义：该参数用于表示组件PID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/MCASTTIMER]] · 组播定时器信息（MCASTTIMER）

## 使用实例

查询组播定时器信息：

```
DSP MCASTTIMER:COMPONENTYPE=MGM;
```

```
RETCODE = 0  操作成功。

结果如下
--------
组件类型    组件PID     定时器名称                    定时器ID    定时器状态    定时器周期    下次超时时间

Mgm组件     47841293    MGM_PaeJoin_Calq              262145      RUNNING       00:00:00      14:16:31:590ms
Mgm组件     47841293    CSM_Msg_Retry_Calq            262147      RUNNING       00:00:00      00:00:11:600ms
Mgm组件     47841293    Job Schedule Protect Timer    262148      RUNNING       00:00:30      00:00:15:060ms
Mgm组件     47841293    Pid Node Send timer           262149      IDLE          00:00:00      00:00:00:005ms
Mgm组件     47841293    Pid Node Send timer           262150      IDLE          00:00:00      00:00:00:005ms
Mgm组件     47841293    Pid Node Send timer           262151      IDLE          00:00:00      00:00:00:005ms
Mgm组件     47841293    Pid Node Send timer           262160      IDLE          00:00:00      00:00:00:005ms
(结果个数 = 7)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询组播定时器信息（DSP-MCASTTIMER）_00441241.md`
