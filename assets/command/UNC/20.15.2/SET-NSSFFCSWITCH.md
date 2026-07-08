---
id: UNC@20.15.2@MMLCommand@SET NSSFFCSWITCH
type: MMLCommand
name: SET NSSFFCSWITCH（设置NSSF流控开关）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: NSSFFCSWITCH
command_category: 配置类
applicable_nf:
- NSSF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- NSSF业务及策略管理
- NSSF流控管理
status: active
---

# SET NSSFFCSWITCH（设置NSSF流控开关）

## 功能

**适用NF：NSSF**

该命令用于设置NSSF流控开关状态。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| NSSFFCSWITCH |
| --- |
| FUNC_ON |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NSSFFCSWITCH | NSSF流控开关 | 可选必选说明：必选参数<br>参数含义：该参数表示NSSF流控开关状态。<br>数据来源：本端规划<br>取值范围：<br>- FUNC_ON（打开）<br>- FUNC_OFF（关闭）<br>默认值：无。<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NSSFFCSWITCH]] · NSSF流控开关（NSSFFCSWITCH）

## 使用实例

当运营商希望使用NSSF的自保流控功能时，需要通过该命令打开NSSF的流控开关：

```
SET NSSFFCSWITCH: NSSFFCSWITCH=FUNC_ON;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-NSSFFCSWITCH.md`
