---
id: UDG@20.15.2@MMLCommand@LST RELAYAUTHKEY
type: MMLCommand
name: LST RELAYAUTHKEY（查询媒体中继鉴权密钥）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: RELAYAUTHKEY
command_category: 查询类
applicable_nf:
- UPF
- PGW-U
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 媒体中继
- 媒体中继鉴权密钥
status: active
---

# LST RELAYAUTHKEY（查询媒体中继鉴权密钥）

## 功能

**适用NF：UPF、PGW-U**

该命令用于查询媒体中继鉴权密钥。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RELAYAUTHKEYNAME | 媒体中继鉴权密钥名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定媒体中继认证密钥名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@RELAYAUTHKEY]] · 媒体中继鉴权密钥（RELAYAUTHKEY）

## 使用实例

查询媒体中继鉴权密钥：

```
LST RELAYAUTHKEY:;
```

```

RETCODE = 0  操作成功

结果如下
------------------------
媒体中继鉴权密钥名称  =  auth1
		主鉴权密钥  =  *****
		备鉴权密钥  =  *****
媒体中继认证密钥描述  =  NULL
        配置域名称  =  NULL
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-RELAYAUTHKEY.md`
