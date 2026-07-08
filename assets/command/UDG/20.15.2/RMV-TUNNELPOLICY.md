---
id: UDG@20.15.2@MMLCommand@RMV TUNNELPOLICY
type: MMLCommand
name: RMV TUNNELPOLICY（删除隧道策略）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: TUNNELPOLICY
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- VPN管理
- VPN隧道管理
- 隧道策略
status: active
---

# RMV TUNNELPOLICY（删除隧道策略）

## 功能

该命令用于删除隧道策略。

## 注意事项

- 该命令执行后立即生效。
- 若删除隧道策略名，则当前隧道策略下的隧道选择策略将被同时删除。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TNLPOLICYNAME | 隧道策略名字 | 可选必选说明：必选参数<br>参数含义：该参数用于表示隧道策略名字。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～39。<br>默认值：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@TUNNELPOLICY]] · 隧道策略（TUNNELPOLICY）

## 使用实例

删除隧道策略：

```
RMV TUNNELPOLICY:TNLPOLICYNAME="tp";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-TUNNELPOLICY.md`
