---
id: UDG@20.15.2@MMLCommand@DSP OSPFLSDBSTATEVERBOSE
type: MMLCommand
name: DSP OSPFLSDBSTATEVERBOSE（查询OSPF LSDB详细信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: OSPFLSDBSTATEVERBOSE
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- OSPF管理
- 查询OSPF LSDB的状态信息
status: active
---

# DSP OSPFLSDBSTATEVERBOSE（查询OSPF LSDB详细信息）

## 功能

该命令用于显示OSPF LSDB详细信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCESSID | OSPF进程号 | 可选必选说明：可选参数<br>参数含义：该参数表示OSPF进程号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无 |
| LSATYPE | LSA类型 | 可选必选说明：必选参数<br>参数含义：该参数表示LSA类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- Router：Router LSA。<br>- Network：Network LSA。<br>- Sum_Net：ABR Summary LSA。<br>- Sum_Asbr：ASBR Summary LSA。<br>- External：AS-External LSA。<br>- NSSA：NSSA LSA。<br>- Opq_Link：Opaque Link LSA。<br>- Opq_Area：Opaque Area LSA。<br>- Opq_As：Opaque AS LSA。<br>默认值：无 |
| LINKSTATEID | LSA报文中的链路状态ID | 可选必选说明：可选参数<br>参数含义：该参数表示LSA报文中的链路状态ID。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。点分十进制格式。<br>默认值：无 |

## 操作的配置对象

- [OSPF LSDB详细信息（OSPFLSDBSTATEVERBOSE）](configobject/UDG/20.15.2/OSPFLSDBSTATEVERBOSE.md)

## 使用实例

- 查询OSPF全进程下LSDB中Router LSA的详细信息：
  ```
  DSP OSPFLSDBSTATEVERBOSE:LSATYPE=Router;
  ```
  ```

  RETCODE = 0  操作成功。

  Router LSA信息
  ------------------------
                 OSPF进程号  =  1
                     区域号  =  0.0.0.0
                 路由器标识  =  192.168.3.111
                    LSA类型  =  Router LSA
      LSA报文中的链路状态ID  =  192.168.3.111
  发布或产生LSA的路由器标识  =  192.168.3.111
         LSA的老化时间（s）  =  701
                    LSA长度  =  36
                  LSA序列号  =  0x80000002
                  LSA校验和  =  0xa02e
                    LSA选项  =  E
                LSA选项标志  =  ASBR ABR
                     链路ID  =  192.168.14.0
                   链路数据  =  255.255.255.0
                   链路类型  =  Stub Network
               服务类型度量  =  1
  (结果个数 = 1)
  ---    END
  ```
- 查询OSPF全进程下LSDB中Network LSA的详细信息：
  ```
  DSP OSPFLSDBSTATEVERBOSE:LSATYPE=Network;
  ```
  ```

  RETCODE = 0  操作成功。

  Network LSA信息
  -----------------------
                       OSPF进程号  =  1
                           区域号  =  0.0.0.0
                       路由器标识  =  192.168.3.111
                          LSA类型  =  Network LSA
            LSA报文中的链路状态ID  =  192.168.3.111
        发布或产生LSA的路由器标识  =  192.168.3.111
                LSA的老化时间（s） =  266
                          LSA长度  =  32
                        LSA序列号  =  0x80000001
                        LSA校验和  =  0x66c4
                          LSA选项  =  E
                         网络掩码  =  255.255.255.0
               与网络连接的路由器  =  192.168.3.112
  (结果个数 = 1)
  ---    END
  ```
- 查询OSPF全进程下LSDB中External LSA的详细信息：
  ```
  DSP OSPFLSDBSTATEVERBOSE:LSATYPE=External;
  ```
  ```

  RETCODE = 0  操作成功。

  As-external-LSA信息
  ---------------------------
                 OSPF进程号  =  1
                     区域号  =  0.0.0.0
                 路由器标识  =  192.168.3.111
                    LSA类型  =  AS-External LSA
      LSA报文中的链路状态ID  =  192.168.3.100
  发布或产生LSA的路由器标识  =  192.168.3.112
         LSA的老化时间（s）  =  666
                    LSA长度  =  36
                  LSA序列号  =  0x80000001
                  LSA校验和  =  0x6dd8
                    LSA选项  =  E
                   网络掩码  =  255.255.255.255
                 服务类型ID  =  0
               服务类型度量  =  1
                      E类型  =  2
                 转发IP地址  =  0.0.0.0
                   路由标识  =  1
  (结果个数 = 1)
  ---    END
  ```
- 查询OSPF全进程下LSDB中Opq_Area LSA的详细信息：
  ```
  DSP OSPFLSDBSTATEVERBOSE:LSATYPE=Opq_Area;
  ```
  ```

  RETCODE = 0  操作成功。

  Opaque-area LSA信息
  ---------------------------
                 OSPF进程号  =  1
                     区域号  =  0.0.0.0
                 路由器标识  =  192.168.3.111
                    LSA类型  =  Opaque Area LSA
      LSA报文中的链路状态ID  =  10.10.10.0
  发布或产生LSA的路由器标识  =  192.168.3.111
          LSA的老化时间（s） =  1305
                    LSA长度  =  28
                  LSA序列号  =  0x80000001
                  LSA校验和  =  0x31e3
                    LSA选项  =  E
                 Opaque类型  =  4
                  Opaque ID  =  0
  (结果个数 = 1)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询OSPF-LSDB详细信息（DSP-OSPFLSDBSTATEVERBOSE）_49801974.md`
