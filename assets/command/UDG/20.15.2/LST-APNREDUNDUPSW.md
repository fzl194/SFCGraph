---
id: UDG@20.15.2@MMLCommand@LST APNREDUNDUPSW
type: MMLCommand
name: LST APNREDUNDUPSW（查询指定APN静态地址路由冗余上行报文隧道转发功能开关）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: APNREDUNDUPSW
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 会话管理
- 会话地址管理
- 静态地址用户路由冗余
- APN静态路由冗余上行报文隧道转发功能配置
status: active
---

# LST APNREDUNDUPSW（查询指定APN静态地址路由冗余上行报文隧道转发功能开关）

## 功能

**适用NF：PGW-U、UPF**

该命令用于查询指定APN静态地址路由冗余上行报文隧道转发功能开关。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：可选参数<br>参数含义：指定APN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格以及特殊字符：“_”、“#”、“$”、“&”等，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/APNREDUNDUPSW]] · 指定APN静态地址路由冗余上行报文隧道转发功能开关（APNREDUNDUPSW）

## 使用实例

- 假设用户要查询所有APN下配置的静态地址路由冗余上报隧道转发功能相关信息：
  ```
  LST APNREDUNDUPSW:;
  ```
  ```

  %%LST APNREDUNDUPSW:;%%
  RETCODE = 20111  There is no data in the table.

  No matching result is found
  ---    END
  ```
- 假设用户要查询APN “huawei.com”下配置的静态地址路由冗余上报隧道转发功能相关信息：
  ```
  LST APNREDUNDUPSW:APN="huawei.com";
  ```
  ```

  %%LST APNREDUNDUPSW: APN="huawei.com";%%
  RETCODE = 0  Operation succeeded

  APN Routing Redundancy Uplink Packet Tunnel Forwarding Switch Information
  -------------------------------------------------------------------------
                                 APN  =  huawei.com
  APN-specific IPV4 Redund up Switch  =  DISABLE
  APN-specific IPV6 Redund up Switch  =  DISABLE
  (Number of results = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询指定APN静态地址路由冗余上行报文隧道转发功能开关（LST-APNREDUNDUPSW）_75097450.md`
