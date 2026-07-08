---
id: UNC@20.15.2@MMLCommand@ADD TAGP
type: MMLCommand
name: ADD TAGP（增加TA群组）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: TAGP
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
max_records: 2048
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 移动性管理
- 跟踪区管理
- 跟踪区群组管理
status: active
---

# ADD TAGP（增加TA群组）

## 功能

**适用网元：MME**

此命令用于增加跟踪区群组记录。跟踪区群组用于定义一组TA组成的区域，以该区域为粒度进行业务策略控制。需要结合 [**ADD TAGPMEM**](../跟踪区群组成员管理/增加TA群组成员(ADD TAGPMEM)_72225263.md) 命令为跟踪区群组添加成员。

## 注意事项

- 此命令最大记录数为2048。
- 此命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TAGPID | 跟踪区群组标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定跟踪区群组标识。<br>数据来源：本端规划<br>取值范围：1～2048<br>默认值：无 |
| TANAME | 跟踪区群组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定跟踪区群组名称。<br>数据来源：本端规划<br>取值范围：0～32位字符串<br>默认值：noname |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@TAGP]] · TA群组（TAGP）

## 使用实例

增加一个TA群组，跟踪区群组标识为1，其群组名称为“shanghai”:

ADD TAGP: TAGPID=1, TANAME="shanghai";

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-TAGP.md`
