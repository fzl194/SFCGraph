---
id: UNC@20.15.2@MMLCommand@SET PCSCFCTRL
type: MMLCommand
name: SET PCSCFCTRL（设置P-CSCF控制配置）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: PCSCFCTRL
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
- GGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- IMS管理
- P-CSCF管理
- P-CSCF故障恢复控制
status: active
---

# SET PCSCFCTRL（设置P-CSCF控制配置）

## 功能

**适用NF：PGW-C、SMF、GGSN**

该命令用于配置P-CSCF控制属性。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| FAILRST |
| --- |
| ENABLE |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| FAILRST | 故障恢复 | 可选必选说明：可选参数<br>参数含义：该参数用于设置检测到P-CSCF故障时，是否主动向用户侧发起UpdateBearerRequest消息更新P-CSCF地址。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE（不使能）<br>- ENABLE（使能）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST PCSCFCTRL查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PCSCFCTRL]] · P-CSCF控制配置（PCSCFCTRL）

## 使用实例

关闭P-CSCF故障后主动发送UpdateBearerRequest消息：

```
SET PCSCFCTRL: FAILRST=DISABLE;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置P-CSCF控制配置（SET-PCSCFCTRL）_09653206.md`
