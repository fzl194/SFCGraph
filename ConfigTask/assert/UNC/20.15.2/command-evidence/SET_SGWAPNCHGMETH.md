# 命令证据包：SET SGWAPNCHGMETH
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/SGW计费控制/SGW APN计费方式/设置SGW APN计费方式（SET SGWAPNCHGMETH）_09896992.md`
> 用该命令的特性数：1

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：SGW-C**

![](设置SGW APN计费方式（SET SGWAPNCHGMETH）_09896992.assets/notice_3.0-zh-cn_2.png)

本命令属于高危命令，修改配置会影响新激活的SGW用户是否产生S-GW话单，可能导致用户无法计费。

SET SGWAPNCHGMETH命令用来控制APN下的用户是否产生S-GW话单。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后只对新激活用户生效。
- 该命令最大记录数为10000。
- 参数APN在表APN中必须存在才能配置成功。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | Offline |
| --- | --- |
| 初始值 | INHERIT |

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| APN | APN名称 | global_planned | required | 无 | 字符串类型，输入长度范围为1～63。不支持空格以及特殊字符：“_”、“#”、“$”、“&”等。 |
| OFFLINE | APN离线计费开关 | local_planned | required | 无 | 枚举类型。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-011201

**md：`WSFD-011201/WSFD-011201 支持离线计费参考信息（适用于GGSN_SGW-C_PGW-C）_29423866.md`**
- 操作步骤上下文（±2 行原文）：
  L19:
    > - [**ADD CHARGEMETHOD**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/计费属性计费控制/增加计费方式（ADD CHARGEMETHOD）_09896795.md)
    > - [**SET SGWCHARGECFG**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/SGW计费控制/SGW计费基础参数/SGW计费配置（SET SGWCHARGECFG）_09896989.md)
    > - [**SET SGWAPNCHGMETH**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/SGW计费控制/SGW APN计费方式/设置SGW APN计费方式（SET SGWAPNCHGMETH）_09896992.md)
    > - [**SET SGWCHGMETH**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/SGW计费控制/计费属性控制/设置SGW Charge Method（SET SGWCHGMETH）_09896985.md)
    > - [**ADD OFCTEMPLATE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/离线计费基础参数/离线计费模板/增加离线计费模板（ADD OFCTEMPLATE）_09896908.md)

**md：`WSFD-011201/配置离线计费方式（SGW-C）_02167102.md`**
- 数据规划表（该命令的参数行）：
  | **SET SGWAPNCHGMETH** | APN名称（APN） | apn-test | 已配置数据中获取 | 设置SGW APN计费方式。如果未配置本命令，OFFLINE默认值为INHERIT。<br>- OFFLINE默认值都是INHERIT。<br>- 在APN中配置INHERIT则计费方式继承基于计费属性的配置。 |
  | **SET SGWAPNCHGMETH** | APN离线计费开关（OFFLINE） | ENABLE | 本端规划 | 设置SGW APN计费方式。如果未配置本命令，OFFLINE默认值为INHERIT。<br>- OFFLINE默认值都是INHERIT。<br>- 在APN中配置INHERIT则计费方式继承基于计费属性的配置。 |
- 任务示例脚本（该命令行）：
  `SET SGWAPNCHGMETH: APN="apn-test",OFFLINE=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L71:
    >       **SET SGWCHGMETH**
    >     b. 基于APN使能SGW-C的离线计费方式。
    >       **SET SGWAPNCHGMETH**
    > 4. 设置SGW-C基于号段组的计费方式。
    >     a. 配置IMSI及MSISDN号码段。
  L104:
    > 
    > ```
    > SET SGWAPNCHGMETH: APN="apn-test",OFFLINE=ENABLE;
    > ```
    > 

## ④ 自动比对
- 命令真相参数（2）：['APN', 'OFFLINE']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'已配置数据中获取': 1, '本端规划': 1}（多值→atom 应考虑 decision_driven）
