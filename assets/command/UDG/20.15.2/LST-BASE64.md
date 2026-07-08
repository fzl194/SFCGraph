---
id: UDG@20.15.2@MMLCommand@LST BASE64
type: MMLCommand
name: LST BASE64（查询Base64编码规则）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: BASE64
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 业务控制公共配置
- BASE64编码
status: active
---

# LST BASE64（查询Base64编码规则）

## 功能

**适用NF：PGW-U、UPF**

该命令用于显示Base64编码规则，显示是否需要对重定向加密结果进行base64编码，显示编码后特殊字符的转换规则。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/BASE64]] · Base64编码规则（BASE64）

## 使用实例

假如运营商想要查询重定向的加密结果，是否进行base64编码，以及特殊字符的替换规则，命令如下：

```
LST BASE64:;
```

```

RETCODE = 0  操作成功。

Base64编码规则信息
------------------
  重定向Base64编码标识  =  不使能
    重定向等号替换标识  =  不替换
  重定向等号替换字符串  =  NULL
  重定向斜杠替换字符串  =  NULL
  重定向加号替换字符串  =  NULL
业务报表等号替换字符串  =  NULL
  业务报表等号替换标识  =  不替换
业务报表加号替换字符串  =  NULL
业务报表Base64编码标识  =  不使能
业务报表斜杠替换字符串  =  NULL
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询Base64编码规则（LST-BASE64）_86528579.md`
