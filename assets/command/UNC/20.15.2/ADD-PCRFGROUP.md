---
id: UNC@20.15.2@MMLCommand@ADD PCRFGROUP
type: MMLCommand
name: ADD PCRFGROUP（增加PCRF组）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: PCRFGROUP
command_category: 配置类
applicable_nf:
- PGW-C
- GGSN
effect_mode: 立即生效
is_dangerous: false
max_records: 100
category_path:
- 业务服务管理
- 会话管理
- PCC管理
- PCRF Diameter连接
- PCRF组
status: active
---

# ADD PCRFGROUP（增加PCRF组）

## 功能

**适用NF：PGW-C、GGSN**

该命令用于添加PCRF Group，设置是否Gx的failover功能以及设置工作模式。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为100。
- 主备工作模式时，第一个添加到某PCRF组的PCRF将被设置为该组的缺省Master PCRF，后续添加的PCRF将被缺省设置为组内的Slave PCRF，这种状态将一直持续下去，直到通过SET MASTERPCRF改变Master PCRF或者Master PCRF被删除。Master PCRF为该组的主用PCRF，当有PCC用户激活时，系统优先选择Master PCRF。
- 为PCRF分组设置宕机备份功能时，要求此PCRF组必须是有效的（即此PCRF组下至少已绑定了一个有效的PCRF）。
- 一次CCR、CCA消息交互过程中，failover动作最多执行一次。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PCRFGRPNAME | PCRF组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定PCRF组的名字，要求在系统内唯一，数据来源为运营商规划。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～128。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| LOADBALANCEMODE | 负荷分担模式 | 可选必选说明：可选参数<br>参数含义：该参数用于指定PCRF组的工作模式。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- MASTER_SLAVE：主备模式。<br>- LOAD_BALANCE：负荷分担模式。<br>默认值：MASTER_SLAVE<br>配置原则：无 |
| FAILOVERSW | 宕机备份开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定系统是否支持Gx接口failover功能。使能时，在与主PCRF交互失败的情况下，PGW-C会执行Failover动作，将用户消息交互切换到备PCRF上进行处理。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：DISABLE<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PCRFGROUP]] · PCRF组（PCRFGROUP）

## 使用实例

添加PCRF组，“PCRFGRPNAME”为“huawei”，“LOADBALANCEMODE”为MASTER_SLAVE，“FAILOVERSW”为DISABLE：

```
ADD PCRFGROUP:PCRFGRPNAME="huawei",LOADBALANCEMODE=MASTER_SLAVE,FAILOVERSW=DISABLE;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加PCRF组（ADD-PCRFGROUP）_09897090.md`
