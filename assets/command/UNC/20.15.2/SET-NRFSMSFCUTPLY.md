---
id: UNC@20.15.2@MMLCommand@SET NRFSMSFCUTPLY
type: MMLCommand
name: SET NRFSMSFCUTPLY（设置SMSF割接场景NRF处理策略）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: NRFSMSFCUTPLY
command_category: 配置类
applicable_nf:
- NRF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- NRF业务参数
- SMSF割接场景NRF处理策略
status: active
---

# SET NRFSMSFCUTPLY（设置SMSF割接场景NRF处理策略）

## 功能

**适用NF：NRF**

该命令用于设置SMSF割接场景下，NRF的处理策略。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| SMSFCUTOVERSW |
| --- |
| FUNC_OFF |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SMSFCUTOVERSW | SMSF割接场景NRF发现匹配开关 | 可选必选说明：必选参数<br>参数含义：该参数用于控制SMSF割接时NRF服务发现的匹配策略。 当开关设置为FUNC_ON时，NF基于号段和NFtype发现SMSF，若NRF上有满足条件的SMSF，NRF会直接匹配返回；若NRF上注册的SMSF不能满足号段条件，NRF会将现网存量SMSF返回，存量SMSF不在本NRF注册时，NRF将路由到对应大区的NRF进行服务发现。当开关设置为FUNC_OFF时，NRF将会按照发现参数进行正常匹配。<br>数据来源：本端规划<br>取值范围：<br>- FUNC_ON（打开）<br>- FUNC_OFF（关闭）<br>默认值：无。<br>配置原则：无 |

## 操作的配置对象

- [SMSF割接场景NRF处理策略（NRFSMSFCUTPLY）](configobject/UNC/20.15.2/NRFSMSFCUTPLY.md)

## 使用实例

运营商希望NF基于号段和NFtype发现SMSF，若号段条件不匹配时，NRF返回存量SMSF，执行如下命令：

```
SET NRFSMSFCUTPLY: SMSFCUTOVERSW=FUNC_ON;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置SMSF割接场景NRF处理策略（SET-NRFSMSFCUTPLY）_71623462.md`
