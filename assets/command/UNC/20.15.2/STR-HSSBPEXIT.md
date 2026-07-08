---
id: UNC@20.15.2@MMLCommand@STR HSSBPEXIT
type: MMLCommand
name: STR HSSBPEXIT（启动用户退出HSS BYPASS状态）
nf: UNC
version: 20.15.2
verb: STR
object_keyword: HSSBPEXIT
command_category: 动作类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- 可靠性管理
- HSS故障BYPASS功能
status: active
---

# STR HSSBPEXIT（启动用户退出HSS BYPASS状态）

## 功能

**适用网元：MME**

本命令用于启动用户退出HSS BYPASS状态的任务。当用户由于某种原因无法自动退出HSS BYPASS状态，或希望强制分离HSS BYPASS用户，可以通过该命令手动启动用户退出HSS BYPASS状态的任务来退出。

## 注意事项

- 该命令执行后立即生效。
- 当启动退出HSS Bypass任务时，CPU和内存使用率会升高，和周边网元交互消息量增大，待用户退出HSS Bypass任务完成后，系统将恢复正常。
- 相关license授权并开启后，此命令配置才能执行（License部件编码：LKV2HSSBP01）。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RECOVERYACT | 退出Bypass状态恢复动作 | 可选必选说明：必选参数<br>参数含义：该参数用于设置HSS BYPASS状态恢复动作。<br>数据来源：全网规划<br>取值范围：<br>- GRACEFUL_DEREG（优雅分离）：若用户处于连接态，MME待用户进入空闲态后发起显式分离流程，并标记用户退出HSS BYPASS状态；若用户处于空闲态，MME寻呼用户成功后发起显式分离流程，并标记用户退出HSS BYPASS状态；若用户处于分离态，MME标记用户退出HSS Bypass状态。<br>- SUPPLEMENT_INTERACT（补充缺失流程）：MME补齐和HSS交互的位置更新和Notify流程，若成功则标记用户退出HSS BYPASS状态，否则继续标记用户处于HSS BYPASS状态。<br>- FORCED_DEREG（强制分离）：若用户处于连接态，MME立刻发起显式分离流程，并标记用户退出HSS BYPASS状态；若用户处于空闲态，MME寻呼用户成功后发起显式分离流程，并标记用户退出HSS BYPASS状态；若用户处于分离态，MME标记用户退出HSS Bypass状态。<br>默认值：GRACEFUL_DEREG（优雅分离）<br>说明：当该参数选择为SUPPLEMENT_INTERACT（补充缺失流程），且退出流程成功时，如果用户没有MSISDN，退出流程将变为GRACEFUL_DEREG（优雅分离）。 |

## 操作的配置对象

- [用户退出HSS BYPASS状态（HSSBPEXIT）](configobject/UNC/20.15.2/HSSBPEXIT.md)

## 使用实例

启动用户退出HSS BYPASS状态任务，可用如下命令。

```
STR HSSBPEXIT: RECOVERYACT=FORCED_DEREG;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/启动用户退出HSS-BYPASS状态(STR-HSSBPEXIT)_20995641.md`
