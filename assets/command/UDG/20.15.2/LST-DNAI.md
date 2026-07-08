---
id: UDG@20.15.2@MMLCommand@LST DNAI
type: MMLCommand
name: LST DNAI（查询DNAI配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: DNAI
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- DN管理
- DNAI管理
- 数据网络接入标识
status: active
---

# LST DNAI（查询DNAI配置）

## 功能

**适用NF：PGW-U、UPF**

该命令用来查看指定DNAI实例或者已配置所有DNAI实例的配置信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DNAI | 数据网络接入标识 | 可选必选说明：可选参数<br>参数含义：数据网络接入标识。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。名称中不能包含空格，不区分大小写。<br>默认值：无<br>配置原则：输入的DNAI名称需要符合DNAI命名规则。 |

## 操作的配置对象

- [DNAI配置（DNAI）](configobject/UDG/20.15.2/DNAI.md)

## 使用实例

- 显示指定DNAI实例的信息：
  ```
  LST DNAI:DNAI="huawei01.com";
  ```
  ```

  %%LST DNAI: DNAI="huawei01.com";%%
  RETCODE = 0  操作成功

  DNAI信息
  --------
  数据网络接入标识  =  huawei01.com
           绑定VPN  =  使能
         VPN实例名  =  vpn01
      绑定IPv6 VPN  =  不使能
    IPv6 VPN实例名  =  NULL
       NAT功能开关  =  使能
          锁定  =  不使能
  (结果个数 = 1)

  ---    END
  ```
- 查询整机DNAI实例信息：
  ```
  LST DNAI:;
  ```
  ```

  %%LST DNAI:;%%
  RETCODE = 0  操作成功

  DNAI信息
  --------
  数据网络接入标识  绑定VPN  VPN实例名  绑定IPv6 VPN  IPv6 VPN实例名  NAT功能开关  锁定

  huawei01.com      使能     vpn01      不使能        NULL            使能         不使能
  huawei02.com      使能     vpn02      不使能        NULL            使能         不使能
  huawei03.com      使能     vpn03      不使能        NULL            不使能       不使能
  (结果个数 = 3)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询DNAI配置（LST-DNAI）_53878585.md`
