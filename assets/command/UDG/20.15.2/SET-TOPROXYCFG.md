---
id: UDG@20.15.2@MMLCommand@SET TOPROXYCFG
type: MMLCommand
name: SET TOPROXYCFG（设置TCP代理配置）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: TOPROXYCFG
command_category: 配置类
applicable_nf:
- UPF
effect_mode: 对新流生效
is_dangerous: false
max_records: 1
category_path:
- TCP优化服务管理
- TCP代理配置
status: active
---

# SET TOPROXYCFG（设置TCP代理配置）

## 功能

**适用NF：UPF**

该命令用于设置TCP代理配置。

## 注意事项

- 该命令执行后对新数据流生效。
- 该命令最大记录数为1。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | LINKPARALLELSWITCH | TCPLINGERTIMESWITCH | SESSIONCHECKSWITCH | UEKEEPALIVESWITCH | TCPPACINGSWITCH | AUTOADJPARASWITCH | QUICKACKSWITCH | READBUFFERTIME | CHALLENGEACKLIMIT | TCPTIMESTAMPS | TCPRTT | TCPRTTVAR | TCPSYNCOOKIES |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 初始值 | DISABLE | DISABLE | ENABLE | DISABLE | DISABLE | DISABLE | DISABLE | 8 | 2147483647 | 1 | 100 | 200 | ENABLE |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LINKPARALLELSWITCH | TCP并行建链模式开关 | 可选必选说明：可选参数<br>参数含义：设置并行建链开关。<br>数据来源：全网规划<br>取值范围：<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |
| TCPLINGERTIMESWITCH | 延时关闭链接开关 | 可选必选说明：可选参数<br>参数含义：设置TCP代理收到Server侧RST拆链报文时，TCP代理是否延迟给UE侧发RST拆链报文。<br>数据来源：全网规划<br>取值范围：<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |
| SESSIONCHECKSWITCH | 非正常链路核查功能开关 | 可选必选说明：可选参数<br>参数含义：设置是否开启TCP左右侧非正常链路核查功能。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |
| UEKEEPALIVESWITCH | UE侧KEEPALIVE功能开关 | 可选必选说明：可选参数<br>参数含义：设置UE侧KEEPALIVE功能开关。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |
| TCPPACINGSWITCH | TCP Pacing功能开关 | 可选必选说明：可选参数<br>参数含义：设置TCP代理pacing功能开关。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |
| AUTOADJPARASWITCH | 参数自适应功能开关 | 可选必选说明：可选参数<br>参数含义：设置TCP代理参数自适应功能，当开启该功能后，TCP代理根据网络RTT和 重传率自动调节TCPWMEMMAX和TCPRMEMMAX以及TCPPACINGSWITCH参数大小。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |
| QUICKACKSWITCH | 快速ACK开关 | 可选必选说明：可选参数<br>参数含义：设置是否按照快速ACK方式回复ACK给对端。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |
| READBUFFERTIME | 单次从TCP socket读取的报文数目 | 可选必选说明：可选参数<br>参数含义：设置单次从TCP socket读取的报文数目。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围1～20。<br>默认值：无<br>配置原则：当前版本该参数已废弃。 |
| CHALLENGEACKLIMIT | TCP代理收到异常ACK后回复ACK的数量 | 可选必选说明：可选参数<br>参数含义：设置TCP代理收到异常ACK后回复ACK的数量。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围0～2147483647。<br>默认值：无<br>配置原则：无 |
| TCPTIMESTAMPS | TCP时间戳选项 | 可选必选说明：可选参数<br>参数含义：设置TCP时间戳选项。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围0~2。<br>默认值：无<br>配置原则：无 |
| TCPRTT | 每条流的初始RTT | 可选必选说明：可选参数<br>参数含义：设置每条流的初始RTT。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围0～10000。<br>默认值：无<br>配置原则：无 |
| TCPRTTVAR | 每条流的初始RTTVAR | 可选必选说明：可选参数<br>参数含义：设置每条流的初始RTTVAR。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围0～10000。<br>默认值：无<br>配置原则：无 |
| TCPSYNCOOKIES | 是否开启syncookies功能 | 可选必选说明：可选参数<br>参数含义：设置是否开启syncookies功能。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/TOPROXYCFG]] · TCP代理配置（TOPROXYCFG）

## 使用实例

开启TCP并行建链模式开关，开启延时关闭链接开关，开启非正常链路核查功能开关，开启UE侧KEEPALIVE功能开关，开启TCP Pacing功能开关，开启参数自适应功能开关，开启快速ACK开关，设置单次从TCP socket读取的报文数目为8，设置TCP代理收到异常ACK后回复ACK的数量为2147483647，关闭TCP时间戳选项，设置每条流的初始RTT为50，设置每条流的初始RTTVAR为50，开启syncookies功能：

```
SET TOPROXYCFG: LINKPARALLELSWITCH=ENABLE, TCPLINGERTIMESWITCH=ENABLE, SESSIONCHECKSWITCH=ENABLE, UEKEEPALIVESWITCH=ENABLE, TCPPACINGSWITCH=ENABLE, AUTOADJPARASWITCH=ENABLE, QUICKACKSWITCH=ENABLE, READBUFFERTIME=8, CHALLENGEACKLIMIT=2147483647, TCPTIMESTAMPS=0, TCPRTT=50, TCPRTTVAR=50, TCPSYNCOOKIES=ENABLE;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-TOPROXYCFG.md`
