---
id: UNC@20.15.2@MMLCommand@LST DIAMETERAAA
type: MMLCommand
name: LST DIAMETERAAA（查询Diameter AAA服务器）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: DIAMETERAAA
command_category: 查询类
applicable_nf:
- PGW-C
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- Diameter AAA管理
- 服务器配置
- Diameter AAA信息
status: active
---

# LST DIAMETERAAA（查询Diameter AAA服务器）

## 功能

**适用NF：PGW-C**

此命令用于查询Diameter AAA服务器的基本信息。

可以查询一条指定的Diameter AAA服务器信息，也可以查询所有的Diameter AAA服务器信息。

## 注意事项

- 查询特定的Diameter AAA时，必须输入Diameter AAA主机名称。
- 如果不输入参数则是查询全部的Diameter AAA。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| HOSTNAME | 主机名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定Diameter AAA服务器的主机名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~127。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，由软参BIT150控制是否区分大小写。BIT150值为0时，不区分大小写；值为1时，区分大小写，但不允许配置多个仅大小写不同的host-name或realm-name。BIT150详细信息请参见产品文档中的《UNC软件参数》。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/DIAMETERAAA]] · Diameter AAA服务器（DIAMETERAAA）

## 使用实例

- 查询名称为“diameteraaa1”的Diameter AAA的信息：
  ```
  %%LST DIAMETERAAA:HOSTNAME="diameteraaa1";%%
  RETCODE = 0  操作成功

  Diameter AAA信息
  ----------------
     主机名  =  diameteraaa1
       域名  =  www.huawei.com
  VPN实例名  =  vpn1
      WAL值  =  0
  (结果个数 = 1)

  ---    END
  ```
- 查询系统中所有的Diameter AAA的信息：
  ```
  %%LST DIAMETERAAA:;%%
  RETCODE = 0  操作成功

  Diameter AAA信息
  ----------------
  主机名        域名            VPN实例名      WAL值

  diameteraaa1  www.huawei.com  vpn1            0
  diameteraaa2  www.hw.com      vpn2            0
  (结果个数 = 2)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询Diameter-AAA服务器（LST-DIAMETERAAA）_64343882.md`
