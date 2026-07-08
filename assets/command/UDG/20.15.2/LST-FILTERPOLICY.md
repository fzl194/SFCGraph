---
id: UDG@20.15.2@MMLCommand@LST FILTERPOLICY
type: MMLCommand
name: LST FILTERPOLICY（查询路由过滤策略）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: FILTERPOLICY
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- BGP管理
- 路由过滤策略
status: active
---

# LST FILTERPOLICY（查询路由过滤策略）

## 功能

该命令用于查看IPv4或IPv6路由过滤策略。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VRFNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无 |
| AFTYPE | 地址族类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定VRF的地址族类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4uni：IPv4地址族。<br>- ipv4vpn：VPNv4地址族。<br>- ipv6uni：IPv6地址族。<br>- ipv6vpn：VPNv6地址族。<br>默认值：无 |
| EXPORT | 出口方向 | 可选必选说明：可选参数<br>参数含义：该参数用于指定该过滤策略是否应用在出口方向。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：无 |
| IMPORT | 入口方向 | 可选必选说明：可选参数<br>参数含义：该参数用于该过滤策略是否应用在入口方向。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：无 |
| FILTERPROTOCOL | 路由协议 | 可选必选说明：可选参数<br>参数含义：该参数用于指定发布路由信息的协议，对其进行过滤。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- noprotocol：默认应用所有协议。<br>- direct：直连路由。<br>- ospf：OSPF路由。<br>- static：静态路由。<br>- ospfv3：OSPFv3路由。<br>默认值：无<br>配置原则：如果AFTYPE为VPNv4或VPNv6，该参数只能选择noprotocol。 |
| FILTERPROCESSID | 协议进程ID | 可选必选说明：可选参数<br>参数含义：该参数用于指定单播路由协议的进程号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/FILTERPOLICY]] · 路由过滤策略（FILTERPOLICY）

## 使用实例

- 查看名称为“vrf1”的BGP VPN实例下IPv4路由过滤策略：
  ```
  LST FILTERPOLICY:AFTYPE=ipv4uni;
  ```
  ```

  RETCODE = 0  操作成功。

  结果如下
  --------
       VPN实例名称  =  vrf1
        地址族类型  =  IPv4uni
          出口方向  =  FALSE
          入口方向  =  TRUE
          路由协议  =  默认应用所有协议
        协议进程ID  =  0
       ACL规则标识  =  NULL
      前缀过滤策略  =  asssd
      ACL6规则标识  =  NULL
  IPv6前缀过滤策略  =  NULL
  (结果个数 = 1)
  ---    END
  ```
- 查看名称为“vrf1”的BGP VPN实例下IPv6路由过滤策略：
  ```
  LST FILTERPOLICY:AFTYPE=ipv6uni;
  ```
  ```

  RETCODE = 0  操作成功。

  结果如下
  --------
       VPN实例名称  =  vrf1
        地址族类型  =  IPv6uni
          出口方向  =  FALSE
          入口方向  =  TRUE
          路由协议  =  默认应用所有协议
        协议进程ID  =  0
       ACL规则标识  =  NULL
      前缀过滤策略  =  NULL
      ACL6规则标识  =  NULL
  IPv6前缀过滤策略  =  asssd
  (结果个数 = 1)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-FILTERPOLICY.md`
