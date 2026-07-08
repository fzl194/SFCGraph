---
id: UNC@20.15.2@MMLCommand@SET PLMNRATECTRL
type: MMLCommand
name: SET PLMNRATECTRL（设置Serving PLMN速率控制配置）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: PLMNRATECTRL
command_category: 配置类
applicable_nf:
- SGW-C
- PGW-C
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 速率控制
- PLMN速率控制
- Serving PLMN速率控制配置
status: active
---

# SET PLMNRATECTRL（设置Serving PLMN速率控制配置）

## 功能

![](设置Serving PLMN速率控制配置（SET PLMNRATECTRL）_64343918.assets/notice_3.0-zh-cn_2.png)

配置基于全局的Serving PLMN速率控制功能，可能会导致用户业务丢包。

**适用NF：SGW-C、PGW-C**

该命令用于配置全局Serving PLMN速率控制功能，用于限制终端的数据传输速率。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| PLMNRATECTRLSW |
| --- |
| DISABLE |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PLMNRATECTRLSW | Serving PLMN速率控制开关 | 可选必选说明：可选参数<br>参数含义：该参数用于控制开启和关闭Serving PLMN速率控制功能。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE（不使能）<br>- ENABLE（使能）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST PLMNRATECTRL查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PLMNRATECTRL]] · Serving PLMN速率控制配置（PLMNRATECTRL）

## 使用实例

全局Serving PLMN速率控制开关配置为打开：

```
SET PLMNRATECTRL:PLMNRATECTRLSW=ENABLE;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置Serving-PLMN速率控制配置（SET-PLMNRATECTRL）_64343918.md`
