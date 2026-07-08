---
id: UDG@20.15.2@MMLCommand@LST FAULTDETECT
type: MMLCommand
name: LST FAULTDETECT（显示故障策略信息）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: FAULTDETECT
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务公共功能管理
- 系统管理
- 资源管理
- RU管理
status: active
---

# LST FAULTDETECT（显示故障策略信息）

## 功能

该命令用于显示故障策略信息，主要包括故障快速上报配置、进程间通信检查配置和OMU双离线后资源单元强制复位配置等信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/FAULTDETECT]] · 故障策略信息（FAULTDETECT）

## 使用实例

显示故障配置信息：

```
LST FAULTDETECT:
SERVICEINSTANCE="vnfc"
;
```

```
RETCODE = 0  操作成功
结果如下:
------------------------
快速上报使能标志        =  使能
OsNode链路检查使能标志  =  使能
强制复位开关            =  去使能
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-FAULTDETECT.md`
