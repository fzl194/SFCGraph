---
id: UNC@20.15.2@MMLCommand@SET ASNFUNC
type: MMLCommand
name: SET ASNFUNC（设置ASN功能）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: ASNFUNC
command_category: 配置类
applicable_nf:
- PGW-C
- GGSN
- SGW-C
effect_mode: 对新用户生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- GTP-C接口配置管理
- ASN功能管理
status: active
---

# SET ASNFUNC（设置ASN功能）

## 功能

**适用NF：PGW-C、GGSN、SGW-C**

该命令用于配置ASN功能开关属性和ASN同步周期。

## 注意事项

- 该命令执行后只对新激活用户生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| ASNSWITCH | SYNCINTERVAL |
| --- | --- |
| DISABLE | 24 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ASNSWITCH | ASN功能开关 | 可选必选说明：可选参数<br>参数含义：该参数用于控制是否将ASN作为漫游计费标识并在上送预付费系统的CCR中携带。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE（不使能）<br>- ENABLE（使能）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST ASNFUNC查询当前参数配置值。<br>配置原则：无 |
| SYNCINTERVAL | ASN同步周期(小时) | 可选必选说明：可选参数<br>参数含义：该参数用于设置获取ASN值的周期。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~24。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST ASNFUNC查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/ASNFUNC]] · ASN功能（ASNFUNC）

## 使用实例

配置ASN功能开关为使能状态，ASN的定时同步周期为5小时：

```
SET ASNFUNC:ASNSWITCH=ENABLE,SYNCINTERVAL=5;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置ASN功能（SET-ASNFUNC）_35519283.md`
