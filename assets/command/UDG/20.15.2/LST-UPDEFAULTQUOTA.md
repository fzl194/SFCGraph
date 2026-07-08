---
id: UDG@20.15.2@MMLCommand@LST UPDEFAULTQUOTA
type: MMLCommand
name: LST UPDEFAULTQUOTA（查询全局默认配额开关）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: UPDEFAULTQUOTA
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 计费控制
- UP默认配额配置
status: active
---

# LST UPDEFAULTQUOTA（查询全局默认配额开关）

## 功能

**适用NF：PGW-U、UPF**

该命令用于查询在线计费默认配额使能开关。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/UPDEFAULTQUOTA]] · 全局默认配额开关（UPDEFAULTQUOTA）

## 使用实例

查询默认配额使能开关：

```
LST UPDEFAULTQUOTA:;
```

```

 
RETCODE = 0  操作成功。 
 
全局默认配额开关配置信息 
------------------------ 
用户漫游类型  默认配额使能开关  新业务默认配额使能开关  非新业务场景默认配额使能开关

本地          关闭              关闭                    关闭                                     
漫游          关闭              关闭                    关闭 
拜访          关闭              关闭                    关闭    
(结果个数 = 3) 
--- END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-UPDEFAULTQUOTA.md`
