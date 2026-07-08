---
id: UNC@20.15.2@MMLCommand@SET NRFSMSFSEGSW
type: MMLCommand
name: SET NRFSMSFSEGSW（设置SMSF号段白名单功能开关）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: NRFSMSFSEGSW
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

# SET NRFSMSFSEGSW（设置SMSF号段白名单功能开关）

## 功能

![](设置SMSF号段白名单功能开关 （SET NRFSMSFSEGSW）_71303606.assets/notice_3.0-zh-cn_2.png)

该命令与ADD NRFSMSFSEGLIST配合使用，在白名单未设置完成时请勿打开此开关，否则携带非白名单中的号段来发现SMSF时，该号段发现参数在匹配时将会被NRF忽略。

**适用NF：NRF**

该命令用于设置SMSF号段白名单功能开关。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| SEGWHITELISTSW |
| --- |
| FUNC_OFF |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SEGWHITELISTSW | 号段白名单开关 | 可选必选说明：必选参数<br>参数含义：该参数用于表示NRF是否开启SMSF号段白名单功能。当开关设置为FUNC_ON时，若发现参数中携带的号段在白名单内，NRF会使用号段参数匹配，否则将忽略该号段参数。当开关设置为FUNC_OFF时，NRF将会按照发现参数进行正常匹配。<br>数据来源：本端规划<br>取值范围：<br>- FUNC_ON（打开）<br>- FUNC_OFF（关闭）<br>默认值：无。<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NRFSMSFSEGSW]] · SMSF号段白名单功能开关（NRFSMSFSEGSW）

## 使用实例

若希望请求方NF携带非白名单中的号段发现参数来发现SMSF时，NRF忽略该号段发现参数来匹配SMSF。可打开此开关：

```
SET NRFSMSFSEGSW: SEGWHITELISTSW=FUNC_ON;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置SMSF号段白名单功能开关-（SET-NRFSMSFSEGSW）_71303606.md`
