---
id: UDG@20.15.2@MMLCommand@DSP LDPSSMGDSCB
type: MMLCommand
name: DSP LDPSSMGDSCB（显示LDP会话管理模块的下游信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: LDPSSMGDSCB
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- LDP维护
status: active
---

# DSP LDPSSMGDSCB（显示LDP会话管理模块的下游信息）

## 功能

该命令用于显示LDP会话管理模块的下游信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VRFNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：_public_ |
| FECFLAG | 目的地址标志位 | 可选必选说明：可选参数<br>参数含义：该参数用于表示LSP的目的地址标志位。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- FECADDR：指定目的地址。<br>默认值：无 |
| FECADDR | 目的地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“FECFLAG”配置为“FECADDR”时为必选参数。<br>参数含义：该参数用于指定LSP的目的地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无 |
| PREFIXLENGTH | 前缀长度 | 可选必选说明：条件必选参数<br>前提条件：该参数在“FECFLAG”配置为“FECADDR”时为必选参数。<br>参数含义：该参数用于指定目的地址的前缀长度。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～32。<br>默认值：无 |
| PEERID | 对等体的LSR ID | 可选必选说明：可选参数<br>参数含义：该参数用于指定对等体的LSR ID。<br>数据来源：对端协商<br>取值范围：IPv4地址类型。<br>默认值：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@LDPSSMGDSCB]] · LDP会话管理模块的下游信息（LDPSSMGDSCB）

## 使用实例

显示LDP会话管理模块的下游信息：

```
DSP LDPSSMGDSCB:VRFNAME="_public_",FECFLAG=FECADDR,FECADDR="10.10.10.10",PREFIXLENGTH=32;
```

```

RETCODE = 0  操作成功。

结果如下
--------
                              VPN实例名称  =  _public_
                                 目的地址  =  10.10.10.10
                                 前缀长度  =  32
                           对等体的LSR ID  =  10.10.22.33
               向下游发送的标签请求消息ID  =  0x0
                                   出标签  =  32768
                          LSP最大传输单元  =  1500
                                 下游状态  =  建立完成
                                 标签状态  =  标签建立完成
                                 通告状态  =  未通告
                                 订阅标志  =  未订阅
     备升主后是否已完成切换并处于激活状态  =  是
发送标签请求消息的指数回退定时器的值（s）  =  0
                            LDP会话版本号  =  1
                           订阅平滑版本号  =  0
                        LDP邻居备份版本号  =  0
                                   组件ID  =  0x1c0037
                     下游控制块创建的时间  =  2017-11-16 03:08:38
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-LDPSSMGDSCB.md`
