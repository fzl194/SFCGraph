---
id: UDG@20.15.2@MMLCommand@LST MULTREDIRECTEX
type: MMLCommand
name: LST MULTREDIRECTEX（显示扩展的多级重定向密码）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: MULTREDIRECTEX
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 重定向控制
- 多级重定向控制
- 多级重定向密码扩展
status: active
---

# LST MULTREDIRECTEX（显示扩展的多级重定向密码）

## 功能

**适用NF：PGW-U、UPF**

该命令用于显示多级重定向字段加密的密码。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [扩展的多级重定向密码（MULTREDIRECTEX）](configobject/UDG/20.15.2/MULTREDIRECTEX.md)

## 使用实例

假如运营商想要查询加密，配置如下：

```
LST MULTREDIRECTEX:;
```

```

RETCODE = 0  操作成功

AES256 密码信息
---------------------------
 多级重定向名称  =  test
   AES 加密模式  =  GCM
   AES256 密码  =  *****
(Number of results = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示扩展的多级重定向密码（LST-MULTREDIRECTEX）_27223631.md`
