---
id: UDG@20.15.2@MMLCommand@LST VPNINST
type: MMLCommand
name: LST VPNINST（查询VPN实例）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: VPNINST
command_category: 查询类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- DN管理
- VPN管理
- VPN
status: active
---

# LST VPNINST（查询VPN实例）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用于显示VPN实例。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VPNINSTANCE | VPN实例名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定VPN实例，该参数一般由运营商规划给出。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～31。区分大小写。<br>默认值：无<br>配置原则：“_public_”是公网缺省VPN的实例名，不对用户体现。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@VPNINST]] · VPN实例（VPNINST）

## 使用实例

- 显示VPNInst业务配置：
  ```
  LST VPNINST:;
  ```
  ```

  RETCODE = 0  操作成功

  VPN实例信息
  ------------------------
  VPN实例名

  vpn1               
  vpn2               
  (结果个数 = 2)

  ---    END
  ```
- 指定VPN实例名显示VPNInst业务配置：
  ```
  LST VPNINST: VPNINSTANCE="vpn1";
  ```
  ```

  RETCODE = 0  操作成功

  VPN实例信息
  ------------------------
  VPN实例名  =  vpn1
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-VPNINST.md`
