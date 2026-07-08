---
id: UDG@20.15.2@MMLCommand@LST UPN4UPATH
type: MMLCommand
name: LST UPN4UPATH（查询N4U路径相关属性）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: UPN4UPATH
command_category: 查询类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 路径管理
- GTP路径管理
- GTP协议参数管理
- N4U路径全局参数
status: active
---

# LST UPN4UPATH（查询N4U路径相关属性）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用来查看N4U路径相关属性。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/UPN4UPATH]] · N4U路径相关属性（UPN4UPATH）

## 使用实例

查询N4 GTP-U路径相关属性：

```
LST UPN4UPATH:;
```

```

RETCODE = 0  操作成功

N4 GTP路径配置
--------------
N4接口的GTP-U路径断告警后发送echo消息的次数  =  0
            N4接口发送GTP心跳请求的间隔时间  =  60
               是否去活路径上已激活的上下文  =  使能
          N4接口的GTP请求消息的重发时间间隔  =  3
      N4接口的GTP请求消息的最大尝试发送次数  =  5
                                   Echo开关  =  使能
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询N4U路径相关属性（LST-UPN4UPATH）_18404303.md`
