---
id: UDG@20.15.2@MMLCommand@DSP VERSION
type: MMLCommand
name: DSP VERSION（显示系统版本信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: VERSION
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务公共功能管理
- 系统管理
- 版本信息
status: active
---

# DSP VERSION（显示系统版本信息）

## 功能

该命令用于显示VNFC的版本信息。

在日常的维护和版本升级时，可使用本命令显示系统当前的基础包、补丁包版本信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/VERSION]] · 系统版本信息（VERSION）

## 使用实例

显示VNFC的版本信息：

```
DSP VERSION:
SERVICEINSTANCE="vnfc"
;
```

```
RETCODE = 0  操作成功

结果如下:
-------------------------
      包类型  =  版本包
    版本类型  =  基础版本
      版本号  =  V100R005C00
版本应用类型  =  BaseApp
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示系统版本信息（DSP-VERSION）_59103553.md`
