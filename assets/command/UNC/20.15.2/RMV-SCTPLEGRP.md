---
id: UNC@20.15.2@MMLCommand@RMV SCTPLEGRP
type: MMLCommand
name: RMV SCTPLEGRP（删除SCTP本地实体组）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: SCTPLEGRP
command_category: 配置类
applicable_nf:
- MME
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- S1接口管理
- SCTP本地实体组
status: active
---

# RMV SCTPLEGRP（删除SCTP本地实体组）

## 功能

**适用网元：MME、AMF**

该命令用于删除SCTP本端实体组配置。

## 注意事项

- 该命令执行后立即生效。
- SCTP本地实体组下存在实体或者被NGAP或SFGAP本地实体引用时，不允许删除。

## 权限

manage-ug，system-ug，monitor-ug，visit-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SCTPGROUPID | SCTP本地实体组标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定SCTP本地实体组的标识。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0~255。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SCTPLEGRP]] · SCTP本地实体组（SCTPLEGRP）

## 使用实例

删除实体组ID为0的SCTP本地实体组。

```
RMV SCTPLEGRP: SCTPGROUPID=0;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-SCTPLEGRP.md`
