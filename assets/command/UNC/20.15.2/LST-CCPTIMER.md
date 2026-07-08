---
id: UNC@20.15.2@MMLCommand@LST CCPTIMER
type: MMLCommand
name: LST CCPTIMER（查询融合计费Proxy定时器）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: CCPTIMER
command_category: 查询类
applicable_nf:
- NCG
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NCG业务及策略管理
- 融合计费Proxy定时器
status: active
---

# LST CCPTIMER（查询融合计费Proxy定时器）

## 功能

**适用NF：NCG**

该命令用于查询融合计费Proxy定时器。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TID | 定时器标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定定时器标识。<br>数据来源：本端规划<br>取值范围：<br>- “CCTIMEOUT（等待计费响应时长（秒））”：该参数用于设置NCG等待计费响应消息时长，当超过该时长，则认为计费响应消息响应失败。<br>- “UCITIMER（计费会话停止时长（秒））”：该参数用于配置NCG会话业务停止时长，超过该时长后NCG释放计费会话信息。<br>- “RECOVERINTERVAL（计费转发自动恢复间隔（秒））”：该参数用于设置在OCS响应计费消息失败， NCG会话级代OCS应答SMF计费请求的时间间隔，超时之后NCG再次尝试向OCS转发计费请求。<br>- “SYSLEVELRECOVERINTERVAL（设备级计费转发自动恢复间隔（秒））”：该参数用于设置收到标识对端不可用的返回码后，NCG设备级代OCS应答SMF计费请求的时间间隔，超时之后NCG再次尝试向OCS转发计费请求。<br>- “ONLINECDFRSP（代应答消息等待CDF回响应时长（秒））”：该参数用于设置代应答场景下AGF等待CDF回响应时长，当超过该时长，则认为CDF回响应失败。<br>- “OFFLINECDFRSP（离线消息等待CDF回响应时长（秒））”：该参数用于设置离线计费场景下AGF等待CDF回响应时长，当超过该时长，则认为CDF回响应失败。<br>- “RECOVERTOPOREQ（恢复向TOPO查询的时间间隔（秒））”：该参数用于设置某会话向TOPO查询异常后，该会话恢复向TOPO查询的时间间隔。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/CCPTIMER]] · 融合计费Proxy定时器（CCPTIMER）

## 使用实例

查询TID为CCTIMEOUT的融合计费Proxy定时器的时长：

```
LST CCPTIMER: TID=CCTIMEOUT;
RETCODE = 0  操作成功

结果如下
--------
  定时器标识  =  等待计费响应时长(秒)
定时器的时长  =  20
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询融合计费Proxy定时器（LST-CCPTIMER）_45110919.md`
