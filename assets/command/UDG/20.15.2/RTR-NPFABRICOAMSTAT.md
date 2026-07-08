---
id: UDG@20.15.2@MMLCommand@RTR NPFABRICOAMSTAT
type: MMLCommand
name: RTR NPFABRICOAMSTAT（清除NP Fabric统计数据）
nf: UDG
version: 20.15.2
verb: RTR
object_keyword: NPFABRICOAMSTAT
command_category: 动作类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 系统管理
- NP Fabric链路管理
- NP Fabric OAM统计信息
status: active
---

# RTR NPFABRICOAMSTAT（清除NP Fabric统计数据）

## 功能

该命令用于显示清除NP Fabric统计数据。

## 注意事项

- 该命令执行后立即生效。
- 该命令仅适用于NP卡加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RESNAME | 源资源名称 | 可选必选说明：必选参数。<br>参数含义：该参数用于指定源资源名称。<br>数据来源：本端规划。<br>取值范围：字符串类型，输入长度范围为1～128。不支持空格，区分大小写。<br>配置原则：FRAME-x-SLOT-y，区分大小写。其中x为框号，y为槽位号，可通过<br>[DSP NPNODE](../../../FEMF/NP状态查询（DSP NPNODE）_18818228.md)<br>查询。例：FRAME-0-SLOT-8表示0框8板。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/NPFABRICOAMSTAT]] · NP Fabric统计数据（NPFABRICOAMSTAT）

## 使用实例

清除资源名称为FRAME-0-SLOT-8到所有远端资源的NP Fabric统计数据：

```
RTR NPFABRICOAMSTAT:RESNAME="FRAME-0-SLOT-8";
```

```
RETCODE = 0  操作成功。

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/清除NP-Fabric统计数据（RTR-NPFABRICOAMSTAT）_87356184.md`
