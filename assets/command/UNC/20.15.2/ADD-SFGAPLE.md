---
id: UNC@20.15.2@MMLCommand@ADD SFGAPLE
type: MMLCommand
name: ADD SFGAPLE（增加SFGAP本端实体）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: SFGAPLE
command_category: 配置类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- N2接口管理
- SFGAP本端实体管理
status: active
---

# ADD SFGAPLE（增加SFGAP本端实体）

## 功能

**适用NF：AMF**

在部署感知的场景下，通过ADD SFGAPLE增加SFGAP本端实体，AMF可以通过SFGAP本端实体和感知gNodeB完成链路建立，并实现感知gNodeB接入到AMF。一个SFGAP本端实体可引用一个SCTP本端实体组，一个SCTP本端实体组下最多可配置32个SCTP本端实体。

## 注意事项

- 该命令执行后立即生效。

- 系统中配置多个SFGAP本端实体时，用户接入哪个SFGAP端点由无线侧决定，AMF不做强制选择。
- 添加SFGAP本端实体引用SCTP本端实体组时需要检查该SCTP本端实体组下是否添加SCTP本端实体，如果未添加不允许引用。
- 同一个SCTP本端实体组不能同时被ADD SFGAPLE和ADD NGAPLE引用。

- 最多可输入32条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SFGAPLEIDX | SFGAP本端实体索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定SFGAP本端实体的索引，该索引作为SFGAP本端实体的唯一标识。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~1023。<br>默认值：无<br>配置原则：无 |
| SCTPGROUPID | SCTP本端实体组标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定SFGAP本端实体引用的SCTP本端实体组索引，一个SFGAP本端实体最多可引用32个SCTP本端实体。该本端实体组索引下最多配置32个本端实体。通过ADD SCTPLEGRP配置SCTP本端实体组。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~255。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SFGAPLE]] · SFGAP本端实体（SFGAPLE）

## 使用实例

若运营商要配置一个SFGAP本端实体，SFGAP本端实体索引为1，SCTP本端实体组标识为1，可以用如下命令：

```
ADD SFGAPLE: SFGAPLEIDX=1, SCTPGROUPID=1;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加SFGAP本端实体（ADD-SFGAPLE）_75822964.md`
