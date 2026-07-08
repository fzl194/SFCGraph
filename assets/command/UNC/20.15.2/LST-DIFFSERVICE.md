---
id: UNC@20.15.2@MMLCommand@LST DIFFSERVICE
type: MMLCommand
name: LST DIFFSERVICE（查询差异化服务接入门限）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: DIFFSERVICE
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
- 差异化服务配置
status: active
---

# LST DIFFSERVICE（查询差异化服务接入门限）

## 功能

**适用网元：SGSN**

该命令用于查询差异化服务配置信息。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| AT | 接入类型 | 可选必选说明：必选参数<br>参数含义：该参数用于设置待查询的用户接入门限或者PDP接入门限。<br>取值范围：<br>- “USER(用户接入)”：差异化服务触发类型为用户类型<br>- “PDP(PDP接入)”：差异化服务触发类型为PDP类型<br>默认值： 无 |
| USRPRI | 用户级别 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定待查询的用户签约QoS属性中的分配保留优先级（Allocation/Retention Priority）。<br>前提条件：此参数在<br>“AT”<br>设置为<br>“USER(用户接入)”<br>或<br>“PDP(PDP接入)”<br>时生效。<br>取值范围：<br>- “HIGHLEVELUSER(高端用户)”：分配保留优先级为1。<br>- “NORMALUSER(普通用户)”：分配保留优先级为2。<br>- “LOWLEVELUSER(低端用户)”：分配保留优先级为3。<br>默认值：无<br>说明：不输入该参数时，查询所有用户级别的接入门限。 |
| SRVLVL | 业务级别 | 可选必选说明：条件可选参数<br>参数含义：待查询的业务级别，由用户PDP上下文QoS中的流量等级（Traffic class）、下行保证速率（Guaranteed bit rate for downlink）和发送控制优先级（Traffic handling priority）确定。<br>前提条件：此参数在<br>“接入类型”<br>选取为<br>“PDP(PDP接入)”<br>时生效。<br>取值范围：<br>- “CONVERSATION(Conversation)”：流量等级为Conversational class。<br>- “STREAMINGGBRMORE25KBPS(StreamGBRMore25kbps)”：流量等级为Streaming class，下行保证速率大于等于25kbit/s。<br>- “STREAMINGGBRLESS24KBPS(StreamGBRLess24kbps)”：流量等级为Streaming class，下行保证速率小于等于24kbit/s。<br>- “INTERACTIVETRAFFICPRI1(InteractiveTrafficPri1)”：流量等级为Interactive class，发送控制优先级为1。<br>- “INTERACTIVETRAFFICPRI2(InteractiveTrafficPri2)”：流量等级为Interactive class，发送控制优先级为2。<br>- “INTERACTIVETRAFFICPRI3(InteractiveTrafficPri3)”：流量等级为Interactive class，发送控制优先级为3。<br>- “BACKGROUND(Background)”：流量等级为Background class。<br>- “NONE(None)”：通用业务级别，表示该用户没有业务级别，设置的门限就是该用户级别所有业务级别的门限。<br>默认值：无<br>说明：不输入该参数时，查询所有业务级别的接入门限。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/DIFFSERVICE]] · 差异化服务接入门限（DIFFSERVICE）

## 使用实例

查询以“PDP方式”接入，用户级别为“高端用户”，业务级别为“Background”的差异化服务配置信息：

LST DIFFSERVICE: AT=PDP, USRPRI=HIGHLEVELUSER, SRVLVL=BACKGROUND;

```
%%LST DIFFSERVICE: AT=PDP, USRPRI=HIGHLEVELUSER, SRVLVL=BACKGROUND;%%
RETCODE = 0  操作成功。

差异化服务配置表
-------------------------------------
            用户级别  =  高端用户     
            业务级别  =  Background      
PDP数负荷拒绝门限(%)  =  20      
PDP数负荷恢复门限(%)  =  10
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-DIFFSERVICE.md`
