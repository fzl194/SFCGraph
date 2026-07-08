---
id: UNC@20.15.2@MMLCommand@SET RESTOFUNC
type: MMLCommand
name: SET RESTOFUNC（设置容灾功能）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: RESTOFUNC
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 网络管理
- MME容灾管理
- 容灾功能管理
status: active
---

# SET RESTOFUNC（设置容灾功能）

## 功能

**适用网元：MME**

本命令用于控制设备容灾功能的运行方式，以及业务恢复流程的方式。

## 注意事项

- 该命令执行后立即生效。
- “WSFD-201201MME链式备份”特性正式启用时，“容灾功能运行模式”参数应设置为“运行模式”。
- “容灾功能运行模式”参数从“调测模式”改为“运行模式”，应先删除[**ADD RESTOUSR**](../容灾用户特征管理/增加容灾用户特征参数(ADD RESTOUSR)_26305926.md)记录。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SRESTOM | 业务恢复模式 | 可选必选说明：可选参数<br>参数含义：本参数用于控制设备故障后，备份用户的Service Request、Intra TAU流程，或者pool内的inter TAU流程是通过容灾设备无损恢复，还是通过重新附着接入网络。<br>数据来源：本端规划<br>取值范围：<br>- “BRIEF_RESTO(二次呼叫恢复)”<br>- “FULL_RESTO(一次呼叫恢复)”<br>系统初始设置值：FULL_RESTO(一次呼叫恢复)<br>配置原则：<br>- 若选择“一次呼叫恢复”，备份用户的Service Request、Intra TAU流程，或者pool内的inter TAU流程通过容灾设备无损恢复。<br>- 若选择“二次呼叫恢复”，备份用户的Service Request、Intra TAU流程，或者pool内的inter TAU流程通过重新附着接入网络。 |
| RESTOWORK | 容灾功能运行模式 | 可选必选说明：可选参数<br>参数含义：本参数用于控制“WSFD-<br>201201<br>MME链式备份”特性启用后，链式备份功能服务的用户范围。<br>数据来源：本端规划<br>取值范围：<br>- “VALIDATE(调测模式)”<br>- “NORMAL(运行模式)”<br>系统初始设置值：VALIDATE(调测模式)<br>配置原则：<br>- 若选择“调测模式”，链式备份功能服务的用户范围仅限于[**ADD RESTOUSR**](../容灾用户特征管理/增加容灾用户特征参数(ADD RESTOUSR)_26305926.md)设定的“IMSI前缀”的用户范围。<br>- 若选择“运行模式”，链式备份功能服务面向所有用户范围。<br>- “WSFD-201201MME链式备份”特性正式启用时，本参数应设置为“运行模式”。 |
| DULR | HSS注册策略 | 可选必选说明：可选参数<br>参数含义：本参数用于控制Service Request（或TAU Request）流程触发用户在新的USN上恢复接入（非attach方式）时，是否立即发起Update Location流程在HSS上注册新的位置。启用“WSFD-<br>201201<br>MME链式备份”特性后，若USN故障或S1-MME链路故障，用户发起Service Request（或TAU Request）将触发在新的USN上恢复接入，无需重新attach。若启用“WSFD-<br>201202<br>本地VLR”特性后，用户在新的USN上恢复接入时，用户的签约数据从备份USN上获取。由于用户接入的USN发生了变更，新的USN需发起Update Location流程在HSS上注册新的位置，而用户发起Service Request流程的忙时话务模型比较高，Update Location流程可能会造成HSS拥塞。<br>数据来源：本端规划<br>取值范围：<br>- “IMMEDIATELY(立即更新位置)”<br>- “DELAY(延迟更新位置)”<br>系统初始设置值：<br>“IMMEDIATELY(立即更新位置)”<br>配置原则：<br>- 若选择“IMMEDIATELY(立即更新位置)”，新的USN需在恢复接入时发起Update Location流程。<br>- 若选择“DELAY(延迟更新位置)”，新的USN在恢复接入时不发起Update Location流程，而是延迟一段时间再发起Update Location流程，减缓突发的Update Location对HSS产生的冲击。<br>说明：- 若参数设为“DELAY(延迟更新位置)”，恢复用户的Homogeneous Support of IMS Voice Over PS Sessions、UE SRVCC Capability或Visited PLMN ID发生变更，USN将在恢复流程中立即发起Update Location流程，不做延迟处理。<br>- 若参数设为“DELAY(延迟更新位置)”，USN未完成新接入用户的Update Location流程之前，对应接入用户的VoLTE被叫流程由旧侧备份USN的备份数据完成恢复流程，VoLTE被叫流程不受影响。USN未完成新接入用户的Update Location流程之前，HSS发起的签约数据变更流程不会被处理，需等待Update Location流程之后获取新的签约数据。 |
| CHECKSCOPE | 恢复用户的合法性校验范围 | 可选必选说明：可选参数<br>参数含义：本参数用于设置NAS Count校验范围以控制是否允许用户通过Service Request（或TAU Request）流程在新的MME上恢复业务。<br>启用“WSFD-<br>201201<br>MME链式备份”特性后，Service Request/TAU触发的恢复流程中，新的MME从备份MME获取用户备份信息后，校验Service Request（或TAU Request）的Uplink NAS Count。<br>假设用户的备份上下文中Uplink NAS Count值为A，用户发起Service Request（或TAU Request）的Uplink NAS Count值为B，X为本参数设定值，当[A+1]<=B<=[A+1+X]时，NAS Count合法性校验通过，用户通过恢复流程恢复业务；否则，恢复失败，用户需重新attach后才能进行业务。<br>数据来源：本端规划<br>取值范围：0～10<br>系统初始设置值：0<br>配置原则：<br>NAS Count校验能够减少恢复的用户上下文信息与周边网元、终端信息的不一致性的比例。本参数的取值越小，检验越严格，出现恢复前后用户信息不一致的比例越小。本参数的取值越大，校验越宽松，出现恢复前后用户信息不一致的比例越大。在某些情况下，例如MME进入流控状态，用户可能尝试多次Service Request流程，进而NAS Count不停累加，超出校验范围，用户恢复业务失败。因此在这些情况下，本参数取值越小，能够通过恢复流程恢复业务的用户数可能减少。因此：<br>- 如果在公网内部署，终端的行为比较复杂，权衡正确性和恢复用户数的关系，建议的取值范围是0~4，推荐值为0。<br>- 如果在专网内部署（例如企业、政府部门网络），终端的行为比公网终端简单，建议以恢复用户数的比例作为主要因素，建议取值范围根据恢复用户数的比例调整，推荐配置为5。 |
| RESTOSEG | 号段匹配 | 可选必选说明：可选参数<br>参数含义：本参数用于控制链式备份功能是否仅服务于指定号段的用户。<br>数据来源：本端规划<br>取值范围：<br>- “YES (是)”<br>- “NO (否)”<br>系统初始设置值：“NO (否)”<br>配置原则：<br>- 若选择“YES (是)”，链式备份功能服务的用户范围仅限于[ADD RESTOUSRSEG](../容灾用户号段管理/增加容灾用户号段参数 (ADD RESTOUSRSEG)_10674069.md)设定的用户范围。<br>- 若选择“NO (否)”，链式备份功能服务面向所有用户范围。<br>- 如果“容灾功能运行模式”参数为“VALIDATE(调测模式)”时，调测功能开启，号段匹配功能不生效。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/RESTOFUNC]] · 容灾功能（RESTOFUNC）

## 使用实例

希望开启MME链式备份容灾功能时，执行如下命令：

```
SET RESTOFUNC: SRESTOM=FULL_RESTO, RESTOWORK=VALIDATE;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置容灾功能(SET-RESTOFUNC)_72345713.md`
