---
id: UDG@20.15.2@MMLCommand@RMV L3SERVICEDUALUPG
type: MMLCommand
name: RMV L3SERVICEDUALUPG（删除一个微服务迁移流程）
nf: UDG
version: 20.15.2
verb: RMV
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

# RMV L3SERVICEDUALUPG（删除一个微服务迁移流程）

## 功能

灰度升级中，执行此命令，删除一个微服务迁移过程。

> **说明**
> - 该命令执行后立即生效。
>
> - 需要先确保数据库中至少存在一个实例，可以用[**ADD L3SERVICEDUALUPG**](增加一个微服务迁移过程（ADD L3SERVICEDUALUPG）_88662246.md)添加。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| L3SERVICE | L3Service | 可选必选说明：必选参数<br>参数含义：该参数用于标识一个微服务。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [一个微服务迁移流程（L3SERVICEDUALUPG）](configobject/UDG/20.15.2/L3SERVICEDUALUPG.md)

## 使用实例

删除服务名为AM的微服务迁移流程：

```
%%RMV L3SERVICEDUALUPG: L3SERVICE="AM";%%
RETCODE = 0  操作成功

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除一个微服务迁移流程（RMV-L3SERVICEDUALUPG）_33781927.md`
