# 命令证据包：ADD HTTPLEGRP
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/HTTP管理/HTTP本端实体组管理/增加HTTP本端实体组（ADD HTTPLEGRP）_29213277.md`
> 用该命令的特性数：2

## ② 命令真相（mml_commands.jsonl）
**功能**：该命令用于添加HTTP本端实体组信息，可将多个HTTP本端实体配置关联到一个组。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。

- 在一个HTTP本端实体组下最多只能配置32个HTTP本端实体。

- 最多可输入64条记录。

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| INDEX | 索引 | local_planned | required | 无 | 整数类型，取值范围是1~64。 |
| DESC | 描述 | global_planned | optional | 无 | 字符串类型，输入长度范围是0~255。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-010308

**md：`WSFD-010308/WSFD-010308 SBI接口加密参考信息_70185217.md`**
- 操作步骤上下文（±2 行原文）：
  L19:
    > - [**修改TLS参数(MOD TLSPARA)**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/HTTP管理/HTTP安全管理/HTTP TLS安全管理/修改TLS参数（MOD TLSPARA）_83972192.md)
    > - [**查询TLS参数(LST TLSPARA)**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/HTTP管理/HTTP安全管理/HTTP TLS安全管理/查询TLS参数（LST TLSPARA）_84132104.md)
    > - [**增加本端地址组(ADD HTTPLEGRP)**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/HTTP管理/HTTP本端实体组管理/增加HTTP本端实体组（ADD HTTPLEGRP）_29213277.md)
    > - [**删除本端地址组(RMV HTTPLEGRP)**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/HTTP管理/HTTP本端实体组管理/删除HTTP本端实体组（RMV HTTPLEGRP）_83813640.md)
    > - [**查询本端地址组(LST HTTPLEGRP)**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/HTTP管理/HTTP本端实体组管理/查询HTTP本端实体组（LST HTTPLEGRP）_83653658.md)

**md：`WSFD-010308/激活SBI接口加密特性(CERT)_70185215.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD HTTPLEGRP**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/HTTP管理/HTTP本端实体组管理/增加HTTP本端实体组（ADD HTTPLEGRP）_29213277.md) | 索引 | AMF：1<br>NRF：2 | 本端规划 | - |
- 任务示例脚本（该命令行）：
  `ADD HTTPLEGRP: INDEX=1, DESC="AMF";`
  `ADD HTTPLEGRP: INDEX=2, DESC="NRF";`
- 操作步骤上下文（±2 行原文）：
  L88:
    >       [**ADD TLSPARA**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/HTTP管理/HTTP安全管理/HTTP TLS安全管理/增加TLS参数（ADD TLSPARA）_84132096.md)
    >     d. 增加AMF HTTP本端地址组信息。
    >       [**ADD HTTPLEGRP**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/HTTP管理/HTTP本端实体组管理/增加HTTP本端实体组（ADD HTTPLEGRP）_29213277.md)
    >     e. 增加逻辑IP地址。" **IPv4地址"** 、" **IPv6地址** "以及 **"VPN实例名称"** 全网规划。
    >       **[ADD LOGICIP](../../../../../OM参考/命令/UNC MML命令/平台服务管理/IP管理/IP配置/增加逻辑IP地址（ADD LOGICIP）_09587376.md)**
  L107:
    >       [**ADD TLSPARA**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/HTTP管理/HTTP安全管理/HTTP TLS安全管理/增加TLS参数（ADD TLSPARA）_84132096.md)
    >     d. 增加NRF HTTP本端地址组信息。
    >       [**ADD HTTPLEGRP**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/HTTP管理/HTTP本端实体组管理/增加HTTP本端实体组（ADD HTTPLEGRP）_29213277.md)
    >     e. 增加逻辑IP地址。" **IPv4地址"** 、" **IPv6地址** "以及 **"VPN实例名称"** 全网规划。
    >       **[ADD LOGICIP](../../../../../OM参考/命令/UNC MML命令/平台服务管理/IP管理/IP配置/增加逻辑IP地址（ADD LOGICIP）_09587376.md)**
  L149:
    > 
    > ```
    > ADD HTTPLEGRP: INDEX=1, DESC="AMF";
    > ```
    > 

**md：`WSFD-010308/激活SBI接口加密特性(PSK)_57783838.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD HTTPLEGRP**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/HTTP管理/HTTP本端实体组管理/增加HTTP本端实体组（ADD HTTPLEGRP）_29213277.md) | 索引(INDEX) | AMF：1<br>NRF：2 | 本端规划 | - |
- 任务示例脚本（该命令行）：
  `ADD HTTPLEGRP: INDEX=1, DESC="AMF";`
- 操作步骤上下文（±2 行原文）：
  L75:
    >       [**ADD TLSPARA**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/HTTP管理/HTTP安全管理/HTTP TLS安全管理/增加TLS参数（ADD TLSPARA）_84132096.md)
    >     g. 增加AMF HTTP本端地址组信息。
    >       [**ADD HTTPLEGRP**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/HTTP管理/HTTP本端实体组管理/增加HTTP本端实体组（ADD HTTPLEGRP）_29213277.md)
    >     h. 增加逻辑IP地址。" **IPv4地址"** 、" **IPv6地址** "以及 **"VPN实例名称"** 全网规划。
    >       **[**ADD LOGICIP**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/IP管理/IP配置/增加逻辑IP地址（ADD LOGICIP）_09587376.md)**
  L132:
    > 
    > ```
    > ADD HTTPLEGRP: INDEX=1, DESC="AMF";
    > ```
    > 

### WSFD-109101

**md：`WSFD-109101/配置QoS能力开放功能_48518810.md`**
- 数据规划表（该命令的参数行）：
  | **[ADD HTTPLEGRP](../../../../../../../OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/HTTP管理/HTTP本端实体组管理/增加HTTP本端实体组（ADD HTTPLEGRP）_29213277.md)** | 索引（INDEX） | 3 | 本端规划 | 增加HTTP本端实体组 |
  | **[ADD HTTPLEGRP](../../../../../../../OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/HTTP管理/HTTP本端实体组管理/增加HTTP本端实体组（ADD HTTPLEGRP）_29213277.md)** | 描述（DESC） | BSF | 全网规划 | 增加HTTP本端实体组 |
- 任务示例脚本（该命令行）：
  `ADD HTTPLEGRP: INDEX=3, DESC="BSF";`
- 操作步骤上下文（±2 行原文）：
  L72:
    >   [**ADD LOGICIP**](../../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IP管理/IP配置/增加逻辑IP地址（ADD LOGICIP）_09587376.md)
    > 5. 配置HTTP本端端点组信息。
    >   **[ADD HTTPLEGRP](../../../../../../../OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/HTTP管理/HTTP本端实体组管理/增加HTTP本端实体组（ADD HTTPLEGRP）_29213277.md)**
    > 6. 配置HTTP本端端点信息。
    >   **[ADD HTTPLE](../../../../../../../OM参考/命令/UNC MML命令/平台服务管理/HTTP功能管理/HTTP管理/HTTP本端实体管理/增加HTTP本端实体（ADD HTTPLE）_84132094.md)**
  L120:
    > 3. 配置HTTP本端端点组信息。
    >   ```
    >   ADD HTTPLEGRP: INDEX=3, DESC="BSF";
    >   ```
    > 4.

## ④ 自动比对
- 命令真相参数（2）：['DESC', 'INDEX']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'本端规划': 3, '全网规划': 1}（多值→atom 应考虑 decision_driven）
