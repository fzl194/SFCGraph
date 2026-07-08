---
id: UDG@20.15.2@MMLCommand@LST LDPAUTHGROUP
type: MMLCommand
name: LST LDPAUTHGROUP（查询LDP认证组配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: LDPAUTHGROUP
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- MPLS管理
- LDP管理
- LDP认证组管理
status: active
---

# LST LDPAUTHGROUP（查询LDP认证组配置）

## 功能

该命令用于查询配置的LDP认证组。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VRFNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无 |
| AUTHPEERGROUPNAME | 认证组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定认证组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～169；字符串由数字、字母、“.”、“-”或“_”组成。<br>默认值：无 |

## 操作的配置对象

- [LDP认证组（LDPAUTHGROUP）](configobject/UDG/20.15.2/LDPAUTHGROUP.md)

## 使用实例

查询LDP认证组：

```
LST LDPAUTHGROUP:;
```

```
RETCODE = 0  操作成功。

结果如下
--------
                    VPN实例名称  =  _public_
                     认证组名称  =  bb
                    LDP认证类型  =  KeyChain认证类型
                  认证组MD5密码  =  NULL
             认证组KeyChain名字  =  key1
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询LDP认证组配置（LST-LDPAUTHGROUP）_50281554.md`
