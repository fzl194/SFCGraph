---
id: UNC@20.15.2@MMLCommand@MOD GUREDIRPLCY
type: MMLCommand
name: MOD GUREDIRPLCY（修改GU重定向策略）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: GUREDIRPLCY
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 移动性管理
- GU重定向策略管理
status: active
---

# MOD GUREDIRPLCY（修改GU重定向策略）

## 功能

**适用网元：MME**

此命令用于修改GU重定向策略。

## 注意事项

- 此命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| AREA | 区域范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定区域的标识类型。<br>数据来源：整网规划<br>取值范围：<br>- “PLMN(PLMN)”：表示该区域标识类型为指定PLMN区域。<br>- “TA(指定跟踪区)”：表示该区域标识类型为指定跟踪区。<br>默认值：无<br>说明：本表“区域范围”为“PLMN(PLMN)”的记录可以与“区域范围”为“TA(指定跟踪区)”的记录共存；“区域范围”为“TA(指定跟踪区)”的记录优先级更高。 |
| MCC | 移动国家码 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定移动国家代码。<br>前提条件：该参数在<br>“AREA(区域范围)”<br>参数设置为<br>“TA(指定跟踪区)”<br>或者<br>“PLMN(PLMN)”<br>时，才需要配置。<br>数据来源：整网规划<br>取值范围：3位的十进制数字<br>默认值：无 |
| MNC | 移动网号 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定移动网号。<br>前提条件：该参数在<br>“AREA(区域范围)”<br>参数设置为<br>“TA(指定跟踪区)”<br>或者<br>“PLMN(PLMN)”<br>时，才需要配置。<br>数据来源：整网规划<br>取值范围：2～3位的十进制数字<br>默认值：无 |
| TAC | 跟踪区域码 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定跟踪区域码。<br>前提条件：该参数在<br>“AREA(区域范围)”<br>参数设置为<br>“TA(指定跟踪区)”<br>时，才需要配置。<br>数据来源：整网规划<br>取值范围：0x0000～0xFFFF<br>默认值：无 |
| GUREDIRPLCY | redir-policy取值 | 可选必选说明：条件可选参数<br>参数含义：<br>该参数用于指定是否允许向GERAN或者UTRAN 进行不安全的重定向<br>。<br>数据来源：整网规划<br>取值范围：<br>- "ALLOWED(Unsecured redirection to GERAN or UTRAN allowed)"<br>- "NOT_ALLOWED(Unsecured redirection to GERAN or UTRAN not allowed)"<br>默认值：<br>"ALLOWED(Unsecured redirection to GERAN or UTRAN allowed)"<br>说明：redir-policy（Redirection to GERAN or UTRAN security policy）为Network policy信元中标识位，协议取值定义如下：<br>0：Unsecured redirection to GERAN or UTRAN allowed<br>1：Unsecured redirection to GERAN or UTRAN not allowed<br>用于指示UE能否向GERAN或者UTRAN 进行不安全的重定向，其它详细描述参考24.301。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@GUREDIRPLCY]] · GU重定向策略（GUREDIRPLCY）

## 使用实例

修改一条GU重定向策略配置， “区域范围” 为 “PLMN” ， “移动国家码” 为460， **“移动网号”** 为01， “redir-policy取值” 为 “ALLOWED” ：

MOD GUREDIRPLCY: AREA=PLMN, MCC="460", MNC="01", GUREDIRPLCY=ALLOWED;

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-GUREDIRPLCY.md`
