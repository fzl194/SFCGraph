---
id: UNC@20.15.2@MMLCommand@LST ARPPARA
type: MMLCommand
name: LST ARPPARA（查询ARP策略参数配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: ARPPARA
command_category: 查询类
applicable_nf:
- SGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- QoS管理
- Pre-R8 QoS
- QoS应用
- ARP转换
status: active
---

# LST ARPPARA（查询ARP策略参数配置）

## 功能

**适用网元：SGSN**

该命令用于查询ARP策略参数配置。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GROUPID | ARP策略组 | 可选必选说明：可选参数<br>参数含义：用于指定“用户级别”和“业务级别”共同确定的记录归属的ARP策略组。<br>数据来源：整网规划<br>取值范围：<br>- “G0(系统缺省组)”<br>- “G1(自定义组1)”<br>- “G2(自定义组2)”<br>- “G3(自定义组3)”<br>- “G4(自定义组4)”<br>- “G5(自定义组5)”<br>- “G6(自定义组6)”<br>- “G7(自定义组7)”<br>- “G8(自定义组8)”<br>- “G9(自定义组9)”<br>默认值：无<br>说明：- “用户级别”和“业务级别”参数在同一个ARP策略组下最多只能配置21条记录，“ARP策略组”、“用户级别”和“业务级别”三者唯一确定一条记录。<br>- “ARP策略组”为“G0(系统缺省组)”的记录是系统默认配置，只能修改其对应的ARP属性值，不能被删除，用于系统缺省场景下对全网用户的取值。<br>- 最多只能配置10组记录。 |
| USRPRI | 用户级别 | 可选必选说明：可选参数<br>参数含义：该参数用于指定用户级别，根据用户协商QoS属性中的分配保留优先级（Allocation/Retention Priority）确定。<br>数据来源：整网规划<br>取值范围：<br>- “HIGHLEVELUSER(高端用户)”：核心网侧协商的ARP为1。<br>- “NORMALUSER(普通用户)”：核心网侧协商的ARP为2。<br>- “LOWLEVELUSER(低端用户)”：核心网侧协商的ARP为3。<br>默认值：无 |
| SRVLVL | 业务级别 | 可选必选说明：可选参数<br>参数含义：该参数用于指定业务级别。根据用户PDP上下文QoS中的流量等级（Traffic class），下行保证速率（Guaranteed bit rate for downlink）和发送控制优先级（Traffic handling priority）确定。<br>数据来源：整网规划<br>取值范围：<br>- “CONVERSATION(Conversation)”：流量等级为Conversational class。<br>- “STREAMINGGBRMORE25KBPS(StreamingGBRMore25kbps)”：流量等级为Streaming class，下行保证速率大于等于25kbit/s。<br>- “STREAMINGGBRLESS24KBPS(StreamingGBRLess24kbps)”：流量等级为Streaming class，下行保证速率小于25kbit/s。<br>- “INTERACTIVETRAFFICPRI1(InteractiveTrafficPri1)”：流量等级为Interactive class，发送控制优先级为1。<br>- “INTERACTIVETRAFFICPRI2(InteractiveTrafficPri2)”：流量等级为Interactive class，发送控制优先级为2。<br>- “INTERACTIVETRAFFICPRI3(InteractiveTrafficPri3)”：流量等级为Interactive class，发送控制优先级为3。<br>- “BACKGROUND(Background)”：流量等级为Background class。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/ARPPARA]] · ARP策略参数配置（ARPPARA）

## 使用实例

1. 查询所有的ARPPARA配置信息：
  LST ARPPARA:;
  ```
  %%LST ARPPARA:;%%
  RETCODE = 0  操作成功。

  输出结果如下
  --------------
   ARP策略组   用户级别  业务级别                承载优先级  抢占性        被抢占性    排队属性    描述  

   系统缺省组  高端用户  Conversation            4           可能触发抢占  不允许抢占  允许排队    NULL  
   系统缺省组  高端用户  StreamingGBRMore25kbps  5           可能触发抢占  不允许抢占  允许排队    NULL  
   系统缺省组  高端用户  StreamingGBRLess24kbps  5           可能触发抢占  不允许抢占  允许排队    NULL  
   系统缺省组  高端用户  InteractiveTrafficPri1  6           可能触发抢占  不允许抢占  允许排队    NULL  
   系统缺省组  高端用户  InteractiveTrafficPri2  6           可能触发抢占  不允许抢占  允许排队    NULL  
   系统缺省组  高端用户  InteractiveTrafficPri3  6           可能触发抢占  不允许抢占  允许排队    NULL  
   系统缺省组  高端用户  Background              7           可能触发抢占  不允许抢占  允许排队    NULL  
   系统缺省组  普通用户  Conversation            7           可能触发抢占  允许抢占    允许排队    NULL  
   系统缺省组  普通用户  StreamingGBRMore25kbps  8           可能触发抢占  允许抢占    允许排队    NULL  
   系统缺省组  普通用户  StreamingGBRLess24kbps  8           可能触发抢占  允许抢占    允许排队    NULL  
   系统缺省组  普通用户  InteractiveTrafficPri1  9           可能触发抢占  允许抢占    允许排队    NULL  
   系统缺省组  普通用户  InteractiveTrafficPri2  9           可能触发抢占  允许抢占    允许排队    NULL  
   系统缺省组  普通用户  InteractiveTrafficPri3  9           可能触发抢占  允许抢占    允许排队    NULL  
   系统缺省组  普通用户  Background              10          可能触发抢占  允许抢占    允许排队    NULL  
   系统缺省组  低端用户  Conversation            10          不触发抢占    允许抢占    不允许排队  NULL  
   系统缺省组  低端用户  StreamingGBRMore25kbps  11          不触发抢占    允许抢占    不允许排队  NULL  
   系统缺省组  低端用户  StreamingGBRLess24kbps  11          不触发抢占    允许抢占    不允许排队  NULL  
   系统缺省组  低端用户  InteractiveTrafficPri1  12          不触发抢占    允许抢占    不允许排队  NULL  
   系统缺省组  低端用户  InteractiveTrafficPri2  12          不触发抢占    允许抢占    不允许排队  NULL  
   系统缺省组  低端用户  InteractiveTrafficPri3  12          不触发抢占    允许抢占    不允许排队  NULL  
   系统缺省组  低端用户  Background              13          不触发抢占    允许抢占    不允许排队  NULL  
  (结果个数 = 21)

  ---    END
  ```
2. 查询ARP策略组为“系统缺省组（G0）”，用户级别为“HIGHLEVELUSER(高端用户)”，业务级别为“CONVERSATION(Conversation)”的配置信息：LST ARPPARA: GROUPID=G0, USRPRI=HIGHLEVELUSER, SRVLVL=CONVERSATION;
  ```
  %%LST ARPPARA: GROUPID=G0, USRPRI=HIGHLEVELUSER, SRVLVL=CONVERSATION;%%
  RETCODE = 0  操作成功。

  输出结果如下
  --------------
   ARP策略组  =  系统缺省组
    用户级别  =  高端用户
    业务级别  =  Conversation
  承载优先级  =  4
      抢占性  =  可能触发抢占
    被抢占性  =  不允许抢占
    排队属性  =  允许排队
        描述  =  NULL
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-ARPPARA.md`
