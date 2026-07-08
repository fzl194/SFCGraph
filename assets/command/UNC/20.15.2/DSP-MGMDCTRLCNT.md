---
id: UNC@20.15.2@MMLCommand@DSP MGMDCTRLCNT
type: MMLCommand
name: DSP MGMDCTRLCNT（查询IGMP报文统计计数）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: MGMDCTRLCNT
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP组播
- MGMD
- IGMP报文统计计数
status: active
---

# DSP MGMDCTRLCNT（查询IGMP报文统计计数）

## 功能

该命令用于显示IGMP报文统计计数。

## 注意事项

该命令仅适用于非NP卡场景和NP卡非加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ADDRESSFAMILY | 地址族 | 可选必选说明：必选参数<br>参数含义：该参数用于指定地址族类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4unicast：IPv4单播。<br>默认值：无 |
| VRFNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用来指定VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：_public_<br>配置原则：通过LST L3VPNINST查看当前已存在的VPN实例。 |
| IFNAME | 接口名称 | 可选必选说明：可选参数<br>参数含义：该参数用来指定接口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：请使用LST INTERFACE命令查看可用接口。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/MGMDCTRLCNT]] · IGMP报文统计计数（MGMDCTRLCNT）

## 使用实例

显示IGMP报文统计计数：

```
DSP MGMDCTRLCNT: VRFNAME="_public_", ADDRESSFAMILY=ipv4unicast, IFNAME="Ethernet64/0/3 ";
```

```
RETCODE = 0  操作成功。

结果如下
------------------------
                VPN实例名称  =  _public_
                     地址族  =  IPv4单播
                   接口名称  =  Ethernet64/0/3
                   接口地址  =  10.0.0.1
     有效的通用查询报文数目  =  0
     无效的通用查询报文数目  =  0
     忽略的通用查询报文数目  =  0
   有效的特定组查询报文数目  =  0
   无效的特定组查询报文数目  =  0
   忽略的特定组查询报文数目  =  0
 有效的特定源组查询报文数目  =  0
 无效的特定源组查询报文数目  =  0
 忽略的特定源组查询报文数目  =  0
有效的V1V2的ASM加入报文数目  =  0
无效的V1V2的ASM加入报文数目  =  0
忽略的V1V2的ASM加入报文数目  =  0
有效的V1V2的SSM加入报文数目  =  0
无效的V1V2的SSM加入报文数目  =  0
忽略的V1V2的SSM加入报文数目  =  0
有效的V1V2的ASM离开报文数目  =  0
无效的V1V2的ASM离开报文数目  =  0
忽略的V1V2的ASM离开报文数目  =  0
有效的V1V2的SSM离开报文数目  =  0
无效的V1V2的SSM离开报文数目  =  0
忽略的V1V2的SSM离开报文数目  =  0
     有效的V3 IS_IN报文数目  =  0
     无效的V3 IS_IN报文数目  =  0
     忽略的V3 IS_IN报文数目  =  0
     有效的V3 IS_EX报文数目  =  0
     无效的V3 IS_EX报文数目  =  0
     忽略的V3 IS_EX报文数目  =  0
     有效的V3 TO_IN报文数目  =  0
     无效的V3 TO_IN报文数目  =  0
     忽略的V3 TO_IN报文数目  =  0
     有效的V3 TO_EX报文数目  =  0
     无效的V3 TO_EX报文数目  =  0
     忽略的V3 TO_EX报文数目  =  0
     有效的V3 ALLOW报文数目  =  0
     无效的V3 ALLOW报文数目  =  0
     忽略的V3 ALLOW报文数目  =  0
     有效的V3 BLOCK报文数目  =  0
     无效的V3 BLOCK报文数目  =  0
     忽略的V3 BLOCK报文数目  =  0
               有效的源数量  =  0
               无效的源数量  =  0
               忽略的源数量  =  0
         发送的通用查询数量  =  2
发送的V1V2的ASM加入报文数目  =  0
发送的V1V2的SSM加入报文数目  =  0
发送的V1V2的ASM离开报文数目  =  0
发送的V1V2的SSM离开报文数目  =  0
       发送的特定组查询数量  =  0
     发送的特定源组查询数量  =  0
     发送的V3 IS_IN报文数目  =  0
     发送的V3 IS_EX报文数目  =  0
     发送的V3 TO_IN报文数目  =  0
     发送的V3 TO_EX报文数目  =  0
     发送的V3 ALLOW报文数目  =  0
     发送的V3 BLOCK报文数目  =  0
             忽略的未知类型  =  0
               发送的源数量  =  0
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-MGMDCTRLCNT.md`
