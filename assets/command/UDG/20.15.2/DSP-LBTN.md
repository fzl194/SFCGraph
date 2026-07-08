---
id: UDG@20.15.2@MMLCommand@DSP LBTN
type: MMLCommand
name: DSP LBTN（查询隧道信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: LBTN
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- CSLB功能管理
- 业务管理
- 隧道管理
- CSLB隧道信息
status: active
---

# DSP LBTN（查询隧道信息）

## 功能

该命令用于查询隧道信息，辅助定位隧道转发失败的问题。

## 注意事项

该命令批量下发可能导致执行超时。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TNGRPID | 隧道组ID | 可选必选说明：可选参数<br>参数含义：该参数用于表示业务VNFC定义的隧道组的标识。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0~4294967295。<br>默认值：无 |
| TNID | 隧道ID | 可选必选说明：可选参数<br>参数含义：该参数用于表示业务VNFC定义的隧道的标识。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0~4294967295。<br>默认值：无 |
| SRVVNFCID | 业务VNFCID | 可选必选说明：可选参数<br>参数含义：该参数用于指定业务VNFC的唯一标识，通过在业务VNFC下执行<br>**[LST NODE](../../../../单体服务公共功能管理/系统管理/基础参数/查询节点信息/查询节点信息（LST NODE）_27372977.md)**<br>获得，所得NODE ID（节点ID）即为业务VNFC ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0~4294967295<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/LBTN]] · 隧道信息（LBTN）

## 使用实例

查询所有隧道信息。

DSP LBTN:;

```
%%DSP LBTN:;%%
RETCODE = 0  操作成功。
操作结果如下：
--------------
            IP类型  =  IPV6
	业务VNFCID  =  4
	  隧道组ID  =  1
            隧道ID  =  1
        隧道组名称  =  tngrp10
           VPN名称  =  _public_
            IP类型  =  IPV6
            源IPV4  =  10.0.0.0
          源端口号  =  11
          目的IPV4  =  10.255.255.255
        目的端口号  =  11
          隧道状态  =  正常
            源IPV6  =  2001:0db8::1
          目的IPV6  =  2001:0db8:ffff:ffff:ffff:ffff:ffff:ffff
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询隧道信息（DSP-LBTN）_29627085.md`
