---
id: UNC@20.15.2@MMLCommand@RMV PGWGROUP
type: MMLCommand
name: RMV PGWGROUP（删除P-GW组）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: PGWGROUP
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
- P-GW信息管理
- P-GW组管理
status: active
---

# RMV PGWGROUP（删除P-GW组）

## 功能

**适用网元：SGSN、MME**

该命令用于删除P-GW组。

## 注意事项

- 该命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GRPID | P-GW组号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定P-GW组号。<br>数据来源：本端规划<br>取值范围：0～15<br>默认值：无<br>说明：- 当[**SET PGWBACKOFF**](../../../../操作维护/设备管理/流控管理/业务流控管理/P-GW Backoff流控管理/设置P-GW Back-off流控参数(SET PGWBACKOFF)_72345761.md)命令开启时，不能删除[**SET PGWBACKOFF**](../../../../操作维护/设备管理/流控管理/业务流控管理/P-GW Backoff流控管理/设置P-GW Back-off流控参数(SET PGWBACKOFF)_72345761.md)命令中配置的P-GW组号。<br>- 不能删除[**ADD PGWNODE**](../P-GW节点管理/增加P-GW局向(ADD PGWNODE)_72225387.md)命令中配置的P-GW组号。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PGWGROUP]] · P-GW组（PGWGROUP）

## 使用实例

删除组号为“2”的P-GW组号，则设置“P-GW组号”参数为“2”。运行如下命令：

RMV PGWGROUP: GRPID=2;

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-PGWGROUP.md`
