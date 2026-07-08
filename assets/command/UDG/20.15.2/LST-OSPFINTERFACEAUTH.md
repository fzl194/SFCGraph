---
id: UDG@20.15.2@MMLCommand@LST OSPFINTERFACEAUTH
type: MMLCommand
name: LST OSPFINTERFACEAUTH（查询OSPF接口认证配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: OSPFINTERFACEAUTH
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- OSPF管理
- OSPF接口认证配置
status: active
---

# LST OSPFINTERFACEAUTH（查询OSPF接口认证配置）

## 功能

该命令用于查询OSPF接口认证配置。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCID | OSPF进程号 | 可选必选说明：可选参数<br>参数含义：OSPF进程号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无 |
| AREAID | 区域号 | 可选必选说明：可选参数<br>参数含义：区域号。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。点分十进制格式。<br>默认值：无 |
| IFNAME | 接口名 | 可选必选说明：可选参数<br>参数含义：接口名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：请使用LST INTERFACE命令查看可用接口。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/OSPFINTERFACEAUTH]] · OSPF接口认证配置（OSPFINTERFACEAUTH）

## 使用实例

查询OSPF接口认证配置：

```
LST OSPFINTERFACEAUTH:;
```

```

RETCODE = 0  操作成功。

结果如下
------------------------
                   OSPF进程号  =  1
                       区域号  =  0.0.0.0
                       接口名  =  Ethernet64/0/7
                     认证模式  =  HMAC-SHA256
                 密文口令类型  =  Cipher
                 简单认证密码  =  NULL
MD5/HMAC-MD5/HMAC-SHA256 密码  =  *****
             密文验证字标识符  =  100
                 KeyChain名称  =  NULL
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询OSPF接口认证配置（LST-OSPFINTERFACEAUTH）_00600817.md`
