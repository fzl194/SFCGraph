---
id: UNC@20.15.2@MMLCommand@ADD SCTPLEGRP
type: MMLCommand
name: ADD SCTPLEGRP（增加SCTP本地实体组）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: SCTPLEGRP
command_category: 配置类
applicable_nf:
- MME
- AMF
effect_mode: 立即生效
is_dangerous: false
max_records: 256
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- S1接口管理
- SCTP本地实体组
status: active
---

# ADD SCTPLEGRP（增加SCTP本地实体组）

## 功能

**适用网元：MME、AMF**

本命令用于添加SCTP本端实体组。5G基站(NG RAN)支持多偶联接入，添加SCTP本端实体组用于将多个SCTP本端实体绑定，从而实现多偶联。

## 注意事项

- 该命令执行后立即生效。
- 此命令最大记录数为256。
- 一个SCTP本端实体组只能被一个NGAP或SFGAP本端实体引用。
- 一个SCTP本端实体组可以同时包含IPV4地址的本端实体和IPV6地址的本端实体。

## 权限

无
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SCTPGROUPID | SCTP本地实体组标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定SCTP本地实体组的标识。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0~255。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SCTPLEGRP]] · SCTP本地实体组（SCTPLEGRP）

## 使用实例

增加一个SCTP本地实体组，索引为0。

```
ADD SCTPLEGRP: SCTPGROUPID=0;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加SCTP本地实体组(ADD-SCTPLEGRP)_19186931.md`
