---
id: UNC@20.15.2@MMLCommand@SET PSPKUBEPROBE
type: MMLCommand
name: SET PSPKUBEPROBE（设置是否放通管道大颗粒readiness就绪探测）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: PSPKUBEPROBE
command_category: 配置类
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

# SET PSPKUBEPROBE（设置是否放通管道大颗粒readiness就绪探测）

## 功能

该命令用于设置是否放通管道大颗粒readiness就绪探测。

## 注意事项

无。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| READINESSRU | RU就绪状态检测 | 可选必选说明：可选参数<br>参数含义：该参数用于表示放通管道大颗粒就绪状态检测。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE（放通检测）<br>- ENABLE（真实检测）<br>默认值：DISABLE。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过相关查询命令获取当前参数配置值。<br>配置原则：<br>在FST裸机滚动升级场景下配置ENABLE值，其他场景保持DISABLE。 |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过<br>**[LST VNFC](../../../../单体服务平台功能管理/操作维护/配置管理/VNFC信息/查询VNFC（LST VNFC）_59036046.md)**<br>命令获取。<br>默认值：无<br>配置原则：只能填写通过<br>**[LST VNFC](../../../../单体服务平台功能管理/操作维护/配置管理/VNFC信息/查询VNFC（LST VNFC）_59036046.md)**<br>命令查询到的管理代理标识。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PSPKUBEPROBE]] · 是否放通管道大颗粒readiness就绪探测（PSPKUBEPROBE）

## 使用实例

设置服务实例“CSDB_VNFC”的readiness就绪探测状态为放通检测：

```
%%SET PSPKUBEPROBE: READINESSRU=DISABLE, SERVICEINSTANCE="CSDB_VNFC";%% 
RETCODE = 0  操作成功 
 
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-PSPKUBEPROBE.md`
