---
id: UNC@20.15.2@MMLCommand@LCK CONFIG
type: MMLCommand
name: LCK CONFIG（锁定配置）
nf: UNC
version: 20.15.2
verb: LCK
object_keyword: CONFIG
command_category: 动作类
effect_mode: 立即生效
is_dangerous: true
category_path:
- 平台服务管理
- 单体服务公共功能管理
- 操作维护
- 配置管理
- 配置文件管理
status: active
---

# LCK CONFIG（锁定配置）

## 功能

![](锁定配置（LCK CONFIG）_27994373.assets/notice_3.0-zh-cn_2.png)

该命令属于高危命令，执行该操作后，所有配置请求都会报错，导致所有配置下发失败。

该命令用于锁定配置，禁止配置下发。

## 注意事项

- 该命令执行后立即生效。
- 锁定后所有配置操作都会报错，解锁后执行配置操作会正常返回结果。
- 重复解锁的执行结果为操作成功，重复锁定的执行结果为配置已锁定，但都不会改变原来的锁状态，也不会刷新自动解锁的时间。
- 主备倒换不会改变原来的锁状态，不会刷新自动解锁的时间。
- 主备双复位后会自动变为解锁状态。

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LOCKED | 锁状态 | 可选必选说明：必选参数。<br>参数含义：配置锁定的状态。<br>数据来源：本端规划。<br>取值范围：枚举类型。<br>- UNLOCK(解锁)：锁状态为解锁，允许配置操作。<br>- LOCK(加锁)：锁状态为锁定，锁定配置操作。<br>默认值：无。<br>配置原则：无。 |
| LOCKTIME | 锁定时间（分钟） | 可选必选说明：条件可选参数，该参数在<br>“LOCKED”<br>设置为<br>“LOCK”<br>时为可选参数。<br>参数含义：维持配置锁定状态的时间，在这个时间过后配置锁会自动解锁。<br>数据来源：本端规划。<br>取值范围：整数类型，取值范围为1~60，单位是分钟。<br>默认值：60。<br>配置原则：无。 |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数。<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划。<br>取值范围：字符串类型，通过<br>**LST VNFC**<br>命令获取。<br>默认值：无。<br>配置原则：只能填写通过<br>**LST VNFC**<br>命令查询到的大颗粒服务实例名称。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/CONFIG]] · 锁定配置（CONFIG）

## 使用实例

锁定配置并在10分钟后自动解锁：

```
LCK CONFIG: LOCKED=LOCK, LOCKTIME=10, SERVICEINSTANCE="vnfc";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/锁定配置（LCK-CONFIG）_27994373.md`
