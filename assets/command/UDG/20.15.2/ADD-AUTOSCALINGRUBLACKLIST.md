---
id: UDG@20.15.2@MMLCommand@ADD AUTOSCALINGRUBLACKLIST
type: MMLCommand
name: ADD AUTOSCALINGRUBLACKLIST（增加自动部署RU黑名单）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: AUTOSCALINGRUBLACKLIST
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
max_records: 16
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 自动部署
- 自动化配置RU黑名单
status: active
---

# ADD AUTOSCALINGRUBLACKLIST（增加自动部署RU黑名单）

## 功能

该命令用于向自动化配置RU黑名单中添加成员，所有自动化配置将不会在黑名单列表里的RU上生成。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为16。
- 该命令在自动化配置开关为关闭的状态下才能执行，请先使用SET AUTOCONFIG命令关闭自动配置开关。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUID | RU ID | 可选必选说明：必选参数<br>参数含义：该参数用于指定RU ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为64～9999。<br>默认值：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@AUTOSCALINGRUBLACKLIST]] · 自动部署RU黑名单（AUTOSCALINGRUBLACKLIST）

## 使用实例

将ID为66的RU添加到黑名单列表中：

```
ADD AUTOSCALINGRUBLACKLIST: RUID=66;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/ADD-AUTOSCALINGRUBLACKLIST.md`
