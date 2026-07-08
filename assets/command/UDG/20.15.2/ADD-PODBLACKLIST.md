---
id: UDG@20.15.2@MMLCommand@ADD PODBLACKLIST
type: MMLCommand
name: ADD PODBLACKLIST（增加Pod自愈黑名单）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: PODBLACKLIST
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 可靠性管理
- 微服务可靠性管理
status: active
---

# ADD PODBLACKLIST（增加Pod自愈黑名单）

## 功能

该命令用于增加指定Pod类型到Pod自愈黑名单中。增加到Pod自愈黑名单中的Pod不支持自愈功能。

> **说明**
> - 该命令执行后立即生效。
>
> - 最多可输入1024条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PODTYPE | Pod类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指示Pod自愈黑名单的Pod类型。可通过<br>[**DSP PODINFO**](../../编排管理/POD管理/显示已部署的Pod实例信息（DSP PODINFO）_09587375.md)<br>查询。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~32。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/PODBLACKLIST]] · Pod自愈黑名单（PODBLACKLIST）

## 使用实例

将"ipctrl-pod" pod类型增加到Pod自愈黑名单。

```
ADD PODBLACKLIST: PODTYPE="ipctrl-pod";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/增加Pod自愈黑名单（ADD-PODBLACKLIST）_09587923.md`
