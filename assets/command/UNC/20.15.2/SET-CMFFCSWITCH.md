---
id: UNC@20.15.2@MMLCommand@SET CMFFCSWITCH
type: MMLCommand
name: SET CMFFCSWITCH（设置CMF流控开关）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: CMFFCSWITCH
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 可靠性管理
- 微服务可靠性管理
status: active
---

# SET CMFFCSWITCH（设置CMF流控开关）

## 功能

该命令用于配置CMF流控功能开关。

## 注意事项

- 该命令执行后立即生效。

- CMF Pod单节点部署时不支持CMF流控，第三方CaaS场景不支持CMF流控，CSPEdge裸机场景不支持CMF流控。
- 虚机场景下流控功能开关开启时，CMF Pod的CPU或CMF Pod所在节点的CPU满足任一起控条件，则触发CMF流控。
- FST裸机场景下流控功能开关开启时，CMF Pod的CPU或CMF Pod所关联的SuperPod的CPU满足任一起控条件，则触发CMF流控。
- 流控功能开关关闭时，不触发CMF流控。
- 执行本命令时，FCSWITCH的取值不能为“未设置”，否则将导致配置下发失败。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| FCSWITCH |
| --- |
| NOTSET |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| FCSWITCH | 流控功能开关 | 可选必选说明：必选参数<br>参数含义：该参数用于打开或关闭CMF流控功能。<br>数据来源：本端规划<br>取值范围：<br>- “ON（开启）”：流控功能开关打开。<br>- “OFF（关闭）”：流控功能开关关闭。<br>- “NOTSET（未设置）”：用户未设置流控功能开关，实际配置以DSP DBGHAFD命令查询为准。<br>默认值：无。<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/CMFFCSWITCH]] · CMF流控开关配置数据（CMFFCSWITCH）

## 使用实例

- 打开流控功能开关。
  ```
  SET CMFFCSWITCH: FCSWITCH=ON;
  ```
- 关闭流控功能开关。
  ```
  SET CMFFCSWITCH: FCSWITCH=OFF;
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-CMFFCSWITCH.md`
