---
id: UDG@20.15.2@MMLCommand@SET SACOMMONPARA
type: MMLCommand
name: SET SACOMMONPARA（设置SA业务公共参数）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: SACOMMONPARA
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 1
category_path:
- 用户面服务管理
- 业务匹配策略
- 业务过滤器管理
- 七层规则管理
- SA公共参数
status: active
---

# SET SACOMMONPARA（设置SA业务公共参数）

## 功能

**适用NF：PGW-U、UPF**

该命令用来配置SA业务相关控制参数。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- NoRstPktNum参数配置过小会导致报文解析提前返回失败，影响规则匹配。请合理配置取值，NoRstPktNum参数不建议过小。
- NoRstPktNum默认值0表示不开启此控制功能，即不通过NoRstPktNum配置值控制确定业务的报文数。
- QuicIdenFuncEn和QuicPsrFuncEn开关只针对Quic密文业务增强SA能力，Quic明文业务不涉及。
- QuicIdenFuncEn和QuicPsrFuncEn开关值设置为ENABLE对虚拟机处理性能有至少5%的消耗，开关开启需要咨询华为工程师。
- QuicSaSw开关只针对Quic明文业务增强SA能力，Quic密文业务不涉及。
- SPECMETHODSW参数配置修改后，60s后生效。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | NORSTPKTNUM | CDNENHANCEDSW | QUICSASW | USRRLTRFRSHSW | QUICIDENFUNCEN | QUICPSRFUNCEN | SPECMETHODSW |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 初始值 | 0 | DISABLE | DISABLE | DISABLE | DISABLE | DISABLE | DISABLE |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NORSTPKTNUM | 没有确定业务的报文的个数 | 可选必选说明：可选参数<br>参数含义：控制连续多少个报文没有确定业务，则确定业务。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～255。<br>默认值：无<br>配置原则：无 |
| CDNENHANCEDSW | CDN增强识别功能 | 可选必选说明：可选参数<br>参数含义：该参数用于指定是否开启CDN识别增强功能。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能（关闭）。<br>- ENABLE：使能（开启）。<br>默认值：无<br>配置原则：无 |
| QUICSASW | Quic SA协议确定后进行匹配的开关 | 可选必选说明：可选参数<br>参数含义：该参数用于设置在QUIC SA协议识别状态确定后进行策略匹配的开关。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE：不使能（关闭）。<br>- ENABLE：使能（开启）。<br>默认值：无<br>配置原则：无 |
| USRRLTRFRSHSW | 用户关联识别刷新开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定是否开启协议识别的刷新功能。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能（关闭）。<br>- ENABLE：使能（开启）。<br>默认值：无<br>配置原则：如果想要延长协议的用户关联时间，可以设置该参数为ENABLE。 |
| QUICIDENFUNCEN | Quic协议识别功能增强 | 可选必选说明：可选参数<br>参数含义：该参数用于指定是否开启对全加密Quic承载应用的协议识别增强功能。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能（关闭）。<br>- ENABLE：使能（开启）。<br>默认值：无<br>配置原则：无 |
| QUICPSRFUNCEN | Quic协议解析功能增强 | 可选必选说明：可选参数<br>参数含义：该参数用于指定是否开启对全加密Quic承载应用的协议解析增强功能。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能（关闭）。<br>- ENABLE：使能（开启）。<br>默认值：无<br>配置原则：无 |
| SPECMETHODSW | HTTP特殊方法解析开关 | 可选必选说明：可选参数<br>参数含义：该参数用于设置HTTP特殊方法解析开关。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能（关闭）。<br>- ENABLE：使能（开启）。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/SACOMMONPARA]] · SA业务公共参数（SACOMMONPARA）

## 关联任务

- [[UDG@20.15.2@Task@0-00154]]

## 使用实例

控制连续多少个报文没有确定业务，则确定业务：

```
SET SACOMMONPARA:  NORSTPKTNUM=4;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置SA业务公共参数（SET-SACOMMONPARA）_82837416.md`
