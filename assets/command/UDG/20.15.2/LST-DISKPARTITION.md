---
id: UDG@20.15.2@MMLCommand@LST DISKPARTITION
type: MMLCommand
name: LST DISKPARTITION（查询资源磁盘分区过载配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: DISKPARTITION
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务平台功能管理
- 系统管理
- 资源管理
- 资源实例管理
status: active
---

# LST DISKPARTITION（查询资源磁盘分区过载配置）

## 功能

该命令用来查询不同资源类型的磁盘分区过载阈值。

当资源的磁盘分区使用率超过阈值时，会触发磁盘分区使用率超限告警。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RESOURCETYPE | 资源类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定资源类型。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，区分大小写。<br>默认值：无<br>配置原则：请使用<br>[**LST RESINSTANCETYPE**](../../../../单体服务公共功能管理/系统管理/资源管理/RU管理/查询资源实例类型（LST RESINSTANCETYPE）_59103378.md)<br>命令查询存在的资源类型。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/DISKPARTITION]] · 资源磁盘分区过载配置（DISKPARTITION）

## 使用实例

查询OMU类型磁盘分区过载阈值：

```
LST DISKPARTITION:;
```

```
RETCODE = 0  操作成功

结果如下:
--------
资源类型    磁盘分区名称    分区使用率过载次要级别告警恢复阈值（%）    分区使用率过载次要级别告警上报阈值（%）    分区使用率过载重要级别告警恢复阈值（%）    分区使用率过载重要级别告警上报阈值（%）    分区使用率过载紧急级别告警恢复阈值（%）    分区使用率过载紧急级别告警上报阈值（%）    分区使用率过载告警的采样窗口    分区空间不足告警上报阈值（MB）    分区空间不足告警恢复阈值（MB）
OMU        root       0                                  0                                   85                                  95                                  0                                  0                                   12                          50                             100
       
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询资源磁盘分区过载配置（LST-DISKPARTITION）_59036254.md`
