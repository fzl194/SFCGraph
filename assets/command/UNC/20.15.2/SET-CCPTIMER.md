---
id: UNC@20.15.2@MMLCommand@SET CCPTIMER
type: MMLCommand
name: SET CCPTIMER（设置融合计费Proxy定时器）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: CCPTIMER
command_category: 配置类
applicable_nf:
- NCG
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- NCG业务及策略管理
- 融合计费Proxy定时器
status: active
---

# SET CCPTIMER（设置融合计费Proxy定时器）

## 功能

![](设置融合计费Proxy定时器（SET CCPTIMER）_45110936.assets/notice_3.0-zh-cn_2.png)

该命令用于设置定时器时间。若设置错误，可能影响与SMF应答流程或与OCS的应答流程。

**适用NF：NCG**

该命令用于设置融合计费Proxy定时器。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| TID | VALUE |
| --- | --- |
| CCTIMEOUT | 3 |
| UCITIMER | 3600 |
| RECOVERINTERVAL | 300 |
| SYSLEVELRECOVERINTERVAL | 600 |
| ONLINECDFRSP | 3 |
| OFFLINECDFRSP | 3 |
| RECOVERTOPOREQ | 1800 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TID | 定时器标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定定时器标识。<br>数据来源：本端规划<br>取值范围：<br>- “CCTIMEOUT（等待计费响应时长（秒））”：该参数用于设置NCG等待计费响应消息时长，当超过该时长，则认为计费响应消息响应失败。<br>- “UCITIMER（计费会话停止时长（秒））”：该参数用于配置NCG会话业务停止时长，超过该时长后NCG释放计费会话信息。<br>- “RECOVERINTERVAL（计费转发自动恢复间隔（秒））”：该参数用于设置在OCS响应计费消息失败， NCG会话级代OCS应答SMF计费请求的时间间隔，超时之后NCG再次尝试向OCS转发计费请求。<br>- “SYSLEVELRECOVERINTERVAL（设备级计费转发自动恢复间隔（秒））”：该参数用于设置收到标识对端不可用的返回码后，NCG设备级代OCS应答SMF计费请求的时间间隔，超时之后NCG再次尝试向OCS转发计费请求。<br>- “ONLINECDFRSP（代应答消息等待CDF回响应时长（秒））”：该参数用于设置代应答场景下AGF等待CDF回响应时长，当超过该时长，则认为CDF回响应失败。<br>- “OFFLINECDFRSP（离线消息等待CDF回响应时长（秒））”：该参数用于设置离线计费场景下AGF等待CDF回响应时长，当超过该时长，则认为CDF回响应失败。<br>- “RECOVERTOPOREQ（恢复向TOPO查询的时间间隔（秒））”：该参数用于设置某会话向TOPO查询异常后，该会话恢复向TOPO查询的时间间隔。<br>默认值：无。<br>配置原则：无 |
| VALUE | 定时器的时长 | 可选必选说明：可选参数<br>参数含义：该参数用于指定定时器的时长。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~2147483647，单位是秒。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CCPTIMER查询当前参数配置值。<br>配置原则：<br>TID=CCTIMEOUT时，VALUE取值范围为1～60。<br>TID=UCITIMER时，VALUE取值范围为60～86400。<br>TID=RECOVERINTERVAL时，VALUE取值范围为60～3600。<br>TID=SYSLEVELRECOVERINTERVAL时，VALUE取值范围为60～7200。<br>TID=ONLINECDFRSP时，VALUE取值范围为1~60。<br>TID=OFFLINECDFRSP时，VALUE取值范围为1~60。<br>TID=RECOVERTOPOREQ时，VALUE取值范围为0~3600。 |

## 操作的配置对象

- [融合计费Proxy定时器（CCPTIMER）](configobject/UNC/20.15.2/CCPTIMER.md)

## 使用实例

设置TID为CCTIMEOUT的融合计费Proxy定时器的时长为20：

```
SET CCPTIMER: TID=CCTIMEOUT, VALUE=20;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置融合计费Proxy定时器（SET-CCPTIMER）_45110936.md`
