---
id: UDG@20.15.2@MMLCommand@DSP IPSUIT
type: MMLCommand
name: DSP IPSUIT（显示IPsuit信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: IPSUIT
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
- 逻辑接口管理
- IPSUIT 信息
status: active
---

# DSP IPSUIT（显示IPsuit信息）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用于查询IPSUIT信息。

## 注意事项

Owner PodName标识此IPSuit绑定的ownerid，Binding PodName标识此IPSuit绑定的实例的PodName。当发生ISU/APU发生故障倒换期间，Owner PodName和Binding PodName可能不一致。当IPSuit对应的token挂起时，Binding PodName可能为空，标识当前IPSuit未和任何ISU/APU绑定。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPSUITNAME | IPSuit 名称 | 可选必选说明：可选参数<br>参数含义：IP Suit的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。此名称系统自动生成，取值为1~64。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/IPSUIT]] · IPsuit信息（IPSUIT）

## 使用实例

- 查询IPSUIT信息，IPSUITNAME为“1”：
  ```
  DSP IPSUIT: IPSUITNAME="1";
  ```
  ```

  RETCODE = 0 操作成功。

  IPSuit 信息
  -----------
  Result  =  
                                IPSuit Name  =  1
                              Owner PodName  =  isu-pod-1
                            Binding PodName  =  isu-pod-1
               n3if1/1/0 Interface Info : 
                               IPV4 Address  =  192.168.0.1
                               IPV6 Address  =  2001:0DB8:0:0:0:0:0:0
                               VPN Instance  =  NULL
               s1-uif1/1/0 Interface Info : 
                               IPV4 Address  =  192.168.0.2
                               IPV6 Address  =  2001:0DB8:0:0:0:0:0:1
                               VPN Instance  =  NULL
               paif1/1/0 Interface Info : 
                               IPV4 Address  =  192.168.0.5
                               IPV6 Address  =  2001:0DB8:0:0:0:0:0:2
                               VPN Instance  =  NULL
               s5-sif1/1/0 Interface Info : 
                               IPV4 Address  =  192.168.0.3
                               IPV6 Address  =  2001:0DB8:0:0:0:0:0:3
                               VPN Instance  =  NULL
               n9cif1/1/0 Interface Info : 
                               IPV4 Address  =  192.168.0.4
                               IPV6 Address  =  2001:0DB8:0:0:0:0:0:4
                               VPN Instance  =  NULL
  (结果个数 = 1)

  ---    END
  ```
- 查询所有IPSUIT信息：
  ```
  DSP IPSUIT:;
  ```
  ```

  RETCODE = 0 操作成功。

  IPSuit 信息
  -----------
  Result
                                    IPSuit Name  =  1
                              Owner PodName  =  isu-pod-1
                            Binding PodName  =  isu-pod-1
               n3if1/1/0 Interface Info : 
                               IPV4 Address  =  192.168.0.1
                               IPV6 Address  =  2001:0DB8:0:0:0:0:0:0
                               VPN Instance  =  NULL
               n9cif1/1/0 Interface Info : 
                               IPV4 Address  =  192.168.0.2
                               IPV6 Address  =  2001:0DB8:0:0:0:0:0:1
                               VPN Instance  =  NULL
               paif1/1/0 Interface Info : 
                               IPV4 Address  =  192.168.0.3
                               IPV6 Address  =  2001:0DB8:0:0:0:0:0:2
                               VPN Instance  =  NULL
               s1-uif1/1/0 Interface Info : 
                               IPV4 Address  =  192.168.0.4
                               IPV6 Address  =  2001:0DB8:0:0:0:0:0:3
                               VPN Instance  =  NULL
               s5-sif1/1/0 Interface Info : 
                               IPV4 Address  =  192.168.0.5
                               IPV6 Address  =  2001:0DB8:0:0:0:0:0:4
                               VPN Instance  =  NULL  

                                IPSuit Name  =  2
                              Owner PodName  =  isu-pod-0
                            Binding PodName  =  isu-pod-0
               paif1/2/0 Interface Info : 
                               IPV4 Address  =  192.168.0.6
                               IPV6 Address  =  2001:0DB8:0:0:0:0:0:5
                               VPN Instance  =  NULL
               s1-uif1/2/0 Interface Info : 
                               IPV4 Address  =  192.168.0.7
                               IPV6 Address  =  2001:0DB8:0:0:0:0:0:6
                               VPN Instance  =  NULL
               s5-sif1/2/0 Interface Info : 
                               IPV4 Address  =  192.168.0.8
                               IPV6 Address  =  2001:0DB8:0:0:0:0:0:7
                               VPN Instance  =  NULL
               n3if1/2/0 Interface Info : 
                               IPV4 Address  =  192.168.0.9
                               IPV6 Address  =  2001:0DB8:0:0:0:0:0:8
                               VPN Instance  =  NULL                              
  (结果个数 = 2)

  --- END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示IPsuit信息（DSP-IPSUIT）_09988681.md`
