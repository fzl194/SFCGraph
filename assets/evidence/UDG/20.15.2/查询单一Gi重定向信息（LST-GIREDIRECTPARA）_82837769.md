# 查询单一Gi重定向信息（LST GIREDIRECTPARA）

- [命令功能](#ZH-CN_CONCEPT_0182837769__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0182837769__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0182837769__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0182837769__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0182837769__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0182837769__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0182837769)

**适用NF：SGW-U、PGW-U、UPF**

该命令用来查询指定VPN下的IPv4或IPv6 Gi重定向配置。

#### [注意事项](#ZH-CN_CONCEPT_0182837769)

无。

#### [操作用户权限](#ZH-CN_CONCEPT_0182837769)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0182837769)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VPNINSTANCE | 需绑定的VPN实例名 | 可选必选说明：必选参数<br>参数含义：该参数用于表示Gi重定向所绑定的VPN实例名。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，公网缺省VPN“_public_”不区分大小写，其它的VPN区分大小写。<br>默认值：无<br>配置原则：无 |
| IPTYPE | IP类型 | 可选必选说明：必选参数<br>参数含义：该参数用于表示重定向的目的地址类型。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- IPv4：表示地址类型为IPv4。<br>- IPv6：表示地址类型为IPv6。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0182837769)

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

#### [输出结果说明](#ZH-CN_CONCEPT_0182837769)

参见ADD GIREDIRECTPARA的参数说明。
