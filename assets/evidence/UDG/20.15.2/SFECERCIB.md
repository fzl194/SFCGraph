# 显示基于子接口的上行/下行业务属性表（DSP SFECERCIB）

- [命令功能](#ZH-CN_CONCEPT_0000001549962054__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000001549962054__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000001549962054__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000001549962054__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000001549962054__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0000001549962054__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0000001549962054)

该命令用于根据端口号、内外层VLAN ID显示某一特定的ICIB/ECIB表项。

#### [注意事项](#ZH-CN_CONCEPT_0000001549962054)

该命令仅适用于非NP卡场景和NP卡非加速模式场景。

#### [操作用户权限](#ZH-CN_CONCEPT_0000001549962054)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000001549962054)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TABLEID | 表类型 | 可选必选说明：必选参数<br>参数含义：用于表示待查询表项的表类型/表ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无 |
| PORTNUM | 端口号 | 可选必选说明：必选参数<br>参数含义：用于表示待查询表项所在的接口编号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～63。<br>默认值：无 |
| PEVID | 外层VLAN | 可选必选说明：必选参数<br>参数含义：用于表示外层VLAN ID的表项信息。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4095。<br>默认值：无 |
| CEVID | 内层VLAN | 可选必选说明：可选参数<br>参数含义：用于表示内层VLAN ID的表项信息。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4095。<br>默认值：无 |
| RUNAME | RU名称 | 可选必选说明：必选参数<br>参数含义：用于表示资源单元名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。区分大小写。<br>默认值：无<br>配置原则：<br>- 区分大小写，不支持空格。<br>- 使用DSP RU查看RU名称。 |

#### [使用实例](#ZH-CN_CONCEPT_0000001549962054)

显示指定资源单元、指定外层VLAN ID的CIB表项：

```
DSP SFECERCIB:TABLEID=0,PORTNUM=4,PEVID=1,RUNAME="VNODE_VNRS_VNFC_IPU_0064";
```

```

RETCODE = 0  操作成功
                                                                               
结果如下                                                       
-------------------------                                                       
      表类型  =  0                                                               
      端口号  =  4                                                               
    外层VLAN  =  1                                                               
    内层VLAN  =  2                                                               
      RU名称  =  VNODE_VNRS_VNFC_IPU_0064                                        
        结果  =  *uiEcibIndex : 00004001        
                 usPhbStruct : 0000                                                                      
                 usAclStruct : 0000                       
                 usVlanId1 : 0000                                                        
                 usVlanId2 : 0000         
                 ucVlanOpc : 0000                                          
                 uiMtu : 00000000     
                 uiWork : 00000000                        
                 usAclStruct : 0000      
                 usVrfId : 0000              
                 ucPhbType : 00                        
                 usTranslation : 0000
                 uiIfStatIndex : 00000011                             
                 uiValid : 00000001                                                              
                 usCarStat : 0000                   
                 ucIfCntEn : 00                                                      
                 ucIfStatEn : 01       
                 uiIfRateIndex : 00000011                                  
                 uiCarid : 00000000               
                 usSqid : 0000                        
                 usCtrlVid : 0000                  
                 usVlanTranslation : 0000          
                 usVlanIdMax : 0000        
                 usVlanIdMin : 0000                                                                            
                 ucAddTag : 00                         
                 ucSpecialPrune1 : 00                                                                
                 ucSpecialPrune2 : 00                 
                 ucSpecialPrune3 : 00                                                  
                 ucVlanTagProc : 00   
                 ucBdStatEnable : 00                                    
                 usIPv6MTU : 0000                        
                 ucARPDefend : 00                      
                 ucGreenAction : 00  
                 ucYellowAction : 00         
                 ucRedAction : 00    
                 ucGreenSerCls: 00                                                                           
                 ucYellowSerCls : 00                            
                 ucRedSerCls : 00                                                             
                 ucGreenColor : 00              
                 ucYellowColor : 00                                               
                 ucRedColor : 00
           
                     
(结果个数 = 1)                                                         
---    END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0000001549962054)

| 输出项名称 | 输出项解释 |
| --- | --- |
| 表类型 | 用于表示待查询表项的表类型/表ID。 |
| 端口号 | 用于表示待查询表项所在的接口编号。 |
| 外层VLAN | 用于表示外层VLAN ID的表项信息。 |
| 内层VLAN | 用于表示内层VLAN ID的表项信息。 |
| RU名称 | 用于表示资源单元名称。 |
| 结果 | 用于表示查询到对应表项的详细内容。 |
