# 命令证据包：SET N40MSGSTG
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/融合计费消息缓存/设置缓存开关、回放间隔、回放速率（SET N40MSGSTG）_34667405.md`
> 用该命令的特性数：1

## ② 命令真相（mml_commands.jsonl）
**功能**：![](设置缓存开关、回放间隔、回放速率（SET N40MSGSTG）_34667405.assets/notice_3.0-zh-cn_2.png)

当打开缓存功能后，需要使用命令SET CNVRGDCHGPARA配置参数CHGDATAREFGEN为SMF，即配置生成ChargingDataRef的方法为使用SMF生成，如果使用CHF生成ChargingDataRef时，可能导致放通用户用量丢
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。

- 该命令内的参数具体的生效机制，还需要参考对应的参数说明。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| STGSWITCH | REPLAYINTERVAL | REPLAYRATE | ENCRYPT | STGTXTIMER |
| --- | --- | --- | --- | --- |
| DISABLE | 30 | 500 

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| STGSWITCH | 融合计费消息缓存开关 | global_planned | required | 无。 | <br>- ENABLE（使能） |
| REPLAYINTERVAL | 融合计费消息回放的最小间隔(分钟) | local_planned | conditional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST N40M | 整数类型，取值范围是5~1440，单位是分钟。回放间隔参数修改对应的数值后，需要加锁解锁对应的目录， |
| REPLAYRATE | 融合计费消息回放的速率(个/秒) | local_planned | conditional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST N40M | 整数类型，取值范围是10~10000，单位是个每秒。 |
| ENCRYPT | 加密开关 | local_planned | conditional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST N40M | <br>- ENABLE（使能） |
| STGTXTIMER | 缓存Tx定时器时长(秒) | global_planned | conditional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST N40M | 整数类型，取值范围是0~20，单位是秒。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-011206

**md：`WSFD-011206/WSFD-011206 支持融合计费参考信息_74013176.md`**
- 操作步骤上下文（±2 行原文）：
  L34:
    > - [**SET CTXSTARTRATING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/设置给OCS_CHF发送的消息初始携带的计费属性（SET CTXSTARTRATING）_09897210.md)
    > - [**SET FAILHANDLING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/融合计费模板/设置融合计费模板故障处理动作（SET FAILHANDLING）_09654177.md)
    > - [**SET N40MSGSTG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/融合计费消息缓存/设置缓存开关、回放间隔、回放速率（SET N40MSGSTG）_34667405.md)
    > - [**SET STGTRIGGER**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/融合计费消息缓存/设置融合计费消息缓存期间融合计费消息生成的trigger（SET STGTRIGGER）_34667406.md)
    > 

**md：`WSFD-011206/配置计费消息缓存_31702748.md`**
- 数据规划表（该命令的参数行）：
  | **SET N40MSGSTG** | STGSWITCH（缓存开关） | ENABLE | 固定取值 | 固定配置，开启计费消息缓存功能。 |
  | **SET N40MSGSTG** | REPLAYINTERVAL（回放间隔） | 30 | 本端规划 | 配置缓存消息回放的时间间隔。 |
  | **SET N40MSGSTG** | REPLAYRATE（回放速率） | 500 | 本端规划 | 配置缓存消息回放的速率。 |
- 任务示例脚本（该命令行）：
  `SET N40MSGSTG: STGSWITCH=ENABLE, REPLAYINTERVAL=30, REPLAYRATE=500;`
- 操作步骤上下文（±2 行原文）：
  L59:
    >   **ADD PDUSCACT**
    > - 配置计费消息缓存功能。
    >   **SET N40MSGSTG**
    > - 配置计费消息缓存期间的trigger。
    >   **SET STGTRIGGER**
  L72:
    >   > **说明**
    >   > - **SET STGALARMCTRL**命令的“ALMTHD”参数控制SMF上报**“ALM-81025 话单缓存”**告警的缓存文件占用空间阈值。缓存文件超过该阈值时，上报告警；缓存文件全部被回放后，清除告警。
    >   > - **SET STGALARMCTRL**命令的“MONITORTIME”参数控制告警监控时长，当SMF检查到缓存文件存在且不超过占用空间阈值时，超过告警监控时长后，SMF上报**“ALM-81025 话单缓存”**告警。建议该参数配置为**SET N40MSGSTG**命令配置的融合计费消息回放的最小间隔的2倍以上。
    >   >   如果 “MONITORTIME” 参数配置为0，则告警监控时长受软参 **DWORD507** 控制，该软参用于控制扫描硬盘上缓存文件的周期。
    > - 配置N4接口计费消息相关控制参数。当阈值配置过小，比如流量阈值较低，会导致N4接口频繁上报阈值到，当CHF性能不足响应较慢时，会导致N4接口上报消息堆积，超过最大可缓存的消息规格，用户被去活。该命令主要用于配置SMF在突发和持续高带宽下载场景，用户不被去活。
  L100:
    > 
    > ```
    > SET N40MSGSTG: STGSWITCH=ENABLE, REPLAYINTERVAL=30, REPLAYRATE=500;
    > ```
    > 

**md：`WSFD-011206/调测融合计费的缓存消息回放功能_90005269.md`**
- 操作步骤上下文（±2 行原文）：
  L40:
    >     - [**SET FAILHANDLING**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/融合计费模板/设置融合计费模板故障处理动作（SET FAILHANDLING）_09654177.md)命令“FHACTION”参数配置为“CONTINUE”。
    >     - [**ADD PDUSCACT**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/PDU级结果码处理动作/增加PDU异常返回码动作（ADD PDUSCACT）_09652165.md)命令“SCACT”参数配置为“FAILOVER”或“CONTINUE”。
    >     - [**SET N40MSGSTG**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/融合计费消息缓存/设置缓存开关、回放间隔、回放速率（SET N40MSGSTG）_34667405.md)命令“STGSWITCH”参数配置为“ENABLE”。
    >     - [**SET CNVRGDCHGPARA**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/全局配置/设置融合计费全局参数（SET CNVRGDCHGPARA）_09653056.md)命令“CHGDATAREFGEN”参数配置为“SMF”。
    > 3. 在OM Portal上创建用户跟踪任务。

## ④ 自动比对
- 命令真相参数（5）：['ENCRYPT', 'REPLAYINTERVAL', 'REPLAYRATE', 'STGSWITCH', 'STGTXTIMER']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'固定取值': 1, '本端规划': 2}（多值→atom 应考虑 decision_driven）
