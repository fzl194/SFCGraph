---
id: UDG@20.15.2@MMLCommand@LST TCPMSS
type: MMLCommand
name: LST TCPMSS（查询Tcp Mss配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: TCPMSS
command_category: 查询类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 传输层控制
- TCP MSS
status: active
---

# LST TCPMSS（查询Tcp Mss配置）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用于查询指定APN的TCP MSS值。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示APN的名字。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/TCPMSS]] · Tcp Mss配置（TCPMSS）

## 使用实例

- 查询apn apn1.com的TCP MSS值：
  ```
  LST TCPMSS:APN="apn1.com";
  ```
  ```

  RETCODE = 0 操作成功。

  结果如下
  --------
  APN名称 = apn1.com
  用户漫游类型 = home
  IPv4 TCP报文长度（字节） = 1300
  IPv6 TCP报文长度（字节） = 1400
  (结果个数 = 1)
  --- END
  ```
- 查询所有apn的TCP MSS值：
  ```
  LST TCPMSS:;
  ```
  ```

  RETCODE = 0 操作成功。

  结果如下
  --------
  APN名称 用户漫游类型 IPv4 TCP报文长度（字节） IPv6 TCP报文长度（字节）

  apn1.com home 1300 1400
  apn2.com home&roaming&visiting 496 496
  (结果个数 = 2)
  --- END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询Tcp-Mss配置（LST-TCPMSS）_82837697.md`
