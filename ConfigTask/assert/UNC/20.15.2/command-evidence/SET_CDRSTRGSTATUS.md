# 命令证据包：SET CDRSTRGSTATUS
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费缓存/缓存目录/设置话单缓存目录状态（SET CDRSTRGSTATUS）_09897006.md`
> 用该命令的特性数：1

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：SGW-C、PGW-C、SMF**

该命令用来配置话单缓存目录状态。对话单缓存目录charge1或者charge2中的话单文件进行操作之前，必须在锁定该目录之后才可进行。操作完毕后，要将缓存目录charge1或者charge2解锁。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。
- 该命令最大记录数为2048。
- 话单缓存目录charge1和charge2不能同时被锁定。
- POD缓存路径被锁定时不允许缩容。
- POD缓存路径解锁动作处理完前不允许缩容。
- 使用该命令锁定话单缓存目录之后，如果遇到话单缓存周期扫描，会导致告警清除，需要确认影响后使用该功能。

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| PODNAME | POD名称 | local_planned | required | 无 | 字符串类型，输入长度范围为1～63。 |
| DIRECTORY | 话单缓存目录 | local_planned | required | 无 | 枚举类型。 |
| STATUS | 目录状态 | local_planned | required | 无 | 枚举类型。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-011201

**md：`WSFD-011201/WSFD-011201 支持离线计费参考信息（适用于GGSN_SGW-C_PGW-C）_29423866.md`**
- 操作步骤上下文（±2 行原文）：
  L39:
    > - [**FOC GENERATECDR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费维护/强制生成话单/强制生成话单（FOC GENERATECDR）_09897016.md)
    > - [**SET OFCCDRPARA**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/离线计费基础参数/离线公共参数/配置离线计费话单参数（SET OFCCDRPARA）_09896905.md)
    > - [**SET CDRSTRGSTATUS**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费缓存/缓存目录/设置话单缓存目录状态（SET CDRSTRGSTATUS）_09897006.md)
    > - [**SET CDRSTORAGECTRL**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费缓存/缓存控制/设置话单存储控制参数（SET CDRSTORAGECTRL）_09897001.md)
    > - [**SET ZEROCHGSKIPSW**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/计费参数/设置零流量计费事件忽略开关（SET ZEROCHGSKIPSW）_09896806.md)

**md：`WSFD-011201/配置话单可选功能（GGSN_SGW-C_PGW-C）_95923448.md`**
- 数据规划表（该命令的参数行）：
  | **SET CDRSTRGSTATUS** | POD名称（PODNAME） | pod1 | 本端规划 | 对话单缓存目录<br>**CHARGE1**<br>或者<br>**CHARGE2**<br>中的话单文件进行操作之前，必须锁定目录<br>**CHARGE1**<br>或者<br>**CHARGE2**<br>。操作完成后，要解锁目录<br>**CHARGE1**<br>或者<br>**CHARGE2**<br>。 |
  | **SET CDRSTRGSTATUS** | 目录状态（STATUS） | LOCK | 本端规划 | 对话单缓存目录<br>**CHARGE1**<br>或者<br>**CHARGE2**<br>中的话单文件进行操作之前，必须锁定目录<br>**CHARGE1**<br>或者<br>**CHARGE2**<br>。操作完成后，要解锁目录<br>**CHARGE1**<br>或者<br>**CHARGE2**<br>。 |
  | **SET CDRSTRGSTATUS** | 话单缓存目录（DIRECTORY） | CHARGE1 | 本端规划 | 对话单缓存目录<br>**CHARGE1**<br>或者<br>**CHARGE2**<br>中的话单文件进行操作之前，必须锁定目录<br>**CHARGE1**<br>或者<br>**CHARGE2**<br>。操作完成后，要解锁目录<br>**CHARGE1**<br>或者<br>**CHARGE2**<br>。 |
- 任务示例脚本（该命令行）：
  `SET CDRSTRGSTATUS: PODNAME="pod1",DIRECTORY=CHARGE2,STATUS=UNLOCK;`
  `SET CDRSTRGSTATUS: PODNAME="pod1",DIRECTORY=CHARGE1,STATUS=LOCK;`
  `SET CDRSTRGSTATUS: PODNAME="pod1",DIRECTORY=CHARGE1,STATUS=UNLOCK;`
- 操作步骤上下文（±2 行原文）：
  L54:
    > 2. 配置话单缓存功能。
    >     a. 配置锁定话单缓存目录。
    >       **SET CDRSTRGSTATUS**
    >     b. 配置缓存话单的超期时间。
    >       **SET CDRSTORAGECTRL**
  L60:
    >       > 当话单缓存的时间超过配置的超期时间时，系统会产生告警 **ALM-81059 超期话单缓存** ，提醒操作维护人员尽快处理话单。话单长期超期得不到处理，会导致用户计费信息丢失。
    >     c. 配置解锁话单缓存目录。
    >       **SET CDRSTRGSTATUS**
    > 
    > ## [任务示例](#ZH-CN_OPI_0295923448)
  L85:
    >     a. 配置手动操作话单缓存主目录 **CHARGE1** 。
    >       ```
    >       SET CDRSTRGSTATUS: PODNAME="pod1",DIRECTORY=CHARGE2,STATUS=UNLOCK;
    >       ```
    >       ```

## ④ 自动比对
- 命令真相参数（3）：['DIRECTORY', 'PODNAME', 'STATUS']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'本端规划': 3}（多值→atom 应考虑 decision_driven）
