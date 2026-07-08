---
id: UNC@20.15.2@MMLCommand@LST OSPFNETWORK
type: MMLCommand
name: LST OSPFNETWORK（查询OSPF运行的接口及所属区域）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: OSPFNETWORK
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- OSPF管理
- 指定OSPF运行的接口及所属区域
status: active
---

# LST OSPFNETWORK（查询OSPF运行的接口及所属区域）

## 功能

该命令用于查询在OSPF进程下的区域网段的配置。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCID | 进程号 | 可选必选说明：可选参数<br>参数含义：OSPF进程号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无 |
| AREAID | 区域号 | 可选必选说明：可选参数<br>参数含义：OSPF区域号。<br>数据来源：对端协商<br>取值范围：IPv4地址类型。点分十进制格式。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/OSPFNETWORK]] · OSPF运行的接口及所属区域（OSPFNETWORK）

## 使用实例

查询在OSPF进程下的区域查询网段的配置：

```
LST OSPFNETWORK:;
```

```

RETCODE = 0  操作成功。

结果如下
------------------------
进程号  =  1
区域号  =  0.0.0.0
IP地址  =  192.168.7.0
反掩码  =  0.0.0.255
  描述  =  NULL
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询OSPF运行的接口及所属区域（LST-OSPFNETWORK）_00841057.md`
