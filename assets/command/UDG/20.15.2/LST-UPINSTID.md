---
id: UDG@20.15.2@MMLCommand@LST UPINSTID
type: MMLCommand
name: LST UPINSTID（显示当前配置的NF实例ID）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: UPINSTID
command_category: 查询类
applicable_nf:
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- DN管理
- NE信息管理
- NF实例标识管理
status: active
---

# LST UPINSTID（显示当前配置的NF实例ID）

## 功能

**适用NF：UPF**

该命令用于显示UPF上配置的NF实例ID。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [NF实例ID（UPINSTID）](configobject/UDG/20.15.2/UPINSTID.md)

## 使用实例

获取当前UPF配置的NF实例ID：

```
LST UPINSTID:;
```

```

RETCODE = 0  操作成功。

结果如下
----------
UUID  =  4947a69a-f61b-4bc1-b9da-47c9c5d14b64
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示当前配置的NF实例ID（LST-UPINSTID）_05977152.md`
