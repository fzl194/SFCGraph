---
id: UNC@20.15.2@MMLCommand@LST STATICADDRPARA
type: MMLCommand
name: LST STATICADDRPARA（查询静态地址参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: STATICADDRPARA
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- UE地址管理
- 静态地址参数配置
status: active
---

# LST STATICADDRPARA（查询静态地址参数）

## 功能

**适用NF：PGW-C、SMF、GGSN**

该命令用于查询静态地址相关参数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/STATICADDRPARA]] · 静态地址参数（STATICADDRPARA）

## 使用实例

查询静态地址相关参数：

```
LST STATICADDRPARA:;
RETCODE = 0  操作成功。

结果如下
------------------------
扫描任务开关  =  不使能
扫描开始时间  =  00:00
扫描结束时间  =  00:00
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询静态地址参数（LST-STATICADDRPARA）_32232821.md`
