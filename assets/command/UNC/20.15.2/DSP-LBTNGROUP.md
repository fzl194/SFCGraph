---
id: UNC@20.15.2@MMLCommand@DSP LBTNGROUP
type: MMLCommand
name: DSP LBTNGROUP（查询隧道组信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: LBTNGROUP
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- CSLB功能管理
- 业务管理
- 隧道管理
- CSLB隧道组信息
status: active
---

# DSP LBTNGROUP（查询隧道组信息）

## 功能

该命令用于查询隧道组信息，辅助定位隧道转发失败的问题。

## 注意事项

该命令批量下发可能导致执行超时。

manage-ug；system-ug；monitor-ug

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SRVVNFCID | 业务VNFCID | 可选必选说明：可选参数<br>参数含义：该参数用于指定业务VNFC的唯一标识，通过在业务VNFC下执行<br>**[LST NODE](../../../../单体服务公共功能管理/系统管理/基础参数/查询节点信息/查询节点信息（LST NODE）_59103764.md)**<br>获得，所得NODE ID（节点ID）即为业务VNFCID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0~4294967295。<br>默认值：无<br>配置原则：无 |
| TNGRPID | 隧道组ID | 可选必选说明：可选参数<br>参数含义：该参数用于表示业务VNFC定义的隧道组的标识。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0~4294967295。<br>默认值：无<br>配置原则：无 |
| TNGRPNAME | 隧道组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示业务VNFC定义的隧道组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围0~15。<br>默认值：无<br>配置原则：使用DSP LBTN命令查看可用的隧道组名称 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/LBTNGROUP]] · 隧道组信息（LBTNGROUP）

## 使用实例

查询隧道组。

DSP LBTNGROUP:;

```
%%DSP LBTNGROUP:;%%
RETCODE = 0  操作成功。

操作结果如下：
--------------
  隧道组名称    =  tnc_grp1
  隧道组ID      =  1
  业务VNFCID    =  5
  是否共享隧道  =  共享
  隧道传输QOS   =  1
  探测开关状态  =  打开
  上报状态开关  =  打开
  心跳间隔时长  =  1
  心跳重传次数  =  3
  隧道组状态    =  正常
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-LBTNGROUP.md`
