---
id: UNC@20.15.2@MMLCommand@DSP IKEERRHISTORY
type: MMLCommand
name: DSP IKEERRHISTORY（显示IKE历史信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: IKEERRHISTORY
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- IPSEC功能管理
- 操作维护
- 系统调测
- IPsec调测
- IKE历史信息
status: active
---

# DSP IKEERRHISTORY（显示IKE历史信息）

## 功能

该命令用于显示IKE错误历史信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PODNAME | Pod名称 | 可选必选说明：必选参数<br>参数含义：Pod名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~63。<br>默认值：无<br>配置原则：无 |
| ADDRTYPE | 地址类型 | 可选必选说明：可选参数<br>参数含义：对端地址类型。<br>数据来源：对端协商<br>取值范围：<br>- IPV4（IPv4地址）<br>- IPV6（IPv6地址）<br>默认值：无<br>配置原则：无 |
| PEERIP | 对端IPv4地址 | 可选必选说明：该参数在"ADDRTYPE"配置为"IPV4"时为条件可选参数。<br>参数含义：对端IPv4地址。<br>数据来源：对端协商<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无 |
| PEERIP6 | 对端IPv6地址 | 可选必选说明：该参数在"ADDRTYPE"配置为"IPV6"时为条件可选参数。<br>参数含义：对端IPv6地址。<br>数据来源：对端协商<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |
| VRFNAME | VPN名称 | 可选必选说明：可选参数<br>参数含义：VRF名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~31。<br>默认值：无<br>配置原则：无 |
| PORTNUM | 端口号 | 可选必选说明：可选参数<br>参数含义：端口号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~65535。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [IKE历史信息清空状态（IKEERRHISTORY）](configobject/UNC/20.15.2/IKEERRHISTORY.md)

## 使用实例

显示IKE错误历史信息

```
DSP IKEERRHISTORY:PODNAME="ipsecexec-pod-0192-168-1-1",ADDRTYPE=IPV4;
   RETCODE = 0  操作成功.

   结果如下
   ------------------------
           Pod名称  =  ipsecexec-pod-0192-168-1-1
          地址类型  =  IPv4地址
   对端IPv4地址  =  10.1.1.2
              端口号  =  500
          VPN名称  =  _public_
          历史时间  =  2021-11-25 12:54:36
          历史原因  =  IKEV2_SA_DELETE_TYPE_EXCH_TIME_OUT
   (结果个数 = 1)   ---   END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示IKE历史信息（DSP-IKEERRHISTORY）_80751062.md`
