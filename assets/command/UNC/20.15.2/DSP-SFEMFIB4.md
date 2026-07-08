---
id: UNC@20.15.2@MMLCommand@DSP SFEMFIB4
type: MMLCommand
name: DSP SFEMFIB4（显示MFIB4表项）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: SFEMFIB4
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

# DSP SFEMFIB4（显示MFIB4表项）

## 功能

该命令用于显示MFIB4表项。

## 注意事项

该命令仅适用于非NP卡场景和NP卡非加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SRCIP | 源IP | 可选必选说明：必选参数<br>参数含义：该参数表示源IP地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无 |
| GROUPIP | 组播组IP | 可选必选说明：必选参数<br>参数含义：该参数表示组播组IP地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无 |
| VPN | VPN编号 | 可选必选说明：必选参数<br>参数含义：该参数表示VPN编号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65535。<br>默认值：无 |
| RUNAME | RU名称 | 可选必选说明：必选参数<br>参数含义：该参数表示资源单元名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。区分大小写。<br>默认值：无<br>配置原则：<br>- 区分大小写，不支持空格。<br>- 使用DSP RU查看RU名称。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SFEMFIB4]] · MFIB4表项（SFEMFIB4）

## 使用实例

显示指定资源单元、组播源IP、组播目的IP、VPN的组播MFIB4表项：

```
DSP SFEMFIB4:SRCIP="10.1.1.100",GROUPIP="239.0.0.1",VPN=0,RUNAME="VNODE_VNRS_VNFC_IPU_0064";
```

```

RETCODE = 0  操作成功。

结果如下
------------------------
    源IP  =  10.1.1.100
组播组IP  =  239.0.0.1
 VPN编号  =  0
    结果  =                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
              *GrpIp : ef000001                          *SrcIp : 0a010164            
              *VpnId : 00000000                           Valid : 01                  
              OpCode : 00                                IsFake : 00                  
              StatId : 00000000                            Type : 00                  
        RpfCheckType : 01                              DevTmgId : 00000000            
               TmgId : 00000000                          RpfVid : 0000                
                  PT : 00                                    TB : 0041                
                  TP : 0005                

(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示MFIB4表项（DSP-SFEMFIB4）_00600313.md`
