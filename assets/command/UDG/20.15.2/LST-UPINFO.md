---
id: UDG@20.15.2@MMLCommand@LST UPINFO
type: MMLCommand
name: LST UPINFO（查询 UP 参数信息）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: UPINFO
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
- PFCP路径管理
- UP信息管理
- UP信息
status: active
---

# LST UPINFO（查询 UP 参数信息）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用来查看UPF相关配置属性。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/UPINFO]] ·  UP 参数信息（UPINFO）

## 使用实例

查看UPF相关配置属性：

```
LST UPINFO:;
```

```

RETCODE = 0  操作成功

UP  参数配置
------------
                 名称 = upf27
IPv6地址类型的Node Id = ::
IPv4地址类型的Node Id = 0.0.0.0
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-UPINFO.md`
