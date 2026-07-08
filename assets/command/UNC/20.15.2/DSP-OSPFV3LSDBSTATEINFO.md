---
id: UNC@20.15.2@MMLCommand@DSP OSPFV3LSDBSTATEINFO
type: MMLCommand
name: DSP OSPFV3LSDBSTATEINFO（查询OSPFv3 LSDB的状态信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: OSPFV3LSDBSTATEINFO
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- OSPFv3管理
- 查询OSPFv3 LSDB的状态信息
status: active
---

# DSP OSPFV3LSDBSTATEINFO（查询OSPFv3 LSDB的状态信息）

## 功能

该命令用于查询OSPFv3 LSDB中各类LSA的详细信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCID | OSPFv3进程号 | 可选必选说明：可选参数<br>参数含义：OSPFv3进程号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无 |
| AREAID | OSPFv3区域号 | 可选必选说明：可选参数<br>参数含义：OSPFv3区域号。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。点分十进制格式。<br>默认值：无 |
| LSATYPE | LSA类型 | 可选必选说明：必选参数<br>参数含义：LSA类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- Router-LSA：Router LSA。<br>- Network-LSA：Network LSA。<br>- Inter-Area-Prefix-LSA：Inter Area Router LSA。<br>- Inter-Area-Router-LSA：Inter Area Router LSA。<br>- AS-External-LSA：AS External LSA。<br>- Link-LSA：Link LSA。<br>- Intra-Area-Prefix-LSA：Intra Area Prefix LSA。<br>- Grace-LSA：Grace LSA。<br>- NSSA：NSSA。<br>- RI-Link-LSA：Router Information Link LSA。<br>- RI-Area-LSA：Router Information Area LSA。<br>- RI-AS-LSA：Router Information AS LSA。<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@OSPFV3LSDBSTATEINFO]] · OSPFv3 LSDB的状态信息（OSPFV3LSDBSTATEINFO）

## 使用实例

- 查询OSPFv3全进程下LSDB中Router LSA的详细信息：
  ```
  DSP OSPFV3LSDBSTATEINFO:LSATYPE=Router-LSA;
  ```
  ```

  RETCODE = 0  操作成功。

  Router LSA Information
  ----------------------
                OSPFv3进程号  =  1
                  路由器标识  =  10.10.10.1
                OSPFv3区域号  =  0.0.0.0
                     LSA类型  =  Router LSA
               LSA的老化时间  =  74
       LSA报头中的链路状态ID  =  0.0.0.1
   发布或产生LSA的路由器标识  =  10.10.10.1
                   LSA序列号  =  0x80000004
                    重传次数  =  0
                   LSA校验和  =  0xa08c
                     LSA长度  =  36
                 LSA选项标志  =  -|-|-|-|-
                     LSA选项  =  -|-|-|-|E|V6
       （路由器LSA）链路类型  =  None
                服务类型度量  =  0
                  接口实例ID  =  0x0
                  邻居接口ID  =  0x0
              邻居路由器标识  =  10.10.10.2
  (结果个数 = 1)
  ---    END
  ```
- 查询OSPFv3全进程下LSDB中External LSA的详细信息：
  ```
  DSP OSPFV3LSDBSTATEINFO:LSATYPE=AS-External-LSA;
  ```
  ```

  RETCODE = 0  操作成功。

  External LSA Information
  ------------------------
                OSPFv3进程号  =  1
                  路由器标识  =  10.10.10.1
                     LSA类型  =  AS External LSA
               LSA的老化时间  =  74
       LSA报头中的链路状态ID  =  0.0.0.1
   发布或产生LSA的路由器标识  =  10.10.10.1
                   LSA序列号  =  0x80000004
                    重传次数  =  0
                   LSA校验和  =  0xa08c
                     LSA长度  =  36
                 LSA选项标志  =  E|-|T
                外部花费类型  =  Type 2
                服务类型度量  =  1
        IPv6前缀过滤策略名称  =  2001:db8::
                IPv6前缀长度  =  64
                IPv6前缀选项  =  -|-|-|-|-
          VPN引入路由的tag值  =  1
  (结果个数 = 1)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-OSPFV3LSDBSTATEINFO.md`
