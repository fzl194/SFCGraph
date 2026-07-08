---
id: UDG@20.15.2@MMLCommand@LST HOSTDOMAINPARA
type: MMLCommand
name: LST HOSTDOMAINPARA（查询主机域参数）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: HOSTDOMAINPARA
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务匹配策略
- 业务过滤器管理
- 三四层规则管理
- 主机域参数
status: active
---

# LST HOSTDOMAINPARA（查询主机域参数）

## 功能

**适用NF：PGW-U、UPF**

该命令用来查看主机域相关参数配置。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [主机域参数（HOSTDOMAINPARA）](configobject/UDG/20.15.2/HOSTDOMAINPARA.md)

## 使用实例

查看主机域相关参数配置：

```
%%LST HOSTDOMAINPARA:;
```

```
%%
RETCODE = 0  操作成功

Host主机域配置信息
------------------
多Host学习开关  =  不使能（关闭）
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询主机域参数（LST-HOSTDOMAINPARA）_25540725.md`
