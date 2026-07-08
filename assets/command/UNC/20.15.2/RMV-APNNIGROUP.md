---
id: UNC@20.15.2@MMLCommand@RMV APNNIGROUP
type: MMLCommand
name: RMV APNNIGROUP（删除APNNI组）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: APNNIGROUP
command_category: 配置类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
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

# RMV APNNIGROUP（删除APNNI组）

## 功能

**适用网元：SGSN、MME**

该命令用于删除APNNI组信息。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GRPID | APNNI组号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定APNNI组号。<br>数据来源：本端规划<br>取值范围：0～15<br>默认值：无<br>说明：- 当[**SET PGWBACKOFF**](../../../../操作维护/设备管理/流控管理/业务流控管理/P-GW Backoff流控管理/设置P-GW Back-off流控参数(SET PGWBACKOFF)_72345761.md)命令开启时，不能删除[**SET PGWBACKOFF**](../../../../操作维护/设备管理/流控管理/业务流控管理/P-GW Backoff流控管理/设置P-GW Back-off流控参数(SET PGWBACKOFF)_72345761.md)命令中配置的APNNI组号。<br>- 不能删除[**ADD APNNI**](../APNNI管理/增加APNNI(ADD APNNI)_26305506.md)命令中配置的APNNI组号。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@APNNIGROUP]] · APNNI组（APNNIGROUP）

## 使用实例

删除组号为“2”的APNNI组号，则设置“APNNI组号”参数为“2”。运行如下命令：

RMV APNNIGROUP: GRPID=2;

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-APNNIGROUP.md`
