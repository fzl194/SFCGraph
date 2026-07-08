---
id: UNC@20.15.2@MMLCommand@ADD MMESGSFIXEDFC
type: MMLCommand
name: ADD MMESGSFIXEDFC（增加VLR局向Sgs固定速率流控）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: MMESGSFIXEDFC
command_category: 配置类
applicable_nf:
- SMSF
effect_mode: ''
is_dangerous: false
max_records: 2000
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 信令传输管理
- SMSF管理
- Vlr Sgs固定速率流控
status: active
---

# ADD MMESGSFIXEDFC（增加VLR局向Sgs固定速率流控）

## 功能

**适用NF：SMSF**

此命令用于增加VLR局向Sgs固定速率流控相关参数。

## 注意事项

此命令的最大记录数为2000。

## 权限

manage-ug；system-ug；
G_1，管理员级别命令组；G_2，操作员级别命令组；

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MMEIDX | MME索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定一个MME实体，在全局范围内唯一。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0~1999<br>默认值：无<br>配置原则：<br>该参数来源于ADD SGSMME中的"MMEX"参数。 |
| LURTHD | Location Update Request速率门限(个/秒) | 可选必选说明：可选参数<br>参数含义：该参数用于设置VLR接收Location Update Request速率门限。对应消息数量超过该门限值时，部分消息会被流控，不处理。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为1~1000000，单位是个每秒。<br>默认值：1500<br>配置原则：无 |
| DETACHTHD | Detach Indication速率门限(个/秒) | 可选必选说明：可选参数<br>参数含义：该参数用于设置VLR接收Detach Indication速率门限。对应消息数量超过该门限值时，部分消息会被流控，不处理。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为1~1000000，单位是个每秒。<br>默认值：500<br>配置原则：无 |
| PAGINGTHD | Paging速率门限(个/秒) | 可选必选说明：可选参数<br>参数含义：该参数用于设置VLR发送Paging速率门限。对应消息数量超过该门限值时，部分消息会被流控，不处理。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为1~1000000，单位是个每秒。<br>默认值：2000<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/MMESGSFIXEDFC]] · VLR局向Sgs固定速率流控（MMESGSFIXEDFC）

## 使用实例

增加VLR局向Sgs固定速率流控，MMEIDX为1。

```
ADD MMESGSFIXEDFC: MMEIDX=1;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-MMESGSFIXEDFC.md`
