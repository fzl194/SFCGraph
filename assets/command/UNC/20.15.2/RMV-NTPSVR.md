---
id: UNC@20.15.2@MMLCommand@RMV NTPSVR
type: MMLCommand
name: RMV NTPSVR（删除NTP服务器）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: NTPSVR
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 设备管理
- NTP服务器管理
status: active
---

# RMV NTPSVR（删除NTP服务器）

## 功能

本命令用于删除一条NTP服务器数据记录。

> **说明**
> 执行命令删除NTP服务器后，同步状态更新需等待约三个同步周期（默认一个同步周期为一分钟）。

## 注意事项

- 删除NTP服务器，可能会影响系统的时间准确性，请操作员在执行该操作之前仔细确认任务的可行性。
- 在一次删除操作中，操作员只能删除一条NTP服务器数据记录。
- 禁止在升级、打补丁、回退过程中、升级观察期内删除NTP服务器。

## 参数

| **参数标识** | **参数名称** | **参数说明** |
| --- | --- | --- |
| SVRNAME | NTP服务器名 | 可选必选说明：必选参数。<br>参数含义：标识一条NTP服务器数据记录的关键字段，用于指定需要删除哪一条NTP服务器数据记录，操作员可以使用<br>[**LST NTPSVR**](查询NTP服务器(LST NTPSVR)_54491178.md)<br>命令查询获得。<br>取值范围：长度不超过32个字符。<br>默认值：无。<br>配置原则：无。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NTPSVR]] · NTP服务器（NTPSVR）

## 使用实例

删除一个服务器， “NTP服务器名” 为 “NtpSvrName” :

RMV NTPSVR: SVRNAME="NtpSvrName";

```
%%RMV NTPSVR: SVRNAME="NtpSvrName";%% 
RETCODE = 0  操作成功  
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-NTPSVR.md`
