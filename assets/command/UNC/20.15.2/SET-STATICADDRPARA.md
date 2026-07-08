---
id: UNC@20.15.2@MMLCommand@SET STATICADDRPARA
type: MMLCommand
name: SET STATICADDRPARA（设置静态地址参数）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: STATICADDRPARA
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
- 接入管理
- UE地址管理
- 静态地址参数配置
status: active
---

# SET STATICADDRPARA（设置静态地址参数）

## 功能

**适用NF：PGW-C、SMF、GGSN**

该命令用于设置使用静态地址用户的扫描任务参数，配置静态地址用户的去激活扫描任务，去激活选择了非绑定UPF的用户。

## 注意事项

- 该命令执行后立即生效。

- 扫描开始和结束时间为UTC时间，并且持续时间必须大于10分钟。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| SCANSWT | SCANSTARTTIME | SCANENDTIME |
| --- | --- | --- |
| DISABLE | 00:00 | 00:00 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SCANSWT | 扫描任务开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定静态用户扫描任务的开关。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE（去使能）<br>- ENABLE（使能）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST STATICADDRPARA查询当前参数配置值。<br>配置原则：无 |
| SCANSTARTTIME | 扫描开始时间 | 可选必选说明：该参数在"SCANSWT"配置为"ENABLE"时为条件必选参数。<br>参数含义：该参数用于指定静态地址用户扫描开始UTC时间。<br>数据来源：本端规划<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST STATICADDRPARA查询当前参数配置值。<br>配置原则：无 |
| SCANENDTIME | 扫描结束时间 | 可选必选说明：该参数在"SCANSWT"配置为"ENABLE"时为条件必选参数。<br>参数含义：该参数用于指定静态地址用户扫描结束UTC时间。<br>数据来源：本端规划<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST STATICADDRPARA查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/STATICADDRPARA]] · 静态地址参数（STATICADDRPARA）

## 使用实例

配置静态地址参数，扫描开关关闭：

```
SET STATICADDRPARA: SCANSWT=DISABLE;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-STATICADDRPARA.md`
