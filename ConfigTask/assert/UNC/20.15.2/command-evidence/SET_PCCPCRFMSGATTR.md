# 命令证据包：SET PCCPCRFMSGATTR
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/服务器端信元控制/设置PCRF返回消息属性（SET PCCPCRFMSGATTR）_09897077.md`
> 用该命令的特性数：1

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：PGW-C、SMF**

该命令用于配置激活和更新流程中，UNC是否支持由DRA或PCRF触发的PCRF重选。

如果希望在激活或者更新流程中，UNC根据DRA或者PCRF消息触发的PCRF重选，则可将对应的参数使能。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。
- 该命令最大记录数为1。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | ORGHOSTCCAI | ORGHOSTCCAU | ORGHOSTRAR |
| --- | --- | --- | --- |
| 初始值 | DISABLE | DISABLE | DISABLE |

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| ORGHOSTCCAI | 基于CCA-I Origin-Host AVP触发PCRF重选 | local_planned | optional | 无 | 枚举类型。 |
| ORGHOSTCCAU | 基于CCA-U Origin-Host AVP触发PCRF重选 | local_planned | optional | 无 | 枚举类型。 |
| ORGHOSTRAR | 基于RAR Origin-Host AVP触发PCRF重选 | local_planned | optional | 无 | 枚举类型。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-109101

**md：`WSFD-109101/配置动态PCC功能_30805098.md`**
- 操作步骤上下文（±2 行原文）：
  L111:
    >       [**ADD GLBPCRFGROUP**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/全局PCRF组/增加全局PCRF组绑定关系（ADD GLBPCRFGROUP）_09897116.md)
    > 5. **可选：**配置基于整机粒度控制在激活过程中根据PCRF返回的重定向指示重选PCRF。缺省不支持。
    >   [**SET PCCPCRFMSGATTR**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/服务器端信元控制/设置PCRF返回消息属性（SET PCCPCRFMSGATTR）_09897077.md)
    > 6. 开启全局缺省PCC开关。
    >     a. 设置全局缺省的PCRF分组的名称。

## ④ 自动比对
- 命令真相参数（3）：['ORGHOSTCCAI', 'ORGHOSTCCAU', 'ORGHOSTRAR']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
