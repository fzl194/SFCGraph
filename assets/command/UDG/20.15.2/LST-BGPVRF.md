---
id: UDG@20.15.2@MMLCommand@LST BGPVRF
type: MMLCommand
name: LST BGPVRF（查询BGP VPN实例）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: BGPVRF
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- BGP管理
- BGP VPN实例
status: active
---

# LST BGPVRF（查询BGP VPN实例）

## 功能

该命令用于查询已配置的BGP VPN实例。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VRFNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定BGP VPN实例。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@BGPVRF]] · BGP VPN实例（BGPVRF）

## 使用实例

查询所有BGP VPN实例：

```
LST BGPVRF:;
```

```

RETCODE = 0  操作成功

结果如下
-------------------------
        VPN实例名称  =  _public_
         默认地址族  =  IPv4uni
       EBGP接口感知  =  TRUE
       IBGP接口感知  =  FALSE
         路由器编号  =  NULL
VPN路由器号自动选择  =  FALSE
       存活时间（s） =  60
       保持时间（s） =  180
       重连时间（s） =  32
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-BGPVRF.md`
