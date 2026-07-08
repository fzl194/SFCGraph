---
id: UNC@20.15.2@MMLCommand@LST RESERVEDIP
type: MMLCommand
name: LST RESERVEDIP（查询预留IP资源）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: RESERVEDIP
command_category: 查询类
applicable_nf:
- NCG
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NCG业务及策略管理
- 计费管理
- 业务系统管理
- 预留IP资源
status: active
---

# LST RESERVEDIP（查询预留IP资源）

## 功能

**适用NF：NCG**

该命令用于查询预留IP资源的详细信息：

如果需要查询全部信息，请不要输入任何参数。

如果需要查询某方面的详细信息，请输入具体参数。例如，查询用于话单分发的预留IP资源的详细信息，请输入“预留IP资源用途”值为“Bi”。

## 注意事项

- 无。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPRID | 预留IP资源标识 | 可选必选说明：可选参数<br>参数含义：用于表示一个预留IP资源对象，全局唯一。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32。<br>默认值：无<br>配置原则：无 |
| IPV4 | IPv4地址 | 可选必选说明：条件必选参数<br>参数含义：用于话单接收的IPv4地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型，0.0.0.0-255.255.255.255。<br>默认值：无<br>配置原则：无 |
| IPV6 | IPv6地址 | 可选必选说明：可选参数<br>参数含义：用于话单接收的IPv6地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。::～FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF。<br>默认值：无<br>配置原则：无 |
| IPRPURPOSE | 预留IP资源用途 | 可选必选说明：可选参数<br>参数含义：预留IP资源用途。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- Bi：Bi<br>- Omi：Omi<br>- OmiAndBi：Omi&Bi<br>默认值：无<br>配置原则：无 |
| PRFNAME | 格式引擎包名 | 可选必选说明：可选参数<br>参数含义：格式引擎包定义了CG话单处理的业务规则，主要包括话单字段过滤配置、分拣条件配置、通道配置、话单处理脚本等。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～255。<br>默认值：无<br>配置原则：无 |
| MNAME | 模块名称 | 可选必选说明：可选参数<br>参数含义：预留IP资源对应的模块。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～255。<br>默认值：无<br>配置原则：无 |
| RUID | RU的ID | 可选必选说明：可选参数<br>参数含义：RU的ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为64～4294967294。<br>默认值：无<br>配置原则：该值需要执行<br>[**LST SERVICERUSTATE**](../../../../../平台服务管理/单体服务编排功能管理/系统管理/资源管理/RU信息/查询RU的信息(LST SERVICERUSTATE)_29626965.md)<br>命令，查询出存在的RU ID进行填写。 |
| VPNNAME | 虚拟网络名称 | 可选必选说明：可选参数<br>参数含义：该参数为VPN名称，是业务消息转发时的鉴权参数。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [预留IP资源（RESERVEDIP）](configobject/UNC/20.15.2/RESERVEDIP.md)

## 使用实例

查询预留IP资源，示例如下：

```
LST RESERVEDIP:;
```

```
RETCODE = 0  操作成功。

结果如下:
--------
 预留IP资源标识  =  IP_66_Reserved_1st
       IPv4地址  =  10.31.14.3
       IPv6地址  =  ::
 预留IP资源用途  =  Bi
   格式引擎包名  =  PS_R15_VF80_Unicom.tar.gz
         模块名  =  AP66_1
         RU的ID  =  65
   虚拟网络名称  =  _public_
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询预留IP资源（LST-RESERVEDIP）_80309656.md`
