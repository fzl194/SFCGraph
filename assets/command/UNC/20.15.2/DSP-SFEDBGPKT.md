---
id: UNC@20.15.2@MMLCommand@DSP SFEDBGPKT
type: MMLCommand
name: DSP SFEDBGPKT（显示调测捕获报文）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: SFEDBGPKT
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- 转发引擎实例FEI
- 软转发调测报文
status: active
---

# DSP SFEDBGPKT（显示调测捕获报文）

## 功能

该命令用来显示调测捕获报文。

## 注意事项

- 该命令执行后立即生效。
- 报文头长度过长情形可能不会显示所有的报文内容。
- 该命令仅适用于非NP卡场景和NP卡非加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | 资源单元名称 | 可选必选说明：可选参数<br>参数含义：该参数用来表示资源单元名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～60。<br>默认值：无<br>配置原则：<br>- 区分大小写，不支持空格。<br>- 使用DSP RU查看RU名称。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SFEDBGPKT]] · 调测捕获报文（SFEDBGPKT）

## 使用实例

显示资源单元名称为“VNODE_VNRS_VNFC_IPU_0064”的所有过滤报文信息：

```
DSP SFEDBGPKT: RUNAME="VNODE_VNRS_VNFC_IPU_0066";
```

```
                                                                       
RETCODE = 0  操作成功.                                                                                                     
                                                                                                                                    
结果如下                                                                                                            
------------------------                                                                                                            
返回结果  =                                                                                                                           
                                                                                                                                    
SFE packet number: 1                                                                                                                
(TIME08:48:25:392)SFE debug packet information:                                                                                     
Current Board : 64
Recv from PAE ExtPort packet: PktLen = 98 SP = 0                                                                                    
FA 16 3E 28 B4 3D FA 16  3E 68 8C 11 08 00 45 00                                                                                    
00 54 01 08 00 00 FF 01  B6 9C 01 01 01 02 01 01                                                                                    
01 01                                                                                                                               
                                                                                                                                    
SFE packet number: 2                                                                                                                
(TIME08:48:25:392)SFE debug packet information:                                                                                     
Current Board : 64
Send to CP packet: PktLen = 98                                                                                                      
FA 16 3E 28 B4 3D FA 16  3E 68 8C 11 08 00 45 00                                                                                    
00 54 01 08 00 00 FF 01  B6 9C 01 01 01 02 01 01                                                                                    
01 01                                                                                                                               
                                                                                                                                    
SFE packet number: 3                                                                                                                
(TIME08:48:25:392)SFE debug packet information:                                                                                     
Current Board : 64
Send to LDM packet: PktLen = 98                                                                                                     
FA 16 3E 28 B4 3D FA 16  3E 68 8C 11 08 00 45 00                                                                                    
00 54 01 08 00 00 FF 01  B6 9C 01 01 01 02 01 01                                                                                    
01 01                                                                                                                               
                                                                                                                                    
SFE packet number: 4                                                                                                                
(TIME08:48:25:392)SFE debug packet information:                                                                                     
Current Board : 64
Recv from LDM packet: PktLen = 98                                                                                                   
FA 16 3E 68 8C 11 FA 16  3E 28 B4 3D 08 00 45 00                                                                                    
00 54 02 7C 00 00 FF 01  B5 28 01 01 01 01 01 01                                                                                    
01 02                                                                                                                               
                                                                                                                              
(结果个数 = 1)                                                                                                             
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-SFEDBGPKT.md`
