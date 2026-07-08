---
id: UDG@20.15.2@MMLCommand@DSP NOSHETEROMODE
type: MMLCommand
name: DSP NOSHETEROMODE（查询NOS异构模式）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: NOSHETEROMODE
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务公共功能管理
- 系统管理
- EOX管理
status: active
---

# DSP NOSHETEROMODE（查询NOS异构模式）

## 功能

该命令用来查询NOS异构模式。

在日常的维护时，可使用本命令查询OMU异构开关状态。

该命令仅在 Full-stack 虚机场景下支持。

## 注意事项

无。

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过<br>**LST VNFC**<br>命令获取。<br>默认值：无<br>配置原则：只能填写通过<br>**LST VNFC**<br>命令查询到的管理代理标识。 |

## 操作的配置对象

- [NOS异构模式（NOSHETEROMODE）](configobject/UDG/20.15.2/NOSHETEROMODE.md)

## 使用实例

查询NOS异构模式：

```
DSP NOSHETEROMODE:SERVICEINSTANCE="vnfc";
```

```
RETCODE = 0  操作成功

结果如下:
-------------------------
OMU异构开关  =  打开
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询NOS异构模式(DSP-NOSHETEROMODE)_74671533.md`
