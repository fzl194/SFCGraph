---
id: UDG@20.15.2@MMLCommand@DSP SFEBLKBOX
type: MMLCommand
name: DSP SFEBLKBOX（显示SFE黑匣子）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: SFEBLKBOX
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- 转发引擎实例FEI
- SFE黑匣子
status: active
---

# DSP SFEBLKBOX（显示SFE黑匣子）

## 功能

该命令用于显示指定资源单元上的SFE黑匣子信息。

## 注意事项

该命令仅适用于非NP卡场景和NP卡非加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| BOXID | 黑匣子ID | 可选必选说明：必选参数<br>参数含义：指定黑匣子ID。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4：指定类型为ipv4的黑匣子。<br>- ipv6-route：指定类型为ipv6-route的黑匣子。<br>- mc：指定类型为mc的黑匣子。<br>- qos：指定类型为qos的黑匣子。<br>- cpu-defend：指定类型为cpu-defend的黑匣子。<br>- sfe：指定类型为sfe的黑匣子。<br>- bfd：指定类型为bfd的黑匣子。<br>- ipv4-nexthop：指定类型为ipv4-nexthop的黑匣子。<br>- fim：指定类型为fim的黑匣子。<br>- mc-brief：指定类型为mc-brief的黑匣子。<br>- frame：指定类型为frame的黑匣子。<br>- frame-error：指定类型为frame-error的黑匣子。<br>- frame-message：指定类型为frame-message的黑匣子。<br>- frame-performance：指定类型为frame-performance的黑匣子。<br>- fwd-smooth：指定类型为fwd-smooth的黑匣子。<br>- tblm-tpi：指定类型为tblm-tpi的黑匣子。<br>- tblm-cst：指定类型为tblm-cst的黑匣子。<br>- tblm-frm：指定类型为tblm-frm的黑匣子。<br>- ipv4-arp：指定类型为ipv4-arp的黑匣子。<br>- ipv6-nd：指定类型为ipv6-nd黑匣子。<br>- bfd-event：指定类型为bfd-event的黑匣子。<br>- fim-stat：指定类型为fim-stat的黑匣子。<br>- gre：指定类型为gre的黑匣子。<br>- pbuf-leak：指定类型为pbuf-leak的黑匣子。<br>- ipv6-nexthop：指定类型为ipv6-nexthop的黑匣子。<br>- ip-trace：指定类型为ip-trace的黑匣子。<br>- fei-ipsec：指定类型为fei-ipsec的黑匣子。<br>- xst：指定类型为xst的黑匣子。<br>- mpls：指定类型为mpls的黑匣子。<br>- ffm：指定类型为ffm的黑匣子。<br>- if-vlan：指定类型为if-vlan的黑匣子。<br>- l2：指定类型为l2的黑匣子。<br>- devmlib：指定类型为devmlib的黑匣子。<br>- ha：指定类型为ha的黑匣子。<br>- channel：指定类型为channel的黑匣子。<br>- overload：指定类型为overload的黑匣子。<br>- log：指定类型为log的黑匣子。<br>默认值：无 |
| RUNAME | RU名称 | 可选必选说明：必选参数<br>参数含义：资源单元名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。区分大小写。<br>默认值：无<br>配置原则：<br>- 区分大小写，不支持空格。<br>- 使用DSP RU查看RU名称。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@SFEBLKBOX]] · SFE黑匣子（SFEBLKBOX）

## 使用实例

显示指定资源单元的SFE黑匣子信息：

```
DSP SFEBLKBOX:BOXID=frame,RUNAME="VNODE_VNRS_VNFC_IPU_0066";
```

```
RETCODE = 0  操作成功

结果如下
-------------------------
时间戳                      结果                                                                                                 
                                                                                                                                    
[2018-06-26 10:20:33:145]    MODULE:15, PARAM-MAIN:3176, PARAM:                                                                     
 [FEI]:CONSTRUCT_STAGE3 has completed!                                                                                              
[2018-06-26 10:20:33:145]    MODULE:15, PARAM-MAIN:3021, PARAM:                                                                     
 [FEI]:CONSTRUCT_STAGE3:Init SaveLcsAssignCfg!                                                                                      
[2018-06-26 10:20:27:095]    MODULE:15, PARAM-MAIN:2915, PARAM:                                                                     
 [FEI]:CONSTRUCT_STAGE3: Init module OK!                                                                                            
[2018-06-26 10:20:27:075]    MODULE:15, PARAM-MAIN:301, PARAM:                                                                      
----BlackBox FRAME Module----                                                                                                       
                                                                                 
(结果个数 = 4)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-SFEBLKBOX.md`
