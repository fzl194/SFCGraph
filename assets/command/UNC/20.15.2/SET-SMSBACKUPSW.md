---
id: UNC@20.15.2@MMLCommand@SET SMSBACKUPSW
type: MMLCommand
name: SET SMSBACKUPSW（设置SMSF热备容灾功能开关状态）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: SMSBACKUPSW
command_category: 配置类
applicable_nf:
- SMSF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- SMSF业务管理
- 热备容灾
status: active
---

# SET SMSBACKUPSW（设置SMSF热备容灾功能开关状态）

## 功能

**适用NF：SMSF**

该命令用于设置SMSF热备容灾功能开关状态。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| SMSBACKUPFUNCSW |
| --- |
| FUNC_OFF |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SMSBACKUPFUNCSW | SMSF热备容灾功能开关 | 可选必选说明：必选参数<br>参数含义：该参数用于表示SMSF热备容灾功能开关。<br>数据来源：本端规划<br>取值范围：<br>- “FUNC_ON（打开）”：功能开关打开<br>- “FUNC_OFF（关闭）”：功能开关关闭<br>默认值：无。<br>配置原则：无 |

## 操作的配置对象

- [SMSF热备容灾功能开关状态（SMSBACKUPSW）](configobject/UNC/20.15.2/SMSBACKUPSW.md)

## 使用实例

运营商希望设置SMSF热备容灾功能开关为打开时，执行如下命令：

```
SET SMSBACKUPSW: SMSBACKUPFUNCSW=FUNC_ON;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置SMSF热备容灾功能开关状态（SET-SMSBACKUPSW）_30680378.md`
