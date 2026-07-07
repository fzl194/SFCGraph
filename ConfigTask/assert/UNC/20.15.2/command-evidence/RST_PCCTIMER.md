# 命令证据包：RST PCCTIMER
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/复位PCC定时器/复位PCC定时器（RST PCCTIMER）_09897075.md`
> 用该命令的特性数：2

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：SGW-C、PGW-C、SMF**

此命令用于重启PCC定时器。
**notes（规格/上限→应投影 atom rule）**：
- 该命令执行后立即生效。

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| TIMERTYPE | PCC定时器 | local_planned | required | 无 | 枚举类型。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-109101

**md：`WSFD-109101/实现原理_29056158.md`**
- 操作步骤上下文（±2 行原文）：
  L159:
    > 由于二次协商流程会导致Gx接口的信令交互增加，故 UNC 会在第一个会话建立过程中学习并存储对端PCRF的实际能力，即实际的协商结果，后续会话建立时，直接根据对端的实际能力发起协商，从而可以一次协商成功，提高协商成功率。在网络中实际部署时建议将本地配置的PCRF feature能力与PCRF实际支持的feature能力一致，减少二次协商过程。
    > 
    > 考虑到PCRF的升级场景， UNC 需定时清除本地缓存的对端PCRF能力，以保证新接入的用户可以发起全新的协商流程，从而学习到对端PCRF新的真实的支持能力。在 UNC 上可以使用 [**SET PCCTIMER**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/定时器/设置PCC定时器（SET PCCTIMER）_09897082.md) 命令配置本地缓存的定时器时长，或使用 [**RST PCCTIMER**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/复位PCC定时器/复位PCC定时器（RST PCCTIMER）_09897075.md) 命令手动重启定时器清除本地缓存的对端能力信息。
    > 
    > 如果 UNC 动态协商功能使能，而PCRF不支持Supported-Features AVP，则PCRF会返回值为DIAMETER_AVP_UNSUPPORTED的Result-Code AVP，并且携带Failed-AVP AVP指示无法识别Supported-Features AVP，最终IP-CAN会话创建失败。

### WSFD-201207

**md：`WSFD-201207/WSFD-201207 语音PCF_PCRF故障Bypass参考信息_85304300.md`**
- 操作步骤上下文（±2 行原文）：
  L70:
    > **[LST PCCTIMER](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/定时器/查询PCC定时器（LST PCCTIMER）_96782686.md)**
    > 
    > **[RST PCCTIMER](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/复位PCC定时器/复位PCC定时器（RST PCCTIMER）_09897075.md)**
    > 
    > [**ADD PCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md)

## ④ 自动比对
- 命令真相参数（1）：['TIMERTYPE']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
