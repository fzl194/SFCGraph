---
id: UDG@20.15.2@MMLCommand@DSP SRROUTE
type: MMLCommand
name: DSP SRROUTE（显示静态路由）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: SRROUTE
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- 静态路由调测
status: active
---

# DSP SRROUTE（显示静态路由）

## 功能

该命令用于显示配置的Ipv4静态路由的详细信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| AFTYPE | 地址族 | 可选必选说明：可选参数<br>参数含义：该参数用来指定VPN实例的地址族信息。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4unicast：IPv4单播。<br>默认值：ipv4unicast |
| VRFNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示路由前缀所属VPN实例的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：不输入默认查询公网。 |
| PREFIX | 路由前缀 | 可选必选说明：可选参数<br>参数含义：该参数用于表示路由前缀信息。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无 |
| MASKLENGTH | 路由掩码长度 | 可选必选说明：可选参数<br>参数含义：该参数用于表示路由的掩码长度。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～32。<br>默认值：无<br>配置原则：不可单独以掩码查询路由。掩码需要和前缀一起配置。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/SRROUTE]] · IPv4静态路由（SRROUTE）

## 使用实例

显示IPv4静态路由表：

```
DSP SRROUTE:;
```

```

RETCODE = 0  操作成功

结果如下
-------------------------
                      地址族  =  IPv4单播
                 VPN实例名称  =  _public_
                    路由前缀  =  10.0.0.1
                路由掩码长度  =  32
                路由接口名字  =  NULL0
               下一跳VPN名字  =  _public_
                  路由下一跳  =  10.0.0.2
                  路由优先级  =  125
                   路由Tag值  =  0
                 BFD检测结果  =  Disable
                     BFD类型  =  NULL
                    路由状态  =  Active Primary
              路由迭代下一跳  =  NULL
                         IID  =  0x34000040
                路由接口状态  =  UP
              路由迭代出接口  =  NULL
                   BFD会话名  =  --
                  路由开销值  =  0
                路由本地地址  =  NULL
                路由远程地址  =  NULL
            继承迭代路由cost  =  FALSE
                      隧道ID  =  --
                是否永久发布  =  FALSE
                        标签  =  NULL
                 EFM接口名称  =  --
                 EFM探测结果  =  Disable
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-SRROUTE.md`
