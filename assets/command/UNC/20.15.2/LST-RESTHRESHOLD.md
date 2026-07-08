---
id: UNC@20.15.2@MMLCommand@LST RESTHRESHOLD
type: MMLCommand
name: LST RESTHRESHOLD（查询资源过载和过载恢复阈值）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: RESTHRESHOLD
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

# LST RESTHRESHOLD（查询资源过载和过载恢复阈值）

## 功能

该命令用来查看不同资源类型的资源过载和过载恢复阈值。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RESTYPE | 资源类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定资源类型。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，区分大小写。<br>默认值：无<br>配置原则：请使用<br>[**LST RESINSTANCETYPE**](../../../../单体服务公共功能管理/系统管理/资源管理/RU管理/查询资源实例类型（LST RESINSTANCETYPE）_59103378.md)<br>命令查询存在的资源类型。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/RESTHRESHOLD]] · 资源过载和过载恢复阈值（RESTHRESHOLD）

## 使用实例

查询IPU_A类型的资源过载和过载恢复阈值：

```
LST RESTHRESHOLD:RESTYPE="IPU_A";
```

```
RETCODE = 0  操作成功

结果如下:
-------------------------
                                资源类型  =  IPU_A
 CPU使用率过载次要级别告警的恢复阈值（%） =  50
 CPU使用率过载次要级别告警的上报阈值（%） =  60
 CPU使用率过载重要级别告警的恢复阈值（%） =  75
 CPU使用率过载重要级别告警的上报阈值（%） =  80
 CPU使用率过载紧急级别告警的恢复阈值（%） =  85
 CPU使用率过载紧急级别告警的上报阈值（%） =  95
内存使用率过载次要级别告警的恢复阈值（%） =  50
内存使用率过载次要级别告警的上报阈值（%） =  60
内存使用率过载重要级别告警的恢复阈值（%） =  75
内存使用率过载重要级别告警的上报阈值（%） =  80
内存使用率过载紧急级别告警的恢复阈值（%） =  85
内存使用率过载紧急级别告警的上报阈值（%） =  95
(结果个数 = 1)
 ---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-RESTHRESHOLD.md`
