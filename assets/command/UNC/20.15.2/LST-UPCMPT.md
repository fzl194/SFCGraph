---
id: UNC@20.15.2@MMLCommand@LST UPCMPT
type: MMLCommand
name: LST UPCMPT（查询UP节点协议兼容性配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: UPCMPT
command_category: 查询类
applicable_nf:
- SGW-C
- PGW-C
- SMF
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- PFCP接口管理
- UP管理
- UP节点协议兼容性管理
status: active
---

# LST UPCMPT（查询UP节点协议兼容性配置）

## 功能

**适用NF：SGW-C、PGW-C、SMF、GGSN**

该命令用于查询UP节点协议兼容性配置。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| UPFINSTANCEID | UPF实例标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定UPF实例标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~36。参数必须满足以下约束规则：1.如果输入为uuid格式（格式例如：a6a61c6f-0d3a-4221-b1da-424eda3ccf67）只能为A-F、a-f、0-9的字符。2.如果输入不为uuid格式，长度不能超过18且不允许输入只包含0-9和“.”的字符串，例如：1.2.3.4、不允许输入只包含十六进制数（A-F、a-f、0-9）和“:”的字符串，例如：1::2、FBFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF。不区分大小写。<br>默认值：无<br>配置原则：<br>该参数取值应与ADD UPNODE中参数“NFINSTANCENAME”保持一致，使用该前需通过ADD UPNODE添加一组记录。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@UPCMPT]] · UP节点协议兼容性配置（UPCMPT）

## 使用实例

查询UPF实例标识为upf_instance_1的UP节点协议兼容性配置，执行如下命令：

```
%%LST UPCMPT: UPFINSTANCEID="upf_instance_1";%%
RETCODE = 0  操作成功

结果如下
--------
                                      UPF实例标识  =  upf_instance_1
                                  APN/DNN编码格式  =  不携带OI信息
                             网络切片选择辅助信息  =  继承
                          Node ID信元FQDN编码格式  =  点分格式
                             是否携带地址池占位符  =  继承全局
                 是否携带运营商定制的RAT Type信元  =  不使能
           是否携带运营商定制的L2TP User Info信元  =  不使能
         是否携带运营商定制的L2TP Tunnel Info信元  =  不使能
是否携带运营商定制的User Location Information信元  =  不使能
             是否携带UE IP Address信元的S/D标记位  =  不使能
                      网络实例Domian Name编码格式  =  点分格式
                                  是否支持OpenUPF  =  不支持OpenUPF
                           UPF Pa接口配置严格匹配  =  关闭Pa接口严格匹配
                                     L2TP隧道信息  =  不使能
                                  L2TP用户PCO信息  =  不使能
                            Http重定向对端接口值  =  Core
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-UPCMPT.md`
