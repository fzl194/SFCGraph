---
id: UDG@20.15.2@MMLCommand@DSP FWDSTAT
type: MMLCommand
name: DSP FWDSTAT（查询转发消息统计）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: FWDSTAT
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- CSLB功能管理
- 系统管理
- 进程状态
- 转发统计
status: active
---

# DSP FWDSTAT（查询转发消息统计）

## 功能

该命令用于查询转发消息的统计，转发消息中不包含敏感信息。

## 注意事项

该命令批量下发可能导致执行超时。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：必选参数<br>参数含义：RU名称，通过查询<br>**[LST SERVICERUSTATE](../../../../单体服务编排功能管理/系统管理/资源管理/RU信息/查询RU的信息(LST SERVICERUSTATE)_29626965.md)**<br>获得。<br>取值范围：0 ~ 63字符。<br>默认值：无<br>配置原则：不支持CSLB_OM_RU类型的RU。 |
| PROCTYPE | 进程类型 | 可选必选说明：可选参数<br>参数含义：进程类型。<br>取值范围:<br>- “PROC_TYPE_MPEP(E_PROC_TYPE_MPEP) ”<br>默认值：无 |
| PROCNO | 进程号 | 可选必选说明：可选参数<br>参数含义：进程号，通过查询<br>**[DSP LBPROC](../进程信息/查询CSLB进程（DSP LBPROC）_29627093.md)**<br>获得。<br>取值范围：0~63<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/FWDSTAT]] · 转发消息统计（FWDSTAT）

## 使用实例

-
  查询转发消息的统计

  ```
  DSP FWDSTAT:RUNAME="CSLB_IP_RU2_0064",PROCTYPE=PROC_TYPE_MPEP,PROCNO=3;
  %%DSP FWDSTAT: RUNAME="CSLB_IP_RU2_0064",PROCTYPE=PROC_TYPE_MPEP,PROCNO=3;%%
  RETCODE = 0  操作成功。

  操作结果如下：
  --------------
                            RU名称  =  CSLB_IP_RU2_0064
                          进程类型  =  PROC_MPEP
                            进程号  =  3
        接收的上行IPv4报文数（千）  =  0
      接收的上行IPv4报文流量（MB）  =  0
  接收的上行需重组的IPv4分片报文数  =  0
      重组失败的上行IPv4分片报文数  =  0
          重组成功的上行IPv4报文数  =  0
      匹配策略失败的上行IPv4报文数  =  0
        发送的上行IPv4报文数（千）  =  3907
      发送的上行IPv4报文流量（MB）  =  0
        接收的下行IPv4报文数（千）  =  3907
      接收的下行IPv4报文流量（MB）  =  0
          寻址失败的下行IPv4报文数  =  0
        发送的下行IPv4报文数（千）  =  0
      发送的下行IPv4报文流量（MB）  =  0
        接收的上行IPv6报文数（千）  =  0
      接收的上行IPv6报文流量（MB）  =  0
  接收的上行需重组的IPv6分片报文数  =  0
      重组失败的上行IPv6分片报文数  =  0
          重组成功的上行IPv6报文数  =  0
      匹配策略失败的上行IPv6报文数  =  0
        发送的上行IPv6报文数（千）  =  0
      发送的上行IPv6报文流量（MB）  =  0
        接收的下行IPv6报文数（千）  =  0
      接收的下行IPv6报文流量（MB）  =  0
          寻址失败的下行IPv6报文数  =  0
        发送的下行IPv6报文数（千）  =  0
      发送的下行IPv6报文流量（MB）  =  0
  (结果个数 = 1)
  ---    END 
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-FWDSTAT.md`
