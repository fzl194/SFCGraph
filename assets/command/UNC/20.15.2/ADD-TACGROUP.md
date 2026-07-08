---
id: UNC@20.15.2@MMLCommand@ADD TACGROUP
type: MMLCommand
name: ADD TACGROUP（增加TAC组）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: TACGROUP
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 虚拟APN映射管理
- 基于TAC位置的虚拟APN映射管理
- 虚拟APN映射的TAC组
status: active
---

# ADD TACGROUP（增加TAC组）

## 功能

**适用NF：PGW-C、SMF**

该命令用来添加TAC组，当需要使用本地配置的TAC组时，使用此命令。

## 注意事项

- 该命令执行后立即生效。

- 最多可输入3000条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TACGROUPNAME | TAC组名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定TAC组名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~32。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| TACTYPE | TAC类型 | 可选必选说明：必选参数<br>参数含义：TAC类型。<br>数据来源：本端规划<br>取值范围：<br>- S1Tac（S1TAC）<br>- N2Tac（N2TAC）<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@TACGROUP]] · TAC组（TACGROUP）

## 使用实例

假设运营商需要去添加一个新的TAC组beijing：

```
ADD TACGROUP:TACGROUPNAME="beijing",TACTYPE=S1Tac;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-TACGROUP.md`
