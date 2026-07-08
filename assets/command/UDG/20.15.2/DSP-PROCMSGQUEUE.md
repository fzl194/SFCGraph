---
id: UDG@20.15.2@MMLCommand@DSP PROCMSGQUEUE
type: MMLCommand
name: DSP PROCMSGQUEUE（显示进程消息队列信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: PROCMSGQUEUE
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务公共功能管理
- 操作维护
- 系统调测
- 进程和组件信息
status: active
---

# DSP PROCMSGQUEUE（显示进程消息队列信息）

## 功能

该命令用于显示进程内的消息队列使用信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCID | 进程ID | 可选必选说明：必选参数<br>参数含义：网元内一个进程的进程ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无 |
| COMPNAME | 组件名 | 可选必选说明：可选参数<br>参数含义：进程内一个组件的名字。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，区分大小写。<br>默认值：无 |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。 |

## 操作的配置对象

- [进程消息队列信息（PROCMSGQUEUE）](configobject/UDG/20.15.2/PROCMSGQUEUE.md)

## 使用实例

查询进程内消息队列的使用情况：

```
DSP PROCMSGQUEUE:PROCID=1001,COMPNAME="SEM_Agent"
,SERVICEINSTANCE="vnfc"
;
```

```
RETCODE = 0  操作成功

结果如下:
--------
进程ID    组件名       组件ID        队列名称                  消息数目    消息最大数目    消息最大数目的时间  

1001      SEM_Agent    0x80030401    VRP_MSG_QUE_ID_SMP        0           1               2016-04-19 12:11:30 
1001      SEM_Agent    0x80030401    VRP_MSG_QUE_ID_FWD_PKT    0           0               2016-04-19 04:11:29 
1001      SEM_Agent    0x80030401    VRP_MSG_QUE_ID_FWD_TBL    0           0               2016-04-19 04:11:29 
1001      SEM_Agent    0x80030401    VRP_MSG_QUE_ID_APP_1ST    0           0               2016-04-19 04:11:29 
1001      SEM_Agent    0x80030401    VRP_MSG_QUE_ID_APP_2ND    0           0               2016-04-19 04:11:29 
1001      SEM_Agent    0x80030401    VRP_MSG_QUE_ID_APP_3RD    0           0               2016-04-19 04:11:29 
1001      SEM_Agent    0x80030401    VRP_MSG_QUE_ID_APP_4TH    0           9               2016-04-19 12:11:32 
1001      SEM_Agent    0x80030401    VRP_MSG_QUE_ID_SSP        0           32              2016-04-19 12:11:32 
(结果个数 = 8)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示进程消息队列信息（DSP-PROCMSGQUEUE）_59103920.md`
