---
id: UNC@20.15.2@MMLCommand@SET HLRBYPASS
type: MMLCommand
name: SET HLRBYPASS（设置HLR故障Bypass功能控制参数）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: HLRBYPASS
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
max_records: 1
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- 可靠性管理
- HLR故障BYPASS功能
status: active
---

# SET HLRBYPASS（设置HLR故障Bypass功能控制参数）

## 功能

**适用网元：SGSN**

该命令用于设置HLR故障Bypass功能控制参数。开启HLR全故障智能业务逃生功能开关后，在HLR全故障状态下业务可以惯性运行。

## 注意事项

- 该命令执行后立即生效。

- 此命令的最大记录数为1。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| BPSW | HLR Bypass功能开关 | 可选必选说明：可选参数<br>参数含义：<br>该参数用于控制开启和关闭HLR Bypass功能。<br>取值范围：<br>OFF（关闭）<br>ON（开启）<br>系统初始设置值：OFF（关闭） |
| RECOVERYACT | 退出Bypass状态恢复动作 | 可选必选说明：可选参数<br>参数含义：<br>该参数用于设置退出HLR Bypass状态的恢复动作。<br>取值范围：<br>- GRACEFUL_DEREG（优雅分离）：若用户处于连接态，SGSN待用户进入空闲态后发起显式分离流程，并标记用户退出HLR Bypass状态；若用户处于空闲态，SGSN寻呼用户成功后发起显式分离流程，并标记用户退出HLR Bypass状态；若用户处于分离态，SGSN标记用户退出HLR Bypass状态。 |
| SCANRATE | 整系统扫描速率(个/秒) | 可选必选说明：可选参数<br>参数含义：<br>该参数用于指定HLR Bypass状态的用户扫描速率。该参数为0时，按照10min扫描一轮。<br>取值范围：<br>整数类型，取值范围为0~10000。<br>系统初始设置值：0<br>配置原则：该参数应能被SPP进程个数的十倍整除，否则该参数将向上取整。例如，SPP进程数为4，当该参数设为41~80(个/秒)时，实际扫描速率按80(个/秒)处理。 |
| SCANINTERVAL | 扫描时间间隔(秒) | 可选必选说明：可选参数<br>参数含义：<br>该参数用于表示开启HLR Bypass功能后，允许同一用户连续两次向HLR发探测消息的最小时间间隔。<br>取值范围：<br>整数类型，取值范围为1~600。<br>系统初始设置值：600<br>配置原则：<br>- 如果达到扫描时间间隔后，当前任务未扫描完成，则下一个扫描时间间隔后再尝试启动。<br>- 如果达到扫描时间间隔后，当前任务已扫描完成，则立即启动重新扫描。<br>- 当系统正在扫描时，该参数修改不生效。<br>- 当扫描到无用户在HLR Bypass状态时，停止扫描。 |

## 操作的配置对象

- [HLR故障Bypass功能控制参数（HLRBYPASS）](configobject/UNC/20.15.2/HLRBYPASS.md)

## 使用实例

设置HLR故障Bypass功能控制参数，指定整系统扫描速率(个/秒)为100、扫描时间间隔(秒)为200：

```
SET HLRBYPASS: BPSW=ON, RECOVERYACT=GRACEFUL_DEREG, SCANRATE=100, SCANINTERVAL=200;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置HLR故障Bypass功能控制参数(SET-HLRBYPASS)_04085588.md`
