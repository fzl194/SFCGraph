---
id: UNC@20.15.2@MMLCommand@LST SRVHANDOVER
type: MMLCommand
name: LST SRVHANDOVER（查询业务切换策略）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SRVHANDOVER
command_category: 查询类
applicable_nf:
- SGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- 会话管理
- 业务切换策略
status: active
---

# LST SRVHANDOVER（查询业务切换策略）

## 功能

**适用网元：SGSN**

该命令用于查询业务切换策略信息。切换策略控制就是根据业务级别、用户级别确定用户在2G和3G网络中的切换策略，来引导2G和3G的网络业务承载和网络负荷。切换策略可以由运营商配置。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SRVLVL | 业务级别 | 可选必选说明：可选参数<br>参数含义：该参数需根据用户PDP上下文QoS中的流量等级（Traffic class）、下行保证速率（Guaranteed bit rate for downlink）和发送控制优先级（Traffic handling priority）确定。<br>取值范围：<br>- “CONVERSATION(Conversation)”：流量等级为Conversational class。<br>- “STREAMINGGBRMORE25KBPS(StreamGBRMore25kbps)”：流量等级为Streaming class，下行保证速率大于等于25kbit/s。<br>- “STREAMINGGBRLESS24KBPS(StreamGBRLess24kbps)”：流量等级为Streaming class，下行保证速率小于24kbit/s。<br>- “INTERACTIVETRAFFICPRI1(InteractiveTrafficPri1)”：流量等级为Interactive class，发送控制优先级为1。<br>- “INTERACTIVETRAFFICPRI2(InteractiveTrafficPri2)”：流量等级为Interactive class，发送控制优先级为2。<br>- “INTERACTIVETRAFFICPRI3(InteractiveTrafficPri3)”：流量等级为Interactive class，发送控制优先级为3。<br>- “BACKGROUND(Background)”：流量等级为Background class。<br>默认值：无 |
| USRPRI | 用户级别 | 可选必选说明：可选参数<br>参数含义：待查询的用户签约QoS属性中的分配保留优先级（Allocation/Retention Priority）。<br>取值范围：<br>- “HIGHLEVELUSER(高端用户)”：分配/保留优先级为1。<br>- “NORMALUSER(普通用户)”：分配/保留优先级为2。<br>- “LOWLEVELUSER(低端用户)”：分配/保留优先级为3。<br>- “NONE(None)”：通用用户级别，表示该用户没有用户级别，设置的门限就是该业务级别所有用户级别的切换策略。<br>默认值：无<br>说明：在相同业务级别下，配置不同的用户级别，其中配置了“通用用户级别”，表示在相同的业务级别下，对已配置用户级别之外的所有用户级别都使用“通用用户级别”的策略。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SRVHANDOVER]] · 业务切换策略（SRVHANDOVER）

## 使用实例

查询业务级别为 “BACKGROUND(Background)” ，用户级别为 “HIGHLEVELUSER(高端用户)” 的业务切换策略：

```
%%LST SRVHANDOVER:SRVLVL=BACKGROUND, USRPRI=HIGHLEVELUSER;%%
RETCODE = 0  操作成功。

业务切换配置表
--------------
                 业务级别  =  Background
                 用户级别  =  高端用户
        WCDMA业务切换策略  =  建议切换到GPRS
         GPRS业务切换策略  =  建议切换到WCDMA
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询业务切换策略(LST-SRVHANDOVER)_72225347.md`
