---
id: UDG@20.15.2@MMLCommand@DSP RMPREFIXINFO
type: MMLCommand
name: DSP RMPREFIXINFO（查询路由管理前缀信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: RMPREFIXINFO
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- 路由基础调测
- 查询路由管理基本信息
status: active
---

# DSP RMPREFIXINFO（查询路由管理前缀信息）

## 功能

该命令用来查询路由管理前缀信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VRFNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无 |
| VRFID | VRF索引 | 可选必选说明：可选参数<br>参数含义：该参数用于表示VRF索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无 |
| AFTYPE | 地址族 | 可选必选说明：必选参数<br>参数含义：该参数用于表示地址族。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4unicast：IPv4单播。<br>- ipv6unicast：IPv6单播。<br>默认值：无 |
| ADDR4 | IPv4前缀 | 可选必选说明：条件必选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv4unicast”时为必选参数。<br>参数含义：该参数用于表示IPv4前缀。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无 |
| ADDR6 | IPv6前缀 | 可选必选说明：条件必选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv6unicast”时为必选参数。<br>参数含义：该参数用于表示IPv6前缀。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。<br>默认值：无 |
| MASK4 | 掩码长度 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv4unicast”时为可选参数。<br>参数含义：该参数用于表示掩码长度。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～32。<br>默认值：无 |
| MASK6 | 掩码长度 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv6unicast”时为可选参数。<br>参数含义：该参数用于表示掩码长度。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～128。<br>默认值：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@RMPREFIXINFO]] · 路由管理前缀信息（RMPREFIXINFO）

## 使用实例

- 查询路由管理IPv4前缀信息：
  ```
  DSP RMPREFIXINFO:AFTYPE=ipv4unicast,ADDR4="127.0.0.1";
  ```
  ```

  RETCODE = 0  操作成功。

  结果如下
  --------
           VPN实例名称  =  _public_
               VRF索引  =  0
              IPv4前缀  =  127.0.0.1
              掩码长度  =  32
                表名字  =  base
            路由拓扑ID  =  0
              拓扑名字  =  base
          前缀标记信息  =  NULL
  前缀通告被流控的次数  =  1
              引入标记  =  0x1
              协议类型  =  Direct
            协议进程ID  =  0
            路由优先级  =  0
             JOB优先级  =  极高
                标签值  =  0
                开销值  =  0
                版本号  =  1
                 QoS值  =  0x0
              Trace Id  =  0
            路由的标记  =  0x80002064
     路由存活时间（s）  =  7154
                IIDG值  =  0x1
               IID数量  =  1
              IIDG标记  =  0x30
        IIDG被流控次数  =  0
        IIDG被引用次数  =  3
              路由类型  =  NOFRR NOLABEL
                 主IID  =  0x100000B
                 备IID  =  0xFFFFFFFF
                主标签  =  0xFFFFFFFF
                备标签  =  0xFFFFFFFF
                属性ID  =  0x0
  (结果个数 = 1)
  ---    END
  ```
- 查询路由管理IPv6前缀信息：
  ```
  DSP RMPREFIXINFO:AFTYPE=ipv6unicast,ADDR6="2001:DB8::";
  ```
  ```

  RETCODE = 0  操作成功。

  结果如下
  --------
           VPN实例名称  =  _public_
               VRF索引  =  0
              IPv6前缀  =  2001:DB8::
              掩码长度  =  128
                表名字  =  base
            路由拓扑ID  =  0
              拓扑名字  =  base
          前缀标记信息  =  NULL
  前缀通告被流控的次数  =  1
              引入标记  =  0x0
              协议类型  =  Direct
            协议进程ID  =  0
            路由优先级  =  0
             JOB优先级  =  极高
                标签值  =  0
                开销值  =  0
                版本号  =  1
                 QoS值  =  0x0
              Trace Id  =  0
            路由的标记  =  0x80002124
     路由存活时间（s）  =  159
                IIDG值  =  0x4
               IID数量  =  1
              IIDG标记  =  0x30
        IIDG被流控次数  =  0
        IIDG被引用次数  =  1
              路由类型  =  NOFRR NOLABEL
                 主IID  =  0x1000070
                 备IID  =  0xFFFFFFFF
                主标签  =  0xFFFFFFFF
                备标签  =  0xFFFFFFFF
                属性ID  =  0x0
  (结果个数 = 1)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-RMPREFIXINFO.md`
