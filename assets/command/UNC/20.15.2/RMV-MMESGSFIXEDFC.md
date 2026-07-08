---
id: UNC@20.15.2@MMLCommand@RMV MMESGSFIXEDFC
type: MMLCommand
name: RMV MMESGSFIXEDFC（删除VLR局向Sgs固定速率流控）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: MMESGSFIXEDFC
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

# RMV MMESGSFIXEDFC（删除VLR局向Sgs固定速率流控）

## 功能

**适用NF：SMSF**

此命令用于删除VLR局向Sgs固定速率流控。删除后，Sgs固定速率流控不再生效。

## 注意事项

无。

## 权限

manage-ug；system-ug；
G_1，管理员级别命令组；G_2，操作员级别命令组；

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MMEIDX | MME索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定一个MME实体，在全局范围内唯一。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0~1999<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/MMESGSFIXEDFC]] · VLR局向Sgs固定速率流控（MMESGSFIXEDFC）

## 使用实例

删除MMEIDX为1的VLR局向Sgs固定速率流控。

```
RMV MMESGSFIXEDFC: MMEIDX=1;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-MMESGSFIXEDFC.md`
