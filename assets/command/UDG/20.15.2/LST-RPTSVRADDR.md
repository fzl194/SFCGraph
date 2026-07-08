---
id: UDG@20.15.2@MMLCommand@LST RPTSVRADDR
type: MMLCommand
name: LST RPTSVRADDR（显示报表服务器接入点配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: RPTSVRADDR
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务报表管理
- 报表服务器管理
- 报表服务器地址
status: active
---

# LST RPTSVRADDR（显示报表服务器接入点配置）

## 功能

**适用NF：PGW-U、UPF**

该命令用于查询配置的接入点。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RPTSVRNAME | 报表服务器名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置对应的报表服务器名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/RPTSVRADDR]] · 报表服务器接入点配置（RPTSVRADDR）

## 使用实例

- 显示所有配置的接入点：
  ```
  LST RPTSVRADDR:;
  ```
  ```

  RETCODE = 0 操作成功

  接入点信息
  ----------
  接入点名称  报表服务器名称  IP类型  IPv4地址      IPv6地址  VPN实例名称  端口号  

  access01    und01           IPV4    192.168.0.1   ::        test_vpn     100     
  access02    und02           IPV4    192.168.0.10  ::        test_vpn     100     
  (结果个数 = 2)

  ---    END
  ```
- 显示udn01报表服务器下的接入点：
  ```
  LST RPTSVRADDR: RPTSVRNAME="und01";
  ```
  ```

  RETCODE = 0 操作成功

  接入点信息
  ----------
      接入点名称  =  access01
  报表服务器名称  =  und01
          IP类型  =  IPV4
        IPv4地址  =  192.168.0.1
        IPv6地址  =  ::
     VPN实例名称  =  test_vpn
          端口号  =  100
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-RPTSVRADDR.md`
