---
id: UNC@20.15.2@MMLCommand@STR VLRFAULTEXIT
type: MMLCommand
name: STR VLRFAULTEXIT（启动用户退出VLR故障增强状态）
nf: UNC
version: 20.15.2
verb: STR
object_keyword: VLRFAULTEXIT
command_category: 动作类
applicable_nf:
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- 可靠性管理
- VLR故障增强功能
status: active
---

# STR VLRFAULTEXIT（启动用户退出VLR故障增强状态）

## 功能

**适用网元：MME**

本命令用于启动用户退出VLR故障增强状态的任务。VLR故障恢复后，将VLR故障增强功能（ [SET VLRFAULTEN](设置VLR故障增强功能(SET VLRFAULTEN)_92948544.md) ）开关设置为关闭状态，然后可以通过本命令主动触发用户退出VLR故障增强状态。如果VLR故障增强功能（ [SET VLRFAULTEN](设置VLR故障增强功能(SET VLRFAULTEN)_92948544.md) ）开关设置为开启状态，那么本命令执行不生效。

## 注意事项

- 如果系统当前已启动用户退出VLR故障增强状态任务且未结束，再次执行本命令会重启任务。
- 通过本命令触发分离用户时，若用户处于连接态，MME立刻发起显式分离流程，并标记用户退出VLR故障增强状态；若用户处于空闲态，MME寻呼用户成功后发起显式分离流程，并标记用户退出VLR故障增强状态；若用户处于分离态，MME标记用户退出VLR故障增强状态。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| EXITPLCY | 故障状态退出策略 | 可选必选说明：必选参数<br>参数含义：该<br>**参**<br>数用于VLR故障恢复后，MME主动触发用户退出VLR故障增强状态的策略。<br>数据来源：全网规划<br>取值范围：<br>- IMSI_DETACH（IMSI分离）<br>- EPS_DETACH（EPS分离）<br>系统初始设置值：IMSI_DETACH（IMSI分离）<br>配置原则：使用EPS分离方式，可能会造成相关用户业务中断，用户短时间内重新附着，造成网络拥塞。 |
| SCANRATE | 故障恢复扫描速率(个/秒) | 可选必选说明：可选参数<br>参数含义：系统在关闭VLR故障增强功能后，需要对处于故障增强状态的用户进行分离，触发用户重新联合附着。该参数用于指定整系统的用户扫描速率。该参数为0时，按照30min扫描一轮计算。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为0~10000。<br>系统初始设置值：0<br>配置原则：该参数应能被SPP进程个数的十倍整除，否则实际扫描速率将向上取整。例如，SPP进程数为4，当该参数设为41~80(个/秒)时，实际扫描速率按80(个/秒)处理。<br>说明：启动VLR故障增强状态退出任务前，先通过DSP MMDBGINFO命令查询当前处于VLR故障增强状态的用户数，设置合适的故障恢复扫描速率：<br>DSP MMDBGINFO: MSTATE=MASTER, DBGINDEX=5;<br>回显中<br>“名称”<br>为<br>“MM_FEATURE_VLR_FAULT_USER_NUM”<br>对应的<br>“值”<br>即为当前处于VLR故障增强状态的用户数，如果没有该名称，表示当前处于VLR故障增强状态的用户数为0。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/VLRFAULTEXIT]] · 用户退出VLR故障增强状态（VLRFAULTEXIT）

## 使用实例

启动用户退出VLR故障增强状态任务，可用如下命令：

```
STR VLRFAULTEXIT: EXITPLCY=IMSI_DETACH;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/STR-VLRFAULTEXIT.md`
