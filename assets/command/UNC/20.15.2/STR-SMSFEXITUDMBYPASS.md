---
id: UNC@20.15.2@MMLCommand@STR SMSFEXITUDMBYPASS
type: MMLCommand
name: STR SMSFEXITUDMBYPASS（启动用户退出UDM Bypass任务）
nf: UNC
version: 20.15.2
verb: STR
object_keyword: SMSFEXITUDMBYPASS
command_category: 动作类
applicable_nf:
- SMSF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- SMSF业务管理
- UDM Bypass管理
status: active
---

# STR SMSFEXITUDMBYPASS（启动用户退出UDM Bypass任务）

## 功能

**适用NF：SMSF**

该命令用于启动用户退出UDM Bypass任务。当UDM故障已恢复但用户尚未退出UDM Bypass状态时，可以执行该命令使用户退出UDM Bypass状态。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QUITTYPE | 退出方式 | 可选必选说明：必选参数<br>参数含义：该参数用于指定用户退出UDM Bypass的方式。<br>数据来源：本端规划<br>取值范围：<br>- “SUPPLEMENT_UDM_INTERACT（补充缺失的UDM流程）”：SMSF补齐和UDM交互的注册、签约数据获取和订阅三次流程，若成功则标记用户退出UDM Bypass状态，否则继续标记用户处于UDM Bypass状态。<br>- “DEREG（去注册）”：SMSF发起去注册，标记用户退出UDM Bypass状态。<br>默认值：无<br>配置原则：无 |
| SCANRATE | 扫描速率(个/秒) | 可选必选说明：必选参数<br>参数含义：该参数用于指定每个DS（Domain服务）每秒扫描多少个用户，扫描到处于UDM Bypass的用户后，SMSF根据QUITTYPE参数设置使用户退出UDM Bypass状态。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~1000，单位是个每秒。<br>默认值：无<br>配置原则：<br>DS个数 × 扫描速率 = 整系统扫描速率。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SMSFEXITUDMBYPASS]] · 用户退出UDM Bypass任务（SMSFEXITUDMBYPASS）

## 使用实例

如果希望进入到UDM Bypass状态的用户能够退出该状态，可以通过该命令使用户退出UDM Bypass状态，执行如下命令：

```
STR SMSFEXITUDMBYPASS: QUITTYPE=SUPPLEMENT_UDM_INTERACT, SCANRATE=20;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/STR-SMSFEXITUDMBYPASS.md`
