---
id: UDG@20.15.2@MMLCommand@DSP SRVVNFCMSGSTAT
type: MMLCommand
name: DSP SRVVNFCMSGSTAT（查询服务VNFC消息统计）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: SRVVNFCMSGSTAT
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- CSLB功能管理
- 业务管理
- 服务管理
- 服务VNFC消息统计
status: active
---

# DSP SRVVNFCMSGSTAT（查询服务VNFC消息统计）

## 功能

该命令用于查询业务VFNC业务消息统计情况

## 注意事项

- DSP SRVVNFCMSGSTAT命令的统计值在MLBP进程复位后会被清零。
- 该命令批量下发可能导致执行超时。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PEERVNFCID | 服务VNFC ID | 可选必选说明：必选参数<br>参数含义：该参数用于指定业务VNFC的唯一标识，通过在业务VNFC下执行<br>**[LST NODE](../../../../单体服务公共功能管理/系统管理/基础参数/查询节点信息/查询节点信息（LST NODE）_27372977.md)**<br>获得，所得NODEID即为服务VNFC ID。<br>数据来源：本端规划<br>默认值：无 |
| DATATYPE | 数据类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定数据类型。<br>数据来源：本端规划<br>默认值：无<br>取值范围：<br>- “SRV_DATA_TYPE_LBPLY(负载均衡策略) ”<br>- “SRV_DATA_TYPE_NEXTHOP(下一跳) ”<br>- “SRV_DATA_TYPE_XTUPLE(X元组) ”<br>- “SRV_DATA_TYPE_ENEXTHOP(扩展下一跳) ”<br>- “SRV_DATA_TYPE_EXCHANGE(交换表) ”<br>- “SRV_DATA_TYPE_VPN(VPN) ” |
| POLICYID | 策略索引 | 可选必选说明：可选参数<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/SRVVNFCMSGSTAT]] · 服务VNFC消息统计（SRVVNFCMSGSTAT）

## 使用实例

%%DSP SRVVNFCMSGSTAT: PEERVNFCID=4, DATATYPE=SRV_DATA_TYPE_LBPLY, POLICYID=0;%%

RETCODE = 0 操作成功

```
结果如下:
-------------------------
     服务VNFC ID  =  4
        数据类型  =  负载均衡策略
        策略索引  =  0
      接收消息数  =  117000
  接收异常消息数  =  0
    数据增加次数  =  63500
数据增加失败次数  =  0
    数据删除次数  =  53500
数据删除失败次数  =  0
发送消息失败次数  =  0
    发送消息次数  =  117000
    上次清除时间  =  NULL
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-SRVVNFCMSGSTAT.md`
