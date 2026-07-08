---
id: UDG@20.15.2@MMLCommand@LST GIREDIRECTPARA
type: MMLCommand
name: LST GIREDIRECTPARA（查询单一Gi重定向信息）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: GIREDIRECTPARA
command_category: 查询类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务安全防护
- 用户攻击防护
- Gi重定向
- Gi重定向参数
status: active
---

# LST GIREDIRECTPARA（查询单一Gi重定向信息）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用来查询指定VPN下的IPv4或IPv6 Gi重定向配置。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VPNINSTANCE | 需绑定的VPN实例名 | 可选必选说明：必选参数<br>参数含义：该参数用于表示Gi重定向所绑定的VPN实例名。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，公网缺省VPN“_public_”不区分大小写，其它的VPN区分大小写。<br>默认值：无<br>配置原则：无 |
| IPTYPE | IP类型 | 可选必选说明：必选参数<br>参数含义：该参数用于表示重定向的目的地址类型。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- IPv4：表示地址类型为IPv4。<br>- IPv6：表示地址类型为IPv6。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/GIREDIRECTPARA]] · 单一Gi重定向信息（GIREDIRECTPARA）

## 使用实例

- 查询缺省VPN的IPv4 Gi重定向信息：
  ```
  LST GIREDIRECTPARA:VPNINSTANCE="_public_",IPTYPE=IPv4;
  ```
  ```

  RETCODE = 0  操作成功。

  IPv4 Gi重定向配置信息
  ---------------------
     需绑定的VPN实例名  =  _public_
  重定向的目的地址类型  =  IPv4
        IPv4重定向动作  =  IP地址
      IPv4重定向IP地址  =  192.168.0.1
  (结果个数 = 1)
  ---    END
  ```
- 查询名为“vpn1”的VPN下的IPv6 Gi重定向信息：
  ```
  LST GIREDIRECTPARA: VPNINSTANCE="vpn1",IPTYPE=IPv6;
  ```
  ```

  RETCODE = 0  操作成功。

  IPv6 Gi重定向配置信息
  ---------------------
     需绑定的VPN实例名  =  vpn1
  重定向的目的地址类型  =  IPv6
        IPv6重定向动作  =  IP地址
      IPv6重定向IP地址  =  fe80:1234:5678:9abc:d012:3456:789a:bcde
  (结果个数 = 1)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询单一Gi重定向信息（LST-GIREDIRECTPARA）_82837769.md`
