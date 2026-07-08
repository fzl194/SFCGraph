---
id: UDG@20.15.2@MMLCommand@LST ICAPSERVER
type: MMLCommand
name: LST ICAPSERVER（查询ICAP服务器）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: ICAPSERVER
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- ICAPC管理
- ICAP服务器
status: active
---

# LST ICAPSERVER（查询ICAP服务器）

## 功能

**适用NF：PGW-U、UPF**

该命令用于查询指定的增值业务的ICAP Server服务器的相关配置。如果没有具体指定服务器的名称，则显示所有已配置的增值业务的ICAP Server服务器的信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ICAPSERVERNAME | ICAP服务器名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定ICAP Server的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格。不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/ICAPSERVER]] · ICAP服务器（ICAPSERVER）

## 使用实例

查询本地配置的ICAP Server信息：

```
LST ICAPSERVER: ICAPSERVERNAME="is1";
```

```

RETCODE = 0  操作成功

ICAP服务器信息
--------------
         ICAP服务器名称  =  is1
  ICAP 服务器IP地址类型  =  IPV4
       ICAP服务器IP地址  =  172.16.39.136
         ICAP服务器类型  =  URL过滤
         ICAP服务器端口  =  1344
                VPN实例  =  NULL
  TCP尝试建链间隔（秒）  =  5
OPTIONS消息的间隔（秒）  =  10
             配置域名称  =  NULL
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-ICAPSERVER.md`
