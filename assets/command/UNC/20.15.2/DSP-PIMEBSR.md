---
id: UNC@20.15.2@MMLCommand@DSP PIMEBSR
type: MMLCommand
name: DSP PIMEBSR（查询EBSR信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: PIMEBSR
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP组播
- PIM配置
- BSR信息
status: active
---

# DSP PIMEBSR（查询EBSR信息）

## 功能

该命令用于显示EBSR信息。

## 注意事项

该命令仅适用于非NP卡场景和NP卡非加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ADDRESSFAMILY | 地址族 | 可选必选说明：必选参数<br>参数含义：该参数用于表示地址族类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4unicast：IPv4单播。<br>默认值：无 |
| VRFNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用来表示VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：_public_<br>配置原则：通过LST L3VPNINST查看当前已存在的VPN实例。 |
| BSRADDR | 当选ASBSR地址 | 可选必选说明：条件可选参数<br>前提条件：该参数在“ADDRESSFAMILY”配置为“ipv4unicast”时为可选参数。<br>参数含义：该参数用来表示当选ASBSR地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无 |
| MASTERSLAVETYPE | OMU类型 | 可选必选说明：可选参数<br>参数含义：该参数表示OMU类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- MASTER：主。<br>- SLAVE：备。<br>默认值：MASTER |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PIMEBSR]] · EBSR信息（PIMEBSR）

## 使用实例

显示EBSR信息：

```
DSP PIMEBSR:VRFNAME="_public_",ADDRESSFAMILY=ipv4unicast;
```

```
RETCODE = 0  操作成功。

结果如下
--------
                 VPN实例名称  =  _public_
                      地址族  =  IPv4单播
               当选ASBSR地址  =  192.168.1.1
    该BSR是否为管理域中的BSR  =  管理区域BSR
                      组地址  =  239.0.0.1
              组地址掩码长度  =  16
             当选ASBSR优先级  =  0
           当选ASBSR哈希长度  =  30
               当选ASBSR状态  =  Elected状态
      当选ASBSR成为BSR的时间  =  00:17:12
当选ASBSR发送下一个BSM的时间  =  00:00:12
                候选RP的个数  =  1
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询EBSR信息（DSP-PIMEBSR）_50121218.md`
