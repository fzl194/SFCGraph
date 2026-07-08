---
id: UDG@20.15.2@MMLCommand@LST PFCPOVERLOADRPT
type: MMLCommand
name: LST PFCPOVERLOADRPT（查询过载上报开关）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: PFCPOVERLOADRPT
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
- PFCP负荷上报管理
- PFCP过载上报
status: active
---

# LST PFCPOVERLOADRPT（查询过载上报开关）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用来显示过载上报功能的配置。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/PFCPOVERLOADRPT]] · 过载上报开关（PFCPOVERLOADRPT）

## 使用实例

查询过载上报功能配置：

```
LST PFCPOVERLOADRPT:;
```

```

RETCODE = 0 操作成功

过载上报功能开关
----------------------------------
过载上报开关 = ENABLE
    上报阈值 = 85
停止上报阈值 = 80
变化范围阈值 = 5
    定时器值 = 1
  定时器单元 = 10 分钟
(结果个数 = 1)

--- END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-PFCPOVERLOADRPT.md`
