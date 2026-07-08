---
id: UDG@20.15.2@MMLCommand@SET SCFMVNFMLNK
type: MMLCommand
name: SET SCFMVNFMLNK（配置超时时间）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: SCFMVNFMLNK
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 编排管理
- 部署规格管理
status: active
---

# SET SCFMVNFMLNK（配置超时时间）

## 功能

该命令用于设置VNFM-VNF之间同步消息超时时间。

> **说明**
> - 该命令执行后立即生效。
>
> - 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：
>
> | LNKTIME |
> | --- |
> | 180 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LNKTIME | 同步消息超时时间 | 可选必选说明：必选参数<br>参数含义：该参数用于表示VNFM-VNF之间同步消息的最大等候时间。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是180~600，单位是秒。180 <= LNKTIME <= 600。<br>默认值：无。<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/SCFMVNFMLNK]] · 超时时间配置（SCFMVNFMLNK）

## 使用实例

设置最大等候时间为180秒。

```
%%SET SCFMVNFMLNK: LNKTIME=180;%%
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-SCFMVNFMLNK.md`
