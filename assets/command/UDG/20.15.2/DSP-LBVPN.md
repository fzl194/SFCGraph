---
id: UDG@20.15.2@MMLCommand@DSP LBVPN
type: MMLCommand
name: DSP LBVPN（查询CSLB上的VPN信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: LBVPN
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- CSLB功能管理
- 业务管理
- VPN管理
- VPN信息
status: active
---

# DSP LBVPN（查询CSLB上的VPN信息）

## 功能

在CSLB上查询业务、CSLB和VNRS根据VPN名称分配的VPN索引。完成VPN配置后，可以通过这个命令检查是否有VPN分配失败。

## 注意事项

该命令批量下发可能导致执行超时。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SRVVNFCID | 业务VNFC ID | 可选必选说明：可选参数<br>参数含义：该参数用于指定业务VNFC的唯一标识，通过在窗口下执行<br>**[LST NODE](../../../../单体服务公共功能管理/系统管理/基础参数/查询节点信息/查询节点信息（LST NODE）_27372977.md)**<br>获得，所得NODEID即为服务VNFC ID。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为0~4294967295。<br>默认值：无 |
| VPNNAME | VPN名称 | 可选必选说明：可选参数<br>参数含义：业务配置的VPN名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为0~31。<br>默认值：无 |
| VPNQUERYMODE | VPN查询模式 | 可选必选说明：可选参数<br>参数含义：设置VPN查询模式。<br>数据来源：本端规划<br>取值范围：枚举类型<br>- VALID：查询有效的VPN。<br>- INVALID：查询无效的VPN。<br>- ALL：查询所有VPN。<br>默认值：INVALID |

## 操作的配置对象

- [CSLB上的VPN信息（LBVPN）](configobject/UDG/20.15.2/LBVPN.md)

## 使用实例

- 查询CSLB上的VPN信息。
  DSP LBVPN: VPNQUERYMODE=ALL;
  ```
  %%DSP LBVPN: VPNQUERYMODE=ALL;%%
  RETCODE = 0  操作成功

  操作结果如下：
  --------------
  业务VNFCID  VPN名称   业务分配的VPN索引  CSLB分配的VPN索引  VNRS分配的VPN索引  

  999         _public_  0                  0                  1                  
  2504        _public_  1                  0                  1                  
  129         _public_  1                  0                  1                  
  (结果个数 = 3)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询CSLB上的VPN信息（DSP-LBVPN）_29627074.md`
