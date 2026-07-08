---
id: UNC@20.15.2@MMLCommand@RMV S1TACID
type: MMLCommand
name: RMV S1TACID（删除TAC组内绑定的S1TAC号段）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: S1TACID
command_category: 配置类
applicable_nf:
- PGW-C
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 虚拟APN映射管理
- 基于TAC位置的虚拟APN映射管理
- TAC组的S1 TAC段
status: active
---

# RMV S1TACID（删除TAC组内绑定的S1TAC号段）

## 功能

**适用NF：PGW-C**

该命令用来删除TAC组内绑定的TAC号段。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TACSECNUM | TAC段编号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定TAC段编号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~15999。<br>默认值：无<br>配置原则：无 |
| TACGROUPNAME | TAC组名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定TAC组名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~32。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：<br>本参数通过ADD TACGROUP命令进行配置，且TAC类型必须是S1TAC。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/S1TACID]] · TAC组内绑定的S1TAC号段（S1TACID）

## 使用实例

假设运营商需要在一个本地已经配置的TAC组绑定一个TAC号段：

```
RMV S1TACID: TACSECNUM=2, TACGROUPNAME="beijing";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除TAC组内绑定的S1TAC号段（RMV-S1TACID）_09654426.md`
