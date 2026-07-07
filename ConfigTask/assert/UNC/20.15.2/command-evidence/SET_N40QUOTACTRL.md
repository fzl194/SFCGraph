# 命令证据包：SET N40QUOTACTRL
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/全局配置/设置N40接口配额的控制参数（SET N40QUOTACTRL）_96805505.md`
> 用该命令的特性数：1

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：PGW-C、SMF**

该命令用来控制N40接口配额的控制参数。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| ZEROQUOTAACT | ZEROTIMEQTACT | BLKTIMER | ONLMETERINGTYPE | TCMODE |
| --- | --- | --- | --- | --- |
| NORMAL | TERMINATE | 0 | DEFAULT | DEFAULT |

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| ZEROQUOTAACT | CHF下发零配额的动作 | local_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST N40Q | <br>- “NORMAL（正常处理）”：按正常配额处理，下发零配额给UPF。 |
| ZEROTIMEQTACT | CHF下发零时长配额的动作 | local_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST N40Q | <br>- “TERMINATE（去活会话）”：去活PDU会话。 |
| BLKTIMER | RG级阻塞处理时间间隔(分钟) | global_planned | conditional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST N40Q | 整数类型，取值范围是0~1440。 |
| ONLMETERINGTYPE | 在线计费上报统计类型 | global_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST N40Q | <br>- “DEFAULT（缺省）”：按GrantedUnit下发的配额类型上报给CHF。 |
| TCMODE | 费率切换模式 | local_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST N40Q | <br>- “DEFAULT（缺省）”：费率切换发生的时间点按费率切换配置（ADD TARIFFGR |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-011206

**md：`WSFD-011206/配置费率切换_86411191.md`**
- 数据规划表（该命令的参数行）：
  | **SET N40QUOTACTRL** | 费率切换模式（TCMODE） | DEFAULT | 本端规划 | 费率切换发生的时间点按照<br>**ADD TARIFFGROUP**<br>命令配置的费率切换生效。 |
- 任务示例脚本（该命令行）：
  `SET N40QUOTACTRL: TCMODE=DEFAULT;`
- 操作步骤上下文（±2 行原文）：
  L66:
    >       **ADD TARIFFGROUP**
    >     d. **可选** ：配置费率切换模式。
    >       **SET N40QUOTACTRL**
    >       > **说明**
    >       > - 当“TCMODE”参数配置为“DEFAULT”时，表示费率切换发生的时间点按照**ADD TARIFFGROUP**命令配置的费率切换生效。
  L127:
    >   //配置费率切换模式。
    >   ```
    >   SET N40QUOTACTRL: TCMODE=DEFAULT;
    >   ```
    > 2. 配置全局的费率切换组。

## ④ 自动比对
- 命令真相参数（5）：['BLKTIMER', 'ONLMETERINGTYPE', 'TCMODE', 'ZEROQUOTAACT', 'ZEROTIMEQTACT']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'本端规划': 1}（多值→atom 应考虑 decision_driven）
