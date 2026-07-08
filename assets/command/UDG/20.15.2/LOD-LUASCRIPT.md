---
id: UDG@20.15.2@MMLCommand@LOD LUASCRIPT
type: MMLCommand
name: LOD LUASCRIPT（加载Lua脚本）
nf: UDG
version: 20.15.2
verb: LOD
object_keyword: LUASCRIPT
command_category: 动作类
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

# LOD LUASCRIPT（加载Lua脚本）

## 功能

该命令用于加载Lua脚本。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SCRIPTNAME | 脚本名称 | 可选必选说明：必选参数<br>参数含义：需要加载的Lua脚本文件名称。<br>数据来源：本端规划<br>取值范围：0~256。<br>默认值：无<br>配置原则：无 |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@LUASCRIPT]] · Lua脚本（LUASCRIPT）

## 使用实例

```
加载Lua脚本：
LOD LUASCRIPT: SCRIPTNAME="TcmcTypeInner.lua", SERVICEINSTANCE="vnfc";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LOD-LUASCRIPT.md`
