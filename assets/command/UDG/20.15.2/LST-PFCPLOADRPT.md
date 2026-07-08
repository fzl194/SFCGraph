---
id: UDG@20.15.2@MMLCommand@LST PFCPLOADRPT
type: MMLCommand
name: LST PFCPLOADRPT（查询系统负荷上报开关）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: PFCPLOADRPT
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
- PFCP负荷上报
status: active
---

# LST PFCPLOADRPT（查询系统负荷上报开关）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用来显示系统的负荷上报功能的配置。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/PFCPLOADRPT]] · 系统负荷上报开关（PFCPLOADRPT）

## 使用实例

查询负荷上报功能配置：

```
LST PFCPLOADRPT:;
```

```
 
RETCODE = 0 操作成功

负荷上报功能开关
------------------------------
      负荷上报开关  =  ENABLE
          上报阈值  =  80
      停止上报阈值  =  75
      变化范围阈值  =  5
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询系统负荷上报开关（LST-PFCPLOADRPT）_93531879.md`
