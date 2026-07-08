---
id: UDG@20.15.2@MMLCommand@LST KEYCHAINKEYID
type: MMLCommand
name: LST KEYCHAINKEYID（查询Keychain Key ID的配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: KEYCHAINKEYID
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP安全管理
- Keychain
- Keychain Key ID配置
status: active
---

# LST KEYCHAINKEYID（查询Keychain Key ID的配置）

## 功能

该命令用于查询Keychain Key ID的各种配置信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| KEYCHAINNAME | Keychain名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定Keychain名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～47。不含问号或空格，大小写不敏感。<br>默认值：无 |
| KEYID | Key索引 | 可选必选说明：可选参数<br>参数含义：该参数用于指定Key索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～63。<br>默认值：无 |

## 操作的配置对象

- [Keychain Key ID的配置（KEYCHAINKEYID）](configobject/UDG/20.15.2/KEYCHAINKEYID.md)

## 使用实例

查询Keychain Key ID配置：

```
LST KEYCHAINKEYID:KEYCHAINNAME="ospf",KEYID=1;
```

```

RETCODE = 0  操作成功。

结果如下
--------
      Keychain名称  =  ospf
           Key索引  =  1
            密码字  =  *****
          认证算法  =  HMAC-SHA-256
是否默认发送Key ID  =  是
          生效模式  =  周周期
      发送时长类型  =  NULL
      发送起始日期  =  NULL
      发送起始时间  =  00:00
   发送时长（min）  =  NULL
      发送结束日期  =  NULL
      发送结束时间  =  00:00
      接收时长类型  =  NULL
      接收起始日期  =  NULL
      接收起始时间  =  00:00
   接收时长（min）  =  NULL
      接收结束日期  =  NULL
      接收结束时间  =  00:00
      发送每周周期  =  星期一 & 星期三 & 星期五
      接收每周周期  =  星期二 & 星期四 & 星期六
      发送每月周期  =  NULL
      接收每月周期  =  NULL
      发送每年周期  =  NULL
      接收每年周期  =  NULL
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询Keychain-Key-ID的配置（LST-KEYCHAINKEYID）_00441125.md`
