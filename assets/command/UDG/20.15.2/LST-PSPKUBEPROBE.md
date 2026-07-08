---
id: UDG@20.15.2@MMLCommand@LST PSPKUBEPROBE
type: MMLCommand
name: LST PSPKUBEPROBE（查询是否放通管道大颗粒readiness就绪探测）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: PSPKUBEPROBE
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务编排功能管理
- 操作维护
- 系统调测
- 升级维护
status: active
---

# LST PSPKUBEPROBE（查询是否放通管道大颗粒readiness就绪探测）

## 功能

该命令用于查询当前是否放通管道大颗粒readiness就绪探测。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过<br>**[LST VNFC](../../../../单体服务平台功能管理/操作维护/配置管理/VNFC信息/查询VNFC（LST VNFC）_59036046.md)**<br>命令获取。<br>默认值：无<br>配置原则：只能填写通过<br>**[LST VNFC](../../../../单体服务平台功能管理/操作维护/配置管理/VNFC信息/查询VNFC（LST VNFC）_59036046.md)**<br>命令查询到的管理代理标识。 |

## 操作的配置对象

- [是否放通管道大颗粒readiness就绪探测（PSPKUBEPROBE）](configobject/UDG/20.15.2/PSPKUBEPROBE.md)

## 使用实例

```
%%LST PSPKUBEPROBE: SERVICEINSTANCE="CSDB_VNFC";%% 
RETCODE = 0  操作成功
 
结果如下 
-------- 
Ru就绪状态检测  =  真实检测 
(结果个数 = 1) 
 
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询是否放通管道大颗粒readiness就绪探测（LST-PSPKUBEPROBE）_30310421.md`
