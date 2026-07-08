---
id: UDG@20.15.2@MMLCommand@SET CFGDEBUG
type: MMLCommand
name: SET CFGDEBUG（设置调试配置信息）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: CFGDEBUG
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务公共功能管理
- 操作维护
- 配置管理
- 配置文件管理
status: active
---

# SET CFGDEBUG（设置调试配置信息）

## 功能

该命令用于修改、删除、增加网元配置对象的数据。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DEBUGINFO | 调试信息 | 可选必选说明：可选参数<br>参数含义：维护命令的自定义参数。如果不需要自定义参数，则保持默认值<br>“default”<br>。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1~128。<br>默认值：default<br>配置原则：无 |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@CFGDEBUG]] · CFG诊断日志（CFGDEBUG）

## 使用实例

```
设置调试配置：
SET CFGDEBUG: DEBUGINFO="default", SERVICEINSTANCE="vnfc";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-CFGDEBUG.md`
