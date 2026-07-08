---
id: UDG@20.15.2@MMLCommand@DSP L2TPSESSION
type: MMLCommand
name: DSP L2TPSESSION（查询L2TP隧道下L2TP会话相关信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: L2TPSESSION
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 会话管理
- L2TP隧道管理
- L2TP会话查询
status: active
---

# DSP L2TPSESSION（查询L2TP隧道下L2TP会话相关信息）

## 功能

**适用NF：PGW-U、UPF**

该命令用于查看指定L2TP会话或指定接口的指定L2TP隧道下所有L2TP会话的相关信息。当运营商想查看隧道的会话信息时，可以使用该命令进行查询。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INTERFACENAME | 接口名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定查询的Gi接口名字。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：无 |
| TUNNELID | L2TP隧道号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定查询的隧道号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～64000。<br>默认值：无<br>配置原则：无 |
| SESSIONID | L2TP会话号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定查询的会话号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～65535。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@L2TPSESSION]] · L2TP隧道下L2TP会话相关信息（L2TPSESSION）

## 使用实例

- 运营商如果需要查看giif1/0/0接口下，隧道ID为1，会话ID为2的会话的信息：
  ```
  DSP L2TPSESSION: INTERFACENAME="giif1/0/0",TUNNELID=1,SESSIONID=2;
  ```
  ```

  L2TP session info
  -----------------
          Remote Name  =  NULL
         Group Number  =  869
      Local Tunnel ID  =  1
     Remote Tunnel ID  =  5
             Sessions  =  1
          Remote Port  =  1701
            Giif Name  =  giif1/0/0
              IP Type  =  IPV6
  Remote IPv4 Address  =  NULL
  Remote IPv6 Address  =  2001:DB8:0:0:0:0:0:84
    Giif IPv4 Address  =  NULL
    Giif IPv6 Address  =  FE80:64:83:3:0:0:0:82
               Uptime  =  0 days, 0 hours, 0 minutes
     Local Session Id  =  1
    Remote Session Id  =  101
               Msisdn  =  12341234
  (Number of results = 1)
  ```
- 运营商如果需要查看giif1/0/0接口下，ID为1的隧道的所有会话信息：
  ```
  DSP L2TPSESSION:INTERFACENAME="giif1/0/0",TUNNELID=1;
  ```
  ```

  L2TP session info
  -----------------
  Remote Name    Group Number    Local Tunnel ID    Remote Tunnel ID    Sessions    Giif Name    Remote Port    IP Type    Remote IPv4 Address    Remote IPv6 Address    Giif IPv4 Address    Giif IPv6 Address    Uptime                        Local Session Id   Remote Session Id   Msisdn
  NULL           1               1                  5                   1            Giif1/0/0    1701           IPV4       192.168.6.97          NULL                   10.0.4.1             NULL                0 days, 0 hours, 1 minutes    1                  102                 8613801040032        
  NULL           1               1                  5                   1            Giif1/0/0    1701           IPV4       192.168.6.97          NULL                   10.0.4.1             NULL                0 days, 0 hours, 1 minutes    1                  102                 8613801040032        
  (Number of results = 2)
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-L2TPSESSION.md`
