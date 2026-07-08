---
id: UNC@20.15.2@MMLCommand@LST PROCFAULTALM
type: MMLCommand
name: LST PROCFAULTALM（查询进程故障告警上报模式）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: PROCFAULTALM
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务公共功能管理
- 系统管理
- 资源管理
- RU管理
status: active
---

# LST PROCFAULTALM（查询进程故障告警上报模式）

## 功能

该命令用于查询进程故障告警上报模式。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PROCFAULTALM]] · 进程故障告警上报模式（PROCFAULTALM）

## 使用实例

显示进程故障告警上报模式：

```
LST PROCFAULTALM:
SERVICEINSTANCE="vnfc"
;
```

```
RETCODE = 0  操作成功

结果如下:
--------
告警快速上报使能位  =  使能
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询进程故障告警上报模式（LST-PROCFAULTALM）_59103884.md`
