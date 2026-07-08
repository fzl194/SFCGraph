---
id: UDG@20.15.2@MMLCommand@LST OSPFV3AREAAUTH
type: MMLCommand
name: LST OSPFV3AREAAUTH（查询OSPFv3区域认证配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: OSPFV3AREAAUTH
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- OSPFv3管理
- OSPFv3区域认证配置
status: active
---

# LST OSPFV3AREAAUTH（查询OSPFv3区域认证配置）

## 功能

该命令用于查询OSPFv3区域认证配置。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCID | OSPFv3进程号 | 可选必选说明：可选参数<br>参数含义：OSPFv3进程号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无 |
| AREAID | OSPFv3区域号 | 可选必选说明：可选参数<br>参数含义：OSPFv3区域号。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。点分十进制格式。<br>默认值：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@OSPFV3AREAAUTH]] · OSPFv3区域认证配置（OSPFV3AREAAUTH）

## 使用实例

查询OSPFv3区域认证配置：

```
LST OSPFV3AREAAUTH:;
```

```

RETCODE = 0  操作成功。

结果如下
------------------------
    OSPFv3进程号  =  1
    OSPFv3区域号  =  0.0.0.0
        认证模式  =  HMAC-SHA256
    认证密码类型  =  Cipher
    密文验证密码  =  *****
密文验证字标识符  =  1000
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-OSPFV3AREAAUTH.md`
