---
id: UNC@20.15.2@MMLCommand@DSP CGSTATUS
type: MMLCommand
name: DSP CGSTATUS（查询CG状态）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: CGSTATUS
command_category: 查询类
applicable_nf:
- SGW-C
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 离线计费
- GTPP信令
- CG状态
status: active
---

# DSP CGSTATUS（查询CG状态）

## 功能

**适用NF：SGW-C、PGW-C、SMF**

该命令用于查询所有CG或指定CG的工作状态。如果不输入要查询CG的IP地址，则显示所有CG信息。

## 注意事项

返回的记录数超过300条时，可能不全。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CGIPVERSION | CG IP版本 | 可选必选说明：可选参数<br>参数含义：该参数用于指定CG IP类型。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- IPV4：IPv4。<br>- IPV6：IPv6。<br>默认值：无<br>配置原则：无 |
| CGIPV4ADDR | CG IPv4地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“CGIPVERSION”配置为“IPV4”时为必选参数。<br>参数含义：指定CG服务器的IPv4地址。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无 |
| CGIPV6ADDR | CG IPv6地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“CGIPVERSION”配置为“IPV6”时为必选参数。<br>参数含义：指定CG服务器的IPv6地址。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/CGSTATUS]] · CG状态（CGSTATUS）

## 使用实例

查询IP地址为192.168.61.60的CG的链路状态：

```
DSP CGSTATUS: CGIPVERSION=IPV4, CGIPV4ADDR="192.168.61.60";
```

```

RETCODE = 0  操作成功

CG状态
------
POD名称   Ga IP地址     CG端口号  CG类型   CG状态    Ga端口号  CG IP地址     

uncpod-0  172.20.10.70  25008     R8 ALL   abnormal  10601     192.168.61.60  
uncpod-0  172.20.10.70  34007     R7       abnormal  10601     192.168.61.60  
uncpod-0  172.20.10.70  25006     R6       abnormal  10601     192.168.61.60  
uncpod-0  172.20.10.70  25005     R5       abnormal  10601     192.168.61.60  
uncpod-0  172.20.10.70  25004     R4       abnormal  10601     192.168.61.60  
uncpod-0  172.20.10.70  25098     R98      abnormal  10601     192.168.61.60  
uncpod-0  172.20.10.70  25099     R99      abnormal  10601     192.168.61.60  
uncpod-0  172.20.10.70  25009     R9 ALL   abnormal  10601     192.168.61.60  
uncpod-0  172.20.10.70  25010     R10 ALL  abnormal  10601     192.168.61.60  
(结果个数 = 9)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-CGSTATUS.md`
