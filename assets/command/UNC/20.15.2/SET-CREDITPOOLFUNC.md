---
id: UNC@20.15.2@MMLCommand@SET CREDITPOOLFUNC
type: MMLCommand
name: SET CREDITPOOLFUNC（设置Credit Pooling功能）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: CREDITPOOLFUNC
command_category: 配置类
applicable_nf:
- PGW-C
- GGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 在线计费
- 信用控制
- 信用池功能控制
status: active
---

# SET CREDITPOOLFUNC（设置Credit Pooling功能）

## 功能

**适用NF：PGW-C、GGSN**

该命令用于设置Credit Pooling功能参数。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| CREDITPOOLSW |
| --- |
| DISABLE |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CREDITPOOLSW | Credit Pooling功能开关 | 可选必选说明：可选参数<br>参数含义：该参数用于配置Credit Pooling功能开关。<br>数据来源：全网规划<br>取值范围：<br>- “DISABLE（不使能）”：不开启Credit Pooling功能。<br>- “ENABLE（使能）”：开启Credit Pooling功能。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CREDITPOOLFUNC查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@CREDITPOOLFUNC]] · Credit Pooling功能（CREDITPOOLFUNC）

## 使用实例

需要支持Credit Pooling功能时，可以执行如下命令：

```
SET CREDITPOOLFUNC:CREDITPOOLSW=ENABLE;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-CREDITPOOLFUNC.md`
