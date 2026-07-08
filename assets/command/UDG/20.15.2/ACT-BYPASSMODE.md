---
id: UDG@20.15.2@MMLCommand@ACT BYPASSMODE
type: MMLCommand
name: ACT BYPASSMODE（激活节点BYPASS模式）
nf: UDG
version: 20.15.2
verb: ACT
object_keyword: BYPASSMODE
command_category: 动作类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 设备管理
- Bypass模式管理
status: active
---

# ACT BYPASSMODE（激活节点BYPASS模式）

## 功能

![](激活节点BYPASS模式（ACT BYPASSMODE）_47816793.assets/notice_3.0-zh-cn.png)

降低磁盘故障引起业务完全不可用的风险。

该功能仅支持华为虚拟化层软件FusionSphere，不支持第三方虚拟化层软件。

BYPASS是将操作系统以及关键服务运行在指定的存储模式（存储模式由“BYPASS模式”开关控制）中的一种方案，激活BYPASS模式，下次重启会按照BYPASS要求将操作系统以及关键服务运行在指定的存储模式中。

> **说明**
> 该命令仅在 Full-stack 虚机场景下支持。

> **说明**
> - 该命令仅限admin用户可以执行。

## 参数

| **参数标识** | **参数名称** | **参数说明** |
| --- | --- | --- |
| MEID | 网元ID | 可选必选说明：必选参数。<br>参数含义：用于指示系统需要修改指定网元ID下的节点数据。<br>取值范围：0～65535。<br>默认值：无。<br>配置原则：网元ID可以通过执行<br>[LST ME](../../系统管理/版本信息/查询网元配置信息（LST ME）_47084797.md)<br>查询。 |
| BYPASSMODE | BYPASS模式 | 可选必选说明：必选参数。<br>参数含义：标识是否激活指定网元的BYPASS的模式。<br>取值范围：<br>- “None（默认模式）”：不激活BYPASS模式，业务运行在虚拟机创建时的存储中。<br>- “MemoryDiskMode（内存模式）”：激活BYPASS模式，业务运行在内存盘中。<br>默认值：无。<br>配置原则：无。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/BYPASSMODE]] · 节点BYPASS模式（BYPASSMODE）

## 使用实例

```
%%ACT BYPASSMODE: MEID=0, BYPASSMODE=None;%%
RETCODE = 0  操作成功
操作结果如下
------------
网元ID  节点IP            结果  
0       10.0.0.3          成功
0       10.0.0.2          成功
0       10.0.0.1          成功
(结果个数 = 3)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/激活节点BYPASS模式（ACT-BYPASSMODE）_47816793.md`
