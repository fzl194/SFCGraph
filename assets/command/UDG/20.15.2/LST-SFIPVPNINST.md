---
id: UDG@20.15.2@MMLCommand@LST SFIPVPNINST
type: MMLCommand
name: LST SFIPVPNINST（查询SFIP VPN实例）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: SFIPVPNINST
command_category: 查询类
applicable_nf:
- EPSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- SFIP管理
- 网络管理
- SFIP VPN实例
status: active
---

# LST SFIPVPNINST（查询SFIP VPN实例）

## 功能

**适用NF：EPSN**

该命令用于显示VPN实例。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VPNINSTANCE | VPN实例名 | 可选必选说明：可选参数<br>参数含义：该参数用于设置VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/SFIPVPNINST]] ·  SFIP VPN实例（SFIPVPNINST）

## 使用实例

- 显示全部SFIPVPNInst业务配置：
  ```
  LST SFIPVPNINST:;
  ```
  ```

  RETCODE = 0  操作成功

  VPN实例信息
  ------------------------
  VPN实例名          描述信息  

  vpn1               vpn1         
  vpn2               vpn2         
  (结果个数  = 2)

  ---    END
  ```
- 指定VPN实例名显示SFIPVPNInst业务配置：
  ```
  LST SFIPVPNINST: VPNINSTANCE="vpn1";
  ```
  ```

  RETCODE = 0  操作成功

  VPN实例信息
  ------------------------
  VPN实例名  =  vpn1
  描述信息   =  vpn1
  (结果个数  = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-SFIPVPNINST.md`
