---
id: UDG@20.15.2@MMLCommand@SET SBITCPPARA
type: MMLCommand
name: SET SBITCPPARA（设置SBI接口TCP控制参数）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: SBITCPPARA
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- HTTP功能管理
- HTTP管理
- TCP安全管理
status: active
---

# SET SBITCPPARA（设置SBI接口TCP控制参数）

## 功能

![](设置SBI接口TCP控制参数（SET SBITCPPARA）_83813644.assets/notice_3.0-zh-cn.png)

该参数需要进行全网规划，根据对端的连接能力进行设置，阈值设置过低可能会导致正常的SBI连接失败。

该命令用于设置TCP SYN包流控阈值以及单个IP的最大TCP连接数。TCP SYN报文数量过大，可能导致系统无法接收正常的TCP连接请求。通过该命令设置相关参数可以预防TCP SYN Flood攻击，保护系统正常运行。

> **说明**
> - 该命令执行后立即生效。
>
> - 该命令参数SYNPKTFCTHD设置TCP SYN报文流控阈值的功能仅在POD内生效；若TLB开关打开，则TCP SYN流控还受到[**SET TLBGLBCONF**](../HTTP服务端负载管理/整系统负载管理/全局属性/设置TLB全局配置（SET TLBGLBCONF）_69954926.md)命令设置的TLBRCVSYNTHD参数和RPTDTSYNTHD参数影响。
>
> - 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：
>
> | SYNPKTFCTHD | PEERIPCONNLIMIT |
> | --- | --- |
> | 5000 | 0 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SYNPKTFCTHD | SYN包流控阈值(pps) | 可选必选说明：可选参数<br>参数含义：该参数用于指定SYN包流控的阈值。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1000~50000，单位是包每秒。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SBITCPPARA查询当前参数配置值。<br>配置原则：无 |
| PEERIPCONNLIMIT | 单个对端IP连接限制数 | 可选必选说明：可选参数<br>参数含义：该参数用于当本端作为Server时，单个TCP进程对于单个Client IP地址的连接数限制。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0，64~1024，单位是个。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SBITCPPARA查询当前参数配置值。<br>配置原则：<br>当需要连接数控制，避免出现连接攻击时，配置该参数。配置0则表示不限制链接数。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/SBITCPPARA]] · SBI接口TCP控制参数（SBITCPPARA）

## 使用实例

设置TCP SYN报文流控阈值为20000，TCP连接数上限为500。

```
SET SBITCPPARA:SYNPKTFCTHD=20000,PEERIPCONNLIMIT=500;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置SBI接口TCP控制参数（SET-SBITCPPARA）_83813644.md`
