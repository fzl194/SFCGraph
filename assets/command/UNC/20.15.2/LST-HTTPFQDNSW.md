---
id: UNC@20.15.2@MMLCommand@LST HTTPFQDNSW
type: MMLCommand
name: LST HTTPFQDNSW（查询HTTP是否支持FQDN）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: HTTPFQDNSW
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- HTTP功能管理
- HTTP管理
- HTTP FQDN管理
status: active
---

# LST HTTPFQDNSW（查询HTTP是否支持FQDN）

## 功能

该命令用于查询HTTP是否支持FQDN。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/HTTPFQDNSW]] · HTTP是否支持FQDN（HTTPFQDNSW）

## 使用实例

查询HTTP是否支持FQDN，可以用如下命令：

```
%%LST HTTPFQDNSW:;%%
RETCODE = 0  操作成功

结果如下
--------
        全局FQDN开关  =  关闭
间接路由场景FQDN开关  =  关闭
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-HTTPFQDNSW.md`
