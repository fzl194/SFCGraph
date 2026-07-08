---
id: UDG@20.15.2@MMLCommand@DSP LDPREMOTEPEER
type: MMLCommand
name: DSP LDPREMOTEPEER（显示LDP远端邻居状态）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: LDPREMOTEPEER
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- MPLS管理
- LDP管理
- LDP远端邻居管理
status: active
---

# DSP LDPREMOTEPEER（显示LDP远端邻居状态）

## 功能

该命令用于显示LDP远端邻居状态。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VRFNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无 |
| REMOTEPEERNAME | 远端邻居名 | 可选必选说明：可选参数<br>参数含义：该参数用于表示远端邻居名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/LDPREMOTEPEER]] · LDP远端邻居（LDPREMOTEPEER）

## 使用实例

显示LDP远端邻居状态：

```
DSP LDPREMOTEPEER:;
```

```

RETCODE = 0  操作成功。

结果如下
--------
            VPN实例名称  =  _public_
             远端邻居名  =  r2
           远端邻居状态  =  激活的
协商的hello hold值（s）  =  45
           自动创建标识  =  无自动触发
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-LDPREMOTEPEER.md`
