---
id: UDG@20.15.2@MMLCommand@DSP SFEBFDERECV
type: MMLCommand
name: DSP SFEBFDERECV（显示BFD-ERECV表）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: SFEBFDERECV
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- 转发引擎实例FEI
- BFD报文接收表
status: active
---

# DSP SFEBFDERECV（显示BFD-ERECV表）

## 功能

该命令用于显示指定资源单元上指定本端描述符的BFD报文出方向接收信息表。

## 注意事项

该命令仅适用于非NP卡场景和NP卡非加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LOCALDISCRI | 本端描述符 | 可选必选说明：必选参数<br>参数含义：指定本端描述符。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65535。<br>默认值：无 |
| RUNAME | RU名称 | 可选必选说明：必选参数<br>参数含义：指定资源单元名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。区分大小写。<br>默认值：无<br>配置原则：<br>- 区分大小写，不支持空格。<br>- 使用DSP RU查看RU名称。 |

## 操作的配置对象

- [BFD-ERECV表（SFEBFDERECV）](configobject/UDG/20.15.2/SFEBFDERECV.md)

## 使用实例

显示指定资源单元的BFD-ERECV表项：

```
DSP SFEBFDERECV:RUNAME="VNODE_VNRS_VNFC_IPU_0066",LOCALDISCRI=16391;
```

```

RETCODE = 0  操作成功                                                
                                                                                
结果如下                                                       
-------------------------                                                       
           RU名称  =  VNODE_VNRS_VNFC_IPU_0066                                 
             结果  =   *MyDiscr : 00004007                 Status : 01                                                                 
                      FirstFlag : 01                           TC : 00                                                   
                    PacketState : 00                   RemoteDiag : 00                                     
                     RecPktInfo : 00000000                Counter : 00000001 
                          Timer : 000000004cf99ac0     EntryIndex : 000000b0                
                          Valid : 0001                    BfdFlag : 0000                    
                        BfdType : 0001                  PwdLength : 0000                    
                         DetNum : 0003                BfdGlbIndex : 00000001  
                                                                                
                                                                                
(结果个数 = 2)                                                         
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示BFD-ERECV表（DSP-SFEBFDERECV）_49961770.md`
