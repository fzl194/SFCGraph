---
id: UNC@20.15.2@MMLCommand@DSP IPSECSATABLE
type: MMLCommand
name: DSP IPSECSATABLE（显示IPsec SA表信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: IPSECSATABLE
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- IPSEC功能管理
- 操作维护
- 系统调测
- IPsec调测
- IPSECSA表
status: active
---

# DSP IPSECSATABLE（显示IPsec SA表信息）

## 功能

该命令用于查询IPsec Sa表信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PODNAME | Pod名称 | 可选必选说明：可选参数<br>参数含义：该参数用于描述IPSEC SA的pod名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~63。<br>默认值：无<br>配置原则：无 |
| SAID | SA标识 | 可选必选说明：可选参数<br>参数含义：该参数用于描述IPSEC SA的SA标识。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~4294967295。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/IPSECSATABLE]] · IPsec SA表信息（IPSECSATABLE）

## 使用实例

显示IPsec SA表信息

```
DSP IPSECSATABLE:;
        RETCODE = 0 操作成功

        结果如下
        ------------------------
                              Pod名称  =  ipsecexec-pod-0192-168-1-1
                               SA标识  =  0
                         下一个SA标识  =  0
                              IKE Pid  =  26738720
                             策略索引  =  1
                             策略名称  =  NULL
                         策略序列号  =  1
                               源端口  =  500
                             目的端口  =  500
                              ACL组ID  =  1
                          ACL规则编号  =  1
                             接口索引  =  14
                         安全参数索引  =  3066727525
                         隧道源IPV4地址  =  10.1.1.1
                       隧道目的IPv4地址  =  10.1.1.2
                         隧道源IPV6地址  =  0::0
                       隧道目的IPv6地址  =  0::0
                             链路MTU = 1500
                               协议号  =  50
                               SA模式  =  0
                                 模式  =  1
                             加密算法  =  7
                             认证算法  =  8
                            Block大小  =  16
                                 标记  =  0
                          入向VPN索引  =  0
                          出向VPN索引  =  0
               下一个SA的安全参数索引  =  0
                            配对SA ID  =  1
                 配对SA的安全参数索引  =  587287825
                                 方向  =  2
                         流量生命周期  =  1843200
        (结果个数 = 1)
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-IPSECSATABLE.md`
