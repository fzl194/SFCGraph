---
id: UDG@20.15.2@MMLCommand@SET PKICRLCHECK
type: MMLCommand
name: SET PKICRLCHECK（设置CRL检查）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: PKICRLCHECK
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- IPSEC功能管理
- IP服务
- IP安全管理
- 公钥基础设施
- 使能CRL检查
status: active
---

# SET PKICRLCHECK（设置CRL检查）

## 功能

该命令用于设置是否进行CRL检查。

> **说明**
> - 该命令执行后立即生效。
>
> - 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：
>
> | ISCRLENABLE |
> | --- |
> | FALSE |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ISCRLENABLE | CRL检查 | 可选必选说明：可选参数<br>参数含义：该参数用于表示是否进行CRL检查。<br>数据来源：本端规划<br>取值范围：<br>- TRUE(TRUE)<br>- FALSE(FALSE)<br>默认值：FALSE。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST PKICRLCHECK查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/PKICRLCHECK]] · CRL检查（PKICRLCHECK）

## 使用实例

- 设置不进行CRL检查：
  ```
  SET PKICRLCHECK: ISCRLENABLE=FALSE;
  ```
- 设置进行CRL检查：
  ```
  SET PKICRLCHECK: ISCRLENABLE=TRUE;
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置CRL检查（SET-PKICRLCHECK）_41702627.md`
