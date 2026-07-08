---
id: UDG@20.15.2@MMLCommand@DSP LDPLSPMGDSSUB
type: MMLCommand
name: DSP LDPLSPMGDSSUB（显示LDP的下游信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: LDPLSPMGDSSUB
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

# DSP LDPLSPMGDSSUB（显示LDP的下游信息）

## 功能

该命令用于显示LDP的下游信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VRFNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：_public_ |
| FECFLAG | 目的地址标志位 | 可选必选说明：可选参数<br>参数含义：该参数用于表示目的地址标志位。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- NOFEC：不指定目的地址。<br>- FECADDR：指定目的地址。<br>默认值：NOFEC |
| FECADDR | 目的地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“FECFLAG”配置为“FECADDR”时为必选参数。<br>参数含义：该参数用于表示目的地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无 |
| PREFIXLENGTH | 前缀长度 | 可选必选说明：条件必选参数<br>前提条件：该参数在“FECFLAG”配置为“FECADDR”时为必选参数。<br>参数含义：该参数用于表示前缀长度。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～32。<br>默认值：无 |
| PEERID | 对等体的LSR ID | 可选必选说明：可选参数<br>参数含义：该参数用于表示对等体的LSR ID。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/LDPLSPMGDSSUB]] · LDP的下游信息（LDPLSPMGDSSUB）

## 使用实例

显示LDP的下游信息：

```
DSP LDPLSPMGDSSUB:;
```

```

RETCODE = 0  操作成功

结果如下
------------------------
      VPN实例名称  =  _public_
         目的地址  =  192.168.2.2
         前缀长度  =  32
   对等体的LSR ID  =  192.168.2.2
           出标签  =  3
  LSP最大传输单元  =  65535
         订阅状态  =  订阅
         主备角色  =  主
LDP邻居备份版本号  =  1
LDP邻居平滑版本号  =  0
    LDP会话版本号  =  1
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示LDP的下游信息（DSP-LDPLSPMGDSSUB）_49962110.md`
