---
id: UDG@20.15.2@MMLCommand@SET SSUAGINGCFG
type: MMLCommand
name: SET SSUAGINGCFG（设置SSU容器业务相关老化功能配置）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: SSUAGINGCFG
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 1
category_path:
- 智能板管理
- vvip
- 流老化时间
status: active
---

# SET SSUAGINGCFG（设置SSU容器业务相关老化功能配置）

## 功能

**适用NF：PGW-U、UPF**

该命令用于设置SSU容器业务相关老化功能配置。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | FLOWAGINGTIME | SESSAGINGTIME |
| --- | --- | --- |
| 初始值 | 36 | 60 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| FLOWAGINGTIME | 业务流老化时间（秒） | 可选必选说明：可选参数<br>参数含义：该参数用于设置SSU容器业务流老化时间。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为5~7200，单位为秒。<br>默认值：无<br>配置原则：该取值必须大于SSG容器的业务流老化时间加上SSU容器的单据采样周期。 |
| SESSAGINGTIME | 用户会话老化时间（分钟） | 可选必选说明：可选参数<br>参数含义：该参数用于设置SSU容器业务用户老化时间。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为5~7200，单位为分钟。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [SSU容器业务相关老化功能配置（SSUAGINGCFG）](configobject/UDG/20.15.2/SSUAGINGCFG.md)

## 使用实例

设置SSU容器业务相关老化功能配置：

```
SET SSUAGINGCFG: FLOWAGINGTIME=56, SESSAGINGTIME=5;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置SSU容器业务相关老化功能配置（SET-SSUAGINGCFG）_28121355.md`
