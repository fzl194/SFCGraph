---
id: UDG@20.15.2@MMLCommand@SET NPECMPLOCALPRE
type: MMLCommand
name: SET NPECMPLOCALPRE（设置优选本单板TRUNK出接口开关）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: NPECMPLOCALPRE
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 系统管理
- 转发引擎实例FEI
- 优选本单板TRUNK出接口
status: active
---

# SET NPECMPLOCALPRE（设置优选本单板TRUNK出接口开关）

## 功能

该命令用来设置NP优选本单板TRUNK出接口开关。

## 注意事项

- 该命令执行后立即生效。
- 该命令仅适用于NP卡加速模式场景。
- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：
  | LOCALPREDISABLE |
  | --- |
  | FALSE |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LOCALPREDISABLE | 关闭优选本单板TRUNK出接口开关 | 可选必选说明：必选参数。<br>参数含义：该参数用于指定关闭优选本单板TRUNK出接口开关状态。<br>数据来源：本端规划。<br>取值范围：<br>- “FALSE”：开启优选本单板TRUNK出接口开关。<br>- “TRUE”：关闭优选本单板TRUNK出接口开关。<br>默认值：无。<br>配置原则：无。 |

## 操作的配置对象

- [优选本单板TRUNK出接口开关（NPECMPLOCALPRE）](configobject/UDG/20.15.2/NPECMPLOCALPRE.md)

## 使用实例

设置关闭优选本单板TRUNK出接口开关：

```
SET NPECMPLOCALPRE: LOCALPREDISABLE=TRUE;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置优选本单板TRUNK出接口开关（SET-NPECMPLOCALPRE）_85018276.md`
