---
id: UDG@20.15.2@MMLCommand@LST KEYCHAIN
type: MMLCommand
name: LST KEYCHAIN（查询Keychain的配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: KEYCHAIN
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP安全管理
- Keychain
- Keychain配置
status: active
---

# LST KEYCHAIN（查询Keychain的配置）

## 功能

该命令用于查询Keychain的全局属性。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| KEYCHAINNAME | Keychain名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定Keychain名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～47。不含问号或空格，大小写不敏感。<br>默认值：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@KEYCHAIN]] · Keychain的配置（KEYCHAIN）

## 使用实例

查询Keychain信息：

```
LST KEYCHAIN:KEYCHAINNAME="ospf";
```

```

RETCODE = 0  操作成功。

结果如下
--------
           Keychain名称  =  ospf
               生效模式  =  绝对时间
               时间模式  =  LMT
       接收容错时长类型  =  持续某段时间
接收容错时间时长（min）  =  100
                TCP类型  =  254
               HMAC-MD5  =  5
           HMAC-SHA1-12  =  2
           HMAC-SHA1-20  =  6
                    MD5  =  3
                  SHA-1  =  4
           HMAC-SHA-256  =  7
                SHA-256  =  8
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-KEYCHAIN.md`
