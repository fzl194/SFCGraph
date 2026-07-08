---
id: UDG@20.15.2@MMLCommand@DSP SFELOCALIP
type: MMLCommand
name: DSP SFELOCALIP（显示LOCAL-IP表项）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: SFELOCALIP
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

# DSP SFELOCALIP（显示LOCAL-IP表项）

## 功能

该命令用于根据目的IP地址、源IP地址和VPN编号显示LOCAL-IP表项。

## 注意事项

该命令仅适用于非NP卡场景和NP卡非加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DESTINATION | 目的IP地址 | 可选必选说明：必选参数<br>参数含义：地址借用的目的IP地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无 |
| SOURCE | 源IP地址 | 可选必选说明：必选参数<br>参数含义：地址借用的源IP地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无 |
| VPN | VPN编号 | 可选必选说明：必选参数<br>参数含义：使用的VPN编号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无 |
| RUNAME | RU名称 | 可选必选说明：必选参数<br>参数含义：资源单元名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。区分大小写。<br>默认值：无<br>配置原则：<br>- 区分大小写，不支持空格。<br>- 使用DSP RU查看RU名称。 |

## 操作的配置对象

- [LOCAL-IP表项（SFELOCALIP）](configobject/UDG/20.15.2/SFELOCALIP.md)

## 使用实例

显示指定资源单元的LOCAL-IP表项：

```
DSP SFELOCALIP:DESTINATION="192.168.1.1",SOURCE="192.168.1.2",VPN=0,RUNAME="VNODE_VNRS_VNFC_IPU_0064";
```

```

RETCODE = 0  操作成功                                                 
                                                                                
结果如下                                                       
------------------------                                                        
               RU名称  =  VNODE_VNRS_VNFC_IPU_0064                              
           目的IP地址  =  192.168.1.1                                          
             源IP地址  =  192.168.1.2                                          
              VPN编号  =  0                                                     
             隧道编号  =  128                                                   
        IPsec接口索引  =  65                                                    
           目的RU索引  =  66                                                                                                                                
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示LOCAL-IP表项（DSP-SFELOCALIP）_00865501.md`
