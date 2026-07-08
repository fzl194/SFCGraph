---
id: UDG@20.15.2@MMLCommand@DSP EXPLOG
type: MMLCommand
name: DSP EXPLOG（查询日志导出状态）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: EXPLOG
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- SFIP管理
- SFIP日志管理
- 日志导出
status: active
---

# DSP EXPLOG（查询日志导出状态）

## 功能

该命令用于查询日志导出状态。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@EXPLOG]] · 日志导出状态（EXPLOG）

## 使用实例

查询日志导出状态：

```
DSP EXPLOG:;
```

```

RETCODE = 0  操作成功

执行详细信息
------------
      导出开关  =  打开
    IP版本信息  =  IPV4
服务器IPv4地址  =  10.104.64.129
服务器IPv6地址  =  ::
    服务器端口  =  22
    服务器指纹  =  NULL
  日志导出状态  =  NULL
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-EXPLOG.md`
