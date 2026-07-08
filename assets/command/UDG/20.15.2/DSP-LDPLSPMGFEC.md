---
id: UDG@20.15.2@MMLCommand@DSP LDPLSPMGFEC
type: MMLCommand
name: DSP LDPLSPMGFEC（显示LDP LSP管理组件的FEC信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: LDPLSPMGFEC
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

# DSP LDPLSPMGFEC（显示LDP LSP管理组件的FEC信息）

## 功能

该命令用于显示LDP LSP管理组件的FEC信息。

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

- [[configobject/UDG/20.15.2/LDPLSPMGFEC]] · LDP LSP管理组件的FEC信息（LDPLSPMGFEC）

## 使用实例

显示LDP LSP管理组件的FEC信息：

```
DSP LDPLSPMGFEC:FECADDR="192.168.1.1",PREFIXLENGTH=32;
```

```

RETCODE = 0  操作成功。

结果如下
--------
                    VPN实例名称  =  _public_
                       目的地址  =  192.168.1.1
                       前缀长度  =  32
                       路由开销  =  0
      上次更新到现在的时间（s）  =  277
                       路由类型  =  Direct
                       策略结果  =  Egress角色
                   主机路由标记  =  TRUE
           直连Loopback接口路由  =  TRUE
                   网关地址标记  =  TRUE
                 下一跳切换处理  =  FALSE
               路由开销更新处理  =  FALSE
                   标签请求标记  =  FALSE
                     备份版本号  =  1
                     平滑版本号  =  0
                        FEC事件  =  空
                       等待处理  =  FALSE
                   缓存资源个数  =  0
                        FRR角色  =  主路径
                         IID索引 =  0x1b000032
                         下一跳  =  192.168.0.2
                         出接口  =  LoopBack0
                      FEC触发源  =  下游Mapping触发
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-LDPLSPMGFEC.md`
