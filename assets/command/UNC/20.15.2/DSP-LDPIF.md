---
id: UNC@20.15.2@MMLCommand@DSP LDPIF
type: MMLCommand
name: DSP LDPIF（显示LDP接口状态）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: LDPIF
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- MPLS管理
- LDP管理
- LDP接口管理
status: active
---

# DSP LDPIF（显示LDP接口状态）

## 功能

该命令用于显示LDP接口状态。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VRFNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无 |
| IFNAME | 接口名 | 可选必选说明：可选参数<br>参数含义：该参数用于表示接口名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：请使用LST INTERFACE命令查看可用接口。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@LDPIF]] · LDP接口（LDPIF）

## 使用实例

显示LDP接口状态：

```
DSP LDPIF:;
```

```

RETCODE = 0  操作成功。

结果如下
--------
       VPN实例名称  =  _public_
            接口名  =  Ethernet64/0/3
          接口状态  =  激活的
      标签发布模式  =  DU
协商的hello hold值  =  15
   接口有效的MTU值  =  1500
      自动创建标识  =  默认值
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-LDPIF.md`
