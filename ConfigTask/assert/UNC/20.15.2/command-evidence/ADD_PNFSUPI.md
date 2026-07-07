# 命令证据包：ADD PNFSUPI
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端NF实例SUPI信息管理/增加对端NF的SUPI信息（ADD PNFSUPI）_09651473.md`
> 用该命令的特性数：2

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：AMF、SMF、NSSF、SMSF、NCG**

- 该命令用于增加本地配置对端NF实例支持的SUPI的信息。该命令用于在网络中没有部署NRF，或对端NF没有注册到NRF，或网络中存在NRF但需基于运营商策略本地配置周边NF的场景下，配置对端NF实例相关的信息。
- 当NFINSTANCEID配置为"sbidialtest"时，该命令用于新增model-D或model-C间接路由拨测
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。

- 除参数INDEX外，其它参数的组合输入必须唯一。
  当命令ADD PNFWILDCARD的参数SUPICFGSWITCH配置为ON，且本地没有配置对端NF实例支持的SUPI时，代表此对端NF允许所有SUPI号段范围的用户访问。
- 最多配置80条NFINSTANCEID为“sbidialtest”的记录。
- 输入指定索引时，如果该索引未被使用，则使用该索引，否

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| INDEX | 索引 | local_planned | required | 无 | 整数类型，取值范围是0~4294967295。 |
| NFINSTANCEID | NF实例标识 | global_planned | required | 无 | 字符串类型，输入长度范围是0~50。NFINSTANCEID参数建议满足以下约束规则：1.如果输入为 |
| QUERYTYPE | 查询方式 | global_planned | required | 无 | <br>- “START_END（START_END）”：号段 |
| RANGESTART | 起始号段 | global_planned | conditional | 无 | 字符串类型，输入长度范围是5~15。 |
| RANGEEND | 终止号段 | global_planned | conditional | 无 | 字符串类型，输入长度范围是5~15。 |
| PATTERN | 模式 | global_planned | conditional | 无 | 字符串类型，输入长度范围是0~50。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-106406

**md：`WSFD-106406/WSFD-106406 基于号段选择LMF参考信息_18282465.md`**
- 操作步骤上下文（±2 行原文）：
  L14:
    > - **[ADD PNFWILDCARD](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端NF通配策略管理/增加对端NF的通配策略（ADD PNFWILDCARD）_35374733.md)**
    > - [**ADD PNFPROFILE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端NF实例概述信息管理/增加对端NF实例概述信息（ADD PNFPROFILE）_09653772.md)
    > - **[ADD PNFSUPI](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端NF实例SUPI信息管理/增加对端NF的SUPI信息（ADD PNFSUPI）_09651473.md)**
    > - **[SET NGLCSPARA](../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/5G定位服务管理/定位服务管理/设置5G定位服务参数（SET NGLCSPARA）_44007975.md)**
    > 

**md：`WSFD-106406/激活基于号段选择LMF_69042496.md`**
- 数据规划表（该命令的参数行）：
  | **[ADD PNFSUPI](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端NF实例SUPI信息管理/增加对端NF的SUPI信息（ADD PNFSUPI）_09651473.md)** | 索引（INDEX） | 1 | 本端规划 | AMF本地配置LMF1支持的SUPI号段，后续符合条件的SUPI号段范围的用户业务会直接选择到LMF1。 |
  | **[ADD PNFSUPI](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端NF实例SUPI信息管理/增加对端NF的SUPI信息（ADD PNFSUPI）_09651473.md)** | NF实例标识（NFINSTANCEID） | LMF_Instance_1 | 全网规划 | AMF本地配置LMF1支持的SUPI号段，后续符合条件的SUPI号段范围的用户业务会直接选择到LMF1。 |
  | **[ADD PNFSUPI](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端NF实例SUPI信息管理/增加对端NF的SUPI信息（ADD PNFSUPI）_09651473.md)** | 查询方式（QUERYTYPE） | START_END | 全网规划 | AMF本地配置LMF1支持的SUPI号段，后续符合条件的SUPI号段范围的用户业务会直接选择到LMF1。 |
  | **[ADD PNFSUPI](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端NF实例SUPI信息管理/增加对端NF的SUPI信息（ADD PNFSUPI）_09651473.md)** | 起始号段（RANGESTART） | 12345 | 全网规划 | AMF本地配置LMF1支持的SUPI号段，后续符合条件的SUPI号段范围的用户业务会直接选择到LMF1。 |
  | **[ADD PNFSUPI](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端NF实例SUPI信息管理/增加对端NF的SUPI信息（ADD PNFSUPI）_09651473.md)** | 终止号段（RANGEEND） | 12346 | 全网规划 | AMF本地配置LMF1支持的SUPI号段，后续符合条件的SUPI号段范围的用户业务会直接选择到LMF1。 |
- 任务示例脚本（该命令行）：
  `ADD PNFSUPI: INDEX=1,NFINSTANCEID="LMF_Instance_1", QUERYTYPE=START_END, RANGESTART="12345",RANGEEND="12346";`
- 操作步骤上下文（±2 行原文）：
  L56:
    >   **[ADD PNFPROFILE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端NF实例概述信息管理/增加对端NF实例概述信息（ADD PNFPROFILE）_09653772.md)**
    > 3. AMF上配置LMF支持的SUPI/GPSI号段信息。
    >   **[ADD PNFSUPI](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端NF实例SUPI信息管理/增加对端NF的SUPI信息（ADD PNFSUPI）_09651473.md)**
    >   **[ADD PNFGPSI](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端NF实例GPSI信息/增加对端NF的GPSI信息（ADD PNFGPSI）_09652127.md)**
    > 4. AMF上开启基于SUPI/GPSI号段选择LMF开关。
  L92:
    > 
    > ```
    > ADD PNFSUPI: INDEX=1,NFINSTANCEID="LMF_Instance_1", QUERYTYPE=START_END, RANGESTART="12345",RANGEEND="12346";
    > ```
    > 

### WSFD-011206

**md：`WSFD-011206/配置CHF选择方式_92091086.md`**
- 任务示例脚本（该命令行）：
  `ADD PNFSUPI: INDEX=1,NFINSTANCEID="CHF_Instance_0", QUERYTYPE=START_END,RANGESTART="123031200100001",RANGEEND="123031200100001";`
- 操作步骤上下文（±2 行原文）：
  L90:
    >     1. 基于NRF选择CHF，不需要专有配置。
    >     2. 基本本地配置选择CHF。
    >       选择支持特定SUPI的CHF： **ADD PNFSUPI**
    >       选择支持特定GPSI的CHF： **ADD PNFGPSI**
    > - 配置基于SMF本地配置的全局默认CHF组选择CHF。
  L179:
    > 
    > ```
    > ADD PNFSUPI: INDEX=1,NFINSTANCEID="CHF_Instance_0", QUERYTYPE=START_END,RANGESTART="123031200100001",RANGEEND="123031200100001";
    > ADD PNFGPSI: INDEX=1,NFINSTANCEID="CHF_Instance_0", QUERYTYPE=START_END,RANGESTART="138100000000000",RANGEEND="138100000000001";
    > ```

## ④ 自动比对
- 命令真相参数（6）：['INDEX', 'NFINSTANCEID', 'PATTERN', 'QUERYTYPE', 'RANGEEND', 'RANGESTART']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'本端规划': 1, '全网规划': 4}（多值→atom 应考虑 decision_driven）
