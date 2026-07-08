---
id: UNC@20.15.2@MMLCommand@SET GLBPGWCHGPAUSE
type: MMLCommand
name: SET GLBPGWCHGPAUSE（设置全局计费暂停配置）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: GLBPGWCHGPAUSE
command_category: 配置类
applicable_nf:
- PGW-C
effect_mode: 对新用户生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 计费暂停管理
- PGW计费暂停管理
status: active
---

# SET GLBPGWCHGPAUSE（设置全局计费暂停配置）

## 功能

**适用NF：PGW-C**

该命令用于设置全局的PGW的计费暂停功能。

## 注意事项

- 该命令执行后只对新激活用户生效。

- 当SGW-U与PGW-U合一部署时，由U面根据本地策略决策是否计费暂停，C面不支持计费暂停功能。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| CHGPAUSESWITCH |
| --- |
| DISABLE |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CHGPAUSESWITCH | 计费暂停开关 | 可选必选说明：可选参数<br>参数含义：该参数用于表示计费暂停功能开关。<br>数据来源：全网规划<br>取值范围：<br>- DISABLE（不使能）<br>- ENABLE（使能）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST GLBPGWCHGPAUSE查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/GLBPGWCHGPAUSE]] · 全局计费暂停配置（GLBPGWCHGPAUSE）

## 使用实例

全局使能计费暂停，进行如下设置：

```
SET GLBPGWCHGPAUSE: CHGPAUSESWITCH = ENABLE;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置全局计费暂停配置（SET-GLBPGWCHGPAUSE）_42502266.md`
