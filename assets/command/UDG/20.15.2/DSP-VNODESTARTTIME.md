---
id: UDG@20.15.2@MMLCommand@DSP VNODESTARTTIME
type: MMLCommand
name: DSP VNODESTARTTIME（显示虚拟节点启动时间信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: VNODESTARTTIME
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务平台功能管理
- 系统管理
- 应用编排管理
status: active
---

# DSP VNODESTARTTIME（显示虚拟节点启动时间信息）

## 功能

该命令用于显示虚拟节点启动时间信息，包括Guest OS启动时间点，Guest OS启动完成时间点，软件启动时间点，软件启动完成时间点。

当发现系统缓慢时，可在系统启动之后查看各阶段用了多少时间。

> **说明**
> 该命令仅在虚机场景下支持。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VNODENAME | 虚拟节点名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定虚拟节点名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无 |
| VNFCNAME | VNFC名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定VNFC实例名称。请使用LST VNFC命令查询存在的VNFC名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@VNODESTARTTIME]] · 虚拟节点启动时间信息（VNODESTARTTIME）

## 使用实例

显示名所有虚拟节点的启动时间信息：

```
DSP VNODESTARTTIME:;
```

```
RETCODE = 0  操作成功

结果如下
-------------------------
虚拟节点名称               VNFC名称     Guest OS启动时间点    Guest OS启动完成时间点               软件启动时间点         软件启动完成时间点

OMU1                       VNFP         2018-12-11 09:13:16    2018-12-11 09:24:36                 2018-12-11 09:24:58    2018-12-11 09:24:58           
OMU2                       VNFP         2018-12-10 08:57:58    2018-12-11 09:44:37                 2018-12-11 09:45:49    2018-12-11 09:45:49           
VNODE_CSLB_VNFC_OMU_0001    kk           2018-12-11 09:13:16    2018-12-12 02:45:57                 2018-12-12 02:46:19    0000-00-00 00:00:00           
VNODE_CSLB_VNFC_OMU_0002    kk           2018-12-10 08:57:58    2018-12-12 02:45:59                 2018-12-12 02:47:14    0000-00-00 00:00:00           
(结果个数 = 4)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-VNODESTARTTIME.md`
