---
id: UDG@20.15.2@MMLCommand@DSP SFECERPORT
type: MMLCommand
name: DSP SFECERPORT（显示指定端口出/入方向的表项）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: SFECERPORT
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- 转发引擎实例FEI
- SFE表项统计
status: active
---

# DSP SFECERPORT（显示指定端口出/入方向的表项）

## 功能

该命令用于显示指定端口出/入方向的表项。

## 注意事项

该命令仅适用于非NP卡场景和NP卡非加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TABLEID | 表ID | 可选必选说明：必选参数<br>参数含义：用于表示需要查询的表项。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无 |
| TPINDEX | 目标端口索引 | 可选必选说明：必选参数<br>参数含义：用于表示目的端口索引的表项。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65535。<br>默认值：无 |
| RUNAME | RU名称 | 可选必选说明：必选参数<br>参数含义：用于表示资源单元名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。区分大小写。<br>默认值：无<br>配置原则：<br>- 区分大小写，不支持空格。<br>- 使用DSP RU查看RU名称。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@SFECERPORT]] · 指定端口出/入方向的表项（SFECERPORT）

## 使用实例

显示指定资源单元、指定表类型、指定目标端口索引的IPAT表项：

```
DSP SFECERPORT:TABLEID=0,TPINDEX=4,RUNAME="VNODE_VNRS_VNFC_IPU_0064";
```

```

RETCODE = 0  操作成功                                               
                                                                                
结果如下                                                       
-------------------------                                                       
           资源单元编号  =  64                                                   
                   表ID  =  0                                                    
           目标端口索引  =  4                                                    
                 RU名称  =  VNODE_VNRS_VNFC_IPU_0064                             
                   结果  =  *uiIpatIndex : 00000004                      
                            usMacHi16 : 0050                                                           
                            uiMacLow32 : 568ffc0a        
                            usTagType : 0004                                             
                            VrfId : 0000 
                            uiPortEncapType : 00000000                                                                                                           
                            uiFwdType : 00000000                        
                            ucIpv4Enable : 00000001                                                                            
                            uiAclType : 00000000             
                            usTrustType : 0000                                                       
                            usMTU : 0000        
                            uiIfStatIndex : 00040000                                                                 
                            usQidxColorBaTid : 0000                      
                            uiwork : 00000001   
                            uiIpv6AclKey : 00000000    
                            uiSIT1 : 00000003                                     
                            uiSIT2 : 00000000             
                            uiDfltRt : 00000000                                                            
                            uiType : 00000000    
                            uiAclLocation : 00000000                                                                   
                            usGid : 0000               
                            usCarCntId : 0000                                                                               
                            usVpnRedirectFlag : 0000               
                            usUntagSubIfEn : 0000                                                                 
                            usRedirectVpnID : 0000                  
                            uiIfRateIndex : 00000004                                               
                            ucIfCntEn : 01      
                            ucIfStatEn : 01                                       
                            ucDHCPSnpEnable : 01             
                            uctrustenable : 00                                                                                          
                            ucDHCPAddrCheck : 00           
                            ucDHCPIPCheck : 00                                                                                   
                            ucDHCPArpCheck : 00                 
                            ucAlarmChaddrFlag :00                                                                             
                            ucAlarmIpFlag : 00    
                            ucAlarmArpFlag : 00                                                               
                            ucAlarmReplyFlag : 00                
                            ucArpDefend : 00000000                                           
                            ucVrrpEnNum : 0000
                            IPv6Enable : 0000                                                                                                               
                            usTpID : 00                                                                    
                                                                                                                                                         
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-SFECERPORT.md`
