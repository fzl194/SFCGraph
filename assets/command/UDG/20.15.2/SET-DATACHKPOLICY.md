---
id: UDG@20.15.2@MMLCommand@SET DATACHKPOLICY
type: MMLCommand
name: SET DATACHKPOLICY（设置APP配置数据检查功能）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: DATACHKPOLICY
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务公共功能管理
- 操作维护
- 配置管理
- 配置检查
status: active
---

# SET DATACHKPOLICY（设置APP配置数据检查功能）

## 功能

该命令用于设置APP配置数据检查功能开关状态。

## 注意事项

- 该命令执行后立即生效。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| AUTOSWITCH |
| --- |
| on |

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| AUTOSWITCH | 自动检查开关 | 可选必选说明：必选参数<br>参数含义：自动检查开关。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- on：开启。<br>- off：关闭。<br>默认值：无 |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识，0表示VNFP。 |

## 操作的配置对象

- [APP配置数据检查功能（DATACHKPOLICY）](configobject/UDG/20.15.2/DATACHKPOLICY.md)

## 使用实例

设置APP配置数据自动检查开关状态为on：

```
SET DATACHKPOLICY:AUTOSWITCH=on
,SERVICEINSTANCE="vnfc"
;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置APP配置数据检查功能（SET-DATACHKPOLICY）_59104253.md`
