---
id: UDG@20.15.2@MMLCommand@ADD L3SERVICEDUALUPG
type: MMLCommand
name: ADD L3SERVICEDUALUPG（增加一个微服务迁移过程）
nf: UDG
version: 20.15.2
verb: ADD
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

# ADD L3SERVICEDUALUPG（增加一个微服务迁移过程）

## 功能

灰度升级中，执行此命令，增加一个微服务迁移过程。

> **说明**
> - 该命令执行后立即生效。
>
> - 最多可输入100000条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| L3SERVICE | L3Service | 可选必选说明：必选参数<br>参数含义：该参数用于标识一个微服务。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：无 |
| OLDVERSION | OldVersion | 可选必选说明：必选参数<br>参数含义：该参数用于标识一个老版本。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~1024。<br>默认值：无<br>配置原则：无 |
| NEWVERSION | NewVersion | 可选必选说明：必选参数<br>参数含义：该参数用于标识新版本。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~1024。<br>默认值：无<br>配置原则：无 |
| OLDPODNUM | OldPODNum | 可选必选说明：必选参数<br>参数含义：该参数用于标识老pod数量。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~2147483647。<br>默认值：无<br>配置原则：无 |
| NEWPODNUM | NewPODNum | 可选必选说明：必选参数<br>参数含义：该参数用于标识新版本pod数量。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~2147483647。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/L3SERVICEDUALUPG]] · 一个微服务迁移流程（L3SERVICEDUALUPG）

## 使用实例

增加一个微服务类型为AM的迁移过程，设置旧版本为21.1，新版本为21.5，老版本Pod数量为10，新版本Pod数量为2：

```
%%ADD L3SERVICEDUALUPG: L3SERVICE="AM", OLDVERSION="21.1", NEWVERSION="21.5", OLDPODNUM=10, NEWPODNUM=2;%%
RETCODE = 0  操作成功

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/ADD-L3SERVICEDUALUPG.md`
