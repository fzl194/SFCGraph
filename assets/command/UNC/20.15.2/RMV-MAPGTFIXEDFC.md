---
id: UNC@20.15.2@MMLCommand@RMV MAPGTFIXEDFC
type: MMLCommand
name: RMV MAPGTFIXEDFC（删除VLR局向Map固定速率流控）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: MAPGTFIXEDFC
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
- Vlr Map固定速率流控
status: active
---

# RMV MAPGTFIXEDFC（删除VLR局向Map固定速率流控）

## 功能

**适用NF：SMSF**

此命令用于删除VLR局向Map固定速率流控。删除后，VLR局向MAP固定速率流控不再生效。

## 注意事项

无。

## 权限

manage-ug；system-ug；
G_1，管理员级别命令组；G_2，操作员级别命令组；

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GTNUM | GT地址 | 可选必选说明：必选参数<br>参数含义：该参数用于表示用于流控的局向SMSC的GT地址。<br>数据来源：本端规划<br>取值范围：1～16位十进制数字<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/MAPGTFIXEDFC]] · VLR局向Map固定速率流控（MAPGTFIXEDFC）

## 使用实例

删除GT地址为1的VLR局向Map固定速率流控，可以用如下命令：

```
RMV MAPGTFIXEDFC: GTNUM="1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-MAPGTFIXEDFC.md`
