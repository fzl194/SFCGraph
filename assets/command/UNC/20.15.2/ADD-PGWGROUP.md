---
id: UNC@20.15.2@MMLCommand@ADD PGWGROUP
type: MMLCommand
name: ADD PGWGROUP（增加P-GW组）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: PGWGROUP
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
- P-GW信息管理
- P-GW组管理
status: active
---

# ADD PGWGROUP（增加P-GW组）

## 功能

**适用网元：SGSN、MME**

该命令用于增加P-GW组。使用P-GW组是更精细化的管理P-GW局向。MME支持基于P-GW Back-off timer的APN级流控功能会使用到本命令。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为16。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GRPID | P-GW组号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定P-GW组号。<br>数据来源：本端规划<br>取值范围：0～15<br>默认值：无 |
| DESC | 描述 | 可选必选说明：可选参数<br>参数含义：该参数用于P-GW组描述信息。<br>数据来源：本端规划<br>取值范围：0～256位字符串<br>默认值：noname |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PGWGROUP]] · P-GW组（PGWGROUP）

## 使用实例

运营商希望增加新的组号为2的P-GW组号来管理P-GW局向，描述为“M2M P-GW Group”，则设置“P-GW组号”参数为“2”、“描述”参数为“M2M P-GW Group”。运行如下命令：

ADD PGWGROUP: GRPID=2, DESC="M2M P-GW Group";

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加P-GW组(ADD-PGWGROUP)_72225385.md`
