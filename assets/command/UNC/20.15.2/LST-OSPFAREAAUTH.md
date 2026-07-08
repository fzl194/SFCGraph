---
id: UNC@20.15.2@MMLCommand@LST OSPFAREAAUTH
type: MMLCommand
name: LST OSPFAREAAUTH（查询OSPF区域认证配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: OSPFAREAAUTH
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- OSPF管理
- OSPF区域认证配置
status: active
---

# LST OSPFAREAAUTH（查询OSPF区域认证配置）

## 功能

该命令用于查询OSPF区域认证配置。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCID | OSPF进程号 | 可选必选说明：可选参数<br>参数含义：OSPF进程号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无 |
| AREAID | 区域号 | 可选必选说明：可选参数<br>参数含义：区域号。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。点分十进制格式。<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@OSPFAREAAUTH]] · OSPF区域认证配置（OSPFAREAAUTH）

## 使用实例

查询OSPF区域认证配置：

```
LST OSPFAREAAUTH:;
```

```

RETCODE = 0  操作成功。

结果如下
------------------------
                   OSPF进程号  =  1
                       区域号  =  0.0.0.0
                     认证模式  =  HMAC-SHA256
                 密文口令类型  =  Cipher
MD5/HMAC-MD5/HMAC-SHA256 密码  =  *****
                 简单认证密码  =  NULL
             密文验证字标识符  =  100
                 KeyChain名称  =  NULL
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-OSPFAREAAUTH.md`
