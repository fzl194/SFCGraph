---
id: UNC@20.15.2@MMLCommand@SET TMAPINTF
type: MMLCommand
name: SET TMAPINTF（设置Tm接口参数）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: TMAPINTF
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- Tm接口管理
- Tm接口参数管理
status: active
---

# SET TMAPINTF（设置Tm接口参数）

## 功能

**适用NF：MME**

本命令用于控制Tm接口的管理参数。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LPORT | Tm接口侦听端口号 | 可选必选说明：可选参数<br>参数含义：本参数用于指定Tm接口的侦听端口号。<br>数据来源：全网规划<br>取值范围：20001~65534<br>系统初始设置值：29527<br>配置原则：该参数需要和对端协商，避免两端设置不一致。 |
| TUDPCHK | Tm接口UDP校验功能 | 可选必选说明：可选参数<br>参数含义：本参数用于控制Tm接口的UDP层启用或关闭校验功能。<br>数据来源：全网规划<br>取值范围：<br>- “OFF(关闭)”<br>- “ON(开启)”<br>系统初始设置值：ON<br>配置原则：当需要提升Tm接口消息的传输可靠性，建议将参数设为ON。 |
| ECHOSIG | ECHO Request探测 | 可选必选说明：可选参数<br>参数含义：该参数控制是否发送Echo Request进行路径管理。<br>数据来源：全网规划<br>取值范围：<br>- “OFF(关闭)”<br>- “ON(开启)”<br>系统初始设置值：ON |
| TMEI | ECHO探测间隔（s） | 可选必选说明：可选参数<br>参数含义：该参数定义了Tm接口路径上发送Echo Request的间隔时间。<br>数据来源：本端规划<br>取值范围：60~3600s<br>系统初始设置值：60s |
| PEERRECOVERYSW | 对端Recovery处理开关 | 可选必选说明：可选参数<br>参数含义：该参数用于控制对端Recovery值变化时，是否通知业务层进行处理。<br>数据来源：全网规划<br>取值范围：<br>- “OFF(关闭)”<br>- “ON(开启)”<br>系统初始设置值：ON |
| DNSTMPATHFILTERSW | 过滤故障状态的Tm路径开关 | 可选必选说明：可选参数<br>参数含义：该参数用于针对DNS解析的IP地址列表，是否根据Tm路径状态过滤故障状态的对端地址。当Tm路径不存在时，不进行Tm路径状态的判断。<br>数据来源：全网规划<br>取值范围：<br>- “OFF(关闭)”<br>- “ON(开启)”<br>系统初始设置值：ON<br>配置原则：开关开启时，DNS解析结果只使用非故障状态的Tm路径的IP地址列表(目前只支持一个对端IP地址)；开关关闭时，不进行Tm路径状态的判断。 |
| NESTATUSTHRESHOLD | 容灾探测故障门限 | 可选必选说明：可选参数<br>参数含义：该参数定义了MME主动探测TSN容灾状态的故障门限。MME发起容灾探测，期间持续接收不到TSN的响应，当连续探测周期数大于该门限值时，则认为TSN故障。<br>数据来源：全网规划<br>取值范围：1~100<br>系统初始设置值：4 |
| SWDURATION | TSN倒换等待时长（秒） | 可选必选说明：可选参数<br>参数含义：TSN发生主备倒换时，MME等待TSN升主通知的时长。<br>数据来源：全网规划<br>取值范围：1s~900s<br>系统初始设置值：120s |

## 操作的配置对象

- [[configobject/UNC/20.15.2/TMAPINTF]] · Tm接口参数（TMAPINTF）

## 使用实例

当现网需要使用宽带集群系统时，本命令用于设置Tm接口的管理参数，可执行此命令：

```
SET TMAPINTF:LPORT=29527;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置Tm接口参数(SET-TMAPINTF)_88088456.md`
