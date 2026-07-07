# 命令证据包：SET RGRESCTRL
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/RG资源控制/设置RG资源控制配置（SET RGRESCTRL）_96243210.md`
> 用该命令的特性数：1

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：PGW-C、SMF**

该命令用于设置RG老化功能以及RG超出规格后的处理动作。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。

- RG老化时长是通过业务级QHT下发到UDG。
- 根据UDG上报业务QHT时，决策是否进行RG老化。
- 配置Gy接口携带流量计费信息时（ADD DCCTEMPLATE下使能QUOTATOTAL开关），RG老化功能不生效。
- 配置Gy接口携带流量计费信息时（ADD DCCTEMPLATE下使能PRIVATEATTR开关），RG老化功能不生效。
- 使用RG老化功

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| ONLRGAGESW | 在线计费RG老化控制 | local_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST RGRE | <br>- “DISABLE（不使能）”：RG老化功能不使能 |
| ONLAGETIMER | 在线计费RG老化时长 (分) | local_planned | conditional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST RGRE | 整数类型，取值范围是0，10~1440，单位是分钟。 |
| ONLBLKTIMER | 在线计费全局业务阻塞处理时间间隔 (分) | local_planned | conditional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST RGRE | 整数类型，取值范围是0，10~1440，单位是分钟。 |
| OFLRGAGESW | 离线计费RG老化控制 | local_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST RGRE | <br>- “DISABLE（不使能）”：RG老化功能不使能 |
| OFLAGETIMER | 离线计费RG老化时长 (分) | local_planned | conditional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST RGRE | 整数类型，取值范围是0，10~1440，单位是分钟。 |
| EXCSRVLMTACT | 超出业务最大规格处理动作 | local_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST RGRE | <br>- “BLOCK（阻塞对应业务）”：阻塞对应业务 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-011206

**md：`WSFD-011206/配置SMF与CHF交互的条件和内容_93420840.md`**
- 数据规划表（该命令的参数行）：
  | ****SET RGRESCTRL**** | 在线计费RG老化控制（ONLRGAGESW） | ENABLE | 本端规划 | 控制在线计费RG老化功能。 |
  | ****SET RGRESCTRL**** | 在线计费RG老化时长 (分)（ONLAGETIMER） | 20 | 本端规划 | 控制在线计费RG老化时长。 |
  | ****SET RGRESCTRL**** | 在线计费全局业务阻塞处理时间间隔 (分)（ONLBLKTIMER） | 0 | 本端规划 | 配置全局业务阻塞或重定向的时长，从阻塞或重定向开始经过这段时间以后，进行RG老化。<br>当配置为0时，表示阻塞时长无效。 |
  | ****SET RGRESCTRL**** | 离线计费RG老化控制（OFLRGAGESW） | ENABLE | 本端规划 | 控制离线计费RG老化功能。 |
  | ****SET RGRESCTRL**** | 离线计费RG老化时长 (分)（OFLAGETIMER） | 20 | 本端规划 | 控制离线计费RG老化时长。 |
- 任务示例脚本（该命令行）：
  `SET RGRESCTRL: ONLRGAGESW=ENABLE,ONLAGETIMER=20,ONLBLKTIMER=0,OFLRGAGESW=ENABLE,OFLAGETIMER=20;`
- 操作步骤上下文（±2 行原文）：
  L87:
    >       **ADD RGTRIGGER**
    > 4. 配置RG老化功能。
    >   ****SET RGRESCTRL****
    >   > **说明**
    >   > 终端用户访问业务匹配到某个RG后，即使后续不再访问该业务，用户更新或时间流量阈值等场景触发向CHF上报用量时，会上报该RG的用量且用量为零，用户长时间在线会造成N40接口的消息变大，同时造成RG及URR等资源浪费。QHT功能可以删除已停止访问业务的RG，但该功能依赖于CHF配合下发QHT Trigger。通过 ****SET RGRESCTRL**** 命令配置RG老化时长，可以保证在QHT功能不使能或QHT使能但QHT值为0场景下，保证已停止访问业务的RG老化，携带Trigger类型为Final，避免大量RG在线造成消息过大。
  L89:
    >   ****SET RGRESCTRL****
    >   > **说明**
    >   > 终端用户访问业务匹配到某个RG后，即使后续不再访问该业务，用户更新或时间流量阈值等场景触发向CHF上报用量时，会上报该RG的用量且用量为零，用户长时间在线会造成N40接口的消息变大，同时造成RG及URR等资源浪费。QHT功能可以删除已停止访问业务的RG，但该功能依赖于CHF配合下发QHT Trigger。通过 ****SET RGRESCTRL**** 命令配置RG老化时长，可以保证在QHT功能不使能或QHT使能但QHT值为0场景下，保证已停止访问业务的RG老化，携带Trigger类型为Final，避免大量RG在线造成消息过大。
    > 
    > ## [任务示例](#ZH-CN_OPI_0193420840)
  L135:
    > 
    > ```
    > SET RGRESCTRL: ONLRGAGESW=ENABLE,ONLAGETIMER=20,ONLBLKTIMER=0,OFLRGAGESW=ENABLE,OFLAGETIMER=20;
    > ```

## ④ 自动比对
- 命令真相参数（6）：['EXCSRVLMTACT', 'OFLAGETIMER', 'OFLRGAGESW', 'ONLAGETIMER', 'ONLBLKTIMER', 'ONLRGAGESW']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'本端规划': 5}（多值→atom 应考虑 decision_driven）
