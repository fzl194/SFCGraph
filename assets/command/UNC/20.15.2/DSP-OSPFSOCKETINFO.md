---
id: UNC@20.15.2@MMLCommand@DSP OSPFSOCKETINFO
type: MMLCommand
name: DSP OSPFSOCKETINFO（查询OSPF与Socket的交互信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: OSPFSOCKETINFO
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- OSPF管理
- 查询OSPF与Socket的交互信息
status: active
---

# DSP OSPFSOCKETINFO（查询OSPF与Socket的交互信息）

## 功能

该命令用于查询OSPF与Socket的交互信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCID | OSPF进程号 | 可选必选说明：可选参数<br>参数含义：OSPF进程号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无 |
| IFNAME | 接口名 | 可选必选说明：必选参数<br>参数含义：接口名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：请使用LST INTERFACE命令查看可用接口。 |

## 操作的配置对象

- [OSPF与Socket的交互信息（OSPFSOCKETINFO）](configobject/UNC/20.15.2/OSPFSOCKETINFO.md)

## 使用实例

查询OSPF进程1接口Ethernet64/0/5与Socket的交互信息：

```
DSP OSPFSOCKETINFO:PROCID=1,IFNAME="Ethernet64/0/5";
```

```

RETCODE = 0  操作成功。

结果如下
------------------------
           OSPF进程号  =  1
             接口索引  =  8
               接口名  =  Ethernet64/0/5
           Socket标识  =  1
           Handle标识  =  1
       Socket组件状态  =  12
       Socket FSM状态  =  3
         连接入口计数  =  0
         断连入口计数  =  0
           发送管道ID  =  524318
           接口管道ID  =  1074266141
     管道开始收发时间  =  106675
  发送到Socket（Pkt）  =  15
 发送到Socket（Byte）  =  668
  从Socket收到（Pkt）  =  12
 从Socket收到（Byte）  =  896
第一次发送Hello包时间  =  2017-07-27 07:38:56
第一次收到Hello包时间  =  2017-07-27 07:39:05
   第一次发送DD包时间  =  2017-07-27 07:39:06
   第一次收到DD包时间  =  2017-07-27 07:39:10
     Mbuf申请失败计数  =  0
     Mbuf发送失败计数  =  0
     Mbuf转发失败计数  =  0
(Number of results = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询OSPF与Socket的交互信息（DSP-OSPFSOCKETINFO）_00441401.md`
