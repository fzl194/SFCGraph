---
id: UDG@20.15.2@MMLCommand@SET PATHSTATUSRPT
type: MMLCommand
name: SET PATHSTATUSRPT（设置用户面路径状态上报功能）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: PATHSTATUSRPT
command_category: 配置类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 1
category_path:
- 用户面服务管理
- 路径管理
- GTP路径管理
- GTP协议参数管理
- 用户面路径状态上报开关
status: active
---

# SET PATHSTATUSRPT（设置用户面路径状态上报功能）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用于配置用户面路径故障/路径恢复上报功能开关。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 该命令使能后，如果用户面路径较多，可能触发大量上报消息，因此当前流控限制每秒处理20个用户面路径。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | PATHRPTSW |
| --- | --- |
| 初始值 | DISABLE |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PATHRPTSW | 路径状态上报开关 | 可选必选说明：必选参数<br>参数含义：设置N4接口上报UPFR和UPRR的开关。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@PATHSTATUSRPT]] · 用户面路径状态上报功能（PATHSTATUSRPT）

## 使用实例

需要使能用户面路径故障/路径恢复上报功能时，配置开关为ENABLE：

```
SET PATHSTATUSRPT: PATHRPTSW=ENABLE;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-PATHSTATUSRPT.md`
