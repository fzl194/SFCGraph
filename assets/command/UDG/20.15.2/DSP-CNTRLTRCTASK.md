---
id: UDG@20.15.2@MMLCommand@DSP CNTRLTRCTASK
type: MMLCommand
name: DSP CNTRLTRCTASK（显示跨层统一联动跟踪任务信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: CNTRLTRCTASK
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 系统调测
- 工程调测
- 5G工程命令
status: active
---

# DSP CNTRLTRCTASK（显示跨层统一联动跟踪任务信息）

## 功能

该命令用于查询跨层统一联动跟踪任务信息。

> **说明**
> - 该命令仅在虚机场景下支持，并且仅支持FusionSphere用户态EVS和用户态OVS组网。
> - 该命令最多可显示10条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TASKID | 任务ID | 可选必选说明：可选参数<br>参数含义：该参数用于表示跨层统一联动跟踪任务的任务ID。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度是14。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/CNTRLTRCTASK]] · 跨层统一联动跟踪任务（CNTRLTRCTASK）

## 使用实例

查询跨层统一联动跟踪任务信息：

```
%%DSP CNTRLTRCTASK:;%%
RETCODE = 0  操作成功

结果如下
--------
         任务ID  =  20220301223015
       任务状态  =  运行中
       失败信息  =  NULL
       启动时间  =  2022-03-01 22:30:16
       停止时间  =  NULL
       有效时间  =  5
       协议类型  =  Tcp报文
   IPv6协议类型  =  NULL
     本端IP地址  =  192.168.1.1
     远端IP地址  =  192.168.1.2
       本端端口  =  1000
       远端端口  =  2000
       跟踪方向  =  双向
       VNFC名称  =  vnfc
         规则ID  =  2
外联口接口名称1  =  Ethernet1/0/0
        RU名称1  =  VNRS_IP_RU_0001
       MAC地址1  =  00:E0:FC:XX:XX:XX
       Pod标识1  =  cslbip-pod-0
    虚拟机标识1  =  e4b82ed1789d49d6af16834xxxxxxxx
外联口接口名称2  =  NULL
        RU名称2  =  NULL
       MAC地址2  =  NULL
       Pod标识2  =  NULL
    虚拟机标识2  =  NULL
外联口接口名称3  =  NULL
        RU名称3  =  NULL
       MAC地址3  =  NULL
       Pod标识3  =  NULL
    虚拟机标识3  =  NULL
外联口接口名称4  =  NULL
        RU名称4  =  NULL
       MAC地址4  =  NULL
       Pod标识4  =  NULL
    虚拟机标识4  =  NULL
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-CNTRLTRCTASK.md`
