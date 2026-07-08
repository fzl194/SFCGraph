---
id: UNC@20.15.2@MMLCommand@STR AMFEXITUDMBYPASS
type: MMLCommand
name: STR AMFEXITUDMBYPASS（启动用户退出UDM Bypass状态任务）
nf: UNC
version: 20.15.2
verb: STR
object_keyword: AMFEXITUDMBYPASS
command_category: 动作类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 可靠性管理
- AMF的UDM故障BYPASS功能
status: active
---

# STR AMFEXITUDMBYPASS（启动用户退出UDM Bypass状态任务）

## 功能

![](启动用户退出UDM Bypass状态任务（STR AMFEXITUDMBYPASS）_13800474.assets/notice_3.0-zh-cn_2.png)

当启动用户退出UDM Bypass任务时，CPU和内存使用率会升高，和周边网元交互消息量增大，待用户退出UDM Bypass任务完成后，系统会恢复正常。

**适用NF：AMF**

该命令用于启动用户退出UDM Bypass任务。当UDM故障已恢复但用户尚未退出UDM Bypass状态时，可以执行该命令使用户退出UDM Bypass状态。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QUITTYPE | 退出方式 | 可选必选说明：必选参数<br>参数含义：该参数用于指定用户退出UDM Bypass的方式。<br>数据来源：本端规划<br>取值范围：<br>- “GRACEFUL_DEREG（优雅去注册）”：若用户处于连接态，AMF待用户进入空闲态后发起显式去注册流程，并标记用户退出UDM Bypass状态；若用户处于空闲态，AMF寻呼用户成功后发起显式去注册流程，并标记用户退出UDM Bypass状态；若用户处于去注册态，AMF标记用户退出UDM Bypass状态。<br>- “SUPPLEMENT_UDM_INTERACT（补充缺失的UDM流程）”：AMF补齐和UDM交互的注册、签约数据获取和订阅三次流程，若成功则标记用户退出UDM Bypass状态，否则继续标记用户处于UDM Bypass状态。<br>- “FORCED_DEREG（强制去注册）”：若用户处于连接态，AMF直接发起显式去注册流程，并标记用户退出UDM Bypass状态；若用户处于空闲态，AMF寻呼用户成功后发起显式去注册流程，并标记用户退出UDM Bypass状态；若用户处于去注册态，AMF标记用户退出UDM Bypass状态。<br>默认值：无<br>配置原则：无 |
| SCANRATE | 扫描速率(个/秒) | 可选必选说明：必选参数<br>参数含义：该参数用于指定每个DS每秒扫描多少个用户，扫描到处于UDM Bypass的用户后，AMF根据QUITTYPE参数设置使用户退出UDM Bypass状态。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~20，单位是个每秒。<br>默认值：无<br>配置原则：<br>DS个数 × 扫描速率 = 整系统扫描速率。<br>DS个数来源于如下命令输出结果中记录个数：<br>DSP FRAMEDBG: DBGSTR="UeamCtrlSvc coordinator all";<br>如果结果没有分批显示，则记录个数为回显中“结果个数”字段的值减1；如果结果分批显示，则记录个数为最终的结果个数减1。 |

## 操作的配置对象

- [用户退出UDM Bypass状态任务（AMFEXITUDMBYPASS）](configobject/UNC/20.15.2/AMFEXITUDMBYPASS.md)

## 使用实例

如果希望进入到UDM Bypass状态的用户能够退出该状态，可以通过该命令使用户退出UDM Bypass状态，以退出方式为优雅去注册方式，扫描速率为1个/秒，执行如下命令：

```
STR AMFEXITUDMBYPASS:QUITTYPE=GRACEFUL_DEREG,SCANRATE=1;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/启动用户退出UDM-Bypass状态任务（STR-AMFEXITUDMBYPASS）_13800474.md`
