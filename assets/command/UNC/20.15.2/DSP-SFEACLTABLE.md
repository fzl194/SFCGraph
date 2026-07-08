---
id: UNC@20.15.2@MMLCommand@DSP SFEACLTABLE
type: MMLCommand
name: DSP SFEACLTABLE（查询SFE ACL表项）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: SFEACLTABLE
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

# DSP SFEACLTABLE（查询SFE ACL表项）

## 功能

该命令用来根据报文内容查询SFE ACL动作信息。

该命令为工程师维护使用。当出现因ACL导致的流量不通时，可使用该命令进行帮助定位。

## 注意事项

该命令仅适用于非NP卡场景和NP卡非加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ACLTYPE | ACL类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定ACL规则的类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- IPv4-ACL：IPv4-ACL类型。<br>- IPv6-ACL：IPv6-ACL类型。<br>- IPv4-Flow-ACL：IPv4-Flow-ACL类型。<br>- IPv6-Flow-ACL：IPv6-Flow-ACL类型。<br>默认值：无 |
| SRCPORT | 源端口号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定报文的源端口号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65535。<br>默认值：无 |
| DESTPORT | 目的端口号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定报文的目的端口号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65535。<br>默认值：无 |
| SRCIP | 源IP地址 | 可选必选说明：条件可选参数<br>前提条件：该参数在“ACLTYPE”配置为“IPv4-ACL” 或 “IPv4-Flow-ACL”时为可选参数。<br>参数含义：该参数用于指定报文的源IP地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无 |
| DESTIP | 目的IP地址 | 可选必选说明：条件可选参数<br>前提条件：该参数在“ACLTYPE”配置为“IPv4-ACL” 或 “IPv4-Flow-ACL”时为可选参数。<br>参数含义：该参数用于指定报文的目的IP地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无 |
| PROTOCOLNUM | 协议号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定报文的协议号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～255。<br>默认值：0 |
| FRAGMENTV4 | IPv4分片类型 | 可选必选说明：条件可选参数<br>前提条件：该参数在“ACLTYPE”配置为“IPv4-ACL”时为可选参数。<br>参数含义：该参数用于指定IPv4报文的分片类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- fragment：检查分片的报文。<br>- fragment-spe-first：检查分片报文中的首片。<br>- fragment-subseq：检查分片报文中的后续片。<br>- non-fragment：检查不分片报文。<br>- non-subseq：检查分片报文中的首片，或不分片报文。<br>默认值：无 |
| FRAGMENTV6 | IPv6分片类型 | 可选必选说明：条件可选参数<br>前提条件：该参数在“ACLTYPE”配置为“IPv6-ACL”时为可选参数。<br>参数含义：该参数用于指定IPv6报文的分片类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- fragment：检查IPv6分片报文。<br>- non-fragment：检查IPv6不分片报文。<br>默认值：无 |
| TP | 接口号 | 可选必选说明：条件必选参数<br>前提条件：该参数在“ACLTYPE”配置为“IPv4-ACL” 或 “IPv6-ACL”时为必选参数。<br>参数含义：该参数用于指定流策略应用的接口编号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65535。<br>默认值：无 |
| VLANID | VLAN ID | 可选必选说明：条件可选参数<br>前提条件：该参数在“ACLTYPE”配置为“IPv4-ACL” 或 “IPv6-ACL”时为可选参数。<br>参数含义：该参数用于指定VLAN ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65535。<br>默认值：无 |
| RUNAME | 资源单元名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定资源单元名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：使用DSP RU查看RU名称。 |
| SRCIPV6 | 源IPv6地址 | 可选必选说明：条件可选参数<br>前提条件：该参数在“ACLTYPE”配置为“IPv6-ACL” 或 “IPv6-Flow-ACL”时为可选参数。<br>参数含义：该参数用于指定IPv6报文的源地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。<br>默认值：无 |
| DESTIPV6 | 目的IPv6地址 | 可选必选说明：条件可选参数<br>前提条件：该参数在“ACLTYPE”配置为“IPv6-ACL” 或 “IPv6-Flow-ACL”时为可选参数。<br>参数含义：该参数用于指定IPv6报文的目的地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。<br>默认值：无 |
| TOS | TOS | 可选必选说明：条件可选参数<br>前提条件：该参数在“ACLTYPE”配置为“IPv4-ACL”时为可选参数。<br>参数含义：该参数用于指定报文的TOS值。TOS表示报文的服务类型（IPv4）。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～15。<br>默认值：无 |
| TC | TC | 可选必选说明：条件可选参数<br>前提条件：该参数在“ACLTYPE”配置为“IPv6-ACL”时为可选参数。<br>参数含义：该参数用于指定报文的TC值。TC表示报文的服务类型（IPv6）。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～15。<br>默认值：无 |
| DSCP | DSCP | 可选必选说明：条件可选参数<br>前提条件：该参数在“ACLTYPE”配置为“IPv4-ACL” 或 “IPv6-ACL”时为可选参数。<br>参数含义：该参数用于指定报文的DSCP值。DSCP表示报文的差分服务代码点。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～63。<br>默认值：无 |
| IPPRE | 报文IP优先级 | 可选必选说明：条件可选参数<br>前提条件：该参数在“ACLTYPE”配置为“IPv4-ACL” 或 “IPv6-ACL”时为可选参数。<br>参数含义：该参数用于指定报文的IP优先级。取值越大优先级越高。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～7。<br>默认值：无 |
| TTL | 报文TTL值 | 可选必选说明：条件可选参数<br>前提条件：该参数在“ACLTYPE”配置为“IPv4-ACL” 或 “IPv6-ACL”时为可选参数。<br>参数含义：该参数用于指定报文的TTL值。TTL表示报文在网络中的生存时间。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～255。<br>默认值：无 |
| ICMPTYPE | ICMP报文类型 | 可选必选说明：条件可选参数<br>前提条件：该参数在“ACLTYPE”配置为“IPv4-ACL” 或 “IPv6-ACL”时为可选参数。<br>参数含义：该参数用于指定ICMP报文类型。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～255。<br>默认值：无 |
| ICMPCODE | ICMP报文代码 | 可选必选说明：条件可选参数<br>前提条件：该参数在“ACLTYPE”配置为“IPv4-ACL” 或 “IPv6-ACL”时为可选参数。<br>参数含义：该参数用于指定ICMP报文代码。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～255。<br>默认值：无 |
| VPNID | VPN ID | 可选必选说明：条件可选参数<br>前提条件：该参数在“ACLTYPE”配置为“IPv4-Flow-ACL” 或 “IPv6-Flow-ACL”时为可选参数。<br>参数含义：该参数用于指定VPN ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SFEACLTABLE]] · SFE ACL表项（SFEACLTABLE）

## 使用实例

- 查询指定资源单元、指定接口、指定协议号的SFE IPv4 ACL表项信息：
  ```
  DSP SFEACLTABLE:RUNAME="VNODE_VNRS_VNFC_IPU_0064",ACLTYPE=IPv4-ACL,PROTOCOLNUM=17,TP=3;
  ```
  ```

  RETCODE = 0  操作成功。                                                 
                                                                                
  结果如下                                                        
  ------------------------        
                         统计使能标志  =  FALSE
                             动作索引  =  0
                             动作映射  =  64
                             过滤类型  =  允许
                           重标记DSCP  =  0
                          重标记Dot1p  =  0
                     重标记IP分片标记  =  0
                      ACL动作URPF类型  =  0
                        ACL动作Car ID  =  0
                       重定向Chain ID  =  0
                          重标记Tos值  =  15                                              
                       重标记IP优先级  =  3                                               
                  绿色报文Car动作类型  =  0                                               
      绿色报文Car动作重标记服务优先级  =  0                                               
            绿色报文Car动作重标记颜色  =  0                                               
                  黄色报文Car动作类型  =  0                                               
      黄色报文Car动作重标记服务优先级  =  0                                               
            黄色报文Car动作重标记颜色  =  0                                                 
                  红色报文Car动作类型  =  0                                               
      红色报文Car动作重标记服务优先级  =  0                                               
            红色报文Car动作重标记颜色  =  0  
                           重定向类型  =  IPv4-Redirect-NHP+TBTP
                   重定向下一跳IP地址  =  192.168.1.1
                        重定向VPN索引  =  0
                         重定向目标RU  =  65
                       重定向目标端口  =  3
                        重定向VLAN ID  =  0
                      重定向VPN组VRF1  =  65535
                      重定向VPN组VRF2  =  65535
                      重定向VPN组VRF3  =  65535
                      重定向VPN组VRF4  =  65535
                      重定向VPN组VRF5  =  65535
                      重定向VPN组VRF6  =  65535
                      重定向VPN组VRF7  =  65535
                      重定向VPN组VRF8  =  65535    
                     下行统计使能标志  =  FALSE
                         下行动作索引  =  0
                         下行动作映射  =  0
                         下行过滤类型  =  允许
                       下行重标记DSCP  =  0
                      下行重标记Dot1p  =  0
                       下行重标记IPDF  =  0
                      下行重标记Tos值  =  0
                   下行重标记IP优先级  =  0
                    下行ACL动作Car ID  =  0
              下行绿色报文Car动作类型  =  0                                               
  下行绿色报文Car动作重标记服务优先级  =  0                                               
        下行绿色报文Car动作重标记颜色  =  0                                               
              下行黄色报文Car动作类型  =  0                                               
  下行黄色报文Car动作重标记服务优先级  =  0                                               
        下行黄色报文Car动作重标记颜色  =  0                                                 
              下行红色报文Car动作类型  =  0                                               
  下行红色报文Car动作重标记服务优先级  =  0                                               
        下行红色报文Car动作重标记颜色  =  0 

  (结果个数 = 1)                                                         
  ---    END
  ```
- 查询指定资源单元、指定接口、指定协议号的SFE IPv6 ACL表项信息：
  ```
  DSP SFEACLTABLE:RUNAME="VNODE_VNRS_VNFC_IPU_0064",ACLTYPE=IPv6-ACL,PROTOCOLNUM=58,TP=3;
  ```
  ```

  RETCODE = 0  操作成功。

  结果如下
  ------------------------                                                        
                         统计使能标志  =  FALSE                                               
                             动作索引  =  1                                                   
                             动作映射  =  129                                                 
                             过滤类型  =  Deny                                                
                           重标记DSCP  =  0                                                   
                          重标记Dot1p  =  0 
                      ACL动作URPF类型  =  0
                        ACL动作Car ID  =  0
                       重定向Chain ID  =  0
                          重标记Tos值  =  15                                              
                       重标记IP优先级  =  3                                               
                  绿色报文Car动作类型  =  0                                               
      绿色报文Car动作重标记服务优先级  =  0                                               
            绿色报文Car动作重标记颜色  =  0                                               
                  黄色报文Car动作类型  =  0                                               
      黄色报文Car动作重标记服务优先级  =  0                                               
            黄色报文Car动作重标记颜色  =  0                                                 
                  红色报文Car动作类型  =  0                                               
      红色报文Car动作重标记服务优先级  =  0                                               
            红色报文Car动作重标记颜色  =  0      
                           重定向类型  =  Redirect-VPN-Group
                 重定向下一跳IPv6地址  =  :: 
                        重定向VPN索引  =  0                                                   
                         重定向目标RU  =  65
                       重定向目标端口  =  3
                        重定向VLAN ID  =  0                                                                          
                      重定向VPN组VRF1  =  2                                                   
                      重定向VPN组VRF2  =  65535                                               
                      重定向VPN组VRF3  =  65535                                               
                      重定向VPN组VRF4  =  65535                                               
                      重定向VPN组VRF5  =  65535                                               
                      重定向VPN组VRF6  =  65535                                               
                      重定向VPN组VRF7  =  65535                                               
                      重定向VPN组VRF8  =  65535
                     下行统计使能标志  =  FALSE
                         下行动作索引  =  0
                         下行动作映射  =  0
                         下行过滤类型  =  允许
                       下行重标记DSCP  =  0
                      下行重标记Dot1p  =  0
                      下行重标记Tos值  =  0
                   下行重标记IP优先级  =  0
                    下行ACL动作Car ID  =  0
              下行绿色报文Car动作类型  =  0                                               
  下行绿色报文Car动作重标记服务优先级  =  0                                               
        下行绿色报文Car动作重标记颜色  =  0                                               
              下行黄色报文Car动作类型  =  0                                               
  下行黄色报文Car动作重标记服务优先级  =  0                                               
        下行黄色报文Car动作重标记颜色  =  0                                                 
              下行红色报文Car动作类型  =  0                                               
  下行红色报文Car动作重标记服务优先级  =  0                                               
        下行红色报文Car动作重标记颜色  =  0 
  
  (结果个数 = 1)                                                         
  ---    END
  ```
- 查询指定资源单元、指定协议号、指定VPN ID的SFE IPv4引流ACL表项信息：
  ```
  DSP SFEACLTABLE:RUNAME="VNODE_VNRS_VNFC_IPU_0064",ACLTYPE=IPv4-Flow-ACL,PROTOCOLNUM=3,VPNID=3;
  ```
  ```

  RETCODE = 0  操作成功。

  结果如下
  ------------------------                                                        
                     RE表项索引  =  3                                               
                        VPN索引  =  5
                        服务ID   =  2
                     Gi服务标志  =  1                                                                                                                                               
  (结果个数 = 1)                                                         
  ---    END
  ```
- 查询指定资源单元、指定协议号、指定VPN ID的SFE IPv6引流ACL表项信息：
  ```
  DSP SFEACLTABLE:RUNAME="VNODE_VNRS_VNFC_IPU_0064",ACLTYPE=IPv6-Flow-ACL,PROTOCOLNUM=58,VPNID=3;
  ```
  ```

  RETCODE = 0  操作成功。

  结果如下
  ------------------------                                                        
                     RE表项索引  =  3                                               
                        VPN索引  =  5
                        服务ID   =  2
                     Gi服务标志  =  1       
  (结果个数 = 1)                                                         
  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-SFEACLTABLE.md`
