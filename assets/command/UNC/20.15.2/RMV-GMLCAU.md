---
id: UNC@20.15.2@MMLCommand@RMV GMLCAU
type: MMLCommand
name: RMV GMLCAU（删除GMLC权限配置）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: GMLCAU
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- LCS
- GMLC权限配置
status: active
---

# RMV GMLCAU（删除GMLC权限配置）

## 功能

**适用网元：MME**

此命令用于删除GMLC权限配置。

## 注意事项

- 此命令执行后立即生效。
- 如果只输入GMLCID，则删除指定GMLC标识的所有记录。
- 如果只输入GMLCID与CLTTYPE，则删除指定GMLC标识与客户端类型的所有记录。
- 如果输入GMLCID、CLTTYPE、SERTYPE，则删除指定的GMLCID、客户端类型与LCS业务类型的记录。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GMLCID | GMLC 标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定GMLC标识。<br>取值范围：0～639<br>默认值 ：无 |
| CLTTYPE | 支持的客户端类型 | 可选必选说明：可选参数<br>参数含义：该参数用于标识客户端（LCS Client）类型。<br>取值范围：<br>- “EMERGENCY_SERVICES（紧急业务）”<br>- “VALUE_ADDED_SERVICES（增值业务）”<br>- “PLMN_OPERATOR_SERVICES（运营商业务）”<br>- “LAWFUL_INTERCEPT_SERVICES（合法定位）”<br>默认值 ：无 |
| SERTYPE | 支持的LCS业务类型 | 可选必选说明：条件可选参数<br>参数含义：该参数用于标识LCS Client的指定定位业务。<br>前提条件：该参数在<br>“支持的客户端类型”<br>输入时本参数有效。<br>取值范围： 0～127<br>默认值 ：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/GMLCAU]] · GMLC权限配置（GMLCAU）

## 使用实例

删除一条 “GMLC 标识” 为 “1” ， “支持的客户端类型” 为 “VALUE_ADDED_SERVICES（增值业务）” ， “支持的LCS业务类型” 为 “3” 的GMLC权限配置记录：

RMV GMLCAU: GMLCID=1, CLTTYPE=VALUE_ADDED_SERVICES,SERTYPE=3;

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-GMLCAU.md`
