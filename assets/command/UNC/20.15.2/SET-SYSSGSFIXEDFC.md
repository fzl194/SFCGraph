---
id: UNC@20.15.2@MMLCommand@SET SYSSGSFIXEDFC
type: MMLCommand
name: SET SYSSGSFIXEDFC（设置VLR整系统Sgs固定速率流控）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: SYSSGSFIXEDFC
command_category: 配置类
applicable_nf:
- SMSF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 信令传输管理
- SMSF管理
- Vlr Sgs固定速率流控
status: active
---

# SET SYSSGSFIXEDFC（设置VLR整系统Sgs固定速率流控）

## 功能

**适用NF：SMSF**

此命令用于设置VLR整系统Sgs固定速率流控参数。

## 注意事项

无。

## 权限

manage-ug；system-ug；
G_1，管理员级别命令组；G_2，操作员级别命令组；

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| FCSWITCH | 流控功能开关 | 可选必选说明：必选参数<br>参数含义：该参数用于表示整系统的Sgs固定速率流控开关。<br>数据来源：本端规划<br>取值范围：<br>- “ON”：整系统Sgs固定速率流控开关开启<br>- “OFF”：整系统Sgs固定速率流控开关关闭<br>默认值：ON<br>配置原则：<br>通常情况下，不建议修改本参数取值，当流控功能发生异常时，把本参数设置为“OFF”。 |
| LURTHD | Location Update Request速率门限(个/秒) | 可选必选说明：条件可选参数<br>参数含义：该参数用于设置VLR接收Location Update Request速率门限。对应消息数量超过该门限值时，部分消息会被流控，不处理。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为1~1000000，单位是个每秒。<br>默认值： 8000<br>配置原则：<br>该参数在“流控功能开关”参数配置为“ON（开启）”时生效。 |
| DETACHTHD | Detach Indication速率门限(个/秒) | 可选必选说明：条件可选参数<br>参数含义：该参数用于设置VLR接收Detach Indication速率门限。对应消息数量超过该门限值时，部分消息会被流控，不处理。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为1~1000000，单位是个每秒。<br>默认值： 1000<br>配置原则：<br>该参数在“流控功能开关”参数配置为“ON（开启）”时生效。 |
| PAGINGTHD | Paging速率门限(个/秒) | 可选必选说明：条件可选参数<br>参数含义：该参数用于设置VLR发送Paging速率门限。对应消息数量超过该门限值时，部分消息会被流控，不处理。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为1~1000000，单位是个每秒。<br>默认值： 4000<br>配置原则：<br>该参数在“流控功能开关”参数配置为“ON（开启）”时生效。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SYSSGSFIXEDFC]] · VLR整系统Sgs固定速率流控（SYSSGSFIXEDFC）

## 使用实例

设置VLR整系统Sgs固定速率流控，流控功能打开，Location Update Request速率门限、Detach Indication速率门限、Paging速率门限均为2000：

```
SET SYSSGSFIXEDFC: FCSWITCH=ON, LURTHD=2000, DETACHTHD=2000, PAGINGTHD=2000;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-SYSSGSFIXEDFC.md`
