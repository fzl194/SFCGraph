---
id: UNC@20.15.2@MMLCommand@DSP RMIID
type: MMLCommand
name: DSP RMIID（查询路由管理IID信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: RMIID
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

# DSP RMIID（查询路由管理IID信息）

## 功能

该命令用来查询路由管理模块的IID信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ADDRESSFAMILY | 地址族 | 可选必选说明：必选参数<br>参数含义：该参数用于表示地址族。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4unicast：IPv4单播。<br>- ipv6unicast：IPv6单播。<br>默认值：无 |
| VRFNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示路由所属VPN的名字。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无 |
| INDEX | IID | 可选必选说明：可选参数<br>参数含义：该参数用于表示IID索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无 |
| ORIGINNEXTHOP | 原始下一跳地址 | 可选必选说明：可选参数<br>参数含义：该参数用于表示路由的原始下一跳地址。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～49。<br>默认值：无 |
| PROTOCOLID | 路由协议名字 | 可选必选说明：可选参数<br>参数含义：该参数用于表示路由协议的名字。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- Direct：直连路由。<br>- OSPF：OSPF路由。<br>- Static：静态路由。<br>- BGP：BGP路由。<br>- wlr：无线路由。<br>默认值：无 |
| VERBOSE | 是否详细信息 | 可选必选说明：必选参数<br>参数含义：该参数用于表示是否查询路由IID详细信息。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- true：是。<br>- false：否。<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@RMIID]] · 路由管理IID信息（RMIID）

## 使用实例

- 查询路由管理模块的IID信息：
  ```
  DSP RMIID:ADDRESSFAMILY=ipv4unicast,VERBOSE=false;
  ```
  ```

  RETCODE = 0  操作成功。

  结果如下
  --------
  IID数量    IID          IID类型    原始下一跳地址    路由协议名字    路由进程ID    子协议ID           下一跳数量

  3          0x1000001    1          0.0.0.0           直连路由        0             NO_SUB_PROTOCOL    1
  3          0x1000002    1          0.0.0.0           直连路由        0             NO_SUB_PROTOCOL    1
  3          0x100000A    1          0.0.0.0           直连路由        0             NO_SUB_PROTOCOL    1
  (结果个数 = 3)
  ---    END
  ```
- 查询路由管理模块的IID详细信息：
  ```
  DSP RMIID:ADDRESSFAMILY=ipv4unicast,VERBOSE=true;
  ```
  ```

  RETCODE = 0  操作成功。

  结果如下
  --------
  IID数量    IID          IID类型    路由协议名字    路由进程ID    子协议ID           下一跳数量    原始下一跳地址    迭代的IID    路由下一跳    路由接口名字    TB high    TB low    TP    隧道ID    隧道类型    隧道所在VRF ID    隧道名称    存活时间

  3          0x1000001    1          直连路由        0             NO_SUB_PROTOCOL    1             0.0.0.0           0            127.0.0.1     NULL0           --         --        --    --        --          --                --          02h21m30s
  3          0x1000002    1          直连路由        0             NO_SUB_PROTOCOL    1             0.0.0.0           0            127.0.0.1     InLoopBack0     --         --        --    --        --          --                --          02h21m30s
  3          0x100000A    1          直连路由        0             NO_SUB_PROTOCOL    1             0.0.0.0           0            127.0.0.1     InLoopBack0     --         --        --    --        --          --                --          02h21m30s
  (结果个数 = 3)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-RMIID.md`
