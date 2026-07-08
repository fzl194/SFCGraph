---
id: UNC@20.15.2@MMLCommand@ADD APNNIGROUP
type: MMLCommand
name: ADD APNNIGROUP（增加APNNI组）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: APNNIGROUP
command_category: 配置类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
max_records: 16
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- 会话管理
- APNNI信息管理
- APNNI组管理
status: active
---

# ADD APNNIGROUP（增加APNNI组）

## 功能

**适用网元：SGSN、MME**

该命令用于增加APNNI组信息。关联了该组的APNNI可以被基于延迟定时器的信令拥塞控制特性和Non-IP数据传输特性使用。

## 注意事项

- 此命令执行后立即生效。
- 该命令最大记录数为16。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GRPID | APNNI组号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定APNNI组号。<br>数据来源：本端规划<br>取值范围：0～15<br>默认值：无 |
| DESC | 描述 | 可选必选说明：可选参数<br>参数含义：APNNI描述信息。<br>数据来源：本端规划<br>取值范围：0～256位字符串<br>默认值：noname |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@APNNIGROUP]] · APNNI组（APNNIGROUP）

## 使用实例

运营商希望增加新的组号为2的APNNI组来管理APNNI成员信息，描述为“M2M APNNI Group”，则设置“APNNI组号”参数为“2”、“描述”参数为“M2M APNNI Group”。运行如下命令：

ADD APNNIGROUP: GRPID=2, DESC="M2M APNNI Group";

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-APNNIGROUP.md`
