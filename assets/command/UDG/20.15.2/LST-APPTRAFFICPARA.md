---
id: UDG@20.15.2@MMLCommand@LST APPTRAFFICPARA
type: MMLCommand
name: LST APPTRAFFICPARA（显示应用流量参数）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: APPTRAFFICPARA
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
- 应用流量参数
status: active
---

# LST APPTRAFFICPARA（显示应用流量参数）

## 功能

**适用NF：PGW-U、UPF**

该命令用于显示应用流量参数。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/APPTRAFFICPARA]] · 应用流量参数（APPTRAFFICPARA）

## 使用实例

查询应用流量参数：

```
LST APPTRAFFICPARA:;
```

```

RETCODE = 0  操作成功。

应用流量参数
------------------------
   应用流量规则开关  =  使能
           规则来源  =  DNS规则衍生
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示应用流量参数（LST-APPTRAFFICPARA）_49101654.md`
