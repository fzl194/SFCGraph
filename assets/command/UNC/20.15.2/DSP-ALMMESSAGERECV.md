---
id: UNC@20.15.2@MMLCommand@DSP ALMMESSAGERECV
type: MMLCommand
name: DSP ALMMESSAGERECV（查询告警接收的信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: ALMMESSAGERECV
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务公共功能管理
- 操作维护
- 告警管理
- 告警接收
status: active
---

# DSP ALMMESSAGERECV（查询告警接收的信息）

## 功能

该命令用于查询告警接收的信息，可以据此定位是否接收到告警信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TARGET | 目标 | 可选必选说明：必选参数<br>参数含义：目标组件。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- NETCONF：NETCONF组件。<br>默认值：无 |
| TYPE | 消息类型 | 可选必选说明：必选参数<br>参数含义：告警接收信息消息类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- GET-ALARM：告警同步。<br>默认值：无 |
| BOARDTYPE | 主控类型 | 可选必选说明：可选参数<br>参数含义：指定主控类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- master：主主控。<br>- slave：备主控。<br>默认值：master |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/ALMMESSAGERECV]] · 告警接收的信息（ALMMESSAGERECV）

## 使用实例

查询告警同步接收Notification的信息：

```
DSP ALMMESSAGERECV:TARGET=NETCONF,TYPE=GET-ALARM
,SERVICEINSTANCE="vnfc"
;
```

```
RETCODE = 0  操作成功

结果如下:
-------------------------
接收时间               传输序列号     传输标志位 

2016-05-29 17:50:36    92864513       最终报文      
2016-05-29 17:53:42    92864514       中间报文 
(结果个数 = 2)
--- END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询告警接收的信息（DSP-ALMMESSAGERECV）_59103706.md`
