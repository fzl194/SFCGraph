---
id: UDG@20.15.2@MMLCommand@DSP LDPLSPMGIID
type: MMLCommand
name: DSP LDPLSPMGIID（显示LDP的IID信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: LDPLSPMGIID
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- LDP维护
status: active
---

# DSP LDPLSPMGIID（显示LDP的IID信息）

## 功能

该命令用于显示LDP的IID信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VRFNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：_public_ |
| FECFLAG | 目的地址标志位 | 可选必选说明：可选参数<br>参数含义：该参数用于表示LSP的目的地址标志位。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- IIDINDEX：指定IID索引。<br>- FECADDR：指定目的地址。<br>默认值：无 |
| FECADDR | 目的地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“FECFLAG”配置为“FECADDR”时为必选参数。<br>参数含义：该参数用于指定LSP的目的地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无 |
| PREFIXLENGTH | 前缀长度 | 可选必选说明：条件必选参数<br>前提条件：该参数在“FECFLAG”配置为“FECADDR”时为必选参数。<br>参数含义：该参数用于指定目的地址的前缀长度。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～32。<br>默认值：无 |
| IIDINDEX | IID索引 | 可选必选说明：条件必选参数<br>前提条件：该参数在“FECFLAG”配置为“IIDINDEX”时为必选参数。<br>参数含义：该参数用于指定LSP的IID索引。<br>数据来源：本端规划<br>取值范围：十六进制整数类型，取值范围为0x0～0xFFFFFFFF。<br>默认值：无 |

## 操作的配置对象

- [LDP的IID信息（LDPLSPMGIID）](configobject/UDG/20.15.2/LDPLSPMGIID.md)

## 使用实例

显示LDP的IID信息：

```
DSP LDPLSPMGIID:VRFNAME="_public_",FECFLAG=IIDINDEX,IIDINDEX="100000F";
```

```

RETCODE = 0  操作成功。

结果如下
--------
             VPN实例名称  =  _public_
                 IID索引  =  0x100000f
是否收到所有对应的下一跳  =  是
            下一跳的类型  =  IP类型
                IP地址族  =  IPv4地址族
              平滑版本号  =  2
              备份版本号  =  1
              下一跳地址  =  192.168.0.1
      下一跳对应的邻居ID  =  10.10.10.10
              出接口名称  =  Ethernet64/0/5
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示LDP的IID信息（DSP-LDPLSPMGIID）_49802610.md`
