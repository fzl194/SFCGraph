---
id: UNC@20.15.2@MMLCommand@MOD PCRFGROUP
type: MMLCommand
name: MOD PCRFGROUP（修改PCRF组）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: PCRFGROUP
command_category: 配置类
applicable_nf:
- PGW-C
- GGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- PCC管理
- PCRF Diameter连接
- PCRF组
status: active
---

# MOD PCRFGROUP（修改PCRF组）

## 功能

**适用NF：PGW-C、GGSN**

此命令用于修改指定的PCRF组是否支持Gx的failover功能以及修改PCRF组的工作模式。

## 注意事项

- 该命令执行后立即生效。
- UNC使用PCC策略和计费控制，为PCRF组设置宕机备份功能时，要求此PCRF组必须是有效的（即此PCRF组下至少已绑定了一个有效的PCRF）。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PCRFGRPNAME | PCRF组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定PCRF组的名字，要求在系统内唯一，数据来源为运营商规划。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～128。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| LOADBALANCEMODE | 负荷分担模式 | 可选必选说明：可选参数<br>参数含义：该参数用于指定PCRF组的工作模式。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- MASTER_SLAVE：主备模式。<br>- LOAD_BALANCE：负荷分担模式。<br>默认值：无<br>配置原则：无 |
| FAILOVERSW | 宕机备份开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定系统是否支持Gx接口failover功能。使能时，在与主PCRF交互失败的情况下，PGW-C会执行Failover动作，将用户消息交互切换到备PCRF上进行处理。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@PCRFGROUP]] · PCRF组（PCRFGROUP）

## 使用实例

修改PCRF组，“PCRFGRPNAME”为“huawei”，“LOADBALANCEMODE”为MASTER_SLAVE，“FAILOVERSW”为ENABLE：

```
MOD PCRFGROUP:PCRFGRPNAME="huawei",LOADBALANCEMODE=MASTER_SLAVE,FAILOVERSW=ENABLE;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-PCRFGROUP.md`
