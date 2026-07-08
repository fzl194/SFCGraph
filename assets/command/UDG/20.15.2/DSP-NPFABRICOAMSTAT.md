---
id: UDG@20.15.2@MMLCommand@DSP NPFABRICOAMSTAT
type: MMLCommand
name: DSP NPFABRICOAMSTAT（显示NP Fabric统计数据）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: NPFABRICOAMSTAT
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 系统管理
- NP Fabric链路管理
- NP Fabric OAM统计信息
status: active
---

# DSP NPFABRICOAMSTAT（显示NP Fabric统计数据）

## 功能

该命令用于显示NP Fabric统计数据。

## 注意事项

- 该命令仅适用于NP卡加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RESNAME | 源资源名称 | 可选必选说明：必选参数。<br>参数含义：该参数用于指定源资源名称。<br>数据来源：本端规划。<br>取值范围：字符串类型，输入长度范围为1～128。不支持空格，区分大小写。<br>配置原则：FRAME-x-SLOT-y，区分大小写。其中x为框号，y为槽位号，可通过<br>[DSP NPNODE](../../../FEMF/NP状态查询（DSP NPNODE）_18818228.md)<br>查询。例：FRAME-0-SLOT-8表示0框8板。<br>默认值：无。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/NPFABRICOAMSTAT]] · NP Fabric统计数据（NPFABRICOAMSTAT）

## 使用实例

显示资源名称为FRAME-0-SLOT-8到所有远端资源的NP Fabric统计数据：

```
DSP NPFABRICOAMSTAT:RESNAME="FRAME-0-SLOT-8";
```

```
RETCODE = 0  操作成功

结果如下
--------
源资源名称      远端资源名称      发送报文总数  接收报文总数  链路中断次数  错包次数  

FRAME-0-SLOT-8  FRAME-0-SLOT-8-0  776250        776206        1              0        
FRAME-0-SLOT-8  FRAME-0-SLOT-7-0  776586        776586        0              0        
(结果个数 = 2)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-NPFABRICOAMSTAT.md`
