---
id: UDG@20.15.2@MMLCommand@SET L3SERVICEUPG
type: MMLCommand
name: SET L3SERVICEUPG（设置服务升级进度）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: L3SERVICEUPG
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 编排管理
- 灰度升级管理
- 服务升级进度
status: active
---

# SET L3SERVICEUPG（设置服务升级进度）

## 功能

灰度升级中，执行此命令，用于设置服务升级进度。

> **说明**
> - 该命令执行后立即生效。
>
> - 需要确定数据库中至少存在一个实例，可以用[**ADD L3SERVICEDUALUPG**](../微服务迁移过程/增加一个微服务迁移过程（ADD L3SERVICEDUALUPG）_88662246.md)增加一个。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| L3SERVICE | L3Service | 可选必选说明：必选参数<br>参数含义：该参数用于标识一个微服务。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无。<br>配置原则：无 |
| POSITION | Position | 可选必选说明：必选参数<br>参数含义：该参数用于标识位于哪一层。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~1024。<br>默认值：无。<br>配置原则：无 |
| MODE | Mode | 可选必选说明：必选参数<br>参数含义：该参数用于标识模式。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~1024。<br>默认值：无。<br>配置原则：无 |
| STATUS | Status | 可选必选说明：必选参数<br>参数含义：该参数用于标识状态。<br>数据来源：本端规划<br>取值范围：<br>- PreUpgrade（PreUpgrade）<br>- InUpgrade（InUpgrade）<br>- PostUpgrade（PostUpgrade）<br>默认值：无。<br>配置原则：无 |
| PROGRESS | Progress | 可选必选说明：必选参数<br>参数含义：该参数用于标识进度。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~100。<br>默认值：无。<br>配置原则：无 |

## 操作的配置对象

- [服务升级进度（L3SERVICEUPG）](configobject/UDG/20.15.2/L3SERVICEUPG.md)

## 使用实例

设置服务AM的升级进度：

```
%%SET L3SERVICEUPG: L3SERVICE="AM", POSITION="Service", MODE="Gray", STATUS=InUpgrade, PROGRESS=20;%%
RETCODE = 0  操作成功

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置服务升级进度（SET-L3SERVICEUPG）_33903415.md`
