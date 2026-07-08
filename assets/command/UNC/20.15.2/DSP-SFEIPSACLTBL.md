---
id: UNC@20.15.2@MMLCommand@DSP SFEIPSACLTBL
type: MMLCommand
name: DSP SFEIPSACLTBL（查询软转发SFE IPSEC-ACL表项信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: SFEIPSACLTBL
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- 转发引擎实例FEI
- SFE IPSECACL表项
status: active
---

# DSP SFEIPSACLTBL（查询软转发SFE IPSEC-ACL表项信息）

## 功能

该命令查询软转发SFE IPSEC-ACL表项信息。

## 注意事项

该命令仅适用于非NP卡场景和NP卡非加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | 资源单元名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定资源单元名称，可使用命令DSP RU查询得到。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：使用DSP RU查看RU名称。 |
| TABLETYPE | IPSEC ACL表类型 | 可选必选说明：必选参数<br>参数含义：该参数表示需要查询的IPSEC ACL表类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- flex：灵活引流ACL。<br>- split：传输模式分流ACL。<br>默认值：无 |
| INDEX | IPSEC ACL索引 | 可选必选说明：必选参数<br>参数含义：该参数表示需要查询的IPSEC ACL表项索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无 |
| SOURCEIP | 源IPv4地址 | 可选必选说明：必选参数<br>参数含义：该参数用于表示需要查询的报文源IP地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无 |
| DESTIP | 目的IPv4地址 | 可选必选说明：必选参数<br>参数含义：该参数用于表示需要查询的报文目的IP地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无 |
| SOURCEPORT | 源端口号 | 可选必选说明：条件必选参数<br>前提条件：该参数在“TABLETYPE”配置为“split”时为必选参数。<br>参数含义：该参数用于表示需要查询的报文源端口号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65535。<br>默认值：无 |
| DESTPORT | 目的端口号 | 可选必选说明：条件必选参数<br>前提条件：该参数在“TABLETYPE”配置为“split”时为必选参数。<br>参数含义：该参数用于表示需要查询的报文目的端口号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65535。<br>默认值：无 |
| PROTOCOL | IP协议类型 | 可选必选说明：条件必选参数<br>前提条件：该参数在“TABLETYPE”配置为“split”时为必选参数。<br>参数含义：该参数用于表示需要查询的报文IP协议类型。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～255。<br>默认值：无 |
| VPNID | VPN编号 | 可选必选说明：必选参数<br>参数含义：该参数用于表示需要查询的报文VPN编号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65535。<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SFEIPSACLTBL]] · 软转发SFE IPSEC-ACL表项信息（SFEIPSACLTBL）

## 使用实例

- 查询灵活引流ACL表类型信息：
  ```
  DSP SFEIPSACLTBL:RUNAME=" VNODE_VNRS_VNFC_IPU_0066",TABLETYPE= flex, INDEX=1,DESTIP="192.168.1.1", SOURCEIP="192.168.1.2",VPNID=3;
  ```
  ```

  RETCODE = 0  操作成功

  结果如下
  -------------------------
  动作索引号  =  0                                                                                       
  RE索引  =  17                                                                                      
  IPSEC出接口索引  =  12                                                                                      
  IPSEC Tunnel口绑定的Vpn  =  3

  (结果个数 = 1)
  ---    END
  ```
- 查询传输模式分流ACL表类型信息：
  ```
  DSP SFEIPSACLTBL:RUNAME=" VNODE_VNRS_VNFC_IPU_0066",TABLETYPE= split, PROTOCOL=17,DESTPORT=0,SOURCEPORT=0,INDEX=1,DESTIP="192.168.1.1", SOURCEIP="192.168.1.2",VPNID=3;
  ```
  ```

  RETCODE = 0  操作成功

  结果如下
  -------------------------
  动作索引号  =  0
  匹配动作 =  0
  目的RU号 = 65
  引擎口索引 = 10                                                                                                                                                                          
  IPSEC出接口索引  =  12                                                                                      
  IPSEC Tunnel口绑定的Vpn  =  3
  与对端建立的隧道编号 = 4001

  (结果个数 = 1)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-SFEIPSACLTBL.md`
