---
id: UNC@20.15.2@MMLCommand@SET FLOWCTRLQUE
type: MMLCommand
name: SET FLOWCTRLQUE（设置流控队列信息）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: FLOWCTRLQUE
command_category: 配置类
applicable_nf:
- SGSN
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 操作维护
- 设备管理
- 流控管理
- 系统流控队列管理
status: active
---

# SET FLOWCTRLQUE（设置流控队列信息）

## 功能

**适用网元：SGSN、MME**

该命令用于设置不同业务类型的流控队列信息。

## 注意事项

- 系统初次运行时，会执行系统初始设置值。
- 设置流控参数，设置不当会导致流控丢包，影响系统业务成功率。
- 此命令需要华为技术支持人员指导下才能执行，请慎重使用。

## 权限

manage-ug;system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APPTYPE | 业务类型 | 可选必选说明： 必选参数<br>参数含义：该参数用于指定业务类型。<br>数据来源：整网规划<br>取值范围：<br>- “APP_2G(2G)”：表示2G业务类型。<br>- “APP_3G(3G)”：表示3G业务类型。<br>- “APP_4G(4G)”：表示4G业务类型。<br>系统初始设置值：见表1 |
| MSG2GTYPE | 2G消息类型 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定2G消息类型。<br>前提条件：该参数在<br>“业务类型”<br>参数配置为<br>“APP_2G(2G)”<br>后生效。<br>数据来源：整网规划<br>取值范围：<br>- “ATTACH(ATTACH)”：表示附着消息。<br>- “RAU(RAU)”：表示路由区更新消息。<br>- “PDP_ACT(PDP_ACT)”：表示激活消息。<br>系统初始设置值：见表1 |
| MSG3GTYPE | 3G消息类型 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定3G消息类型。<br>前提条件：该参数在<br>“业务类型”<br>参数配置为<br>“APP_3G(3G)”<br>后生效。<br>数据来源：整网规划<br>取值范围：<br>- “ATTACH(ATTACH)”：表示附着消息。<br>- “RAU(RAU)”：表示路由区更新消息。<br>- “PDP_ACT(PDP_ACT)”：表示激活消息。<br>- “SERVICE_REQ(SERVICE_REQ)”：表示服务请求消息。<br>系统初始设置值：见表1 |
| MSG4GTYPE | 4G消息类型 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定4G消息类型。<br>前提条件：该参数在<br>“业务类型”<br>参数配置为<br>“APP_4G(4G)”<br>后生效。<br>数据来源：整网规划<br>取值范围：<br>- “ATTACH(ATTACH)”：表示附着消息。<br>- “TAU(TAU)”：表示跟踪区更新消息。<br>- “SERVICE_REQ(SERVICE_REQ)”：表示服务请求消息。<br>- “ENCRYPT(ENCRYPT)”：表示加密消息。<br>- “EMM_VIP(EMM_VIP)”：表示VIP消息。<br>- “EMM_EMGC(EMM_EMGC)”：表示紧急呼叫消息。<br>- “EMM_VOICE(EMM_VOICE)”：表示4G语音消息。<br>系统初始设置值：见表1 |
| WEIGHT | 业务权重 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定业务权重。<br>前提条件：<br>- 该参数在“业务类型”参数配置为“APP_2G(2G)”后生效。<br>- 该参数在“业务类型”参数配置为“APP_3G(3G)”后生效。<br>- 该参数在“业务类型”参数配置为“APP_4G(4G)”后生效。<br>数据来源：整网规划<br>取值范围：0-100<br>系统初始设置值：见表1<br>配置原则：推荐系统初始设置值，如需修改，请联系华为技术支持。<br>说明：此配置决定了流控消息队列每个调度周期的调度次数，数值越大表示被调度的次数越多。 |
| QUELENTH | 队列期望长度 | 可选必选说明：条件必选参数<br>参数含义：队列期望长度指不同业务类型流控消息队列的期望长度。该参数用于指定队列期望长度。<br>前提条件：<br>- 该参数在“业务类型”参数配置为“APP_2G(2G)”后生效。<br>- 该参数在“业务类型”参数配置为“APP_3G(3G)”后生效。<br>- 该参数在“业务类型”参数配置为“APP_4G(4G)”后生效。<br>数据来源：整网规划<br>取值范围：0-10000<br>系统初始设置值：见表1<br>配置原则：推荐系统初始设置值，如需修改，请联系华为技术支持。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/FLOWCTRLQUE]] · 流控队列信息（FLOWCTRLQUE）

## 使用实例

设置流控队列信息，业务类型为2G，消息类型为附着，业务权重数为2，队列期望长度是400：

SET FLOWCTRLQUE: APPTYPE=APP_2G, MSG2GTYPE=ATTACH, WEIGHT=2, QUELENTH=400;

推荐系统初始设置值，如需修改，请联系华为技术支持。

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-FLOWCTRLQUE.md`
