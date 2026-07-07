# 命令证据包：TST CHGCDR
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/计费管理/计费控制/模拟SGSN话单(TST CHGCDR)_72344975.md`
> 用该命令的特性数：1

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用网元：SGSN**

该命令用于模拟生成SGSN话单。话单由SPP或UPP进程生成，生成后发往CDP进程，并存储在SPU硬盘或者发往CG。在新建局时，需要对本局点的计费网络及计费功能进行调测，用以验证SGSN与CG之间对接数据配置的正确性及接口状态是否正常，保证SGSN与CG之间接口可以正常工作。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。
- 要模拟生成话单必须满足以下几个条件：
    - 至少存在一个状态正常的CDP进程。
    - SPU硬盘没有满。
    - 与CG通讯正常。
    - 当[**SET CHGCHAR**](../计费属性参数配置/设置计费属性参数(SET CHGCHAR)_26145368.md)中配置的生成话单类型为“YES(Generate)”。

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| CDRTYPE | 话单类型 | 整网规划 | required | 无 | <br>- “MCDR(MCDR)” |
| SYSTYPE | 系统类型 | 整网规划 | optional | <br>“UMTS” | <br>- “GPRS(GPRS)” |
| IMSI | IMSI | 整网规划 | optional | 无 | 5～15位十进制数字 |
| MSISDN | MSISDN | 整网规划 | optional | 无 | 5～15位十进制数字 |
| CC | 计费属性 | 整网规划 | optional | <br>“NORMAL(普通计费)” | <br>- “NORMAL(普通计费)” |
| LAC | 位置区域码 | 整网规划 | optional | 无 | 0x0000～0xFFFF |
| RAC | 寻呼范围路由区域码 | 整网规划 | optional | 无 | 1～2位十六进制数 |
| CI | 小区标识 | 整网规划 | optional | 无 | 1～4位十六进制数 |
| RUNAME | RU名称 | 整网规划 | optional | 无 | 1 ~ 63位字符串 |
| PID | 进程号 | 整网规划 | optional | 无 | 0～20 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-011201

**md：`WSFD-011201/WSFD-011201 支持离线计费参考信息（适用于SGSN）_29423865.md`**
- 操作步骤上下文（±2 行原文）：
  L18:
    > - [**LST CHGCDR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/计费管理/计费控制/查询计费CDR参数（LST CHGCDR）_72225053.md)
    > - [**DSP CHGCDR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/计费管理/计费控制/显示强制生成用户话单的结果信息(DSP CHGCDR)_26305188.md)
    > - [**TST CHGCDR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/计费管理/计费控制/模拟SGSN话单(TST CHGCDR)_72344975.md)
    > - [**SET CHGPLMNCHAR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/计费管理/PLMN计费属性参数配置/设置PLMN的计费属性参数(SET CHGPLMNCHAR)_26305204.md)
    > - [**LST CHGPLMNCHAR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/计费管理/PLMN计费属性参数配置/查询PLMN的计费属性参数(LST CHGPLMNCHAR)_72344991.md)

## ④ 自动比对
- 命令真相参数（10）：['CC', 'CDRTYPE', 'CI', 'IMSI', 'LAC', 'MSISDN', 'PID', 'RAC', 'RUNAME', 'SYSTYPE']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
