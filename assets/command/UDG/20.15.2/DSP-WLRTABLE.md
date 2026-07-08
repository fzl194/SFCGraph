---
id: UDG@20.15.2@MMLCommand@DSP WLRTABLE
type: MMLCommand
name: DSP WLRTABLE（显示无线路由表）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: WLRTABLE
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- 无线路由调测
- 显示无线路由相关信息
status: active
---

# DSP WLRTABLE（显示无线路由表）

## 功能

该命令用于显示无线路由表。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| AFTYPE | 地址族 | 可选必选说明：必选参数<br>参数含义：该参数用于表示地址族。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4unicast：IPv4单播。<br>- ipv6unicast：IPv6单播。<br>默认值：无 |
| VRFNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示路由所属VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。区分大小写。<br>默认值：_public_ |
| PREFIX4 | IPv4路由前缀 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv4unicast”时为可选参数。<br>参数含义：该参数用于表示IPv4路由前缀。<br>数据来源：对端协商<br>取值范围：IPv4地址类型。<br>默认值：无 |
| PREFIX6 | IPv6路由前缀 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv6unicast”时为可选参数。<br>参数含义：该参数用于表示IPv6路由前缀。<br>数据来源：对端协商<br>取值范围：IPv6地址类型。<br>默认值：无 |
| MASKLENGTH | 路由掩码长度 | 可选必选说明：可选参数<br>参数含义：IPv4场景，该参数用于表示路由的掩码长度；IPv6场景，该参数用于表示路由的前缀长度。<br>数据来源：对端协商<br>取值范围：整数类型，取值范围为0～128。AFTYPE为ipv4unicast时取值范围0～32，AFTYPE为ipv6unicast时取值范围0～128。<br>默认值：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@WLRTABLE]] · 无线路由表（WLRTABLE）

## 使用实例

- 显示IPv4无线路由表：
  ```
  DSP WLRTABLE: AFTYPE=ipv4unicast;
  ```
  ```

  RETCODE = 0 操作成功

  结果如下
  -------------------------
     VPN实例名称 = _public_
    IPv4路由前缀 = 192.168.1.0
    路由掩码长度 = 24
      路由下一跳 = 0.0.0.0
      路由优先级 = 1
         路由tag = 0
  路由出接口名字 = PAE Group
        路由状态 = Active Primary
        路由Cost = 0
         路由IID = 0xb0000033
     路由IID标识 = --
        对端地址 = 192.168.1.2
            标签 = NULL
        路由类型 = WLR_SP
          属性ID = 1
          服务ID = 0
  负载分担策略ID = 1
          元数据 = 0,0,0
        路由标识 = 0x200F
      路由版本号 = 1
      策略组标识 = 2
        分组标识 = 65537/131074
        团体属性 = 10 20 40 50
  (结果个数 = 1)
  --- END
  ```
- 显示IPv6无线路由表：
  ```
  DSP WLRTABLE: AFTYPE=ipv6unicast;
  ```
  ```

  RETCODE = 0 操作成功

  结果如下
  -------------------------
     VPN实例名称 = _public_
    IPv6路由前缀 = 2001:DB8::
    路由掩码长度 = 128
      路由下一跳 = ::
      路由优先级 = 1
         路由tag = 0
  路由出接口名字 = PAE Group
        路由状态 = Active Primary
        路由Cost = 0
         路由IID = 0xb0000033
     路由IID标识 = --
        对端地址 = 192.168.1.2
            标签 = NULL
        路由类型 = WLR_SP
          属性ID = 1
          服务ID = 0
  负载分担策略ID = 1
          元数据 = 0,0,0
        路由标识 = 0x200F
      路由版本号 = 1
      策略组标识 = 0
        分组标识 = 65537/131074
        团体属性 = 10 20 40 50
  (结果个数 = 1)
  --- END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-WLRTABLE.md`
