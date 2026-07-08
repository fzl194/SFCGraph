---
id: UDG@20.15.2@MMLCommand@LST GLOBUEMUTACC
type: MMLCommand
name: LST GLOBUEMUTACC（查询全局用户互访控制配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: GLOBUEMUTACC
command_category: 查询类
applicable_nf:
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务安全防护
- 用户攻击防护
- 用户互访控制
- 全局用户互访控制
status: active
---

# LST GLOBUEMUTACC（查询全局用户互访控制配置）

## 功能

**适用NF：UPF**

该命令用于查询整机终端互访控制功能。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/GLOBUEMUTACC]] · 全局用户互访控制配置（GLOBUEMUTACC）

## 使用实例

查看整机粒度APN内终端互访控制功能状态及APN间终端互访控制功能状态：

```
LST GLOBUEMUTACC:;
```

```

RETCODE = 0  操作成功。

全局用户互访禁止开关
--------------------
不同APN间的控制开关  =  使能 
 同APN内的控制开关  =  使能
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询全局用户互访控制配置（LST-GLOBUEMUTACC）_82837774.md`
