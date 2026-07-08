---
id: UDG@20.15.2@MMLCommand@SET UPGLBSCTPPARA
type: MMLCommand
name: SET UPGLBSCTPPARA（设置SCTP全局参数）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: UPGLBSCTPPARA
command_category: 配置类
applicable_nf:
- UPF
effect_mode: ''
is_dangerous: false
max_records: 1
category_path:
- 用户面服务管理
- SCTP管理
- SCTP基础参数
status: active
---

# SET UPGLBSCTPPARA（设置SCTP全局参数）

## 功能

**适用NF：UPF**

此命令用于设置SCTP全局参数。

## 注意事项

- 命令执行后对新建立的SCTP链路生效。
- 该命令最大记录数为1。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | PATHSELECTMODE | RTOMINVALUE | RTOMAXVALUE | RTOINITVALUE |
| --- | --- | --- | --- | --- |
| 初始值 | ALL | 500 | 1500 | 500 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PATHSELECTMODE | SCTP路径选择模式 | 可选必选说明：可选参数<br>参数含义：该参数用于配置SCTP耦联内使用路径的模式。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- ALL：表示SCTP耦联内的所有路径均为可用路径。<br>- PARALLEL：表示SCTP耦联内仅平行路径为可用路径。<br>默认值：无<br>配置原则：SCTP多归属耦联中，从本端IP地址到对端IP地址之间存在多条路径。当组网路由中全部路径可通时使用全路径方式。当组网限制某些路径不通时，可以不使用这些路径。 |
| RTOMINVALUE | RTO重发超时的最小值（毫秒） | 可选必选说明：可选参数<br>参数含义：该参数用于指定RTO（Retransmission Time-Out）重发超时的最小值。<br>数据来源：对端协商<br>取值范围：整数类型，取值范围为200～1000，单位是毫秒。<br>默认值：无<br>配置原则：<br>- 重发时，新“RtoMinValue (RTO最小值)” = 2 * “旧RtoMinValue (RTO最小值)”。<br>- 对于心跳间隔，正常的时长为：“HeartbeatIntval (心跳间隔)”+ “RtoMinValue (RTO最小值)”，重发的时长为：“HeartbeatIntval (心跳间隔)” + 2 * 旧“RtoMinValue (RTO最小值)”。<br>- 数据重发间隔的时长为：2 * 旧“RtoMinValue (RTO最小值)”。<br>- 此参数值必须小于或等于“RtoInitValue (RTO初始值)”并且小于“RtoMaxValue (RTO最大值)”。<br>- 建议将“RtoMinValue”设置为500毫秒。如果“RtoMinValue”小于500毫秒，请务必保证设置的RtoMinValue大于对端网元SACK延迟证实时间与传输平均时延之和。 |
| RTOMAXVALUE | RTO重发超时的最大值（毫秒） | 可选必选说明：可选参数<br>参数含义：该参数用于指定RTO（Retransmission Time-Out）重发超时的最大值。<br>数据来源：对端协商<br>取值范围：整数类型，取值范围为500～6000，单位是毫秒。<br>默认值：无<br>配置原则：此参数值必须大于“RtoMinValue (RTO最小值)”和“RtoInitValue (RTO初始值)”。 |
| RTOINITVALUE | RTO重发超时的初始值（毫秒） | 可选必选说明：可选参数<br>参数含义：该参数用于指定INIT消息的RTO重发超时的初始值。<br>数据来源：对端协商<br>取值范围：整数类型，取值范围为200～1000，单位是毫秒。<br>默认值：无<br>配置原则：<br>- 重发时，新“RtoInitValue (RTO初始值)” = 2 * 旧“RtoInitValue (RTO初始值)”，且最大不超过“RtoMaxValue (RTO最大值)”。<br>- 此参数值必须大于或等于“RtoMinValue (RTO最小值)”并且小于“RtoMaxValue (RTO最大值)”。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/UPGLBSCTPPARA]] · SCTP全局参数（UPGLBSCTPPARA）

## 使用实例

根据网络规划，需要修改SCTP全局参数，则可以按如下配置：

```
SET UPGLBSCTPPARA: PATHSELECTMODE=PARALLEL;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-UPGLBSCTPPARA.md`
