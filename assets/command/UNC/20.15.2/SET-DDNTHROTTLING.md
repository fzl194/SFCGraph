---
id: UNC@20.15.2@MMLCommand@SET DDNTHROTTLING
type: MMLCommand
name: SET DDNTHROTTLING（设置DDN Throttling功能）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: DDNTHROTTLING
command_category: 配置类
applicable_nf:
- SGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 接入管理运维
- 流控管理
- DDN Throttling功能开关
status: active
---

# SET DDNTHROTTLING（设置DDN Throttling功能）

## 功能

**适用NF：SGW-C、SMF**

该命令用于设置DDN Throttling功能的开关。

## 注意事项

- 该命令执行后立即生效。

- DDN Throttling开启后可能会影响下行寻呼。
- 当开关由ENABLE设置为DISABLE，已经创建的流控任务不会清除。开关关闭期间，UNC不会处理MME下发的DDN Throttling策略，当开关重新开启后，流控任务会按照开关关闭前的策略继续流控，直到流控策略超时。
- DDN Throttling功能开启后，会根据DDN消息的优先级进行流控。高优先级业务流触发的DDN消息不流控。当低优先级业务流触发的DDN消息被全部或部分流控时，最低优先级业务流触发的DDN消息会被全部流控。
- DDN消息优先级可以配置，各命令的优先顺序从高到低是ADD DDNPRIORITYARP，ADD DDNPRIORITYAPN，SET DDNUSERTYPEPRI。只有高优先级命令没有配置时，才会根据低优先级命令的配置识别DDN消息优先级。例如：APN为huawei.com，ARP为2的业务流触发DDN消息，如果配置了ADD DDNPRIORITYARP，该DDN消息就被识别为ADD DDNPRIORITYARP配置的优先级。如果没有配置ADD DDNPRIORITYARP，才会判断有没有配置ADD DDNPRIORITYAPN。如果配置了ADD DDNPRIORITYAPN，该DDN消息就被识别为ADD DDNPRIORITYAPN配置的优先级；依此类推。如果这几条命令都没有配置，所有的DDN消息都被识别为低优先级消息。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| DDNTHROTSWITCH |
| --- |
| DISABLE |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DDNTHROTSWITCH | DDN Throttling功能开关 | 可选必选说明：必选参数<br>参数含义：该参数用于控制DDN Throttling功能是否开启。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE（不使能）<br>- ENABLE（使能）<br>默认值：无。<br>配置原则：无 |

## 操作的配置对象

- [DDN Throttling功能（DDNTHROTTLING）](configobject/UNC/20.15.2/DDNTHROTTLING.md)

## 使用实例

DDN消息较多，对MME/S4-SGSN造成了一定的冲击，需要配置DDNTHROTTLING命令为ENABLE：

```
SET DDNTHROTTLING: DDNTHROTSWITCH=ENABLE;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置DDN-Throttling功能（SET-DDNTHROTTLING）_04284723.md`
