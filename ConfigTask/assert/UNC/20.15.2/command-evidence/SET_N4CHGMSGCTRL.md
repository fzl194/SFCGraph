# 命令证据包：SET N4CHGMSGCTRL
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/全局配置/设置N4接口计费消息相关控制参数（SET N4CHGMSGCTRL）_58680359.md`
> 用该命令的特性数：1

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：SMF、PGW-C、GGSN**

该命令用于配置N4接口计费消息相关控制参数。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| MSGCACHEEPDSW | CACHEFULLACT |
| --- | --- |
| DISABLE | TERMINATE |

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| MSGCACHEEPDSW | 消息缓存池扩展开关 | local_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST N4CH | <br>- “DISABLE（不使能）”：关闭消息缓存池扩展功能。 |
| CACHEFULLACT | 缓存池满的动作 | local_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST N4CH | <br>- “CONTINUE（允许业务继续进行）”：允许业务继续进行，不再进行配额管理。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-011206

**md：`WSFD-011206/配置计费消息缓存_31702748.md`**
- 数据规划表（该命令的参数行）：
  | ****SET N4CHGMSGCTRL**** | 消息缓存池扩展开关（MSGCACHEEPDSW） | ENABLE | 本端规划 | 控制单个会话的N4计费消息缓存池满时（20条消息），是否扩展消息缓存池规格到40条消息，最多支持100个会话进行扩展。如果该会话已缓存的N4计费消息中存在丢中间消息时，该会话不可以扩展。 |
  | ****SET N4CHGMSGCTRL**** | 缓存池满的动作（CACHEFULLACT） | CONTINUE | 本端规划 | 控制单个会话的N4计费消息缓存池满时动作。允许业务继续进行，不再进行配额管理。 |
- 任务示例脚本（该命令行）：
  `SET N4CHGMSGCTRL: MSGCACHEEPDSW=ENABLE, CACHEFULLACT=CONTINUE;`
- 操作步骤上下文（±2 行原文）：
  L75:
    >   >   如果 “MONITORTIME” 参数配置为0，则告警监控时长受软参 **DWORD507** 控制，该软参用于控制扫描硬盘上缓存文件的周期。
    > - 配置N4接口计费消息相关控制参数。当阈值配置过小，比如流量阈值较低，会导致N4接口频繁上报阈值到，当CHF性能不足响应较慢时，会导致N4接口上报消息堆积，超过最大可缓存的消息规格，用户被去活。该命令主要用于配置SMF在突发和持续高带宽下载场景，用户不被去活。
    >   ****SET N4CHGMSGCTRL****
    > 
    > ## [任务示例](#ZH-CN_OPI_0231702748)
  L136:
    > 
    > ```
    > SET N4CHGMSGCTRL: MSGCACHEEPDSW=ENABLE, CACHEFULLACT=CONTINUE;
    > ```

## ④ 自动比对
- 命令真相参数（2）：['CACHEFULLACT', 'MSGCACHEEPDSW']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'本端规划': 2}（多值→atom 应考虑 decision_driven）
