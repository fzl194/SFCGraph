---
id: UDG@20.15.2@MMLCommand@LST OSPFGTSM
type: MMLCommand
name: LST OSPFGTSM（查询OSPF的GTSM配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: OSPFGTSM
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- OSPF管理
- OSPF的Gtsm功能配置
status: active
---

# LST OSPFGTSM（查询OSPF的GTSM配置）

## 功能

该命令用于查询OSPF的GTSM配置。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VRFNAME | VPN实例名 | 可选必选说明：可选参数<br>参数含义：VPN实例名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无 |
| TTL | TTL时间 | 可选必选说明：可选参数<br>参数含义：TTL时间。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～255。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/OSPFGTSM]] · OSPF的GTSM配置（OSPFGTSM）

## 使用实例

查询OSPF的GTSM配置：

```
LST OSPFGTSM:;
```

```

RETCODE = 0  操作成功。

结果如下
------------------------
                   VPN实例名  =  _public_
                     TTL时间  =  20
发送或接收的组播报文TTL是255  =  FALSE
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-OSPFGTSM.md`
