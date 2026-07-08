---
id: UNC@20.15.2@MMLCommand@SET SKIPADJUSTHAFDM
type: MMLCommand
name: SET SKIPADJUSTHAFDM（设置跳过调整HAF域开关）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: SKIPADJUSTHAFDM
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 编排管理
- NFVI分批升级管理
status: active
---

# SET SKIPADJUSTHAFDM（设置跳过调整HAF域开关）

## 功能

该命令用于设置跳过调整HAF域开关。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| SWITCH |
| --- |
| OFF |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SWITCH | 跳过HAF调整域开关 | 可选必选说明：必选参数<br>参数含义：该参数用于表示跳过HAF域调整的触发方式，值为ON表示跳过HAF调整域开关打开，值为OFF表示跳过HAF调整域开关关闭。<br>数据来源：本端规划<br>取值范围：<br>- OFF（关闭跳过HAF调整域开关）<br>- ON（打开跳过调整HAF域开关）<br>默认值：无。<br>配置原则：无 |

## 操作的配置对象

- [跳过调整HAF域开关状态（SKIPADJUSTHAFDM）](configobject/UNC/20.15.2/SKIPADJUSTHAFDM.md)

## 使用实例

设置跳过调整HAF域开关为关闭。

```
SET SKIPADJUSTHAFDM:SWITCH=OFF;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置跳过调整HAF域开关（SET-SKIPADJUSTHAFDM）_68321035.md`
