---
id: UDG@20.15.2@MMLCommand@SET L3SERVICEDUALUPG
type: MMLCommand
name: SET L3SERVICEDUALUPG（设置一个微服务迁移过程）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: L3SERVICEDUALUPG
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 编排管理
- 灰度升级管理
- 微服务迁移过程
status: active
---

# SET L3SERVICEDUALUPG（设置一个微服务迁移过程）

## 功能

灰度升级中，执行此命令，设置一个微服务迁移过程。

> **说明**
> - 该命令执行后立即生效。
>
> - 需要先确保数据库中至少存在一个实例，可以用[**ADD L3SERVICEDUALUPG**](增加一个微服务迁移过程（ADD L3SERVICEDUALUPG）_88662246.md)添加。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| L3SERVICE | L3Service | 可选必选说明：必选参数<br>参数含义：该参数用于标识一个微服务。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无。<br>配置原则：无 |
| OLDVERSION | OldVersion | 可选必选说明：必选参数<br>参数含义：该参数用于标识一个老版本。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~1024。<br>默认值：无。<br>配置原则：无 |
| NEWVERSION | NewVersion | 可选必选说明：必选参数<br>参数含义：该参数用于标识新版本。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~1024。<br>默认值：无。<br>配置原则：无 |
| OLDPODNUM | OldPODNum | 可选必选说明：必选参数<br>参数含义：该参数用于标识老pod数量。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~2147483647。<br>默认值：无。<br>配置原则：无 |
| NEWPODNUM | NewPODNum | 可选必选说明：必选参数<br>参数含义：该参数用于标识新版本pod数量。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~2147483647。<br>默认值：无。<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@L3SERVICEDUALUPG]] · 一个微服务迁移流程（L3SERVICEDUALUPG）

## 使用实例

设置已经存在的微服务AM的迁移流程相关参数：

```
%%SET L3SERVICEDUALUPG: L3SERVICE="AM", OLDVERSION="21.1", NEWVERSION="21.5", OLDPODNUM=5, NEWPODNUM=7;%%
RETCODE = 0  操作成功

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-L3SERVICEDUALUPG.md`
