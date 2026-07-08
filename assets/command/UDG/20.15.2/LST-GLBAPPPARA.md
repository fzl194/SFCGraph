---
id: UDG@20.15.2@MMLCommand@LST GLBAPPPARA
type: MMLCommand
name: LST GLBAPPPARA（显示全局app参数）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: GLBAPPPARA
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 业务匹配策略
- 业务匹配公共配置
- 业务公共参数管理
- 全局应用参数配置
status: active
---

# LST GLBAPPPARA（显示全局app参数）

## 功能

**适用NF：PGW-U、UPF**

该命令用于显示全局app参数配置。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/GLBAPPPARA]] · 全局app参数（GLBAPPPARA）

## 使用实例

显示全局app参数配置参数：

```
LST GLBAPPPARA:;
```

```

RETCODE = 0  操作成功。

全局app参数
--------------------------
  App规则生效条件  =  N4_INDICATION
     通用应用标识  =  NULL
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-GLBAPPPARA.md`
