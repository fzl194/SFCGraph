---
id: UNC@20.15.2@MMLCommand@ADD AREAGP
type: MMLCommand
name: ADD AREAGP（增加区域群）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: AREAGP
command_category: 配置类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
max_records: 50
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 移动性管理
- 区域漫游限制管理
- 区域群管理
status: active
---

# ADD AREAGP（增加区域群）

## 功能

**适用网元：SGSN、MME**

此命令用于增加区域群记录，为区域群成员提供区域群标识，同一个区域群中的成员具有相同的接入控制策略。

如果需要对多个区域采用相同的接入控制策略时，需要执行此命令。

## 注意事项

- 此命令最大记录数为50。
- 此命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| AREAID | 区域群标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定区域群标识。<br>数据来源：整网规划<br>取值范围：1~50<br>默认值：无 |
| AREAN | 区域群名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定区域群名称。<br>数据来源：整网规划<br>取值范围：1~32位字符串<br>默认值：<br>“noname” |

## 操作的配置对象

- [区域群（AREAGP）](configobject/UNC/20.15.2/AREAGP.md)

## 使用实例

增加一条区域群标识为1的区域群记录：

ADD AREAGP: AREAID = 1;

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加区域群(ADD-AREAGP)_26145542.md`
