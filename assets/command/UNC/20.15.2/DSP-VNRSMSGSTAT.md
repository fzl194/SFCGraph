---
id: UNC@20.15.2@MMLCommand@DSP VNRSMSGSTAT
type: MMLCommand
name: DSP VNRSMSGSTAT（查询VNRS消息统计）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: VNRSMSGSTAT
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- CSLB功能管理
- 系统管理
- 链路管理
- VNRS消息统计
status: active
---

# DSP VNRSMSGSTAT（查询VNRS消息统计）

## 功能

该命令用于查询CSLB与VNRS之间的交互消息统计，用于定位CSLB与VNRS之间的通讯问题。

## 注意事项

该命令批量下发可能导致执行超时。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定RU的名称，通过<br>**[LST SERVICERUSTATE](../../../../单体服务编排功能管理/系统管理/资源管理/RU信息/查询RU的信息(LST SERVICERUSTATE)_29626965.md)**<br>获得RU名称。<br>数据来源：本端规划<br>默认值：无<br>取值范围：0~63位字符串 |
| PROCTYPE | 进程类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定CSLB的进程类型。<br>数据来源：本端规划<br>默认值：无<br>取值范围：<br>- “PROC_TYPE_MNCP(PROC_MNCP) ” |
| PROCNO | 进程号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定进程序号，可通过<br>**[DSP PROCESSCSLB](../../../进程管理/查询CSLB进程信息(DSP PROCESSCSLB)_85585647.md)**<br>命令获得。<br>数据来源：本端规划<br>默认值：无<br>取值范围：0~63 |
| LINKINDEX | 链路索引 | 可选必选说明：可选参数<br>参数含义：该参数用于指定链路索引。<br>数据来源：本端规划<br>默认值：无<br>取值范围：0~4294967294<br>说明：首次执行本命令时，无需输入本参数，显示多条记录 。后续查询过程中，根据首次查询结果输入本参数，可以查询索引对应的记录。 |

## 操作的配置对象

- [VNRS消息统计（VNRSMSGSTAT）](configobject/UNC/20.15.2/VNRSMSGSTAT.md)

## 使用实例

查询VNRS消息统计。

%%DSP VNRSMSGSTAT:;%

```
RETCODE = 0  操作成功
结果如下:
-----------------------------
                    RU名称  =  CSLB_IP_RU2_0068
                  进程类型  =  PROC_MNCP
                    进程号  =  1
                  链路索引  =  0
                发送报文数  =  4
            发送报文失败数  =  0
         发送VPN订阅报文数  =  0
    发送服务地址通知报文数  =  0
    发送转发地址通知报文数  =  1
          发送报文超时次数  =  4
                接收报文数  =  8
        接收消息异常报文数  =  4
     接收VPN订阅响应报文数  =  0
     接收VPN订阅更新报文数  =  0
    接收服务地址响应报文数  =  0
    接收转发地址响应报文数  =  0
      发送可达性订阅报文数  =  0
  接收可达性订阅响应报文数  =  0
  接收可达性订阅更新报文数  =  0 
发送更新容灾组优先级报文数  =  0
    发送更新团队属性报文数  =  0
              链路故障次数  =  0
              链路恢复次数  =  1
              上次清除时间  =  2018-10-26 15:18:1.928
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询VNRS消息统计（DSP-VNRSMSGSTAT）_29627100.md`
