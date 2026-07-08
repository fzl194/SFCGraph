---
id: UDG@20.15.2@MMLCommand@LST AUTOSCALINGSRROUTE
type: MMLCommand
name: LST AUTOSCALINGSRROUTE（查询静态路由自动化配置模板）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: AUTOSCALINGSRROUTE
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 自动部署
- 静态路由自动化配置
status: active
---

# LST AUTOSCALINGSRROUTE（查询静态路由自动化配置模板）

## 功能

该命令用于查询静态路由自动化配置模板。

## 注意事项

如果地址族取值为IPv4，则路由掩码长度取值范围为0到32，如果地址族取值为IPv6，则路由掩码长度取值范围为0到128。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SERVICENAME | 服务名称 | 可选必选说明：可选参数<br>参数含义：该参数用来表示接口自动化配置服务模板名称。要求和ADD AUTOSCALINGSERVICE命令中配置的SERVICENAME参数保持一致。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格和中文。<br>默认值：无 |
| IPVERSION | 地址族 | 可选必选说明：可选参数<br>参数含义：该参数用来指定VPN实例的地址族信息。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- IPv4：IPv4地址族。<br>- IPv6：IPv6地址族。<br>默认值：无 |
| VRFNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用来指定VPN实例的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格和中文。<br>默认值：无<br>配置原则：公网需要输入_public_，默认查询所有VPN。 |
| PREFIX4 | 路由前缀IPv4 | 可选必选说明：条件可选参数<br>前提条件：该参数在“IPVERSION”配置为“IPv4”时为可选参数。<br>参数含义：该参数用来指定IPv4前缀信息。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无 |
| PREFIX6 | 路由前缀IPv6 | 可选必选说明：条件可选参数<br>前提条件：该参数在“IPVERSION”配置为“IPv6”时为可选参数。<br>参数含义：该参数用来指定IPv6前缀信息。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。<br>默认值：无 |
| MASKLENGTH | 路由掩码长度 | 可选必选说明：可选参数<br>参数含义：IPv4场景，该参数用于表示路由的掩码长度；IPv6场景，该参数用于表示路由的前缀长度。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～128。<br>默认值：无<br>配置原则：不可单独以掩码查询静态路由自动化配置服务模板。掩码需要和前缀一起配置。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/AUTOSCALINGSRROUTE]] · 静态路由自动化配置模板（AUTOSCALINGSRROUTE）

## 使用实例

查询静态路由自动化配置模板信息：

```
LST AUTOSCALINGSRROUTE: SERVICENAME="abc";
```

```

RETCODE = 0  操作成功

结果如下
-------------------------
                 地址族  =  IPv4地址族
               服务名称  =  abc
            VPN实例名称  =  _public_
           路由前缀IPv4  =  192.168.0.1
           路由前缀IPv6  =  ::
           路由掩码长度  =  32
 IPv4路由下一跳分配方式  =  用户配置方式
 IPv6路由下一跳分配方式  =  NULL
         路由下一跳IPv4  =  192.168.0.3
         路由下一跳IPv6  =  ::
             路由优先级  =  60
            BFD使能标识  =  否
                路由tag  =  0
               路由描述  =  NULL
            BFD模板名称  =  NULL
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-AUTOSCALINGSRROUTE.md`
