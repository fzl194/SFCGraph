---
id: UNC@20.15.2@MMLCommand@ADD RESULTCODESCP
type: MMLCommand
name: ADD RESULTCODESCP（增加配置MODELC/D组网的SCP原因码控制）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: RESULTCODESCP
command_category: 配置类
applicable_nf:
- SMF
- PGW-C
- GGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- PCC管理
- 信令控制
- 返回码控制
status: active
---

# ADD RESULTCODESCP（增加配置MODELC/D组网的SCP原因码控制）

## 功能

**适用NF：SMF、PGW-C、GGSN**

此命令用来配置当UNC收到指定组网场景结果码信息后执行何种操作。例如关闭PCC功能、执行缺省动作、执行宕机备份等。

## 注意事项

- 该命令执行后立即生效。

- SCP返回异常码场景，该配置命令优先级高于ADD RESULTCODECTRL。
- 当PCCTEMPLATE配置为“global”时，表示全局配置，最多能配置100条记录；当PCCTEMPLATE配置为指定PCC模板时，表示该PCC模板下的配置，最多能配置100条记录。

- 最多可输入1100条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PCCTEMPLATE | PCC模板名称 | 可选必选说明：必选参数<br>参数含义：该参数用于设置该返回码所绑定的PCC模板。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。<br>默认值：无<br>配置原则：<br>如果配置为“global”则表示全局配置。<br>如果配置为非“global”，则必须是已经通过ADD PCCTEMPLATE配置过的PCC模板名称。 |
| MODELTYPE | 组网场景 | 可选必选说明：必选参数<br>参数含义：该参数用于设置该返回码所应用的组网场景。<br>数据来源：本端规划<br>取值范围：<br>- “MODELC（组网场景为ModelC）”：组网场景为ModelC<br>- “MODELD（组网场景为ModelD）”：组网场景为ModelD。<br>- “MODELC_D（组网场景为ModelC和ModelD）”：组网场景为ModelC和ModelD。<br>默认值：无<br>配置原则：无 |
| N7RESULTCODEVAL | N7返回码 | 可选必选说明：必选参数<br>参数含义：本参数用于配置N7返回码。<br>数据来源：对端协商<br>取值范围：字符串类型，输入长度范围是1~3。300-599中的一个值或者3xx、4xx、5xx，不区分大小写。其中xx代表一个范围，例如3xx代表300~399。<br>默认值：无<br>配置原则：<br>配置的单个的返回码落在一个范围内时，单个的优先级高。 |
| ERRINFO | 故障码对应的Protocol or application Error信息 | 可选必选说明：必选参数<br>参数含义：该参数用于指定自定义的故障码对应的Protocol or application Error信息。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~128。如果配置为星号（*），表示通配，对该异常码携带所有Protocol or application Error信息都生效。参考3GPP协议29.500的Protocol or application Error。<br>默认值：无<br>配置原则：<br>（1）该参数只能由字母（A-Z或者a-z）、数字（0-9）、下划线（_）、星号（*）组成。该参数不区分大小写。<br>（2）配置为“*”，表示该异常码动作对于所有的Protocol or application Error信息都生效。 |
| INITACTION | Initial流程处理动作 | 可选必选说明：可选参数<br>参数含义：该参数用于控制激活响应消息中携带该返回码的行为。<br>数据来源：本端规划<br>取值范围：<br>- “DEFAULT（缺省动作）”：缺省动作。<br>- “FAILOVER（宕机备份）”：宕机备份。<br>- “TERMINATE（去活会话）”：去活会话。<br>- “LOCALPCC（回滚为本地PCC用户使用本地策略）”：回滚为本地PCC用户使用本地策略。<br>- “INHERIT（继承全局动作）”：继承全局动作。<br>默认值：无<br>配置原则：<br>- 当PCCTEMPLATE配置为“global”且未配置该参数时，默认值为DEFAULT。当PCCTEMPLATE配置为指定PCC模板且未配置该参数时，默认值为INHERIT。<br>- 当此参数配置为DEFAULT时，则沿用ADD RESULTCODECTRL和SET PCCFAILACTION配置综合决策的动作。 |
| INITHOLDTMSW | Initial流程回滚后使能Holding-Time | 可选必选说明：该参数在"INITACTION"配置为"LOCALPCC"时为条件可选参数。<br>参数含义：该参数用于设置激活响应控制的行为生效时是否根据holding-time设置时长保活用户，并在holding-time超时后去活用户。<br>数据来源：本端规划<br>取值范围：<br>- “DISABLE（不使能）”：不使能。<br>- “ENABLE（使能）”：使能。<br>默认值：无<br>配置原则：无 |
| UPDATEACTION | Update流程处理动作 | 可选必选说明：可选参数<br>参数含义：该参数用于控制更新响应消息中携带该返回码的行为。<br>数据来源：本端规划<br>取值范围：<br>- “FAILOVER（宕机备份）”：宕机备份。<br>- “TERMINATE（去活会话）”：去活会话。<br>- “LOCALPCC（回滚为本地PCC用户使用本地策略）”：回滚为本地PCC用户使用本地策略<br>- “INHERIT_PCC（回滚为本地PCC用户继续使用PCRF策略）”：回滚为本地PCC用户继续使用PCRF策略。<br>- “CONTINUE（继续N7会话）”：继续N7会话。<br>- “INHERIT（继承全局动作）”：继承全局动作。<br>默认值：无<br>配置原则：<br>当PCCTEMPLATE配置为“global”且未配置该参数时，默认值为CONTINUE。当PCCTEMPLATE配置为指定PCC模板且未配置该参数时，默认值为INHERIT。 |
| UPDHOLDTMSW | Update流程回滚后使能Holding-Time | 可选必选说明：该参数在"UPDATEACTION"配置为"INHERIT_PCC"、"LOCALPCC"时为条件可选参数。<br>参数含义：该参数用于设置更新响应控制的行为生效时是否根据holding-time设置时长保活用户，并在holding-time超时后去活用户。<br>数据来源：本端规划<br>取值范围：<br>- “DISABLE（不使能）”：不使能。<br>- “ENABLE（使能）”：使能。<br>默认值：无<br>配置原则：无 |
| TERMINACTION | Terminate流程处理动作 | 可选必选说明：可选参数<br>参数含义：该参数用于控制删除响应消息中携带该返回码的行为。<br>数据来源：本端规划<br>取值范围：<br>- “DEFAULT（缺省动作）”：缺省动作。<br>- “FAILOVER（宕机备份）”：宕机备份。<br>- “INHERIT（继承全局动作）”：继承全局动作。<br>默认值：无<br>配置原则：<br>- 当PCCTEMPLATE配置为“global”且未配置该参数时，默认值为DEFAULT。当PCCTEMPLATE配置为指定PCC模板且未配置该参数时，默认值为INHERIT。<br>- 当此参数配置为DEFAULT时，去活用户。 |
| REACTREQ | 重新激活请求 | 可选必选说明：该参数在"UPDATEACTION"配置为"TERMINATE"时为条件可选参数。<br>参数含义：该参数用于指示当用户因异常结果码被去活时，UNC是否通知用户重新激活。<br>数据来源：本端规划<br>取值范围：<br>- “DISABLE（不使能）”：不使能。<br>- “ENABLE（使能）”：使能。<br>- “DEFAULT（缺省取值）”：缺省取值，对5002结果码其作用等同于ENABLE，对非5002结果码其作用等同于DISABLE。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@RESULTCODESCP]] · 配置MODELC/D组网的SCP原因码控制（RESULTCODESCP）

## 使用实例

- 添加全局RESULTCODESCP返回码控制信息，对ModelC组网更新响应消息中“N7RESULTCODEVAL”为“5xx”的消息执行FAILOVER动作：
  ```
  ADD RESULTCODESCP:PCCTEMPLATE="global",MODELTYPE=MODELC,N7RESULTCODEVAL="5xx",ERRINFO="*",INITACTION=DEFAULT,UPDATEACTION=FAILOVER;
  ```
- 为PCC模板“pcctemplate”添加RESULTCODESCP返回码控制信息，对ModelC组网更新响应消息中“N7RESULTCODEVAL”为5xx的消息执行FAILOVER动作：
  ```
  ADD RESULTCODESCP:PCCTEMPLATE="pcctemplate",MODELTYPE=MODELC,N7RESULTCODEVAL="5xx",ERRINFO="*",INITACTION=DEFAULT,UPDATEACTION=FAILOVER;
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-RESULTCODESCP.md`
