---
id: UDG@20.15.2@MMLCommand@SET TETHERDETGLBSW
type: MMLCommand
name: SET TETHERDETGLBSW（设置Tethering用户终端数量检测全局开关）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: TETHERDETGLBSW
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: true
max_records: 1
category_path:
- 用户面服务管理
- 业务匹配策略
- 业务过滤器管理
- Tethering检测
- Tethering用户终端数量检测全局开关
status: active
---

# SET TETHERDETGLBSW（设置Tethering用户终端数量检测全局开关）

## 功能

**适用NF：PGW-U、UPF**

![](设置Tethering用户终端数量检测全局开关（SET TETHERDETGLBSW）_82837448.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，该命令生效范围为整机，开启后可能导致性能下降明显。

该命令用来设置Tethering用户终端数量检测全局开关。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 此命令的生效范围为整机。
- 此命令开启后可能导致性能下降明显。执行命令前请评估对性能的影响，如果无法评估请联系华为技术支持。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | SWITCH |
| --- | --- |
| 初始值 | DISABLE |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SWITCH | 开关标识 | 可选必选说明：可选参数<br>参数含义：该参数用来配置Tethering用户终端数量检测功能开关。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：Tethering终端数量检测功能关闭。<br>- ENABLE：Tethering终端数量检测功能打开。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [Tethering用户终端数量检测全局开关（TETHERDETGLBSW）](configobject/UDG/20.15.2/TETHERDETGLBSW.md)

## 使用实例

假如运营商需使能Tethering用户终端数量检测全局功能：

```
SET TETHERDETGLBSW: SWITCH=ENABLE;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置Tethering用户终端数量检测全局开关（SET-TETHERDETGLBSW）_82837448.md`
