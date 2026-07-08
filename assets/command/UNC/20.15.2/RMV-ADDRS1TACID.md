---
id: UNC@20.15.2@MMLCommand@RMV ADDRS1TACID
type: MMLCommand
name: RMV ADDRS1TACID（删除S1TAC组内S1TAC号段）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: ADDRS1TACID
command_category: 配置类
applicable_nf:
- PGW-C
- GGSN
- SMF
effect_mode: 对新用户生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- UE地址管理
- UE地址池管理
- 地址分配位置区管理
- 地址分配S1TAC段
status: active
---

# RMV ADDRS1TACID（删除S1TAC组内S1TAC号段）

## 功能

**适用NF：PGW-C、GGSN、SMF**

该命令用来删除S1TAC组内绑定的S1TAC号段。

## 注意事项

该命令执行后只对新激活用户生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TACGROUPNAME | S1TAC组名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定S1TAC组名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~32。<br>默认值：无<br>配置原则：<br>该参数使用ADD ADDRTACGROUP命令配置生成。 |
| TACSECNUM | S1TAC段编号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定S1TAC段编号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~15999。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/ADDRS1TACID]] · S1TAC组内S1TAC号段（ADDRS1TACID）

## 使用实例

在一个本地已经配置的S1TAC组删除一个S1TAC号段：

```
RMV ADDRS1TACID:TACGROUPNAME="wz-xs",TACSECNUM=2;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除S1TAC组内S1TAC号段（RMV-ADDRS1TACID）_49644928.md`
