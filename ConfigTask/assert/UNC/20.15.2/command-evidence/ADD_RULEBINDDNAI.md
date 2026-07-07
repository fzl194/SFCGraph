# 命令证据包：ADD RULEBINDDNAI
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/预定义规则DNAI绑定/增加预定义规则关联的DNAI（ADD RULEBINDDNAI）_27170471.md`
> 用该命令的特性数：1

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：SMF、PGW-C、GGSN**

该命令用于增加预定义规则关联的DNAI。

当需要指定预定义规则下发某边缘UPF时，可通过本命令绑定Rule和边缘UPF的DNAI的对应关系来实现。

当一个预定义规则绑定到某边缘UPF所对应的DNAI时，该预定义相关规则就只下发给该边缘UPF。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。

- 仅当指定预定义规则的Rule Range为LOCAL时，才可以绑定到边缘UPF对应的DNAI上。Rule Range为ALL的预定义规则绑定DNAI无实际意义， SMF会将Rule同时下发给中心和所有边缘UPF。Rule Range为CENTRAL时，该预定义规则不能绑定到任何边缘UPF的DNAI上。

- 最多可输入10000条记录。

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| RULENAME | 预定义规则名称 | global_planned | required | 无 | 字符串类型，输入长度范围是1~63。字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。 |
| DNAI | 数据网络访问标识符 | global_planned | required | 无 | 字符串类型，输入长度范围是1~63。字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-109101

**md：`WSFD-109101/WSFD-109101 PCC基本功能（2G_3G_4G）参考信息_29056160.md`**
- 操作步骤上下文（±2 行原文）：
  L40:
    > - [**ADD RESULTCODECTRL**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/增加返回码控制（ADD RESULTCODECTRL）_09897084.md)
    > - [**SET FHBYPASS**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/失败旁路处理/设置失败旁路处理（SET FHBYPASS）_09896714.md)
    > - [**ADD RULEBINDDNAI**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/预定义规则DNAI绑定/增加预定义规则关联的DNAI（ADD RULEBINDDNAI）_27170471.md)
    > - [**ADD USRPROBINDDNAI**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板DNAI绑定/增加用户模板关联的DNAI （ADD USRPROBINDDNAI）_27051919.md)
    > 

**md：`WSFD-109101/配置动态PCC功能_30805098.md`**
- 操作步骤上下文（±2 行原文）：
  L137:
    >   [**ADD RULE**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md)
    > 10. **可选：**配置rule和DNAI关联。可选配置，将rule下发给指定DNAI的辅锚点PGW-U时需要配置。
    >   [**ADD RULEBINDDNAI**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/预定义规则DNAI绑定/增加预定义规则关联的DNAI（ADD RULEBINDDNAI）_27170471.md)
    > 11. PCRF下发预定义规则组时，需要在GGSN/PGW-C上配置预定义规则组对应的本地业务策略组合。
    >     a. 配置UserProfile。

**md：`WSFD-109101/配置本地PCC功能_30805097.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD RULEBINDDNAI**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/预定义规则DNAI绑定/增加预定义规则关联的DNAI（ADD RULEBINDDNAI）_27170471.md) | 规则名称（RULENAME） | rule_test | 全网规划 | 配置的rule需要下发给指定的辅锚点PGW-U时需要配置。例如，rule的<br>“规则生效范围”<br>设置为<br>“LOCAL”<br>时，该规则只下发给DNAI是huawei.com的辅锚点PGW-U。 |
  | [**ADD RULEBINDDNAI**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/预定义规则DNAI绑定/增加预定义规则关联的DNAI（ADD RULEBINDDNAI）_27170471.md) | 数据网络访问标识符（DNAI） | huawei.com | 全网规划 | 配置的rule需要下发给指定的辅锚点PGW-U时需要配置。例如，rule的<br>“规则生效范围”<br>设置为<br>“LOCAL”<br>时，该规则只下发给DNAI是huawei.com的辅锚点PGW-U。 |
- 操作步骤上下文（±2 行原文）：
  L92:
    >       [**ADD RULE**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md)
    >     d. **可选：**配置rule和DNAI关联。可选配置，将rule下发给指定DNAI的辅锚点PGW-U时需要配置。
    >       [**ADD RULEBINDDNAI**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/预定义规则DNAI绑定/增加预定义规则关联的DNAI（ADD RULEBINDDNAI）_27170471.md)
    > 6. 配置业务策略组合。
    >     a. 配置UserProfile。

**md：`WSFD-109101/WSFD-109101 PCC基本功能（5G）参考信息_72466541.md`**
- 操作步骤上下文（±2 行原文）：
  L28:
    > - [**ADD PCFSSCOPEBIND**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCF发现和选择管理/PCF业务服务区绑定/增加PCF业务服务区的绑定关系（ADD PCFSSCOPEBIND）_88537090.md)
    > - [**ADD NGMMSUBDATA**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/签约数据管理/增加用户移动性管理参数（ADD NGMMSUBDATA）_09651362.md)
    > - [**ADD RULEBINDDNAI**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/预定义规则DNAI绑定/增加预定义规则关联的DNAI（ADD RULEBINDDNAI）_27170471.md)
    > - [**ADD USRPROBINDDNAI**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板DNAI绑定/增加用户模板关联的DNAI （ADD USRPROBINDDNAI）_27051919.md)
    > - **[SET AMFPEERSELFUNC](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/可靠性管理/AMF对端选择功能管理/设置AMF对端选择功能参数（SET AMFPEERSELFUNC）_19037048.md)**

**md：`WSFD-109101/激活PCC基本功能_72467890.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD RULEBINDDNAI**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/预定义规则DNAI绑定/增加预定义规则关联的DNAI（ADD RULEBINDDNAI）_27170471.md) | 规则名称（RULENAME） | rule_test | 全网规划 | 配置的rule需要下发给指定的辅锚点UPF时需要配置。例如，rule的<br>“规则生效范围”<br>设置为<br>“LOCAL”<br>时，该规则只下发给DNAI是huawei.com的辅锚点UPF。 |
  | [**ADD RULEBINDDNAI**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/预定义规则DNAI绑定/增加预定义规则关联的DNAI（ADD RULEBINDDNAI）_27170471.md) | 数据网络访问标识符（DNAI） | huawei.com | 全网规划 | 配置的rule需要下发给指定的辅锚点UPF时需要配置。例如，rule的<br>“规则生效范围”<br>设置为<br>“LOCAL”<br>时，该规则只下发给DNAI是huawei.com的辅锚点UPF。 |
- 操作步骤上下文（±2 行原文）：
  L175:
    >       [**ADD RULE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md)
    >     13. 将rule下发给指定DNAI的辅锚点UPF时，配置rule和DNAI关联。
    >       [**ADD RULEBINDDNAI**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/预定义规则DNAI绑定/增加预定义规则关联的DNAI（ADD RULEBINDDNAI）_27170471.md)
    >     14. **可选：**配置SMF上的UserProfile，将本地rule绑定到UserProfile上。用于动态PCC时PCF下发预定义规则组，或本地PCC时的静态规则组。
    >           a. 配置UserProfile。

## ④ 自动比对
- 命令真相参数（2）：['DNAI', 'RULENAME']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'全网规划': 4}（多值→atom 应考虑 decision_driven）
