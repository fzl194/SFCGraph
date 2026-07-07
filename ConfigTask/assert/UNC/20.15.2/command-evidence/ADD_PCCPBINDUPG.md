# 命令证据包：ADD PCCPBINDUPG
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/用户PCC模板绑定/增加用户模板组和PccProfile的绑定关系（ADD PCCPBINDUPG）_09897037.md`
> 用该命令的特性数：1

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：PGW-C、SMF**

本命令用于将PccProfile绑定到UserProfileGroup下，该PccProfile作为本地PCC用户的策略来源，或者会话创建时无法从PCRF/PCF获取有效规则时的策略来源。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。
- 一个UsrProfGroup下面最多可以绑定32个UserProfile。
- 需要预先配置USRPROFGROUP和USERPROFILE。
- UNC整机支持最大的绑定规格是32000。
- 用户激活后优先安装ADD PCCPBINDUPG命令绑定的UserProfile，如果ADD PCCPBINDUPG命令未绑定任何UserProfile，则使用ADD UP

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| USERPROFGNAME | 用户模板组名称 | global_planned | required | 无 | 字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。 |
| PCCPROFILENAME | 用户PCC模板名称 | local_planned | required | 无 | 字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-109101

**md：`WSFD-109101/配置本地PCC功能_30805097.md`**
- 操作步骤上下文（±2 行原文）：
  L107:
    >       > UserProfile Group中可以绑定多个UserProfile，本地PCC用户激活后，UNC根据 [**ADD UPBINDUPG**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md) 中的匹配条件最终只能为本地PCC用户安装一个UserProfile，如果要为本地PCC用户安装多个UserProfile，用以区分不同的业务套餐，需要执行 [步骤 6.f](#ZH-CN_OPI_0230805097__stepe) 。
    >     f. **可选：**将UserProfile绑定到UserProfile Group，为本地PCC用户安装多个UserProfile。
    >       [**ADD PCCPBINDUPG**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/用户PCC模板绑定/增加用户模板组和PccProfile的绑定关系（ADD PCCPBINDUPG）_09897037.md)
    >       > **说明**
    >       > - 重复执行本步骤可以绑定多个UserProfile，实现为本地PCC用户安装多个UserProfile。
  L110:
    >       > **说明**
    >       > - 重复执行本步骤可以绑定多个UserProfile，实现为本地PCC用户安装多个UserProfile。
    >       > - 用户激活后优先安装[**ADD PCCPBINDUPG**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/用户PCC模板绑定/增加用户模板组和PccProfile的绑定关系（ADD PCCPBINDUPG）_09897037.md)命令绑定的UserProfile，如果[**ADD PCCPBINDUPG**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/用户PCC模板绑定/增加用户模板组和PccProfile的绑定关系（ADD PCCPBINDUPG）_09897037.md)命令未绑定任何UserProfile，则使用[**ADD UPBINDUPG**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)中绑定的UserProfile。
    >       > - [**ADD PCCPBINDUPG**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/用户PCC模板绑定/增加用户模板组和PccProfile的绑定关系（ADD PCCPBINDUPG）_09897037.md)命令配置后，common policy仍使用[**ADD UPBINDUPG**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)中配置的匹配条件的UserProfile中的策略。
    >     g. 将UserProfile Group绑定到APN。
  L111:
    >       > - 重复执行本步骤可以绑定多个UserProfile，实现为本地PCC用户安装多个UserProfile。
    >       > - 用户激活后优先安装[**ADD PCCPBINDUPG**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/用户PCC模板绑定/增加用户模板组和PccProfile的绑定关系（ADD PCCPBINDUPG）_09897037.md)命令绑定的UserProfile，如果[**ADD PCCPBINDUPG**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/用户PCC模板绑定/增加用户模板组和PccProfile的绑定关系（ADD PCCPBINDUPG）_09897037.md)命令未绑定任何UserProfile，则使用[**ADD UPBINDUPG**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)中绑定的UserProfile。
    >       > - [**ADD PCCPBINDUPG**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/用户PCC模板绑定/增加用户模板组和PccProfile的绑定关系（ADD PCCPBINDUPG）_09897037.md)命令配置后，common policy仍使用[**ADD UPBINDUPG**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)中配置的匹配条件的UserProfile中的策略。
    >     g. 将UserProfile Group绑定到APN。
    >       [**ADD APNUSRPROFG**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md)

## ④ 自动比对
- 命令真相参数（2）：['PCCPROFILENAME', 'USERPROFGNAME']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
