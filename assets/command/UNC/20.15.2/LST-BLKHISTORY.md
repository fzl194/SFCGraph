---
id: UNC@20.15.2@MMLCommand@LST BLKHISTORY
type: MMLCommand
name: LST BLKHISTORY（查询CSDB RU闭塞信息）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: BLKHISTORY
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- CSDB功能管理
- CSDB管理
- 闭塞管理
status: active
---

# LST BLKHISTORY（查询CSDB RU闭塞信息）

## 功能

该命令用于查询闭塞/解闭CSDB RU结果。

## 注意事项

- 该命令执行后，可立刻查询到结果。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SCALEGROUP | 物理资源组名称 | 可选必选说明：可选。<br>参数含义：该参数用于指定唯一一个物理资源组。<br>数据来源：该物理资源组名称可以通过<br>**[LST SERVICERUSTATE](../../../单体服务编排功能管理/系统管理/资源管理/RU信息/查询RU的信息(LST SERVICERUSTATE)_29626965.md)**<br>命令查询获取，对应<br>**ScaleGroup的名字**<br>。<br>取值范围：字符串类型，长度为1～63。<br>默认值：无。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/BLKHISTORY]] · CSDB RU闭塞信息（BLKHISTORY）

## 使用实例

查询闭塞和解闭历史操作结果:

```
LST BLKHISTORY:;
%%LST BLKHISTORY:;%%
RETCODE = 0  操作成功。
操作结果如下：
-------------------------
闭塞次序       闭塞类型    开始时间               结束时间               物理资源组名称        RU列表        闭塞结果      备注信息
1              闭塞        2018-10-15 9:57:9      2018-10-18 6:28:17     SG1_CSDB_ForCommon    64,65         处理成功       NULL
2              解闭        2018-10-15 9:57:14     2018-10-15 9:57:14     SG1_CSDB_ForCommon    64,65         处理成功       NULL
(结果个数 = 2)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-BLKHISTORY.md`
