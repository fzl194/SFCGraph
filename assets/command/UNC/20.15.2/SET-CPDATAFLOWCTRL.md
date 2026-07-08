---
id: UNC@20.15.2@MMLCommand@SET CPDATAFLOWCTRL
type: MMLCommand
name: SET CPDATAFLOWCTRL（设置CP Data流控参数）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: CPDATAFLOWCTRL
command_category: 配置类
applicable_nf:
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 操作维护
- 设备管理
- 流控管理
- 业务流控管理
- CP Data控制管理
status: active
---

# SET CPDATAFLOWCTRL（设置CP Data流控参数）

## 功能

**适用网元：MME**

此命令用于设置CP Data流控参数。

## 注意事项

无。

## 权限

manage-ug；system-ug。
G_1，管理员级别命令组；G_2，操作员级别命令组。

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CPDATACPUFLOWSW | CP Data CPU过载流控功能开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定MME CPU过载时，是否开启CP Data的流控功能。功能开启后，如果MME的CPU过载，MME将对使用WSFD-<br>215101<br>基于信令面的数据传输特性的终端进行流控，在Attach Accept、Tau Accept、Service Accept、Service Reject消息中携带Control Plane data back-off timer T3448，通知终端延迟发送数据，缓解MME的系统过载状况。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- OFF（关闭）。<br>- ON （打开）。<br>系统初始设置值：OFF（关闭）<br>配置原则：<br>- 系统目前暂不支持。 |
| MINT3448 | T3448最小值（秒） | 可选必选说明：可选参数<br>参数含义：本参数用于设置Control Plane data back-off timer T3448的最小值，用于计算发给终端的Attach Accept、Tau Accept、Service Accept、Service Reject消息中的T3448时长。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～11160。<br>系统初始设置值：900。<br>配置原则：<br>- 该参数的取值必须小于等于“T3448最大值”的取值。<br>- 系统目前暂不支持。 |
| MAXT3448 | T3448最大值（秒） | 可选必选说明：可选参数<br>参数含义：本参数用于设置Control Plane data back-off timer T3448的最大值，用于计算发给终端的Attach Accept、Tau Accept、Service Accept、Service Reject消息中的T3448时长。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～11160。<br>系统初始设置值：1800。<br>配置原则：<br>- 该参数的取值必须大于等于“T3448最小值”的取值。<br>- 系统目前暂不支持。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/CPDATAFLOWCTRL]] · CP Data流控参数（CPDATAFLOWCTRL）

## 使用实例

设置 “CP Data CPU过载流控功能开关” 为 “ON” ， “T3448最小值（秒）” 为 “500” 和 “T3448最大值（秒）” 为 “800” ：

SET CPDATAFLOWCTRL:CPDATACPUFLOWSW=ON,MINT3448 = 500,MAXT3448 = 800;

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置CP-Data流控参数(SET-CPDATAFLOWCTRL)_72345769.md`
