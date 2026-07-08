---
id: UDG@20.15.2@MMLCommand@DSP PIMCTLMSGCNTVRF
type: MMLCommand
name: DSP PIMCTLMSGCNTVRF（查询PIM实例报文统计计数）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: PIMCTLMSGCNTVRF
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP组播
- PIM配置
- PIM报文统计计数
status: active
---

# DSP PIMCTLMSGCNTVRF（查询PIM实例报文统计计数）

## 功能

该命令用于显示PIM实例报文统计计数。

## 注意事项

该命令仅适用于非NP卡场景和NP卡非加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ADDRESSFAMILY | 地址族 | 可选必选说明：必选参数<br>参数含义：该参数用于表示地址族类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4unicast：IPv4单播。<br>默认值：无 |
| VRFNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：_public_<br>配置原则：通过LST L3VPNINST查看当前已存在的VPN实例。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@PIMCTLMSGCNTVRF]] · PIM实例报文统计计数（PIMCTLMSGCNTVRF）

## 使用实例

显示PIM实例报文统计计数：

```
DSP PIMCTLMSGCNTVRF:VRFNAME="_public_",ADDRESSFAMILY=ipv4unicast;
```

```
RETCODE = 0  操作成功。

结果如下
--------
         VPN实例名称  =  _public_
              地址族  =  IPv4单播
    收到注册报文数目  =  0
    发送注册报文数目  =  0
    无效注册报文数目  =  0
    过滤注册报文数目  =  0
收到注册停止报文数目  =  0
发送注册停止报文数目  =  0
无效注册停止报文数目  =  0
过滤注册停止报文数目  =  0
  收到空注册报文数目  =  0
  发送空注册报文数目  =  0
  无效空注册报文数目  =  0
  过滤空注册报文数目  =  0
     收到CRP报文数目  =  0
     发送CRP报文数目  =  0
     无效CRP报文数目  =  0
     过滤CRP报文数目  =  0
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-PIMCTLMSGCNTVRF.md`
