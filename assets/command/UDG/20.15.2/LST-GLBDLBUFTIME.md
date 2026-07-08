---
id: UDG@20.15.2@MMLCommand@LST GLBDLBUFTIME
type: MMLCommand
name: LST GLBDLBUFTIME（查询全局下行数据缓存时长配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: GLBDLBUFTIME
command_category: 查询类
applicable_nf:
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 会话管理
- GTP隧道管理
- 全局下行数据缓存时长
status: active
---

# LST GLBDLBUFTIME（查询全局下行数据缓存时长配置）

## 功能

**适用NF：UPF**

此命令用来查询全局的普通用户下行报文缓存时长。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@GLBDLBUFTIME]] · 全局下行数据缓存时长配置（GLBDLBUFTIME）

## 使用实例

查询全局普通用户下行报文缓存时长：

```
LST GLBDLBUFTIME:;
```

```

RETCODE = 0 操作成功。

全局下行数据缓存时长
----------------------------
普通用户下行数据缓存时长    =  9
NB-IoT用户下行数据缓存时长  =  6
RedCap-NR用户下行数据缓存时长 = 6
(结果个数 = 1)
--- END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-GLBDLBUFTIME.md`
