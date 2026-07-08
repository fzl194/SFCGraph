# 显示指定端口出/入方向的表项（DSP SFECERPORT）

- [命令功能](#ZH-CN_CONCEPT_0000001600841581__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000001600841581__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000001600841581__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000001600841581__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000001600841581__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0000001600841581__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0000001600841581)

该命令用于显示指定端口出/入方向的表项。

#### [注意事项](#ZH-CN_CONCEPT_0000001600841581)

该命令仅适用于非NP卡场景和NP卡非加速模式场景。

#### [操作用户权限](#ZH-CN_CONCEPT_0000001600841581)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000001600841581)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TABLEID | 表ID | 可选必选说明：必选参数<br>参数含义：用于表示需要查询的表项。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无 |
| TPINDEX | 目标端口索引 | 可选必选说明：必选参数<br>参数含义：用于表示目的端口索引的表项。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65535。<br>默认值：无 |
| RUNAME | RU名称 | 可选必选说明：必选参数<br>参数含义：用于表示资源单元名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。区分大小写。<br>默认值：无<br>配置原则：<br>- 区分大小写，不支持空格。<br>- 使用DSP RU查看RU名称。 |

#### [使用实例](#ZH-CN_CONCEPT_0000001600841581)

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

#### [输出结果说明](#ZH-CN_CONCEPT_0000001600841581)

| 输出项名称 | 输出项解释 |
| --- | --- |
| 资源单元编号 | 用于表示资源单元编号。 |
| 表ID | 用于表示需要查询的表项。 |
| 目标端口索引 | 用于表示目的端口索引的表项。 |
| RU名称 | 用于表示资源单元名称。 |
| 结果 | 用于表示查询到对应表项的详细内容。 |
