---
id: UDG@20.15.2@MMLCommand@DSP TNLSTATISTICS
type: MMLCommand
name: DSP TNLSTATISTICS（查询隧道统计信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: TNLSTATISTICS
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- VPN管理
- VPN隧道管理
- 隧道统计信息
status: active
---

# DSP TNLSTATISTICS（查询隧道统计信息）

## 功能

该命令用于查询隧道统计信息。

## 注意事项

只有配置隧道才能使用该命令。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@TNLSTATISTICS]] · 隧道统计信息（TNLSTATISTICS）

## 使用实例

查询隧道统计信息：

```
DSP TNLSTATISTICS:;
```

```

RETCODE = 0  操作成功

结果如下
-------------------------
  隧道类型  =  Gre
  隧道数目  =  1
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-TNLSTATISTICS.md`
