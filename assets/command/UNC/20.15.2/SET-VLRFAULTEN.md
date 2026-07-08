---
id: UNC@20.15.2@MMLCommand@SET VLRFAULTEN
type: MMLCommand
name: SET VLRFAULTEN（设置VLR故障增强功能）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: VLRFAULTEN
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
max_records: 1
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- 可靠性管理
- VLR故障增强功能
status: active
---

# SET VLRFAULTEN（设置VLR故障增强功能）

## 功能

![](设置VLR故障增强功能(SET VLRFAULTEN)_92948544.assets/notice_3.0-zh-cn_2.png)

该命令只有未部署IMS语音，并且VLR全部故障的场景下使用，否则可能造成整网语音不可用。在VLR恢复后请及时关闭该故障增强功能。

**适用网元：MME**

该命令用于设置VLR全故障场景增强功能开关。此配置仅在已明确VLR全故障的场景下应急使用，功能默认关闭。开启VLR故障增强开关后，在VLR全故障的场景下，通过模拟用户联合附着/TAU成功响应，使用户可以驻留4G使用数据业务。

## 注意事项

- 该命令执行后立即生效。

- 此命令的最大记录数为1。

## 权限

manage-ug;system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| FAULTENSW | VLR故障增强功能开关 | 可选必选说明：可选参数<br>参数含义：该<br>**参**<br>数用于控制开启和关闭VLR全故障应急增强功能开关。功能开启后，当联合附着和联合TAU流程中CS注册失败后，MME按照联合接入成功响应UE，并且后续UE发起Extended Service Request流程时，MME可以让UE驻留4G，不回落CS域。<br>数据来源：全网规划<br>取值范围：<br>- OFF（关闭）<br>- ON（开启）<br>系统初始设置值：OFF（关闭）<br>配置原则：当VLR全部故障时，语音业务存在CS语音，但未部署IMS语音，为避免用户大批量脱网，可以开启本功能。<br>说明：用户驻留4G主要通过如下方式实现：MME收到Extended Service Request消息后返回携带#39 CS service temporarily not available原因值和T3442 value信元的Service reject消息。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/VLRFAULTEN]] · VLR故障增强功能（VLRFAULTEN）

## 使用实例

设置VLR全故障场景增强功能开启：

```
SET VLRFAULTEN: FAULTENSW=ON;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-VLRFAULTEN.md`
