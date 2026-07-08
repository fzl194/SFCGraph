---
id: UNC@20.15.2@MMLCommand@SET E2ETRCCFG
type: MMLCommand
name: SET E2ETRCCFG（设置端到端用户跟踪参数）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: E2ETRCCFG
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 跟踪配置管理
- 端到端用户跟踪管理
status: active
---

# SET E2ETRCCFG（设置端到端用户跟踪参数）

## 功能

**适用网元：MME**

此命令用于设置端到端用户跟踪参数。端到端用户跟踪是指同时在多个网元上对指定用户进行呼叫信令跟踪，各个网元将跟踪结果发送到网管。

## 注意事项

- 该命令执行后立即生效。
- ENBPAGING参数功能需要核心网先开启，基站后开启，否则该功能在基站上无法生效，需要基站重新开启该功能或者重建链后才能生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SGS | 是否上报SGs接口消息 | 可选必选说明：可选参数<br>参数含义：该参数用于设置当MME存在端到端用户跟踪任务时，是否上报SGs接口消息到网管。<br>数据来源：整网规划<br>取值范围：<br>- “YES(是)”<br>- “NO(否)”<br>系统初始设置值：<br>“YES(是)” |
| SV | 是否上报Sv接口消息 | 可选必选说明：可选参数<br>参数含义：该参数用于设置当MME存在端到端用户跟踪任务时，是否上报Sv接口消息到网管。<br>数据来源：整网规划<br>取值范围：<br>- “YES(是)”<br>- “NO(否)”<br>系统初始设置值：<br>“YES(是)” |
| ENBPAGING | 基站上报寻呼消息开关 | 可选必选说明：可选参数<br>参数含义：该参数用于设置<br>**eNodeB**<br>在端到端用户跟踪中上报寻呼消息功能开关。当开关开启后，MME在给支持此功能的<br>**eNodeB**<br>发送的寻呼消息中，指示<br>**eNodeB**<br>上报寻呼消息。<br>数据来源：整网规划<br>取值范围：<br>- “OFF（关闭）”<br>- “ON（打开）”<br>系统初始设置值：“OFF（关闭）”<br>配置原则：该功能只在对接华为<br>**eNodeB**<br>时支持。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/E2ETRCCFG]] · 端到端用户跟踪参数（E2ETRCCFG）

## 使用实例

在分析CSFB和SRVCC流程相关问题过程中，需要上报SGs和Sv接口消息到网管时，设置“是否上报SGs接口消息(SGS)”参数为“YES(是)”、“是否上报SV接口消息(SV)”参数为“YES(是)”，配置格式如下：

SET E2ETRCCFG: SGS=YES, SV=YES;

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-E2ETRCCFG.md`
