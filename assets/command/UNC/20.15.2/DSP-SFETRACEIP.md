---
id: UNC@20.15.2@MMLCommand@DSP SFETRACEIP
type: MMLCommand
name: DSP SFETRACEIP（查询SFE IP消息跟踪配置信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: SFETRACEIP
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- 转发引擎实例FEI
- 转发IP消息跟踪任务
status: active
---

# DSP SFETRACEIP（查询SFE IP消息跟踪配置信息）

## 功能

该命令用来查询SFE IP消息跟踪配置信息。

## 注意事项

该命令仅适用于非NP卡场景和NP卡非加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：必选参数<br>参数含义：资源单元名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。区分大小写。<br>默认值：无<br>配置原则：<br>- 区分大小写，不支持空格。<br>- 使用DSP RU查看RU名称。 |
| IPTYPE | IP类型 | 可选必选说明：必选参数<br>参数含义：IP类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4：IPv4类型。<br>- ipv6：IPv6类型。<br>- arp：ARP类型。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SFETRACEIP]] · SFE IP消息跟踪配置信息（SFETRACEIP）

## 使用实例

- 查询指定资源单元的IP消息跟踪IPv4报文配置信息：
  ```
  DSP SFETRACEIP: RUNAME="VNODE_VNRS_VNFC_IPU_0064", IPTYPE=ipv4;
  ```
  ```

  RETCODE = 0  操作成功。                                                 
                                                                                
  IPV4跟踪信息如下                                                           
  ------------------------                                                        
            IP类型  =  IPv4
          IP协议号  =  0
      本端IPv4地址  =  192.168.1.1
  本端IPv4地址掩码  =  255.255.255.255
      对端IPv4地址  =  192.168.1.2
  对端IPv4地址掩码  =  255.255.255.255
        本端端口号  =  0
        对端端口号  =  0
           VPN名称  =  NULL
          协议方向  =  NULL
        重定向类型  =  0
        重定向索引  =  0
          协议名称  =  IP
          流跟踪ID  =  1                                                   
   (结果个数 = 1)                                                         
  ---    END
  ```
- 查询指定资源单元的IP消息跟踪IPv6报文配置信息：
  ```
  DSP SFETRACEIP: RUNAME="VNODE_VNRS_VNFC_IPU_0064", IPTYPE=ipv6;
  ```
  ```

  RETCODE = 0  操作成功。

  IPV6跟踪信息如下 
  ------------------------------------
        IP类型  =  IPv6
      IP协议号  =  0
  本端IPv6地址  =  2001:db8::1
  本端IPv6前缀  =  128
  对端IPv6地址  =  2001:db8::2
  对端IPv6前缀  =  128
    本端端口号  =  0
    对端端口号  =  0
       VPN名称  =  NULL
      协议方向  =  NULL
    重定向类型  =  0
    重定向索引  =  0
      协议名称  =  IP
      流跟踪ID  =  2
  (结果个数 = 1)
  ---    END
  ```
- 查询指定资源单元的IP消息跟踪ARP报文配置信息：
  ```
  DSP SFETRACEIP: RUNAME="VNODE_VNRS_VNFC_IPU_0064", IPTYPE=arp;
  ```
  ```

  RETCODE = 0  操作成功。

  ARP跟踪信息如下
  ---------------
      IP类型  =  ARP
     VPN名称  =  _public_
    协议方向  =  both
  重定向类型  =  0
  重定向索引  =  0
    协议名称  =  ARP
    流跟踪ID  =  3
  (结果个数 = 1)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询SFE-IP消息跟踪配置信息（DSP-SFETRACEIP）_00841413.md`
