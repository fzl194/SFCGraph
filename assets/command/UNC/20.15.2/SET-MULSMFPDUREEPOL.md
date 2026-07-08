---
id: UNC@20.15.2@MMLCommand@SET MULSMFPDUREEPOL
type: MMLCommand
name: SET MULSMFPDUREEPOL（设置是否支持多SMFInfo场景下的PDU会话重建策略）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: MULSMFPDUREEPOL
command_category: 配置类
applicable_nf:
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 跨区域PDU会话管理
- 多SMFInfo会话重建策略
status: active
---

# SET MULSMFPDUREEPOL（设置是否支持多SMFInfo场景下的PDU会话重建策略）

## 功能

![](设置是否支持多SMFInfo场景下的PDU会话重建策略（SET MULSMFPDUREEPOL）_23782838.assets/notice_3.0-zh-cn_2.png)

该命令的错误设置可能会导致PDU会话被错误重建。

**适用NF：SMF**

该命令用于指定SMF是否支持多SMFInfo场景下的会话重建功能。

## 注意事项

- 随移动性流程生效

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| MULSMFPDUREESUP |
| --- |
| NotSupport |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MULSMFPDUREESUP | 是否支持多SMFInfo下会话重建 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SMF是否支持多SMFInfo场景下的会话重建功能。<br>数据来源：本端规划<br>取值范围：<br>- NotSupport（不支持）<br>- Support（支持）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST MULSMFPDUREEPOL查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@MULSMFPDUREEPOL]] · 是否支持多SMFInfo场景下的会话重建功能（MULSMFPDUREEPOL）

## 使用实例

以下命令用于指定SMF支持多SMFInfo场景下的会话重建功能。

```
SET MULSMFPDUREEPOL: MULSMFPDUREESUP=Support;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-MULSMFPDUREEPOL.md`
