---
id: UNC@20.15.2@MMLCommand@RMV AMFRESELPLCY
type: MMLCommand
name: RMV AMFRESELPLCY（删除AMF重选控制策略）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: AMFRESELPLCY
command_category: 配置类
applicable_nf:
- AMF
effect_mode: 对新用户生效
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- AMF区域重选功能管理
- AMF重选控制策略
status: active
---

# RMV AMFRESELPLCY（删除AMF重选控制策略）

## 功能

**适用NF：AMF**

该命令用于删除AMF重选功能控制策略。

## 注意事项

该命令执行后只对新激活用户生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBGRPID | 用户群组标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定应用AMF重选功能的用户群组。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~4294967294。该用户群组标识通过ADD NGUSRGRP进行添加。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@AMFRESELPLCY]] · AMF重选控制策略（AMFRESELPLCY）

## 使用实例

删除用户群组1的AMF重选控制策略记录，执行命令如下：

```
RMV AMFRESELPLCY: SUBGRPID=1;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-AMFRESELPLCY.md`
