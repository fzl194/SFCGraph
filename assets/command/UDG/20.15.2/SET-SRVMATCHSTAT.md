---
id: UDG@20.15.2@MMLCommand@SET SRVMATCHSTAT
type: MMLCommand
name: SET SRVMATCHSTAT（设置业务匹配统计参数）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: SRVMATCHSTAT
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 1
category_path:
- 用户面服务管理
- 业务运维
- 业务性能统计管理
- 业务匹配统计配置
status: active
---

# SET SRVMATCHSTAT（设置业务匹配统计参数）

## 功能

**适用NF：PGW-U、UPF**

该命令用于配置是否开启业务匹配的统计功能。功能开启，当业务匹配到规则的时候，将对应规则的匹配计数加1。功能关闭则不进行规则匹配计数的统计。运营商需要进行规则匹配次数的监控时，可以开启该功能。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | SWITCH |
| --- | --- |
| 初始值 | ENABLE |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SWITCH | 开关 | 可选必选说明：必选参数<br>参数含义：该参数用于设置是否使能业务匹配的统计功能。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能（关闭）。<br>- ENABLE：使能（开启）。<br>默认值：无<br>配置原则：<br>- DISABLE：不需要规则匹配次数的监控时，配置该参数。<br>- ENABLE：需要进行规则匹配次数的监控时，配置该参数。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@SRVMATCHSTAT]] · 业务匹配统计参数（SRVMATCHSTAT）

## 使用实例

运营商需要进行业务匹配统计的监控时，配置如下：

```
SET SRVMATCHSTAT:SWITCH=ENABLE;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-SRVMATCHSTAT.md`
