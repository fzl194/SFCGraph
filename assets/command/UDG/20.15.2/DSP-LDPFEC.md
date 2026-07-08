---
id: UDG@20.15.2@MMLCommand@DSP LDPFEC
type: MMLCommand
name: DSP LDPFEC（显示LDP FEC）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: LDPFEC
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- MPLS管理
- LDP管理
- LDP FEC
status: active
---

# DSP LDPFEC（显示LDP FEC）

## 功能

该命令用于显示LDP FEC。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VRFNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无 |
| FECADDR | 目的地址 | 可选必选说明：可选参数<br>参数含义：该参数用于表示目的地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：当“PREFIXLENGTH”参数被输入的时候，该参数也必须输入。 |
| PREFIXLENGTH | 前缀长度 | 可选必选说明：可选参数<br>参数含义：该参数用于表示目的地址的前缀长度。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～32。<br>默认值：无<br>配置原则：当“FECADDR”参数被输入的时候，该参数也必须输入。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/LDPFEC]] · LDP FEC（LDPFEC）

## 使用实例

显示LDP FEC：

```
DSP LDPFEC:;
```

```

RETCODE = 0  操作成功。

结果如下
--------
VPN实例名称  =  _public_
   目的地址  =  192.168.1.1
   前缀长度  =  32
   路由类型  =  IGP
    FEC状态  =  Up
  LSP下一跳  =  192.168.0.2
     出接口  =  LoopBack100
    LSP数量  =  1
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示LDP-FEC（DSP-LDPFEC）_49802378.md`
