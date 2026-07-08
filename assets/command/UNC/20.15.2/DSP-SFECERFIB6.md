---
id: UNC@20.15.2@MMLCommand@DSP SFECERFIB6
type: MMLCommand
name: DSP SFECERFIB6（显示指定IPv6的FIB表）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: SFECERFIB6
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- 转发引擎实例FEI
- FIB表项统计
status: active
---

# DSP SFECERFIB6（显示指定IPv6的FIB表）

## 功能

该命令用于精确查询转发面的FIB6表。设备上FIB6表较多时，需要使用该命令精确查找指定的FIB6表。

## 注意事项

该命令仅适用于非NP卡场景和NP卡非加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DESTIP | 目的IP地址 | 可选必选说明：必选参数<br>参数含义：该参数用于指定目的IP地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。<br>默认值：无 |
| VPNID | VPN编号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定VPN编号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无 |
| RUNAME | RU名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定资源单元名称，可使用命令DSP RU查询得到。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：使用DSP RU查看RU名称。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SFECERFIB6]] · 指定IPv6的FIB表（SFECERFIB6）

## 使用实例

查询SFE指定IPv6的FIB表：

```
DSP SFECERFIB6:RUNAME="VNODE_VNRS_VNFC_IPU_0066",DESTIP="2001:db8::1",VPNID=0;
```

```

RETCODE = 0  操作成功                                                 
                                                                                
结果如下                                                       
-------------------------    
      RU编号  = 64
  目的IP地址  = 2001:db8::1
     VPN编号  = 0
      RU名称  = VNODE_VNRS_VNFC_IPU_0066                                                                  
    查询结果  = 
      *Vpn : 00000000                            *PfxLen : 00000080                
 *Ipv6Addr : 2001:db8::1                  
  Re6Index : 00000004     
     
                                                                                                                                                    
(结果个数 = 1)                                                         
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-SFECERFIB6.md`
