---
id: UDG@20.15.2@MMLCommand@SAV RUNNINGCONFIG
type: MMLCommand
name: SAV RUNNINGCONFIG（保存运行配置数据）
nf: UDG
version: 20.15.2
verb: SAV
object_keyword: RUNNINGCONFIG
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

# SAV RUNNINGCONFIG（保存运行配置数据）

## 功能

该命令用于保存当前运行配置数据至文件中。当用户完成一组配置，并且已经达到预定功能，可以通过该命令将当前配置文件保存到存储设备中，持久化为磁盘文件。

## 注意事项

- 该命令执行后立即生效。
- 执行该命令会对系统加锁，导致配置命令无法执行。操作结束后，可以正常进行配置。

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TARGET | 目标对象 | 可选必选说明：可选参数<br>参数含义：指定保存运行配置的目标对象所在。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- next-startup：下次启动配置文件。<br>默认值：next-startup |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/RUNNINGCONFIG]] · 保存运行配置数据（RUNNINGCONFIG）

## 使用实例

保存当前运行配置数据至配置文件：

```
SAV RUNNINGCONFIG:
SERVICEINSTANCE="vnfc"
;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SAV-RUNNINGCONFIG.md`
