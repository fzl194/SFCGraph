# 命令证据包：ADD USRPROBINDDNAI
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板DNAI绑定/增加用户模板关联的DNAI （ADD USRPROBINDDNAI）_27051919.md`
> 用该命令的特性数：1

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：SMF、PGW-C、GGSN**

该命令用于增加用户模板关联的DNAI。

当需要指定用户模板下发某边缘UPF时，可通过本命令绑定User Profile和边缘UPF的DNAI的对应关系来实现。

当一个用户模板绑定到某边缘UPF所对应的DNAI时，该用户模板就只下发给该边缘UPF。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。

- 仅当指定用户模板中的Profile Range为LOCAL时，才可以绑定到边缘UPF对应的DNAI上。Profile Range为ALL的用户模板绑定DNAI无实际意义， SMF会将User Profile同时下发给中心和所有边缘UPF。Profile Range为CENTRAL时，该用户模板不能绑定到任何边缘UPF的DNAI上。

- 最多可输入10000条记录

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| USRPRONAME | 用户模板名称 | global_planned | required | 无 | 字符串类型，输入长度范围是1~63。字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。 |
| DNAI | 数据网络访问标识符 | global_planned | required | 无 | 字符串类型，输入长度范围是1~63。字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-109101

**md：`WSFD-109101/WSFD-109101 PCC基本功能（2G_3G_4G）参考信息_29056160.md`**
- 操作步骤上下文（±2 行原文）：
  L41:
    > - [**SET FHBYPASS**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/失败旁路处理/设置失败旁路处理（SET FHBYPASS）_09896714.md)
    > - [**ADD RULEBINDDNAI**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/预定义规则DNAI绑定/增加预定义规则关联的DNAI（ADD RULEBINDDNAI）_27170471.md)
    > - [**ADD USRPROBINDDNAI**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板DNAI绑定/增加用户模板关联的DNAI （ADD USRPROBINDDNAI）_27051919.md)
    > 
    > #### [告警](#ZH-CN_TOPIC_0229056160)

**md：`WSFD-109101/配置动态PCC功能_30805098.md`**
- 操作步骤上下文（±2 行原文）：
  L142:
    >       [**ADD USERPROFILE**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md)
    >     b. **可选：**配置UserProfile和DNAI关联。可选配置，将UserProfile下发给指定DNAI的辅锚点PGW-U时需要配置。
    >       [**ADD USRPROBINDDNAI**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板DNAI绑定/增加用户模板关联的DNAI （ADD USRPROBINDDNAI）_27051919.md)
    >     c. 将已配置的rule绑定到UserProfile。
    >       [**ADD RULEBINDING**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md)

**md：`WSFD-109101/配置本地PCC功能_30805097.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD USRPROBINDDNAI**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板DNAI绑定/增加用户模板关联的DNAI （ADD USRPROBINDDNAI）_27051919.md) | 用户模板名称（USRPRONAME） | up_test | 全网规划 | 配置的Userprofile需要下发给指定的辅锚点PGW-U时需要配置。例如，Userprofile的<br>“模板生效范围”<br>设置为<br>“LOCAL”<br>时，该Userprofile只下发给DNAI是test.com的辅锚点PGW-U。 |
  | [**ADD USRPROBINDDNAI**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板DNAI绑定/增加用户模板关联的DNAI （ADD USRPROBINDDNAI）_27051919.md) | 数据网络访问标识符（DNAI） | test.com | 全网规划 | 配置的Userprofile需要下发给指定的辅锚点PGW-U时需要配置。例如，Userprofile的<br>“模板生效范围”<br>设置为<br>“LOCAL”<br>时，该Userprofile只下发给DNAI是test.com的辅锚点PGW-U。 |
- 操作步骤上下文（±2 行原文）：
  L97:
    >       [**ADD USERPROFILE**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md)
    >     b. **可选：**将UserProfile下发给指定DNAI的辅锚点PGW-U时，配置UserProfile和DNAI关联。
    >       [**ADD USRPROBINDDNAI**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板DNAI绑定/增加用户模板关联的DNAI （ADD USRPROBINDDNAI）_27051919.md)
    >     c. 将已配置的rule绑定到UserProfile。
    >       [**ADD RULEBINDING**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md)

**md：`WSFD-109101/WSFD-109101 PCC基本功能（5G）参考信息_72466541.md`**
- 操作步骤上下文（±2 行原文）：
  L29:
    > - [**ADD NGMMSUBDATA**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/签约数据管理/增加用户移动性管理参数（ADD NGMMSUBDATA）_09651362.md)
    > - [**ADD RULEBINDDNAI**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/预定义规则DNAI绑定/增加预定义规则关联的DNAI（ADD RULEBINDDNAI）_27170471.md)
    > - [**ADD USRPROBINDDNAI**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板DNAI绑定/增加用户模板关联的DNAI （ADD USRPROBINDDNAI）_27051919.md)
    > - **[SET AMFPEERSELFUNC](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/可靠性管理/AMF对端选择功能管理/设置AMF对端选择功能参数（SET AMFPEERSELFUNC）_19037048.md)**
    > 

**md：`WSFD-109101/激活PCC基本功能_72467890.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD USRPROBINDDNAI**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板DNAI绑定/增加用户模板关联的DNAI （ADD USRPROBINDDNAI）_27051919.md) | 用户模板名称（USRPRONAME） | up_test | 全网规划 | 配置的Userprofile需要下发给指定的辅锚点UPF时需要配置。例如，Userprofile的<br>“模板生效范围”<br>设置为<br>“LOCAL”<br>时，该Userprofile只下发给DNAI是test.com的辅锚点UPF。 |
  | [**ADD USRPROBINDDNAI**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板DNAI绑定/增加用户模板关联的DNAI （ADD USRPROBINDDNAI）_27051919.md) | 数据网络访问标识符（DNAI） | test.com | 全网规划 | 配置的Userprofile需要下发给指定的辅锚点UPF时需要配置。例如，Userprofile的<br>“模板生效范围”<br>设置为<br>“LOCAL”<br>时，该Userprofile只下发给DNAI是test.com的辅锚点UPF。 |
- 操作步骤上下文（±2 行原文）：
  L180:
    >             [**ADD USERPROFILE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md)
    >           b. 将UserProfile下发给指定DNAI的辅锚点UPF时，配置UserProfile和DNAI关联。
    >             [**ADD USRPROBINDDNAI**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板DNAI绑定/增加用户模板关联的DNAI （ADD USRPROBINDDNAI）_27051919.md)
    >           c. 将rule绑定到UserProfile。
    >             [**ADD RULEBINDING**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md)

## ④ 自动比对
- 命令真相参数（2）：['DNAI', 'USRPRONAME']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'全网规划': 4}（多值→atom 应考虑 decision_driven）
