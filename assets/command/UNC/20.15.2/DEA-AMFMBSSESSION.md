---
id: UNC@20.15.2@MMLCommand@DEA AMFMBSSESSION
type: MMLCommand
name: DEA AMFMBSSESSION（去激活AMF组播广播会话）
nf: UNC
version: 20.15.2
verb: DEA
object_keyword: AMFMBSSESSION
command_category: 动作类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 5G组播广播管理
- AMF组播广播管理
- 去活AMF组播广播会话
status: active
---

# DEA AMFMBSSESSION（去激活AMF组播广播会话）

## 功能

![](去激活AMF组播广播会话（DEA AMFMBSSESSION）_87947654.assets/notice_3.0-zh-cn_2.png)

执行该命令，AMF会通知广播区域下所有基站释放广播会话，且删除本地广播上下文。

该操作可能会导致AMF和MB-SMF上广播会话状态不一致，同时AMF和基站、MB-SMF间交互消息量增大，待会话删除完成后，系统会恢复正常。

**适用NF：AMF**

该命令用于去激活AMF组播广播会话。

## 注意事项

- 该命令执行后立即生效。

- 当AMF上广播会话残留时，可以使用该命令删除广播会话。其他场景请谨慎使用该命令。
- 删除操作执行成功，仅表示AMF开始删除广播会话，删除过程AMF需要和大量基站交互，执行时间较长，可以执行DSP AMFMBSSESSIONCTX命令查询广播会话删除结果。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SESSIONTYPE | 会话类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定去激活的会话类型。<br>数据来源：本端规划<br>取值范围：<br>- BROADCAST（广播）<br>默认值：无<br>配置原则：无 |
| DEATYPE | 去活方式 | 可选必选说明：必选参数<br>参数含义：该参数用于指定广播会话的去活方式。<br>数据来源：本端规划<br>取值范围：<br>- TMGI（TMGI）<br>默认值：无<br>配置原则：无 |
| MCC | 移动国家代码 | 可选必选说明：该参数在"DEATYPE"配置为"TMGI"时为条件必选参数。<br>参数含义：该参数用于指定移动国家代码。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是3。<br>默认值：无<br>配置原则：无 |
| MNC | 移动网号 | 可选必选说明：该参数在"DEATYPE"配置为"TMGI"时为条件必选参数。<br>参数含义：该参数用于指定移动网号。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是2~3。<br>默认值：无<br>配置原则：无 |
| MBSSERVICEID | 组播广播服务标识 | 可选必选说明：该参数在"DEATYPE"配置为"TMGI"时为条件必选参数。<br>参数含义：该参数用于指定广播服务标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是6。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [AMF组播广播会话（AMFMBSSESSION）](configobject/UNC/20.15.2/AMFMBSSESSION.md)

## 使用实例

去激活MCC为123、MNC为45、TMGI为123456的广播会话，执行如下命令：

```
DEA AMFMBSSESSION:SESSIONTYPE=BROADCAST,DEATYPE=TMGI,MCC="123",MNC="45",MBSSERVICEID="123456";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/去激活AMF组播广播会话（DEA-AMFMBSSESSION）_87947654.md`
