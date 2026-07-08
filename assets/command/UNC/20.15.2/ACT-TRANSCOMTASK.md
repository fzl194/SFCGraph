---
id: UNC@20.15.2@MMLCommand@ACT TRANSCOMTASK
type: MMLCommand
name: ACT TRANSCOMTASK（激活SDR进程间透明通信检测任务）
nf: UNC
version: 20.15.2
verb: ACT
object_keyword: TRANSCOMTASK
command_category: 动作类
effect_mode: 立即生效
is_dangerous: true
category_path:
- 平台服务管理
- 服务通信管理
- 亚健康检测
status: active
---

# ACT TRANSCOMTASK（激活SDR进程间透明通信检测任务）

## 功能

![](激活SDR进程间透明通信检测任务（ACT TRANSCOMTASK）_94730385.assets/notice_3.0-zh-cn_2.png)

该命令是高危命令，操作不当可能会影响性能，请谨慎使用并联系华为技术支持协助操作。

该命令用于激活SDR进程间透明通信检测任务。

## 注意事项

- 该命令执行后立即生效。

- 执行此激活命令前需要确保DTP开关处于开启状态，执行[**LST SDRPARAMS**](../TCP开关控制/查询SDR参数（LST SDRPARAMS）_09587932.md)命令查询DTP开关状态，执行[**SET SDRPARAMS**](../TCP开关控制/设置SDR参数（SET SDRPARAMS）_09587912.md)命令设置DTP开关。
- SRCID不存在时，激活命令执行成功，但激活任务不生效。

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SRCID | 源端ID | 可选必选说明：必选参数<br>参数含义：该参数用于标识SDR进程间的透明通信质量检测的源端ID。该ID为Cell ID，可以通过使用命令<br>[**DSP MSPROCESS**](../../可靠性管理/微服务可靠性管理/显示微服务进程信息（DSP MSPROCESS）_09587887.md)<br>命令输出结果中的Process ID获取。但是Cell ID不能选为SDRE进程类型的Process ID。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：无 |
| HEADCONTENT | 指定检测报文的SDR头部的构造字段 | 可选必选说明：必选参数<br>参数含义：该参数用于指定检测报文的SDR头部的构造字段。需按"topic:xx keytype:xx groupid:xx keyvalue:xx qos:xx" 的格式指定检测报文的topic、keytype、groupid、keyvalue、qos。上述字段均为必选，若缺少会返回错误。其中topic、keytype、groupid的取值范围为0-4294967295；keyvalue的格式为十六进制、大端序，每个字节需要两个字符组成，不足两个字符的在前面补0，字符的范围：0~9或A~F，不需要加0x前缀；qos的取值范围为0-3。每两个相邻字段之间只允许1个空格，多于1个空格，命令会失败。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~1024。<br>默认值：无<br>配置原则：无 |
| PKGLENMODE | 检测报文长度的模式 | 可选必选说明：必选参数<br>参数含义：该参数用于标识SDR进程间的透明通信质量检测报文长度的模式。<br>数据来源：本端规划<br>取值范围：<br>- “MIXEDLEN（混合包长模式）”：探测报文的长度模式为混合模式，自动按预定的包长发包，覆盖不同包长，包长为1024、1500、2000，循环发送这些长度的包。<br>- “FIXEDLEN（指定包长模式）”：探测报文的长度模式为指定长度模式，包长由参数PKGLEN指定，取值范围为1024~10000，单位是字节。<br>默认值：无<br>配置原则：无 |
| PKGLEN | 检测报文的长度(字节) | 可选必选说明：该参数在"PKGLENMODE"配置为"FIXEDLEN"时为条件必选参数。<br>参数含义：该参数用于标识SDR进程间的透明通信质量检测报文的长度。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1024~10000。<br>默认值：1024<br>配置原则：无 |
| DURATION | 检测时长(秒) | 可选必选说明：可选参数<br>参数含义：该参数用于标识SDR进程间的透明通信质量检测时长。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是10~86400。<br>默认值：10<br>配置原则：无 |
| PKGRATE | 检测包速率(个/秒) | 可选必选说明：可选参数<br>参数含义：该参数用于标识SDR进程间的透明通信质量检测的检测包速率。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~1000。<br>默认值：1<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/TRANSCOMTASK]] · SDR进程间透明通信检测任务（TRANSCOMTASK）

## 使用实例

激活SDR进程间透明通信检测任务：

```
%%ACT TRANSCOMTASK: SRCID="vup-pod-010-103-0-238__121__0", HEADCONTENT="topic:10300 qos:0 keytype:12303 groupid:999 keyvalue:00000002", PKGLENMODE=FIXEDLEN, PKGLEN=1024, DURATION=60;%%
RETCODE = 0 操作成功

--- END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/激活SDR进程间透明通信检测任务（ACT-TRANSCOMTASK）_94730385.md`
