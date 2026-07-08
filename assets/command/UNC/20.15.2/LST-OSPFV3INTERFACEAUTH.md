---
id: UNC@20.15.2@MMLCommand@LST OSPFV3INTERFACEAUTH
type: MMLCommand
name: LST OSPFV3INTERFACEAUTH（查询OSPFv3接口认证配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: OSPFV3INTERFACEAUTH
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- OSPFv3管理
- OSPFv3接口认证配置
status: active
---

# LST OSPFV3INTERFACEAUTH（查询OSPFv3接口认证配置）

## 功能

该命令用于查询OSPFv3接口认证配置。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCID | OSPFv3进程号 | 可选必选说明：可选参数<br>参数含义：OSPFv3进程号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无 |
| AREAID | OSPFv3区域号 | 可选必选说明：可选参数<br>参数含义：OSPFv3区域号。<br>数据来源：对端协商<br>取值范围：IPv4地址类型。点分十进制格式。<br>默认值：无 |
| IFNAME | 接口名 | 可选必选说明：可选参数<br>参数含义：接口名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：请使用LST INTERFACE命令查看可用接口。 |
| INSTANCEID | 实例号 | 可选必选说明：可选参数<br>参数含义：实例号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～255。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/OSPFV3INTERFACEAUTH]] · OSPFv3接口认证配置（OSPFV3INTERFACEAUTH）

## 使用实例

查询OSPFv3接口认证配置：

```
LST OSPFV3INTERFACEAUTH:;
```

```

RETCODE = 0  操作成功。

结果如下
------------------------
    OSPFv3进程号  =  1
    OSPFv3区域号  =  0.0.0.0
          接口名  =  Ethernet64/0/8
    认证密码类型  =  Cipher
        认证模式  =  HMAC-SHA256
    密文验证密码  =  *****
密文验证字标识符  =  1000
          实例号  =  0
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询OSPFv3接口认证配置（LST-OSPFV3INTERFACEAUTH）_00866421.md`
